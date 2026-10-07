# Claim ledger

| Claim | Status | Evidence | Boundary |
| --- | --- | --- | --- |
| R3/D3 gains +10 net correct over the recorded ALLaM base on frozen V6 | VERIFIED_TASK_SPECIFIC | `evidence/logic_v6_comparison.json` | Same frozen task and protocol only |
| Math V2 improves dev loss on its pinned grouped MetaMathQA split | VERIFIED_TRAINING_RESULT | `evidence/math_v2_training_summary.json` | Not an external capability benchmark |
| Math V2 is a promoted math expert | NOT_ESTABLISHED | `evidence/math_v2_training_summary.json` | External held-out math evaluation required |
| Adapter-MoE V3 routing plumbing passes its bounded smoke | VERIFIED_BOUNDED_SMOKE | `evidence/moe_v3_verification.json` | Not a capability benchmark |
| Adapter-MoE V3 should be promoted | REJECTED | `evidence/moe_v3_verification.json` | Arithmetic, dialect, and code failures recorded |
| Code Stage2 dev loss proves generalization | REJECTED | `evidence/code_expert_diagnosis.json` | Dev split is structurally leaked |

Rules:
1. A successful job is not automatically a successful model evaluation.
2. Loss improvement is not automatically capability improvement.
3. A routing smoke test is not a quality benchmark.
4. A hash establishes byte identity, not semantic correctness.
5. Negative results remain recorded when they affect promotion decisions.
