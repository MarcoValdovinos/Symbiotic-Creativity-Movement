# ISO/IEC 42001:2023 - Crosswalk SCDR-001 / SCDR-002

**ARKHE ZERO - TOLUCA-GLOBAL-e8d9eac8 | 51%H 49%IA**

| ISO 42001 Clause | Requirement | SCDR-001/002 Implementation |
|------------------|-------------|------------------------------|
| 4.1 Understanding context | AI system context | `human_pct` + `ai_pct` measures context |
| 4.2 Interested parties | Stakeholders | `13-COMPLIANCE/{US,EU,BR,MX}` |
| 5.2 AI Policy | Policy definition | `MANIFIESTO.md` + `LICENCIA_COAUTORIA` |
| 6.1 Risk assessment | AI risks | `LFDA $12.6M` risk + `EU AI Act Art 50` transparency |
| 7.4 Communication | Disclosure | `voz-original.html` + QR `ed13d0a6` |
| 8.2 Data management | Data traceability | `voice_hash` + `chain_anchor.ipfs_cid` |
| 8.4 AI system verification | Verification | `POST /api/v1/calculate` + `GET /api/v1/verify/{id}` |
| 9.1 Monitoring | Performance | `tools/sentinel/track.py` daily |
| 10.2 Continual improvement | SCDR-002 | Evolution from SCDR-001 to SCDR-002 |

**Compliance:** SCDR-002 cumple ISO 42001:2023 para AIMS (AI Management System)
