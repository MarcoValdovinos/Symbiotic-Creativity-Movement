# SCDR-002 Certification Authority - Pricing

## Planes

### BASIC - $49 USD
- SCDR-CERT ID único (SCDR-CERT-2026-XXX)
- Genesis ID
- SHA256 Ancla
- W3C Verifiable Credential vc.json
- Página verificable 【entity-GitHub Pages¦canonical_name=GitHub】
- Badge README
- Tiempo: 24h

### PRO - $149 USD (más vendido)
- Todo BASIC +
- Investigación transparente "No encontramos caso previo"
- OpenTimestamps Bitcoin anchor (prueba inmutable)
- Artículo Dev.to draft
- Product Hunt draft
- SEO index
- Tiempo: 48h

### ENTERPRISE - $499 USD
- Todo PRO +
- Registro INDAUTOR México
- US Copyright Office guidance
- Press Kit + Wikipedia draft
- 2 artículos externos
- Consultoría 1h
- Tiempo: 7 días

## Cómo pagar (desde Termux, sin tarjeta tuya)
1. Crea cuenta Stripe: termux-open https://dashboard.stripe.com/register
2. Crea Payment Link: https://dashboard.stripe.com/payment-links -> $49, $149, $499
3. O 【entity-PayPal¦canonical_name=PayPal】: https://www.paypal.com/paypalme/MarcoValdovinos (ya tienes)

## Cómo certificas (tú)
```bash
# Cliente te paga, tú corres:
./certify.sh cliente-repo 60 40 cliente-nombre
# Genera SCDR-CERT, SHA256, W3C VC, página, etc.

