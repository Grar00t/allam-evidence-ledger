# Evidence roadmap

1. Math V2 external gate: compare the completed candidate with the same pinned base on a held-out math benchmark using identical prompting and scoring; preserve row-level outputs and hashes.
2. Math route admission: only after that gate passes, consider adding a math expert route and rerun base/regression/routing tests.
3. MoE OOD routing gate: keep the learned router telemetry-only until out-of-distribution routing is measured.
4. Code V2 rebuild: use genuinely independent tasks and solutions; do not continue the structurally leaked Stage2 split.
5. Public evidence refresh: add new receipts without overwriting old ones and mark superseded claims explicitly.

No promotion from training loss alone.
