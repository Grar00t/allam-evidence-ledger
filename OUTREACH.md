# Suggested outreach note

Hi Tareq,

I consolidated a small public evidence ledger around my independent ALLaM work so the engineering trail is easier to review in one place:

https://github.com/Grar00t/allam-evidence-ledger

The emphasis is reproducibility rather than headline scores: frozen evaluation receipts, artifact and dataset hashes, paired regressions, explicit claim boundaries, and DO_NOT_PROMOTE decisions when an expert fails its gate.

The strongest completed result is the re-audited R3/D3 symbolic-logic adapter: 367/600 (61.17%) versus 357/600 (59.50%) for the recorded ALLaM-7B base on the same frozen V6 protocol, with 19 improvements, 9 regressions, and the earlier 600/600 result explicitly superseded after audit.

A pinned Math V2 QLoRA run has also completed. Its grouped MetaMathQA dev loss improved from 0.180739 to 0.133401, but I am keeping it labeled candidate until an external held-out math gate is completed. The experimental adapter-MoE branch is similarly fail-closed: unsupported prompts stay on base, the learned router is telemetry-only, and the current V3 bundle remains DO_NOT_PROMOTE because live smoke exposed arithmetic, dialect and code failures.

I also linked the native C11 Niyah.Engine/Casper work and the x86 Assembly Opcode Orchestra project as examples of the systems side of how I work.

This is separate from the private HUMAIN advisory material I sent earlier; the public ledger makes no claim about HUMAIN production systems.

Best,
Sulaiman Alshammari
Saudi Arabia
