# R3/D3 logic V6

R3/D3 is a PEFT/QLoRA adapter over humain-ai/ALLaM-7B-Instruct-preview for a narrow symbolic-entailment task.

## Frozen evaluation

| System | Correct | Accuracy |
| --- | ---: | ---: |
| ALLaM-7B base | 357/600 | 59.50% |
| R3/D3 | 367/600 | 61.17% |

Paired movement:
- wrong to right: 19
- right to wrong: 9
- both wrong: 224
- net gain: +10

Integrity:
- frozen V6 dataset SHA-256: a2d27bc8a249c0d32fdd33c7abc89323d50b1000aba9a18b111bc9334d4c6a63
- base result SHA-256: 11841e08ea8eb237ded20cd50d3525080f072b6ef95f92e62b91957735dc2b48
- adapter result SHA-256: 6a136fbc61109dbfbf756962dfb5afebc4ed3967c14413aa13f8531b263b8a99
- adapter artifact SHA-256: c6a90800e51c3a8f8568cda42edbebf7334f9d81fbafb9a11e10a72b436d0fe7

Boundary: this is evidence for one frozen symbolic-entailment protocol, not broad model superiority.
