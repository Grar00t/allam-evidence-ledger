from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_evidence", ROOT / "scripts" / "verify_evidence.py")
assert SPEC is not None and SPEC.loader is not None
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class VerifyEvidenceTests(unittest.TestCase):
    def make_repo(self, files: dict[str, bytes]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        evidence = root / "evidence"
        evidence.mkdir()

        lines = []
        for name, data in files.items():
            path = evidence / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            lines.append(f"{digest(data)}  {name}")

        (evidence / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        return root

    def run_verify(self, root: Path) -> int:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return VERIFY.verify(root)

    def test_valid_manifest_passes(self) -> None:
        payload = json.dumps({"ok": True}).encode("utf-8")
        root = self.make_repo({"record.json": payload})
        self.assertEqual(0, self.run_verify(root))

    def test_untracked_file_fails(self) -> None:
        root = self.make_repo({"record.json": b'{"ok": true}'})
        (root / "evidence" / "extra.json").write_text('{"extra": true}', encoding="utf-8")
        self.assertEqual(1, self.run_verify(root))

    def test_path_escape_fails(self) -> None:
        root = self.make_repo({"record.json": b'{"ok": true}'})
        outside = root / "outside.json"
        outside.write_text('{"outside": true}', encoding="utf-8")
        manifest = root / "evidence" / "SHA256SUMS.txt"
        manifest.write_text(f"{digest(outside.read_bytes())}  ../outside.json\n", encoding="utf-8")
        self.assertEqual(1, self.run_verify(root))

    def test_duplicate_manifest_entry_fails(self) -> None:
        root = self.make_repo({"record.json": b'{"ok": true}'})
        manifest = root / "evidence" / "SHA256SUMS.txt"
        line = manifest.read_text(encoding="utf-8").strip()
        manifest.write_text(f"{line}\n{line}\n", encoding="utf-8")
        self.assertEqual(1, self.run_verify(root))

    def test_duplicate_manifest_alias_fails(self) -> None:
        payload = b'{"ok": true}'
        root = self.make_repo({"record.json": payload})
        manifest = root / "evidence" / "SHA256SUMS.txt"
        line = manifest.read_text(encoding="utf-8").strip()
        manifest.write_text(f"{line}\n{digest(payload)}  ./record.json\n", encoding="utf-8")
        self.assertEqual(1, self.run_verify(root))

    def test_invalid_json_fails_even_when_hash_matches(self) -> None:
        root = self.make_repo({"record.json": b'{"broken":'})
        self.assertEqual(1, self.run_verify(root))

    def test_nonstandard_json_constant_fails(self) -> None:
        root = self.make_repo({"record.json": b'{"score": NaN}'})
        self.assertEqual(1, self.run_verify(root))

    def test_symlink_evidence_fails(self) -> None:
        payload = b'{"ok": true}'
        root = self.make_repo({"payload.txt": payload})
        evidence = root / "evidence"
        link = evidence / "record.json"
        link.symlink_to("payload.txt")
        manifest = evidence / "SHA256SUMS.txt"
        manifest.write_text(
            manifest.read_text(encoding="utf-8") + f"{digest(payload)}  record.json\n",
            encoding="utf-8",
        )
        self.assertEqual(1, self.run_verify(root))

    def test_nested_manifest_named_file_is_not_exempt(self) -> None:
        root = self.make_repo({"record.json": b'{"ok": true}'})
        nested = root / "evidence" / "archive"
        nested.mkdir()
        (nested / "SHA256SUMS.txt").write_text("not the root manifest\n", encoding="utf-8")
        self.assertEqual(1, self.run_verify(root))


if __name__ == "__main__":
    unittest.main()
