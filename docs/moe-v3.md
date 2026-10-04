# Adapter-MoE V3

The experimental adapter-MoE branch is deliberately fail closed.

- serving policy: explicit_evidence_gates_else_base_v1
- learned router serving authority: false
- bounded route smoke: 8/8
- decision: DO_NOT_PROMOTE

Recorded blockers:
- base arithmetic smoke returned 683 for 37 x 19 instead of 703
- one dialect prompt echoed instead of transforming
- C++ code smoke degenerated into repeated code tags
- dialect and code historical receipts do not pin the exact Hub base revision

Evidence:
- evidence/moe_v3_verification.json
- evidence/code_expert_diagnosis.json
