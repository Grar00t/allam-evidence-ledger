from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_NAME = "SHA256SUMS.txt"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reject_nonstandard_json_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")


def parse_manifest(manifest: Path, evidence: Path) -> tuple[list[tuple[str, str, Path]], list[str]]:
    entries: list[tuple[str, str, Path]] = []
    errors: list[str] = []
    seen: set[str] = set()
    evidence_root = evidence.resolve()

    if not manifest.is_file():
        return entries, [f"missing manifest: {manifest}"]

    for line_number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue

        parts = raw.split(None, 1)
        if len(parts) != 2:
            errors.append(f"manifest line {line_number}: expected '<sha256>  <path>'")
            continue

        expected, name = parts[0].lower(), parts[1].strip()
        if not SHA256_RE.fullmatch(expected):
            errors.append(f"manifest line {line_number}: invalid sha256")
            continue
        if not name:
            errors.append(f"manifest line {line_number}: empty path")
            continue

        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"manifest line {line_number}: path escapes evidence/: {name}")
            continue

        normalized = relative.as_posix()
        if normalized in seen:
            errors.append(f"manifest line {line_number}: duplicate path: {normalized}")
            continue

        lexical_path = evidence / relative
        if lexical_path.is_symlink():
            errors.append(f"manifest line {line_number}: symlink evidence is not allowed: {normalized}")
            continue

        path = lexical_path.resolve()
        try:
            path.relative_to(evidence_root)
        except ValueError:
            errors.append(f"manifest line {line_number}: path escapes evidence/: {normalized}")
            continue

        seen.add(normalized)
        entries.append((expected, normalized, path))

    return entries, errors


def verify(root: Path | None = None) -> int:
    repo_root = root.resolve() if root is not None else Path(__file__).resolve().parents[1]
    evidence = repo_root / "evidence"
    manifest = evidence / MANIFEST_NAME
    entries, errors = parse_manifest(manifest, evidence)

    listed: set[str] = set()
    for expected, name, path in entries:
        listed.add(name)

        if not path.is_file():
            errors.append(f"missing evidence file: {name}")
            continue

        actual = sha256_file(path)
        if actual != expected:
            errors.append(f"hash mismatch: {name}: expected {expected}, got {actual}")
            continue

        if Path(name).suffix.lower() == ".json":
            try:
                json.loads(
                    path.read_text(encoding="utf-8-sig"),
                    parse_constant=reject_nonstandard_json_constant,
                )
            except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
                errors.append(f"invalid json: {name}: {exc}")
                continue

        print(f"PASS {name} {actual}")

    if evidence.is_dir():
        actual_files = {
            relative
            for path in evidence.rglob("*")
            if path.is_file()
            for relative in [path.relative_to(evidence).as_posix()]
            if relative != MANIFEST_NAME
        }
        for name in sorted(actual_files - listed):
            errors.append(f"untracked evidence file: {name}")

    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1

    print(f"PASS manifest coverage {len(listed)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(verify())
