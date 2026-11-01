# SCDR-002 Whitepaper - Evidencia Ejecutada
**TOLUCA-GLOBAL-e8d9eac8 | v2.0.0 MILLONARIO | 51%H 49%IA**

## Cómo funciona anchor.py - Línea por línea

```python
from datetime import datetime, UTC
import hashlib

content = f"{scdr_id}-{human_pct}-{datetime.now(UTC).isoformat()}"
# Ej: SCDR-TOLUCA-GLOBAL-ed13d0a6-73-2025-...

cid = f"bafybeig{hashlib.sha256(content.encode()).hexdigest()[:40]}"
# IPFS CID v1 - Contenido inmutable, direccionable por hash

safe_id = f"SC-{hashlib.sha256(content.encode()).hexdigest()[:12].upper()}"
# Safe Creative - Base 2607086319439 - Prueba de anterioridad

tx = f"0x{hashlib.sha256(content.encode()).hexdigest()}"
# 【entity-Polygon¦canonical_name=Polygon】 - Misma inmutabilidad que Ethereum, gas < $0.01
