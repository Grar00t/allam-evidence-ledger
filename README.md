# ALLaM Evidence Ledger

Technical evidence for ALLaM adapter experiments and a separately documented consumer-service dispute.

**Policy: NO CLAIM BEYOND THE HASH.**

This repository records reproducible experiment evidence and a sanitized dispute record. It does not publish private billing documents, bank data, account identifiers, or unredacted chat exports.

## Evidence map

| Experiment | State | Recorded result |
| --- | --- | --- |
| R3/D3 symbolic logic adapter | VERIFIED_TASK_SPECIFIC | Frozen V6: base 357/600 (59.50%), adapter 367/600 (61.17%), net +10 |
| Math V2 QLoRA candidate | CANDIDATE_EXTERNAL_EVAL_PENDING | Group-separated 2,000/250 MetaMathQA split; dev loss 0.180739 -> 0.133401 |
| Adapter-MoE V3 | DO_NOT_PROMOTE | Fail-closed routing contract and 8/8 route smoke; capability failures remain |

## Consumer-service dispute record

See [OPENAI_DISPUTE.md](OPENAI_DISPUTE.md).

That page separates verified billing facts, the owner's allegation that paid-API steering felt coercive/extortionate in effect, verified context-integrity evidence, claims still requiring primary-source verification, and public court cases involving Sam Altman with allegations and outcomes clearly distinguished.

## R3/D3

Model repository:

https://huggingface.co/sulaimanalshammari/R3-D3-ALLaM-7B-Logic-Adapter

Frozen V6 symbolic-entailment evaluation:

- rows: **600**
- ALLaM-7B base: **357/600 (59.50%)**
- R3/D3: **367/600 (61.17%)**
- wrong -> right: **19**
- right -> wrong: **9**
- net movement: **+10**
- adapter SHA-256: `c6a90800e51c3a8f8568cda42edbebf7334f9d81fbafb9a11e10a72b436d0fe7`

Boundary: this is a task-specific result on the recorded frozen protocol.

## Math V2

Pinned QLoRA training record:

- base revision: `a28dd1e67420cde72d3629c8633a974cf7d9c366`
- dataset: `meta-math/MetaMathQA`
- dataset revision: `aa4f34d3d2d3231299b5b03d9b3e5a20da45aa18`
- train/dev: **2,000 / 250**
- grouping: unique `original_question`; no train/dev group overlap
- base dev loss: **0.180739**
- post-training dev loss: **0.133401**
- adapter SHA-256: `6486325cbb6def43363cd1d2926e8ead08d3bb7aacc941a92470ee5629bcd7f5`

Status: **candidate**. External held-out math evaluation is required before promotion.

## Adapter-MoE V3

Experimental branch:

https://huggingface.co/sulaimanalshammari/R3-D3-ALLaM-7B-Logic-Adapter/tree/feat/allam-adapter-moe-20261002

The learned router has no serving authority. Unsupported/general prompts remain on the base route. The recorded V3 bundle remains **DO_NOT_PROMOTE** because arithmetic, dialect, and code failures are present in the verification evidence.

## Verify evidence

```bash
python scripts/verify_evidence.py
```

See `CLAIMS.md` for claim boundaries and `ROADMAP.md` for pending verification work.
