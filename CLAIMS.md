# Claim ledger

| Claim | Status | Evidence | Boundary |
| --- | --- | --- | --- |
| R3/D3 gains +10 net correct over the recorded ALLaM base on frozen V6 | VERIFIED_TASK_SPECIFIC | evidence/logic_v6_comparison.json | Same frozen task and protocol only |
| Math V2 improves dev loss on its pinned grouped MetaMathQA split | VERIFIED_TRAINING_RESULT | evidence/math_v2_training_receipt.json | Not an external capability benchmark |
| Math V2 is a promoted math expert | NOT_ESTABLISHED | source receipt claim boundary | External held-out math evaluation required |
| Adapter-MoE V3 routing plumbing passes its bounded smoke | VERIFIED_BOUNDED_SMOKE | evidence/moe_v3_verification.json | Not a capability benchmark |
| Adapter-MoE V3 should be promoted | REJECTED | evidence/moe_v3_verification.json | Arithmetic, dialect and code failures recorded |
| Code Stage2 dev loss proves generalization | REJECTED | evidence/code_expert_diagnosis.json | Dev split is structurally leaked |
| Integrity receipts prove factual truth | NOT_CLAIMED | linked Casper docs | Receipts bind bytes, not truth |

Rules:
1. Successful job does not equal successful model evaluation.
2. Loss improvement does not equal capability improvement.
3. Routing smoke does not equal quality benchmark.
4. Hash establishes byte identity, not semantic correctness.
5. Negative results are preserved when they affect promotion.
