const fs=require('fs'); const vm=require('vm');
const html=fs.readFileSync(require('path').join(__dirname,'..','index.html'),'utf8');
const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
function grab(name){ const m=js.match(new RegExp('const '+name+'[ ]*=')); const i=m?m.index:-1; if(i<0) throw name; // find matching end by bracket count
  let j=js.indexOf('=',i)+1; while(/\s/.test(js[j]))j++; const open=js[j], close=open=='['?']':'}'; let d=0,k=j, inStr=null;
  for(;k<js.length;k++){ const c=js[k]; if(inStr){ if(c=='\\'){k++;continue;} if(c==inStr) inStr=null; continue;} if(c=='"'||c=="'"||c=='`'){inStr=c;continue;} if(c==open)d++; else if(c==close){d--; if(d==0)break;} }
  return js.slice(i,k+1)+';'; }
const helpers=`const has = re => t => re.test(t); const countRe=(re,n)=>t=>(t.match(re)||[]).length>=n; const CITE=/x/g; function words(t){return 0}`;
const names=['PROJECTS','SKILLS','METHOD','DOSSIER','STAGES','SECTIONS','THINK','AI_RULES','GLOSS','LV_NAMES','CRITS'];
const code=helpers+names.map(grab).join('\n')+'\nout={'+names.join(',')+'}';
const ctx={}; vm.createContext(ctx); vm.runInContext(code,ctx);
const o=JSON.parse(JSON.stringify(ctx.out)); fs.writeFileSync(require('path').join(__dirname,'data.json'),JSON.stringify(o,null,1));
console.log(Object.keys(o).map(k=>k+':'+o[k].length).join(' '));
