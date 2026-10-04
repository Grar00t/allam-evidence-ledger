# ALLaM Evidence Ledger

A public, evidence-first index of independent engineering experiments around ALLaM, adapter routing, reproducible evaluation, and local/native AI runtimes.

Policy: NO CLAIM BEYOND THE HASH.

This repository is not evidence about HUMAIN production systems and is not affiliated with HUMAIN. Private advisories, private correspondence, proprietary material, private datasets, and ALLaM base-model weights are intentionally excluded.

## Why this exists

The purpose is to preserve a short chain from experiment to receipt to hash to bounded conclusion, including negative results when they affect engineering decisions.

Experimental experts that fail live or external gates remain DO_NOT_PROMOTE.

## Evidence map

| Work | Current state | What is established |
| --- | --- | --- |
| R3/D3 symbolic logic adapter | VERIFIED_TASK_SPECIFIC | Frozen V6: base 357/600, adapter 367/600, net +10 |
| Math V2 QLoRA candidate | CANDIDATE_EXTERNAL_EVAL_PENDING | Group-separated 2000/250 MetaMathQA split; dev loss 0.180739 to 0.133401 |
| Adapter-MoE V3 | DO_NOT_PROMOTE | Fail-closed routing contract and 8/8 route smoke; capability failures remain |
| Niyah.Engine | PUBLIC_RESEARCH_RUNTIME | Native C11 model lifecycle engineering |
| Casper / NIYAH | PUBLIC_RESEARCH_RUNTIME | C11 neural/symbolic runtime and integrity receipts |
| Opcode Orchestra | PUBLIC_SYSTEMS_ENGINEERING | Assembly-first x86 build and verification discipline |

## R3/D3

Public model:
https://huggingface.co/sulaimanalshammari/R3-D3-ALLaM-7B-Logic-Adapter

Frozen V6 symbolic-entailment holdout:
- 600 rows
- ALLaM-7B base: 357/600 (59.50%)
- R3/D3: 367/600 (61.17%)
- wrong to right: 19
- right to wrong: 9
- net movement: +10
- adapter SHA-256: c6a90800e51c3a8f8568cda42edbebf7334f9d81fbafb9a11e10a72b436d0fe7

This is a task-specific result, not a claim of universal reasoning superiority.

## Math V2

The pinned NIYAH QLoRA ALLaM Math V2 run completed on Kaggle and produced a LoRA adapter.

- base revision: a28dd1e67420cde72d3629c8633a974cf7d9c366
- dataset: meta-math/MetaMathQA
- dataset revision: aa4f34d3d2d3231299b5b03d9b3e5a20da45aa18
- train/dev: 2000 / 250
- grouping: unique original_question; no train/dev group overlap
- base dev loss: 0.180739
- post-training dev loss: 0.133401
- adapter SHA-256: 6486325cbb6def43363cd1d2926e8ead08d3bb7aacc941a92470ee5629bcd7f5

Status: candidate only. External held-out math evaluation is still required before promotion.

## Adapter-MoE

Public experimental branch:
https://huggingface.co/sulaimanalshammari/R3-D3-ALLaM-7B-Logic-Adapter/tree/feat/allam-adapter-moe-20261002

The learned router is telemetry-only; unsupported or general prompts remain on the base route. V3 recorded route_matches=8/8, but arithmetic, dialect and code failures remain, so the decision is DO_NOT_PROMOTE.

## Native systems

- Niyah.Engine: https://github.com/Grar00t/Niyah.Engine
- Casper: https://github.com/Grar00t/casper
- Opcode Orchestra: https://github.com/Grar00t/opcode-orchestra

These demonstrate systems work outside a hosted-model wrapper: native C11 model/runtime work, deterministic integrity receipts, and x86 Assembly build/verification.

## Verify the copied evidence

    python scripts/verify_evidence.py

## Deliberately excluded

- HUMAIN private advisories or incident-report material
- private email or correspondence
- private datasets
- ALLaM 7B base-model weights
- claims inferred from screenshots without receipts

See CLAIMS.md and ROADMAP.md.
