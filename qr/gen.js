const Q='/opt/node22/lib/node_modules/npm/node_modules/qrcode-terminal/vendor/QRCode';
const QRCode=require(Q), L=require(Q+'/QRErrorCorrectLevel');
const fs=require('fs');
const urls=JSON.parse(fs.readFileSync(process.argv[2],'utf8')); const out={};
for (const [k,u] of Object.entries(urls)){
  const q=new QRCode(-1,L.L); q.addData(u); q.make(); const n=q.getModuleCount(); let d='';
  for(let r=0;r<n;r++)for(let c=0;c<n;c++) if(q.isDark(r,c)) d+=`M${c+4} ${r+4}h1v1h-1z`;
  out[k]={n:n,svg:`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${n+8} ${n+8}" shape-rendering="crispEdges"><rect width="100%" height="100%" fill="#fff"/><path d="${d}" fill="#000"/></svg>`};
}
fs.writeFileSync(process.argv[3],JSON.stringify(out));
