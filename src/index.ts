export function anchorSCDR(scdrId, humanPct) {
  const ts = new Date().toISOString();
  const content = `${scdrId}-${humanPct}-${ts}`;
  // Simula hash
  const hash = content.split('').reduce((a,b)=>{a=((a<<5)-a)+b.charCodeAt(0);return a&a},0).toString(16);
  const cid = `bafybeig${hash.slice(0,40)}`;
  const tx = `0x${hash}`;
  return { id: scdrId, ipfs_cid: cid, polygon_tx: tx, verify_ipfs: `https://ipfs.io/ipfs/${cid}`, verify_polygon: `https://polygonscan.com/tx/${tx}` };
}
