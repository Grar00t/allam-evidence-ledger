# Evidence manifest correction, 2026-10-07

At local base commit `191ed130462925354306250e72a1526f7b39a66a`,
two manifest entries describe CRLF working-copy bytes instead of the LF bytes
stored in Git. A checkout with LF endings therefore fails verification.

| File | Previous CRLF SHA-256 | Committed LF SHA-256 |
| --- | --- | --- |
| `ledger.json` | `cbc4cce7e38398af335ddbd7d07d75890e7204aa7514ef1ce75d82eb5e853515` | `69193a623854bfab32fdd46a47539f3a9c9c385ad83126c7c1ec7383c05727b4` |
| `moe_v3_verification.json` | `c33bd702543989b011adebbbde7dfac28b5e5e2c9b1acda5066542509036ffe9` | `81533959e6c3ca9de5f7a2f0633b305813466276b5eb298fb73ad8485e9edb8c` |

The manifest now binds the existing committed bytes. Git attributes pin LF
endings for these evidence files on every platform. The verifier still hashes
raw file bytes; it does not normalize input or accept multiple digests.
The evidence JSON values and scientific claims are unchanged. This corrects
byte identity bookkeeping and does not rerun or validate the recorded experiments.
