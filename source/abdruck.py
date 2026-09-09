#!/usr/bin/env python3
# «Der Abdruck» — die 3D-Fassung. Liest versions/quiet/index.html, ersetzt das
# Hero durch eine gescrollte WebGL-Sequenz und dunkelt die restliche Seite ab.
import pathlib, json, re, importlib.util

_root = pathlib.Path(__file__).resolve().parent
if _root.name == "source":
    _root = _root.parent
src = (_root / "versions" / "quiet" / "index.html").read_text(encoding="utf-8")

_spec = importlib.util.spec_from_file_location("abdruck_copy", str(pathlib.Path(__file__).resolve().parent / "abdruck_copy.py"))
_ac = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_ac)
S = _ac.S

# ------------------------------------------------------------------ 1. Hero raus
m = re.search(r'\n<section class="hero">.*?\n</section>\n', src, re.S)
assert m, "hero block"
src = src[:m.start()] + "\n" + src[m.end():]

# ------------------------------------------------------------------ 2. Markup
STAGE = """
<a class="ab-skip" href="#argument">Zum Inhalt springen</a>
<div id="ab" aria-hidden="true">
  <canvas id="abgl"></canvas>
  <div id="abposter"></div>
</div>
<section id="acts" aria-label="Auftakt">
  <div class="ab-copy">
    <p class="ab-era" id="abEra">Der Auszug</p>
    <h1 class="ab-line" id="abLine">Alles steht darin. Gelesen wird es nicht.</h1>
  </div>
  <div class="ab-rail" aria-hidden="true">
    <span class="ab-track"><i id="abDot"></i></span>
    <ol id="abMarks"><li>Auszug</li><li>Licht</li><li>Satz</li><li>Zustellung</li></ol>
  </div>
  <p class="ab-hint" id="abHint" aria-hidden="true">scrollen</p>
  <div class="ab-prose">
    <p>Der Prolog zeigt einen einzigen Körper über fünftausend Jahre: rohen Stein am Feuer, nassen Ton in Uruk, das Auseinanderdriften von Buch und Erzählung, den ungeöffneten Vorsorgeausweis von heute und zuletzt eine Fläche, die von innen leuchtet.</p>
  </div>
</section>
"""

j = src.index('<main id="main">')
j = src.index("\n", j) + 1
src = src[:j] + STAGE.strip("\n") + "\n" + src[j:]

# ------------------------------------------------------------------ 3. CSS
CSS = r"""
<style>
/* ============================================================
   DER ABDRUCK — dunkler Raum, ein Körper, streifendes Licht
   ============================================================ */
:root{
  --paper:#0B0A09;
  --paper-2:#141210;
  --paper-bright:#F6F3EC;
  --ink:#EDE7DC;
  --ink-soft:#9E978C;
  --rule:#241F19;
  --rule-soft:#1A1613;
  --accent:#C08A4A;
  --accent-ink:#D8A868;
  --field:#3A342C;
  --licht:#FFE8C6;
}
html,body{background:#0B0A09}
body{color:var(--ink)}
body:before{
  content:"";position:fixed;inset:0;z-index:60;pointer-events:none;opacity:.04;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='180' height='180' filter='url(%23n)'/></svg>");
}

/* --- die feste Leinwand hinter allem --- */
#ab{position:fixed;inset:0;z-index:0;opacity:0;transition:opacity .5s ease;pointer-events:none}
#ab.on{opacity:1}
#abgl{display:block;width:100%;height:100%}
#abposter{
  position:absolute;inset:0;display:none;
  background:
    radial-gradient(60% 45% at 62% 44%,rgba(255,207,154,.30),transparent 62%),
    radial-gradient(120% 90% at 50% 50%,#191510,#0B0A09 72%);
}
#abposter:after{
  content:"";position:absolute;left:50%;top:50%;width:min(300px,40vw);aspect-ratio:3/4;
  transform:translate(-40%,-50%);
  background:linear-gradient(104deg,#2A2318,#8A6540 40%,#C9C4B6 76%,#3E362C);
  box-shadow:0 60px 120px -60px #000;
}

/* --- die Akte: nur Höhe, der Inhalt ist die Leinwand --- */
#acts{position:relative;z-index:2;height:560vh}
.ab-copy{
  position:sticky;top:0;height:100vh;display:flex;flex-direction:column;justify-content:flex-end;
  width:min(1180px,100% - 2*clamp(20px,5vw,64px));margin-inline:auto;
  padding-bottom:clamp(70px,11vh,132px);pointer-events:none;
}
.ab-era{
  margin:0 0 16px;font:400 11.5px/1.5 var(--mono);letter-spacing:.2em;color:var(--accent-ink);
  opacity:0;transform:translateY(10px);transition:opacity .5s ease,transform .5s ease;
}
.ab-line{
  margin:0;font-weight:400;font-size:clamp(28px,4.8vw,68px);line-height:1.03;letter-spacing:-0.032em;
  max-width:19ch;color:#F6F1E8;text-wrap:balance;
  opacity:0;transform:translateY(16px);transition:opacity .6s ease,transform .7s cubic-bezier(.16,1,.3,1);
  text-shadow:0 2px 40px rgba(0,0,0,.75);
}
#acts.show .ab-era,#acts.show .ab-line{opacity:1;transform:none}
#acts.finale .ab-line{color:#171310;text-shadow:none}
#acts.finale .ab-era{color:#6B4B22}

.ab-rail{position:fixed;right:clamp(14px,3vw,44px);top:50%;transform:translateY(-50%);z-index:3;display:flex;gap:14px;opacity:0;transition:opacity .4s ease}
#acts.show ~ * .ab-rail,.ab-rail.on{opacity:1}
.ab-track{position:relative;width:1px;background:rgba(255,255,255,.14);height:clamp(170px,28vh,250px)}
.ab-track i{position:absolute;left:-3px;width:7px;height:7px;border-radius:50%;background:var(--accent);top:0;transition:top .12s linear}
.ab-rail ol{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;justify-content:space-between;height:clamp(170px,28vh,250px)}
.ab-rail li{font:400 10.5px/1 var(--mono);letter-spacing:.08em;color:rgba(255,255,255,.3);transition:color .3s ease}
.ab-rail li.on{color:var(--accent-ink)}
.ab-hint{
  position:fixed;left:50%;bottom:22px;transform:translateX(-50%);z-index:3;margin:0;
  font:400 10px/1 var(--mono);letter-spacing:.24em;color:rgba(255,255,255,.34);
  transition:opacity .4s ease;
}
.ab-prose{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.ab-skip{position:absolute;left:-9999px;z-index:80}
.ab-skip:focus{left:14px;top:14px;background:var(--paper-bright);color:#16130F;padding:10px 14px;border:1px solid #16130F}

/* --- die restliche Seite, abgedunkelt --- */
.site{position:sticky;z-index:20;background:rgba(11,10,9,.86);backdrop-filter:saturate(140%) blur(14px);border-bottom-color:var(--rule)}
main > section.sec,footer{position:relative;z-index:2;background:#0B0A09}
.window,.frame{color:#15120F}
.frame .pv-h,.frame .pv-h2,.frame .pv-num,.frame .sample{color:#15120F}
.frame .pv-kicker,.frame .pv-numlabel,.frame .pv-line,.frame .pv-p{color:#5E574D}
.frame .colrule{background:#E4E0D5}
.frame{border-color:#2B2620}
.frame .tc{color:#8A8378}
.combo{background:#141210;border-color:var(--rule)}
.stage{background:#0F0D0B;border-color:var(--rule)}
.stagehead{border-bottom-color:var(--rule);color:var(--ink-soft)}
.verts tr:hover td{background:rgba(192,138,74,.07)}
.livelink a{color:var(--accent-ink)}
.d-scroll,.d-spread,.d-phone{box-shadow:0 40px 70px -40px rgba(0,0,0,.95)}
.skip:focus{background:var(--paper-bright);color:#15120F;border-color:#15120F}
h2{letter-spacing:-0.03em}

@media (max-width:820px){
  #acts{height:460vh}
  .ab-rail{display:none}
}
@media (prefers-reduced-motion:reduce){
  #acts{height:auto}
  .ab-copy{position:static;height:auto;padding:70px 0;display:block}
  .ab-era,.ab-line{opacity:1;transform:none}
  #ab,.ab-hint,.ab-rail{display:none}
}
</style>
"""

