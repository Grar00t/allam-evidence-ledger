from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
evidence = root / "evidence"
ok = True
for raw in (evidence / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not raw.strip():
        continue
    expected, name = raw.split(None, 1)
    path = evidence / name.strip()
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    status = "PASS" if actual == expected else "FAIL"
    print(status, path.name, actual)
    ok = ok and actual == expected
sys.exit(0 if ok else 1)
