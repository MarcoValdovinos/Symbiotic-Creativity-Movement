#!/usr/bin/env python3
# ARKHE SENTINEL - Rastrea donde se escucha el movimiento
import requests, json, datetime

REPO = "MarcoValdovinos/Symbiotic-Creativity-Movement"
TOKEN = "" # pon tu GH_TOKEN si quieres datos privados

print(f"=== ARKHE ZERO SENTINEL {datetime.datetime.now().isoformat()} ===")
print(f"Repo: {REPO}")

# 1. 【entity-GitHub¦canonical_name=GitHub】 Stats publicos
try:
    r = requests.get(f"https://api.github.com/repos/{REPO}")
    data = r.json()
    print(f"\n[【entity-GitHub¦canonical_name=GitHub】]")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Forks: {data['forks_count']}")
    print(f"Watchers: {data['watchers_count']}")
    print(f"Open Issues: {data['open_issues_count']}")
    print(f"Template: {data['is_template']}")
    print(f"Updated: {data['updated_at']}")
except Exception as e:
    print(f"Error GitHub: {e}")

# 2. Releases
try:
    r = requests.get(f"https://api.github.com/repos/{REPO}/releases")
    rel = r.json()
    print(f"\n[Releases] {len(rel)} versiones")
    for rel_item in rel[:3]:
        print(f"- {rel_item['tag_name']}: {rel_item['name']} - {rel_item['published_at'][:10]}")
except Exception as e:
    print(f"Error releases: {e}")

# 3. Branches / Bifurcaciones
try:
    r = requests.get(f"https://api.github.com/repos/{REPO}/branches")
    branches = r.json()
    print(f"\n[Bifurcaciones] {len(branches)} ramas")
    for b in branches:
        print(f"- {b['name']}")
except Exception as e:
    print(f"Error branches: {e}")

# 4. Cloudflare check
try:
    r = requests.get("https://arkhe-auth.legadodigitalkronos.workers.dev", timeout=5)
    print(f"\n[Cloudflare] Status: {r.status_code} - {len(r.text)} bytes")
except Exception as e:
    print(f"\n[Cloudflare] Error: {e}")

print("\n=== FIN SENTINEL ===")
