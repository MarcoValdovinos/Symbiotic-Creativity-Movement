#!/usr/bin/env python3
import requests, json, datetime, os

REPO = "MarcoValdovinos/Symbiotic-Creativity-Movement"

print(f"=== ARKHE ZERO SENTINEL {datetime.datetime.now().isoformat()} ===")
print(f"Repo: {REPO}")

# 【entity-GitHub¦canonical_name=GitHub】 public
r = requests.get(f"https://api.github.com/repos/{REPO}")
data = r.json()
print(f"\n[【entity-GitHub¦canonical_name=GitHub】]")
print(f"Stars: {data['stargazers_count']} | Forks: {data['forks_count']} | Watchers: {data['watchers_count']}")
print(f"Template: {data['is_template']} | Updated: {data['updated_at'][:10]}")

# Releases
r = requests.get(f"https://api.github.com/repos/{REPO}/releases")
rel = r.json()
print(f"\n[Releases] {len(rel)}")
for ri in rel[:5]:
    print(f"- {ri['tag_name']}: {ri['name'][:50]}")

# Branches
r = requests.get(f"https://api.github.com/repos/{REPO}/branches")
branches = r.json()
print(f"\n[Bifurcaciones] {len(branches)} ramas")
for b in branches:
    print(f"- {b['name']}")

# Cloudflare
try:
    r = requests.get("https://arkhe-auth.legadodigitalkronos.workers.dev", timeout=5)
    print(f"\n[Cloudflare] LIVE Status {r.status_code} - {len(r.text)} bytes")
except Exception as e:
    print(f"\n[Cloudflare] Error: {e}")

# 【entity-Mercado Pago¦canonical_name=Mercado Pago】
print(f"\n[【entity-Mercado Pago¦canonical_name=Mercado Pago】 LIVE]")
print(f"- Diagnostico $99: https://mpago.la/2YZb7VW")
print(f"- Bronce $149: https://mpago.la/2NZ5fFL")
print(f"- Plata $399: https://mpago.la/2EZNjPh")
print(f"- Oro $799: https://mpago.la/2ngaKaE")
print(f"- Platino $1499: https://mpago.la/2BAwmts")

# Guarda historial
os.makedirs("tools/sentinel/history", exist_ok=True)
with open(f"tools/sentinel/history/{datetime.date.today()}.json", "w") as f:
    json.dump({"date": str(datetime.date.today()), "stars": data['stargazers_count'], "forks": data['forks_count'], "branches": len(branches)}, f)

print("\n=== FIN SENTINEL - Donde se escucha ARKHE ZERO ===")
