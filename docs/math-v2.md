# Math V2 candidate

The pinned NIYAH QLoRA ALLaM Math V2 Kaggle run completed and produced a LoRA adapter plus a training receipt.

Pinned inputs:
- base: `ALLaM-7B-Instruct-preview`
- base revision: `a28dd1e67420cde72d3629c8633a974cf7d9c366`
- dataset: `meta-math/MetaMathQA`
- dataset revision: `aa4f34d3d2d3231299b5b03d9b3e5a20da45aa18`
- seed: `20261002`
- train/dev: `2000 / 250`
- grouping: unique `original_question`; no train/dev group overlap

Training result:

| Metric | Base | After |
| --- | ---: | ---: |
| dev eval loss | 0.18073922396 | 0.13340069354 |

LoRA: r=16, alpha=32, dropout=0.05, trainable parameters=39,976,960, one epoch.
Recorded training device: Tesla T4, BF16 compute.

Artifact:
- bytes: 159967880
- SHA-256: `6486325cbb6def43363cd1d2926e8ead08d3bb7aacc941a92470ee5629bcd7f5`

The adapter weights are not copied into this ledger.

Promotion boundary: candidate math expert only. External held-out math evaluation is required before promotion.