src = src.replace("</head>", CSS.strip() + "\n</head>", 1)
src = src.replace('<meta name="theme-color" content="#E7E7E1">',
                  '<meta name="theme-color" content="#0B0A09">', 1)

# ------------------------------------------------------------------ 4. Script
JS = r"""
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
/* ============================================================
   DER ABDRUCK — ein Körper, fünf Akte, eine Lichtquelle.
   Reliefmapping mit Selbstverschattung, Godrays, Korn.
   Die Schicht ist additiv: ohne dieses Script bleibt die Seite ganz.
   ============================================================ */
(function(){
"use strict";
var COPY = __COPY__;
var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var noGuard = /noguard/.test(location.search);

var acts   = document.getElementById("acts");
var wrapEl = document.getElementById("ab");
var canvas = document.getElementById("abgl");
var poster = document.getElementById("abposter");
var eraEl  = document.getElementById("abEra");
var lineEl = document.getElementById("abLine");
var marks  = document.getElementById("abMarks");
var dot    = document.getElementById("abDot");
var rail   = document.querySelector(".ab-rail");
var hint   = document.getElementById("abHint");
var skip   = document.querySelector(".ab-skip");
if(!acts){return;}

function lang(){ var l=document.documentElement.lang||"de"; return COPY[l]?l:"de"; }
var shown = -1;
function paint(force){
  var c = COPY[lang()];
  if(skip){skip.textContent = c.skip;}
  if(hint && c.hint){hint.textContent = c.hint;}
  if(marks){ for(var i=0;i<marks.children.length && i<c.r.length;i++){ marks.children[i].textContent = c.r[i]; } }
  if(shown >= 0 && (force || eraEl.getAttribute("data-a") !== String(shown))){
    eraEl.textContent  = c["e"+shown];
    lineEl.textContent = c["l"+shown];
    eraEl.setAttribute("data-a", shown);
  }
}
new MutationObserver(function(){paint(true);}).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});

/* ---------- reduzierte Bewegung: fünf ruhige Absätze ---------- */
if (reduce){
  var c = COPY[lang()], box = document.createElement("div");
  for (var i=0;i<5;i++){
    var e = document.createElement("p"); e.className="ab-era"; e.style.opacity=1; e.textContent=c["e"+i];
    var h = document.createElement("p"); h.className="ab-line"; h.style.opacity=1; h.style.margin="0 0 44px"; h.textContent=c["l"+i];
    box.appendChild(e); box.appendChild(h);
  }
  var cp = document.querySelector(".ab-copy"); cp.innerHTML=""; cp.appendChild(box);
  paint(true);
  return;
}
shown = 0; paint(true);

if (typeof THREE === "undefined"){ poster.style.display="block"; wrapEl.classList.add("on"); return; }

/* ---------- Renderer ---------- */
var renderer;
try{ renderer = new THREE.WebGLRenderer({canvas:canvas, antialias:false, alpha:false}); }
catch(e){ poster.style.display="block"; wrapEl.classList.add("on"); return; }
var DPR = Math.min(window.devicePixelRatio||1, 1.75);
renderer.setPixelRatio(DPR);
renderer.setSize(innerWidth, innerHeight, false);
renderer.toneMapping = THREE.NoToneMapping;      /* Tonwert kommt im Post-Pass */
renderer.autoClear = true;

var scene  = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(28, innerWidth/innerHeight, 0.1, 90);
camera.position.set(0.0, 0.0, 11.0);

/* ---------- Hoehenkarten: vier Zustaende derselben Oberflaeche ----------
   Weiss = hoch. Weich gezeichnet, damit die Relief-Beleuchtung Flanken
   bekommt statt senkrechter Waende: eine Kante wirft nur einen Saum,
   eine Flanke traegt das ganze Licht.                                     */
var NOISE = (function(){
  var n=512,c=document.createElement("canvas"); c.width=c.height=n;
  var x=c.getContext("2d"), id=x.createImageData(n,n), d=id.data;
  for(var i=0;i<d.length;i+=4){ var v=190+((Math.random()*65)|0); d[i]=d[i+1]=d[i+2]=v; d[i+3]=255; }
  x.putImageData(id,0,0); return c;
})();

function tex(draw, blur){
  var W=1024,H=1360,c=document.createElement("canvas");
  c.width=W;c.height=H;
  var x=c.getContext("2d");
  x.fillStyle="#000";x.fillRect(0,0,W,H);
  x.fillStyle="#fff";x.strokeStyle="#fff";
  if(blur){ try{ x.filter="blur("+blur+"px)"; }catch(e){} }
  draw(x,W,H);
  try{ x.filter="none"; }catch(e){}
  /* Mikrorelief: die Flaeche ist nie perfekt glatt */
  x.globalCompositeOperation="lighter"; x.globalAlpha=0.032;
  x.drawImage(NOISE,0,0,W,H);
  x.globalAlpha=1; x.globalCompositeOperation="source-over";
  var t=new THREE.CanvasTexture(c);
  t.wrapS=t.wrapT=THREE.ClampToEdgeWrapping;
  t.minFilter=THREE.LinearMipmapLinearFilter; t.magFilter=THREE.LinearFilter;
  t.anisotropy = renderer.capabilities.getMaxAnisotropy ? Math.min(16, renderer.capabilities.getMaxAnisotropy()) : 1;
  return t;
}

/* I + II — der Auszug: zweihundert Zeilen, wie sie ankommen */
var ROWS = [
 ["Gemeldeter Jahreslohn","118 400.00"],["Koordinationsabzug","-26 460.00"],
 ["Versicherter Lohn","91 940.00"],["Altersguthaben 31.12.2026","301 661.50"],
 ["Altersgutschrift 2027   15.0 %","13 791.00"],["Zinssatz obligatorisch","1.25 %"],
 ["Zinssatz ueberobligatorisch","1.00 %"],["Altersrente ab 65","18 099.70"],
 ["Altersrente ab 62","14 902.30"],["Invalidenrente","45 970.00"],
 ["Ehegattenrente","27 582.00"],["Waisenrente","9 194.00"],
 ["Sparbeitrag Arbeitnehmer","574.62"],["Sparbeitrag Arbeitgeber","861.93"],
 ["Moeglicher Einkauf","64 209.00"],["Deckungsgrad der Kasse","108.4 %"],
 ["WEF-Vorbezug","0.00"],["Verpfaendung","keine"],
 ["Freizuegigkeitsleistung","301 661.50"],["Uebertrag Vorjahr","265 004.20"]
];
var T_TABLE = tex(function(x,W,H){
  x.font="600 21px 'IBM Plex Mono', monospace"; x.textBaseline="alphabetic";
  x.fillText("VORSORGEAUSWEIS   Nr. 4 812 977   gueltig ab 01.01.2027", 62, 74);
  x.fillRect(62,92,W-124,3);
  x.font="400 19px 'IBM Plex Mono', monospace";
  var y=136, i=0;
  while(y < H-58){
    var r = ROWS[i % ROWS.length];
    x.textAlign="left";  x.fillText(r[0], 62, y);
    x.textAlign="right"; x.fillText(r[1], W-62, y);
    if(i % 5 === 4){ x.globalAlpha=0.28; x.fillRect(62,y+9,W-124,2); x.globalAlpha=1; }
    y += 30; i++;
  }
  x.textAlign="left";
}, 1.6);

/* III — der Satz: was aus zweihundert Zeilen wird */
var T_SENT = tex(function(x,W,H){
  x.textAlign="center";
  x.font="600 84px Georgia, 'Times New Roman', serif";
  var L=["Sie haben","dieses Jahr","36 657 Franken","dazugewonnen."];
  for(var i=0;i<L.length;i++) x.fillText(L[i], W/2, H*0.30 + i*118);
  x.globalAlpha=0.55;
  x.font="400 26px 'IBM Plex Mono', monospace";
  x.fillText("301 661.50   -   265 004.20", W/2, H*0.30 + L.length*118 + 76);
  x.globalAlpha=1; x.textAlign="left";
}, 2.4);

/* IV — drei Oberflaechen: Reel, Brief, Edition nebeneinander */
var T_TRI = tex(function(x,W,H){
  var pw=W/3, pad=26;
  /* Reel: hochkant, grosse Balken */
  (function(){
    var ox=pad, w=pw-pad*1.5;
    x.globalAlpha=0.30; x.fillRect(ox,140,w,H-280); x.globalAlpha=1;
    x.fillRect(ox+16,180,w-32,7);
    for(var i=0;i<9;i++){
      var bh=[0.30,0.55,0.42,0.78,0.62,0.95,0.48,0.70,0.36][i]*(w-52);
      x.fillRect(ox+22, 250+i*74, bh, 30);
    }
    x.fillRect(ox+16,H-236,w-32,5);
  })();
  /* Brief: Fliesstext */
  (function(){
    var ox=pw+pad*0.5, w=pw-pad*1.5;
    x.globalAlpha=0.22; x.fillRect(ox,120,w,H-240); x.globalAlpha=1;
    x.fillRect(ox+18,168,w*0.62,13);
    for(var i=0;i<26;i++){
      var lw=(w-52)*(0.55+((i*37)%43)/100);
      x.fillRect(ox+18, 224+i*38, lw, 8);
    }
  })();
  /* Edition: zwei Spalten, Kolumnentitel */
  (function(){
    var ox=pw*2+pad*0.5, w=pw-pad*1.5, cw=(w-46)/2;
    x.globalAlpha=0.16; x.fillRect(ox,100,w,H-200); x.globalAlpha=1;
    x.fillRect(ox+16,150,w-32,4);
    for(var c=0;c<2;c++) for(var i=0;i<30;i++){
      var lw=cw*(0.6+((i*29+c*11)%40)/100);
      x.fillRect(ox+16+c*(cw+14), 196+i*34, lw, 7);
    }
    x.fillRect(ox+16,H-142,w-32,4);
  })();
}, 1.8);

/* V — zugestellt: die fertige Seite, ruhig gesetzt */
var T_PAGE = tex(function(x,W,H){
  var m=118;
  x.font="600 62px Georgia, 'Times New Roman', serif";
  x.fillText("Ihr Jahr", m, 250);
  x.fillText("in vier S\u00e4tzen", m, 322);
  x.globalAlpha=0.5; x.fillRect(m,368,W-m*2,3); x.globalAlpha=1;
  for(var i=0;i<11;i++){
    var lw=(W-m*2)*(0.62+((i*41)%37)/100);
    x.fillRect(m, 428+i*40, lw, 10);
  }
  /* eine kleine Kurve, damit die Seite nicht nur Text ist */
  x.lineWidth=11; x.lineJoin="round"; x.lineCap="round";
  x.beginPath();
  for(var k=0;k<=40;k++){
    var t=k/40, px=m+t*(W-m*2), py=H-300 - Math.pow(t,1.35)*230 + Math.sin(t*9.0)*16;
    if(k===0) x.moveTo(px,py); else x.lineTo(px,py);
  }
  x.stroke();
  x.globalAlpha=0.42; x.fillRect(m,H-168,W-m*2,3); x.globalAlpha=1;
  x.font="400 24px 'IBM Plex Mono', monospace";
  x.fillText("+ 36 657.30", m, H-112);
}, 2.0);

/* ---------- der Körper ---------- */
var VERT = [
"varying vec2 vUv; varying vec3 vViewO;",
"uniform vec3 uCamObj; uniform float uSplit;",
"void main(){",
"  vUv = uv;",
"  vec3 p = position;",
/* Kein Riss: die Flaeche ist ein Blatt, das sich hebt. sign() wuerde die
   Dreiecke ueber der Naht zerren und mitten im Satz einen Schlitz lassen. */
"  float cx = uv.x - 0.5, cy = uv.y - 0.5;",
"  p.z += uSplit * (0.34 - cx*cx*2.6 - cy*cy*0.5);",
"  p.z += 0.055 * sin(uv.y * 6.2831 + 1.1) * (0.4 + uSplit);",
"  p.y += uSplit * 0.16 * cx;",
"  vViewO = uCamObj - p;",
"  gl_Position = projectionMatrix * modelViewMatrix * vec4(p,1.0);",
"}"].join("\n");

var FRAG = [
"precision highp float;",
"varying vec2 vUv; varying vec3 vViewO;",
"uniform sampler2D uHA; uniform sampler2D uHB;",
"uniform float uMix, uParallax, uNormal, uShadow, uEmissive, uSeed, uSpec, uSheen;",
"uniform vec3 uAlbA, uAlbB; uniform float uColMix;",
"uniform vec3 uLightDir, uLightCol, uAmb;",
"float gK = 0.0;",
"float h(vec2 uv){ return mix(texture2D(uHA,uv).r, texture2D(uHB,uv).r, gK); }",
"void main(){",
/* Der Uebergang ist eine Kante, kein Mittelwert: an jeder Stelle steht
   entweder die Tabelle oder der Satz, nie beides uebereinander. Sonst
   verschmiert das Reliefmapping zwei Hoehenfelder ineinander.           */
"  float wn = fract(sin(dot(floor(vUv*vec2(52.0,68.0)), vec2(12.9898,78.233)))*43758.5453);",
"  float front = vUv.y*0.80 + wn*0.20;",
"  gK = clamp((uMix*1.55 - front*1.15) * 16.0, 0.0, 1.0);",
"  gK = uMix >= 0.999 ? 1.0 : (uMix <= 0.001 ? 0.0 : gK);",
"  vec3 V = normalize(vViewO);",
/* Parallax-Occlusion: der Blick laeuft in die Flaeche hinein, bis er
   auf das Hoehenfeld trifft. Der Sekantenschritt danach nimmt der
   Silhouette die Treppe.                                              */
"  vec2 P = (V.xy / max(V.z, 0.62)) * uParallax * mix(0.40, 1.0, clamp(abs(V.z),0.0,1.0));",
"  float dL = 1.0/24.0;",
"  vec2 dUV = P * dL;",
"  vec2 curUV = vUv; float curLayer = 0.0; float curDepth = 1.0 - h(curUV);",
"  for(int i=0;i<24;i++){",
"    if(curLayer >= curDepth) break;",
"    curUV -= dUV; curDepth = 1.0 - h(curUV); curLayer += dL;",
"  }",
"  vec2 prevUV = curUV + dUV;",
"  float a = curDepth - curLayer;",
"  float b = (1.0 - h(prevUV)) - (curLayer - dL);",
"  vec2 uv = mix(curUV, prevUV, clamp(a/(a-b+1e-5), 0.0, 1.0));",
"  uv = clamp(uv, 0.0015, 0.9985);",
/* Normale aus dem Hoehengradienten */
"  float e = 1.0/1024.0;",
"  float hx = h(uv+vec2(e,0.0)) - h(uv-vec2(e,0.0));",
"  float hy = h(uv+vec2(0.0,e)) - h(uv-vec2(0.0,e));",
"  vec3 N = normalize(vec3(-hx*uNormal, -hy*uNormal, 1.0));",
"  vec3 L = normalize(uLightDir);",
"  float h0 = h(uv);",
/* Umgebungsverdeckung: was tiefer liegt als seine Nachbarn, bekommt weniger Streulicht */
"  float e2 = 3.5/1024.0;",
"  float nb = (h(uv+vec2(e2,0.0)) + h(uv-vec2(e2,0.0)) + h(uv+vec2(0.0,e2)) + h(uv-vec2(0.0,e2))) * 0.25;",
"  float ao = clamp(1.0 - max(nb - h0, 0.0) * 3.2, 0.30, 1.0);",
/* Selbstverschattung: ein Marsch entlang der Lichtrichtung */
"  float occ = 0.0;",
"  if(L.z > 0.04){",
"    vec2 sp = (L.xy/max(L.z,0.42)) * uParallax * 0.70;",
"    for(int s=1;s<=10;s++){",
"      float t = float(s)/10.0;",
"      float hs = h(clamp(uv + sp*t, 0.0015, 0.9985));",
"      occ = max(occ, (hs - (h0 + t*(1.0-h0))) * 16.0);",
"    }",
"  }",
"  float sh = clamp(1.0 - occ, 0.0, 1.0);",
"  sh = mix(1.0, sh, uShadow);",
"  float ndl = max(dot(N,L), 0.0);",
/* Glanz und Kantenschimmer: die Oberflaeche bekommt ein Material */
"  vec3 Hv = normalize(L + V);",
"  float spec = pow(max(dot(N,Hv), 0.0), 42.0) * uSpec;",
"  float fres = pow(1.0 - clamp(dot(N,V), 0.0, 1.0), 4.0) * uSheen;",
"  vec3 alb = mix(uAlbA, uAlbB, uColMix);",
"  float g = fract(sin(dot(uv*vec2(1234.5,4321.9)+uSeed, vec2(12.9898,78.233)))*43758.5453);",
"  alb *= 0.94 + g*0.12;",
"  vec3 col = alb * (uAmb * ao + uLightCol * ndl * sh * ao);",
"  col += uLightCol * spec * mix(0.30, 1.0, sh);",
"  col += uLightCol * fres * 0.30;",
"  col += alb * uEmissive * (0.55 + h0*0.9);",
"  gl_FragColor = vec4(col, 1.0);",
"}"].join("\n");

var U = {
  uHA:{value:T_TABLE}, uHB:{value:T_TABLE}, uMix:{value:0.0},
  uParallax:{value:0.030}, uNormal:{value:26.0}, uShadow:{value:1.0},
  uEmissive:{value:0.0}, uSeed:{value:0.0},
  uSpec:{value:0.30}, uSheen:{value:0.22},
  uAlbA:{value:new THREE.Color(0x24282D)}, uAlbB:{value:new THREE.Color(0x24282D)}, uColMix:{value:0.0},
  uLightDir:{value:new THREE.Vector3(1,0.1,0.14)},
  uLightCol:{value:new THREE.Color(0x8FA6C4)},
  uAmb:{value:new THREE.Color(0x0A0C10)},
  uCamObj:{value:new THREE.Vector3()}, uSplit:{value:0.0}
};
var slab = new THREE.Mesh(
  new THREE.PlaneGeometry(3.3, 4.4, 48, 64),
  new THREE.ShaderMaterial({uniforms:U, vertexShader:VERT, fragmentShader:FRAG})
);
scene.add(slab);

/* ---------- Staub, nur im Strahl ---------- */
var dust;
(function(){
  var n=560, pos=new Float32Array(n*3), sz=new Float32Array(n);
  for(var i=0;i<n;i++){
    pos[i*3]=(Math.random()-0.5)*11; pos[i*3+1]=(Math.random()-0.5)*8; pos[i*3+2]=(Math.random()-0.5)*6+1.4;
    sz[i]=Math.random()*2.2+0.7;
  }
  var g=new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.BufferAttribute(pos,3));
  g.setAttribute("aSize", new THREE.BufferAttribute(sz,1));
  dust = new THREE.Points(g, new THREE.ShaderMaterial({
    transparent:true, depthWrite:false, blending:THREE.AdditiveBlending,
    uniforms:{uOpacity:{value:0.0}, uCol:{value:new THREE.Color(0xFFD9A8)}, uDpr:{value:DPR}},
    vertexShader:[
      "attribute float aSize; varying float vF; uniform float uDpr;",
      "void main(){",
      "  vec4 mv = modelViewMatrix * vec4(position,1.0);",
      "  vF = clamp(1.0 - abs(position.z)/4.5, 0.0, 1.0);",
      "  gl_PointSize = aSize * uDpr * (36.0 / -mv.z);",
      "  gl_Position = projectionMatrix * mv;",
      "}"].join("\n"),
    fragmentShader:[
      "precision mediump float; varying float vF;",
      "uniform vec3 uCol; uniform float uOpacity;",
      "void main(){",
      "  vec2 d = gl_PointCoord - 0.5;",
      "  float m = smoothstep(0.5, 0.03, length(d));",
      "  gl_FragColor = vec4(uCol, m * vF * uOpacity);",
      "}"].join("\n")
  }));
  scene.add(dust);
})();

/* ---------- Post: Godrays, ACES, Vignette, Aberration, Korn ---------- */
var rt = new THREE.WebGLRenderTarget(1,1,{minFilter:THREE.LinearFilter,magFilter:THREE.LinearFilter,format:THREE.RGBAFormat});
var postScene = new THREE.Scene();
var postCam = new THREE.OrthographicCamera(-1,1,1,-1,0,1);
var PU = {
  tDiffuse:{value:rt.texture}, uLightUV:{value:new THREE.Vector2(0.5,0.5)},
  uRays:{value:0.0}, uTime:{value:0.0}, uGrain:{value:0.055},
  uCA:{value:0.0035}, uVig:{value:0.9}, uExp:{value:1.0},
  uBloom:{value:0.55}, uBloomR:{value:0.012}
};
postScene.add(new THREE.Mesh(new THREE.PlaneGeometry(2,2), new THREE.ShaderMaterial({
  uniforms:PU, depthTest:false, depthWrite:false,
  vertexShader:"varying vec2 vUv; void main(){ vUv=uv; gl_Position=vec4(position.xy,0.0,1.0); }",
  fragmentShader:[
   "precision highp float; varying vec2 vUv;",
   "uniform sampler2D tDiffuse; uniform vec2 uLightUV;",
   "uniform float uRays, uTime, uGrain, uCA, uVig, uExp, uBloom, uBloomR;",
   "vec3 aces(vec3 x){ return clamp((x*(2.51*x+0.03))/(x*(2.43*x+0.59)+0.14), 0.0, 1.0); }",
   "void main(){",
   "  vec2 uv = vUv; vec2 d = uv - 0.5; float r2 = dot(d,d);",
   "  vec3 c;",
   "  c.r = texture2D(tDiffuse, uv + d*uCA*r2*4.0).r;",
   "  c.g = texture2D(tDiffuse, uv).g;",
   "  c.b = texture2D(tDiffuse, uv - d*uCA*r2*4.0).b;",
   "  vec2 dir = (uLightUV - uv) * (1.0/18.0);",
   "  vec2 s = uv; float w = 1.0; vec3 acc = vec3(0.0);",
   "  for(int i=0;i<18;i++){",
   "    s += dir; vec3 t = texture2D(tDiffuse, s).rgb;",
   "    float lum = max(t.r, max(t.g, t.b));",
   "    acc += t * max(lum - 0.42, 0.0) * w; w *= 0.93;",
   "  }",
   "  c += acc * (uRays/18.0);",
   "  vec3 bl = vec3(0.0);",
   "  for(int q=0;q<12;q++){",
   "    float an = float(q)*0.5236;",
   "    vec2 o = vec2(cos(an), sin(an)) * uBloomR;",
   "    bl += max(texture2D(tDiffuse, uv + o).rgb - 0.50, 0.0);",
   "    bl += max(texture2D(tDiffuse, uv + o*0.45).rgb - 0.50, 0.0);",
   "  }",
   "  c += bl * (uBloom/24.0);",
   "  float ld = length((uv - uLightUV) * vec2(1.0, 0.62));",
   "  c += vec3(1.0,0.88,0.70) * exp(-ld*7.0) * uRays * 0.30;",
   "  c += vec3(1.0,0.94,0.84) * exp(-ld*22.0) * uRays * 0.45;",
   "  c = aces(c * uExp);",
   "  float vig = smoothstep(1.05, 0.22, length(d)*1.22);",
   "  c *= mix(1.0, vig, uVig);",
   "  float n = fract(sin(dot(uv*vec2(937.1,431.7) + uTime, vec2(12.9898,78.233)))*43758.5453);",
   "  c += (n - 0.5) * uGrain;",
   "  gl_FragColor = vec4(c, 1.0);",
   "}"].join("\n")
})));

var OFFX = 0.0;
function resize(){
  var w = innerWidth, h = innerHeight;
  OFFX = w > 980 ? 1.25 : 0.0;
  slab.position.x = OFFX;
  renderer.setSize(w, h, false);
  rt.setSize(Math.round(w*DPR), Math.round(h*DPR));
  camera.aspect = w/h; camera.updateProjectionMatrix();
}
resize();
addEventListener("resize", resize);

/* ---------- Akte ---------- */
function C(hex){ return new THREE.Color(hex); }
var ACTS = [
  /* I  Der Auszug — Licht fast parallel: man sieht, dass etwas dasteht,
        lesen kann man es nicht. Kalt, tief, unberuehrt.                    */
  {hA:T_TABLE, hB:T_TABLE, mix:0.0, a:C(0x22262B), b:C(0x22262B), cm:0,
   az:0.12, el:0.085, col:C(0xA9C0DE), amb:C(0x0E1116), par:0.019, nrm:34.0,
   spec:0.70, shn:0.40,
   cam:new THREE.Vector3(0.00,-0.06,10.9), rays:0.26, em:0.0, split:0.0},

  /* II Der Blickwinkel — dasselbe Relief, das Licht steigt und waermt.
        Die Selbstverschattung wird kurz, die Zeilen werden lesbar.         */
  {hA:T_TABLE, hB:T_TABLE, mix:0.0, a:C(0x3A362E), b:C(0x3A362E), cm:0,
   az:0.24, el:0.46, col:C(0xFFD5A0), amb:C(0x141116), par:0.015, nrm:24.0,
   spec:0.42, shn:0.26,
   cam:new THREE.Vector3(0.10, 0.02, 9.5), rays:0.58, em:0.0, split:0.0},

  /* III Die Uebersetzung — die Flaeche bricht auf, links bleibt die Tabelle,
        rechts steht der Satz. Kamera zurueck, damit man beides sieht.       */
  {hA:T_TABLE, hB:T_SENT, mix:1.0, a:C(0x3A362E), b:C(0x6C6355), cm:1,
   az:0.46, el:0.52, col:C(0xF2E4CD), amb:C(0x14120F), par:0.010, nrm:26.0,
   spec:0.28, shn:0.18,
   cam:new THREE.Vector3(0.00, 0.00,13.1), rays:0.42, em:0.0, split:1.0},

  /* IV Drei Oberflaechen — Licht von der Seite, hoch: jedes Feld faellt
        anders aus, weil es anders im Licht liegt.                          */
  {hA:T_SENT, hB:T_TRI, mix:1.0, a:C(0x6C6355), b:C(0x918C80), cm:1,
   az:1.02, el:0.54, col:C(0xEAF0F6), amb:C(0x181B21), par:0.013, nrm:15.0,
   spec:0.30, shn:0.18,
   cam:new THREE.Vector3(0.00, 0.00,10.4), rays:0.12, em:0.0, split:0.22},

  /* V  Zugestellt — breites, warmes Licht, Papierton, Strahlen und ein
        leichtes Eigenleuchten. Die Seite liegt auf dem Tisch.              */
  {hA:T_TRI, hB:T_PAGE, mix:1.0, a:C(0x918C80), b:C(0xCFC9BA), cm:1,
   az:0.21, el:0.33, col:C(0xFFEBCB), amb:C(0x1B160F), par:0.016, nrm:19.0,
   spec:0.34, shn:0.20,
   cam:new THREE.Vector3(0.00, 0.04, 9.3), rays:1.25, em:0.30, split:0.45}
];

var cur = {
  az:ACTS[0].az, el:ACTS[0].el, par:ACTS[0].par, nrm:ACTS[0].nrm, rays:ACTS[0].rays,
  em:0, split:0, mix:0, cm:0, spec:0, shn:0,
  col:ACTS[0].col.clone(), amb:ACTS[0].amb.clone(),
  a:ACTS[0].a.clone(), b:ACTS[0].b.clone(),
  cam:ACTS[0].cam.clone()
};
function lerp(a,b,t){ return a + (b-a)*t; }

var p = 0, target = 0, ticking = false, running = false;
function readScroll(){
  var r = acts.getBoundingClientRect();
  var span = acts.offsetHeight - innerHeight;
  target = span > 0 ? Math.min(1, Math.max(0, -r.top/span)) : 0;
  var visible = r.bottom > -200 && r.top < innerHeight + 200;
  if (visible !== running){
    running = visible;
    wrapEl.classList.toggle("on", visible);
    if (rail) rail.classList.toggle("on", visible);
    if (hint) hint.style.opacity = visible ? "" : "0";
  }
  ticking = false;
}
addEventListener("scroll", function(){ if(!ticking){ ticking=true; requestAnimationFrame(readScroll);} }, {passive:true});
/* Pruefhaken: nur mit ?noguard, damit sich Akte einzeln anfahren lassen */
if(noGuard){ window.__seek = function(v){ target = v; p = v; running = true; wrapEl.classList.add("on"); }; }
readScroll();

var LIGHT = new THREE.Vector3();
var t0 = performance.now(), frames = 0, lastT = t0, slow = 0, shed = false;

function frame(now){
  requestAnimationFrame(frame);
  var t = (now - t0)/1000;

  if (!noGuard){
    frames++;
    if (now - lastT > 1000){
      if (frames < 30) slow++; else slow = 0;
      frames = 0; lastT = now;
      if (slow === 2 && !shed){ shed = true; DPR = 1; renderer.setPixelRatio(1); resize(); PU.uRays.value *= 0.5; }
      if (slow >= 6){ poster.style.display="block"; canvas.style.display="none"; return; }
    }
  }

  p += (target - p) * 0.10;

  /* Akt und lokaler Fortschritt */
  var f = Math.min(0.9999, Math.max(0, p)) * 5.0;
  var i = Math.floor(f), k = f - i;
  var A = ACTS[Math.min(4,i)], B = ACTS[Math.min(4,i+1)];
  var e = k*k*(3.0-2.0*k);                       /* smoothstep zwischen den Akten */

  cur.az   = lerp(A.az,   B.az,   e);
  cur.el   = lerp(A.el,   B.el,   e);
  cur.par  = lerp(A.par,  B.par,  e);
  cur.nrm  = lerp(A.nrm,  B.nrm,  e);
  cur.rays = lerp(A.rays, B.rays, e);
  cur.em   = lerp(A.em,   B.em,   e);
  cur.split= lerp(A.split,B.split,e);
  cur.spec = lerp(A.spec, B.spec, e);
  cur.shn  = lerp(A.shn,  B.shn,  e);
  cur.col.copy(A.col).lerp(B.col, e);
  cur.amb.copy(A.amb).lerp(B.amb, e);

  /* Höhenkarte: innerhalb eines Akts blenden, an der Grenze umhängen */
  U.uHA.value = A.hA; U.uHB.value = A.hB;
  U.uMix.value = A.mix === 0 ? 0.0 : Math.min(1.0, k/0.72);
  U.uAlbA.value.copy(A.a); U.uAlbB.value.copy(A.b);
  U.uColMix.value = A.cm === 0 ? 0.0 : Math.min(1.0, k/0.72);
  if (e > 0.985 && i < 4){ U.uHA.value = B.hA; U.uHB.value = B.hB; U.uMix.value = 0.0;
                           U.uAlbA.value.copy(B.a); U.uAlbB.value.copy(B.b); U.uColMix.value = 0.0; }

  /* Licht: az ist der Streifwinkel, 0.22 rad = 13° */
  var flick = 0.985 + Math.sin(t*0.9)*0.015;
  LIGHT.set(Math.cos(cur.az)*Math.cos(cur.el), Math.sin(cur.el), Math.sin(cur.az)*Math.cos(cur.el));
  U.uLightDir.value.copy(LIGHT);
  U.uLightCol.value.copy(cur.col).multiplyScalar(flick * 1.85);
  U.uAmb.value.copy(cur.amb);
  U.uParallax.value = cur.par;
  U.uNormal.value   = cur.nrm;
  U.uEmissive.value = cur.em;
  U.uSplit.value    = cur.split;
  U.uSpec.value     = cur.spec;
  U.uSheen.value    = cur.shn;
  U.uSeed.value     = 0.0;

  /* Kamera */
  cur.cam.lerpVectors(A.cam, B.cam, e);
  camera.position.set(cur.cam.x + OFFX*0.55, cur.cam.y + cur.em*0.55, cur.cam.z);
  camera.lookAt(OFFX*0.42, cur.em*0.35, 0);
  U.uCamObj.value.copy(camera.position);

  /* Godray-Ursprung: Lichtrichtung auf den Bildschirm projiziert */
  var lp = LIGHT.clone().multiplyScalar(7.0).project(camera);
  PU.uLightUV.value.set((lp.x+1)/2, (lp.y+1)/2);
  PU.uRays.value = cur.rays;
  PU.uTime.value = t;
  PU.uExp.value  = 1.0;

  /* Staub */
  dust.material.uniforms.uOpacity.value = Math.min(1, Math.max(0, (t-1.0)/1.4)) * (0.30 + cur.rays*0.42);
  var pa = dust.geometry.attributes.position;
  for (var d=1; d<pa.array.length; d+=3){
    pa.array[d] += 0.0022;
    if (pa.array[d] > 4.0) pa.array[d] = -4.0;
  }
  pa.needsUpdate = true;

  /* Text, Lineal, Finale */
  var act = Math.min(4, i);
  if (act !== shown){ shown = act; paint(true); }
  acts.classList.toggle("show", k > 0.06 && k < 0.93);
  acts.classList.toggle("finale", p > 0.955);
  if (dot) dot.style.top = (p*100) + "%";
  if (marks){
    var mi = p < 0.24 ? 0 : (p < 0.46 ? 1 : (p < 0.70 ? 2 : 3));
    for (var q=0; q<marks.children.length; q++) marks.children[q].classList.toggle("on", q === mi);
  }
  if (hint) hint.style.opacity = p > 0.03 ? "0" : "";

  if (!running) return;
  renderer.setRenderTarget(rt);
  renderer.render(scene, camera);
  renderer.setRenderTarget(null);
  renderer.render(postScene, postCam);
}
requestAnimationFrame(frame);
})();
</script>
"""

JS = JS.replace("__COPY__", json.dumps(S, ensure_ascii=False, separators=(",", ":")))
src = src.replace("</body>", JS.strip() + "\n</body>", 1)

_o = _root / "versions" / "3d"
_o.mkdir(parents=True, exist_ok=True)
(_o / "index.html").write_text(src, encoding="utf-8")
print("written", len(src), "bytes -> versions/3d/index.html")
