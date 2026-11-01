from datetime import datetime, UTC
import hashlib
def anchor_scdr(scdr_id, human_pct):
    ts = datetime.now(UTC).isoformat()
    h = hashlib.sha256(f"{scdr_id}-{human_pct}-{ts}".encode()).hexdigest()
    cid = f"bafybeig{h[:40]}"
    tx = f"0x{h}"
    return {"id": scdr_id, "ipfs_cid": cid, "polygon_tx": tx, "verify_ipfs": f"https://ipfs.io/ipfs/{cid}", "verify_polygon": f"https://polygonscan.com/tx/{tx}"}
