#!/usr/bin/env python3
# Variant B — the loud one. Takes the built index.html and produces index-bold.html:
# dark ground, a lit document, and motion used as a device rather than a garnish.
import pathlib

_root = pathlib.Path(__file__).resolve().parent
if _root.name == "source":
    _root = _root.parent
src = (_root / "versions" / "quiet" / "index.html").read_text(encoding="utf-8")
_out = _root / "versions" / "bold"
_out.mkdir(parents=True, exist_ok=True)

CSS = r"""
<style>
/* ============================================================
   VARIANT B — dark ground, lit document, deliberate motion
   ============================================================ */
:root{
  --paper:#0B0C0D;
  --paper-2:#121417;
  --paper-bright:#F6F4EE;
  --ink:#F2F0EA;
  --ink-soft:#A3A9AD;
  --rule:#26292C;
  --rule-soft:#1C1F22;
  --accent:#46B98A;
  --accent-ink:#6FD3A8;
  --field:#3B4045;
  --gold:#E9C36B;
  --glow:160;
}
html{background:var(--paper)}
body{background:var(--paper)}

/* things that sit on light paper keep dark ink */
.window,.frame{color:#14171A}
.window .quiet{color:#5E6569}
.frame .pv-h,.frame .pv-h2,.frame .pv-num,.frame .sample{color:#14171A}
.frame .pv-kicker,.frame .pv-numlabel,.frame .pv-line,.frame .pv-p{color:#5E6569}
.frame .colrule{background:#E3E5E7}
.frame{border-color:#2A2E32}
.frame .tc{color:#8A9096}
.skip:focus{background:var(--paper-bright);color:#14171A;border-color:#14171A}

.site{background:rgba(11,12,13,.82);backdrop-filter:saturate(140%) blur(14px)}
.folds i{background:rgba(255,255,255,.05)}
.window{
  box-shadow:
    0 0 0 1px rgba(255,255,255,.10),
    0 40px 80px -40px rgba(0,0,0,.9),
    0 0 90px -30px hsl(var(--glow) 70% 55% / .35);
}
.combo{background:#121417;border-color:var(--rule)}
.stage{background:#0F1113;border-color:var(--rule);position:relative;overflow:hidden}
.stagehead{border-bottom:1px solid var(--rule);color:var(--ink-soft);position:relative;z-index:2}
.stageview{position:relative;z-index:2}
.verts tr:hover td{background:rgba(70,185,138,.06)}
.livelink a{color:var(--accent-ink)}
.d-scroll,.d-spread,.d-phone{box-shadow:0 40px 70px -40px rgba(0,0,0,.95)}

/* ---------- 1. reading progress ---------- */
.b-prog{position:fixed;top:0;left:0;right:0;height:2px;z-index:60;background:transparent;pointer-events:none}
.b-prog i{
  display:block;height:100%;width:100%;transform-origin:0 50%;transform:scaleX(0);
  background:linear-gradient(90deg,var(--accent),var(--gold));
}

/* ---------- 2. headings rise out of a mask ---------- */
.b-w{display:inline-block;overflow:hidden;vertical-align:bottom;padding-bottom:.06em}
.b-w > i{
  display:inline-block;font-style:inherit;transform:translateY(110%);
  transition:transform .78s cubic-bezier(.16,1,.3,1);transition-delay:calc(var(--i)*42ms);
}
.b-in .b-w > i{transform:none}

/* ---------- 3. the printout feeds out ---------- */
.field .doc{clip-path:inset(0 0 0 0)}
.field .doc.is-on{animation:b-feed 1.15s cubic-bezier(.22,.61,.36,1) both}
@keyframes b-feed{from{clip-path:inset(0 0 100% 0)}to{clip-path:inset(0 0 0 0)}}

/* ---------- 4. the envelope reacts to the pointer ---------- */
.envelope{perspective:1100px}
.field{
  transform:translate3d(calc(var(--mx,0)*-14px),calc(var(--my,0)*-10px),0);
  transition:transform .5s cubic-bezier(.16,1,.3,1);
}
.opening{
  transform:rotateX(calc(var(--my,0)*-2.6deg)) rotateY(calc(var(--mx,0)*3.4deg)) translateZ(0);
  transform-style:preserve-3d;transition:transform .45s cubic-bezier(.16,1,.3,1);
}
.window{position:relative;isolation:isolate}
.window:after{
  content:"";position:absolute;inset:0;pointer-events:none;z-index:1;mix-blend-mode:overlay;
  background:radial-gradient(420px circle at var(--px,50%) var(--py,50%),rgba(255,255,255,.9),transparent 62%);
  opacity:0;transition:opacity .4s ease;
}
.envelope:hover .window:after{opacity:.55}

/* ---------- 5. the hero sentence sets itself word by word ---------- */
.tell.is-on .b-w > i{transform:none}
.tell .b-w > i{transition-duration:.72s}

/* ---------- 6. magnetic controls ---------- */
.btn,.chip,.tellnav button,.d-reelnav button,.langs button{
  will-change:transform;transition:transform .5s cubic-bezier(.16,1,.3,1),background .18s ease,color .18s ease,border-color .18s ease;
}
.btn{position:relative;overflow:hidden;isolation:isolate}
.btn:before{
  content:"";position:absolute;inset:0;z-index:-1;background:var(--accent-ink);
  transform:translateY(101%);transition:transform .42s cubic-bezier(.16,1,.3,1);
}
.btn:hover:before{transform:translateY(0)}
.btn:hover{background:var(--accent)}

/* ---------- 7. the five documents run past ---------- */
.b-marquee{
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);
  overflow:hidden;padding:14px 0;background:#0E1012;
}
.b-track{display:flex;width:max-content;animation:b-run 34s linear infinite}
.b-marquee:hover .b-track{animation-play-state:paused}
.b-track span{
  font:400 13px/1 var(--mono);letter-spacing:.14em;text-transform:none;color:var(--ink-soft);
  padding:0 26px;white-space:nowrap;
}
.b-track span b{color:var(--accent);font-weight:400;padding-right:26px}
@keyframes b-run{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ---------- 8. the pill follows the choice ---------- */
.chiprow{position:relative}
.b-pill{
  position:absolute;top:0;left:0;height:0;width:0;border-radius:2px;background:var(--accent);
  transition:transform .5s cubic-bezier(.16,1,.3,1),width .5s cubic-bezier(.16,1,.3,1),height .3s ease;
  pointer-events:none;z-index:0;
}
.chip{position:relative;z-index:1;background:transparent}
.chip[aria-pressed="true"]{background:transparent;border-color:transparent;color:#0B0C0D}
.chip:hover{border-color:var(--ink-soft)}

/* ---------- 9. every vertical has its own light ---------- */
.stage:before{
  content:"";position:absolute;inset:-2px;z-index:1;pointer-events:none;
  background:radial-gradient(70% 60% at 50% -4%,hsl(var(--glow) 62% 48% / .22),transparent 72%);
  transition:background .7s ease;
}

/* ---------- 10. the format morphs in ---------- */
@keyframes b-morph{
  from{opacity:0;transform:scale(.955) translateY(10px);filter:blur(9px)}
  to{opacity:1;transform:none;filter:blur(0)}
}
.b-morph{animation:b-morph .58s cubic-bezier(.16,1,.3,1) both}

/* ---------- 11. the reel plays itself ---------- */
.d-rbar i{position:relative;overflow:hidden}
.d-rbar i.now b{
  position:absolute;inset:0;display:block;background:var(--d-ink);
  transform-origin:0 50%;transform:scaleX(0);animation:b-fill var(--dwell,4200ms) linear both;
}
.d-rbar i.now{background:#E2E4E6}
@keyframes b-fill{to{transform:scaleX(1)}}
.d-phone{cursor:grab;touch-action:pan-y}
.d-phone:active{cursor:grabbing}

/* ---------- 12. rows step forward ---------- */
.verts tbody tr{transition:transform .45s cubic-bezier(.16,1,.3,1)}
.verts tbody tr:hover{transform:translateX(7px)}
.verts tbody tr td:first-child{position:relative}
.verts tbody tr td:first-child:before{
  content:"";position:absolute;left:-14px;top:1.05em;width:0;height:1px;background:var(--accent);
  transition:width .45s cubic-bezier(.16,1,.3,1);
}
.verts tbody tr:hover td:first-child:before{width:8px}

/* ---------- 13. the previews come alive under the cursor ---------- */
.obj .frame{transition:transform .55s cubic-bezier(.16,1,.3,1),box-shadow .55s ease}
.obj:hover .frame{transform:translateY(-6px);box-shadow:0 34px 56px -34px rgba(0,0,0,.9)}
.obj:hover .f-reel .pace i:nth-child(2){background:var(--accent)}
.obj .pace i{transition:background .35s ease}
.obj .f-edition .page:last-child{
  transform-origin:left center;transition:transform .6s cubic-bezier(.16,1,.3,1);
}
.obj:hover .f-edition .page:last-child{transform:perspective(700px) rotateY(-9deg)}
.obj .f-brief .pv-rules{transition:transform .6s cubic-bezier(.16,1,.3,1)}
.obj:hover .f-brief .pv-rules{transform:translateY(-6px)}

/* ---------- 14. links and nav ---------- */
.sections a{position:relative;border-bottom:0}
.sections a:after{
  content:"";position:absolute;left:0;right:0;bottom:-2px;height:1px;background:var(--accent);
  transform:scaleX(0);transform-origin:100% 50%;transition:transform .4s cubic-bezier(.16,1,.3,1);
}
.sections a:hover:after{transform:scaleX(1);transform-origin:0 50%}


/* ---------- 16. oversized display, full-bleed hero, fine grain ---------- */
body:before{
  content:"";position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.035;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");
}
.site,main,footer{position:relative;z-index:1}
.envelope{min-height:clamp(470px,72vh,740px)}
.opening{width:min(860px,100%)}
.window h1{font-size:clamp(31px,5.3vw,74px);line-height:1.05;letter-spacing:-0.032em}
h2{font-size:clamp(30px,4.5vw,58px);letter-spacing:-0.03em;max-width:17ch;line-height:1.04}
.pull{font-size:clamp(23px,3.1vw,40px);line-height:1.16;max-width:24ch;border-left-width:3px}
.combo-out{font-size:clamp(30px,4.3vw,54px);letter-spacing:-0.03em}
.lede{font-size:clamp(18px,1.7vw,23px)}
.mark{font-size:22px;letter-spacing:-0.03em}
.btn{background:#2F9E75;border-color:#2F9E75;color:#F6F4EE;font-size:17px;padding:14px 26px}
.btn:before{background:#3FB98A}
.btn-lg{font-size:19px;padding:17px 34px}
.field pre{color:var(--field)}
.hero{padding:clamp(28px,5vh,64px) 0 clamp(46px,8vh,96px)}

/* ---------- 15. quieter for those who asked ---------- */
@media (prefers-reduced-motion:reduce){
  .b-w > i{transform:none!important}
  .field .doc.is-on{animation:none}
  .b-track{animation:none;transform:none}
  .b-marquee{display:none}
  .d-rbar i.now b{animation:none;transform:scaleX(1)}
  .b-morph{animation:none}
  .field,.opening{transform:none!important}
  .b-prog{display:none}
}
</style>
"""

JS = r"""
<script>
/* ============================================================
   VARIANT B — motion layer. Everything here is additive: the
   page works with this script removed.
   ============================================================ */
(function(){
"use strict";
var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- reading progress ---------- */
(function(){
  if(reduce){return;}
  var el=document.createElement("div");
  el.className="b-prog";el.setAttribute("aria-hidden","true");
  el.innerHTML="<i></i>";
  document.body.appendChild(el);
  var bar=el.firstChild,ticking=false;
  function upd(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.transform="scaleX("+(h>0?Math.min(1,window.scrollY/h):0)+")";
    ticking=false;
  }
  addEventListener("scroll",function(){if(!ticking){ticking=true;requestAnimationFrame(upd);}},{passive:true});
  upd();
})();

/* ---------- split words for the mask reveal ---------- */
function splitWords(el){
  if(el.getAttribute("data-split")==="1"){return;}
  var walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT,null),nodes=[],n;
  while((n=walker.nextNode())){if(n.nodeValue.trim()){nodes.push(n);}}
  var idx=0;
  for(var i=0;i<nodes.length;i++){
    var parts=nodes[i].nodeValue.split(/(\s+)/),frag=document.createDocumentFragment();
    for(var j=0;j<parts.length;j++){
      if(!parts[j]){continue;}
      if(/^\s+$/.test(parts[j])){frag.appendChild(document.createTextNode(parts[j]));continue;}
      var w=document.createElement("span");w.className="b-w";
      var inner=document.createElement("i");
      inner.textContent=parts[j];
      inner.style.setProperty("--i",idx++);
      w.appendChild(inner);frag.appendChild(w);
    }
    nodes[i].parentNode.replaceChild(frag,nodes[i]);
  }
  el.setAttribute("data-split","1");
}

/* ---------- headings rise when they arrive ---------- */
var headObserver=null;
function armHeadings(){
  var hs=document.querySelectorAll("h2, .pull, .why h3, .combo-out");
  for(var i=0;i<hs.length;i++){
    splitWords(hs[i]);
    if(reduce||!("IntersectionObserver" in window)){hs[i].classList.add("b-in");continue;}
    if(!headObserver){
      headObserver=new IntersectionObserver(function(es){
        for(var k=0;k<es.length;k++){
          if(es[k].isIntersecting){es[k].target.classList.add("b-in");headObserver.unobserve(es[k].target);}
        }
      },{threshold:.35});
    }
    if(!hs[i].classList.contains("b-in")){headObserver.observe(hs[i]);}
  }
}

/* ---------- the hero sentence sets itself ---------- */
function armTells(){
  var t=document.querySelectorAll(".tell");
  for(var i=0;i<t.length;i++){
    t[i].removeAttribute("data-split");
    splitWords(t[i]);
  }
}

/* ---------- pointer parallax on the envelope ---------- */
(function(){
  var env=document.querySelector(".envelope");
  if(!env||reduce){return;}
  env.addEventListener("pointermove",function(e){
    var r=env.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
    env.style.setProperty("--mx",(x-.5)*2);
    env.style.setProperty("--my",(y-.5)*2);
    var w=env.querySelector(".window");
    if(w){
      var wr=w.getBoundingClientRect();
      w.style.setProperty("--px",((e.clientX-wr.left)/wr.width*100)+"%");
      w.style.setProperty("--py",((e.clientY-wr.top)/wr.height*100)+"%");
    }
  });
  env.addEventListener("pointerleave",function(){
    env.style.setProperty("--mx",0);env.style.setProperty("--my",0);
  });
})();

/* ---------- magnetic controls ---------- */
(function(){
  if(reduce){return;}
  function magnet(el,strength){
    el.addEventListener("pointermove",function(e){
      var r=el.getBoundingClientRect();
      var dx=(e.clientX-(r.left+r.width/2))/r.width;
      var dy=(e.clientY-(r.top+r.height/2))/r.height;
      el.style.transform="translate("+(dx*strength)+"px,"+(dy*strength*.7)+"px)";
    });
    el.addEventListener("pointerleave",function(){el.style.transform="";});
  }
  function arm(){
    var els=document.querySelectorAll(".btn:not([data-mag]),.chip:not([data-mag]),.tellnav button:not([data-mag]),.d-reelnav button:not([data-mag])");
    for(var i=0;i<els.length;i++){els[i].setAttribute("data-mag","1");magnet(els[i],els[i].classList.contains("btn")?10:6);}
  }
  arm();
  window.__boldMagnet=arm;
})();

/* ---------- the five documents run past ---------- */
(function(){
  if(reduce){return;}
  var verticals=document.getElementById("verticals");
  if(!verticals){return;}
  var wrap=document.createElement("div");
  wrap.className="b-marquee";wrap.setAttribute("aria-hidden","true");
  wrap.innerHTML='<div class="b-track"></div>';
  verticals.parentNode.insertBefore(wrap,verticals);
  function fill(){
    var labels=[],btns=document.querySelectorAll(".tellnav button");
    for(var i=0;i<btns.length;i++){labels.push(btns[i].textContent.trim());}
    if(!labels.length){return;}
    var one="";
    for(var j=0;j<labels.length;j++){one+='<span>'+labels[j]+'<b> —</b></span>';}
    wrap.firstChild.innerHTML=one+one+one+one;
  }
  fill();
  window.__boldMarquee=fill;
})();

/* ---------- the pill follows the choice ---------- */
(function(){
  var rows=document.querySelectorAll(".chiprow");
  function place(row,animate){
    var pill=row.querySelector(".b-pill");
    var on=row.querySelector('[aria-pressed="true"]');
    if(!pill||!on){return;}
    var r=on.getBoundingClientRect(),rr=row.getBoundingClientRect();
    if(!animate){pill.style.transition="none";}
    pill.style.width=r.width+"px";
    pill.style.height=r.height+"px";
    pill.style.transform="translate("+(r.left-rr.left)+"px,"+(r.top-rr.top)+"px)";
    if(!animate){void pill.offsetWidth;pill.style.transition="";}
  }
  for(var i=0;i<rows.length;i++){
    if(!rows[i].querySelector(".chip")){continue;}
    var pill=document.createElement("span");
    pill.className="b-pill";pill.setAttribute("aria-hidden","true");
    rows[i].insertBefore(pill,rows[i].firstChild);
    (function(row){
      place(row,false);
      row.addEventListener("click",function(){requestAnimationFrame(function(){place(row,!reduce);});});
    })(rows[i]);
  }
  addEventListener("resize",function(){
    for(var k=0;k<rows.length;k++){place(rows[k],false);}
  });
  window.__boldPills=function(){for(var k=0;k<rows.length;k++){place(rows[k],false);}};
})();

/* ---------- each vertical brings its own light ---------- */
var HUE={Portfolio:168,Pension:200,School:44,Health:344,Team:272};
function tint(){
  var on=document.querySelector("[data-v][aria-pressed='true']");
  var v=on?on.getAttribute("data-v"):"Pension";
  document.documentElement.style.setProperty("--glow",HUE[v]||160);
}

/* ---------- the stage: morph, autoplay, drag ---------- */
var reelTimer=null,reelLocked=false;
function currentFormat(){
  var on=document.querySelector("[data-f][aria-pressed='true']");
  return on?on.getAttribute("data-f"):"Brief";
}
function stopReel(){if(reelTimer){clearTimeout(reelTimer);reelTimer=null;}}
function boldStage(){
  var view=document.getElementById("stageview");
  if(!view){return;}
  tint();
  var device=view.firstElementChild;
  if(device&&!reduce){
    device.classList.remove("b-morph");void device.offsetWidth;device.classList.add("b-morph");
  }
  if(window.__boldMagnet){window.__boldMagnet();}
  stopReel();
  if(currentFormat()!=="Reel"||reduce||reelLocked){return;}

  var segs=view.querySelectorAll(".d-rbar i");
  var next=view.querySelector('.d-reelnav [data-reel="1"]');
  var last=-1;
  for(var i=0;i<segs.length;i++){if(segs[i].className.indexOf("on")>-1){last=i;}}
  var dwell=4200;
  if(last>-1){
    segs[last].classList.add("now");
    segs[last].style.setProperty("--dwell",dwell+"ms");
    segs[last].innerHTML="<b></b>";
  }
  if(!next||last>=segs.length-1){return;}
  reelTimer=setTimeout(function(){if(next){next.click();}},dwell);
}
(function(){
  var view=document.getElementById("stageview");
  if(!view){return;}
  var mo=new MutationObserver(function(){boldStage();});
  mo.observe(view,{childList:true});
  /* a click on the controls means the visitor is driving now */
  document.addEventListener("click",function(e){
    var t=e.target;
    if(t.closest&&t.closest(".d-reelnav button")){reelLocked=true;stopReel();}
    if(t.closest&&(t.closest("[data-v]")||t.closest("[data-f]"))){reelLocked=false;}
  },true);
  view.addEventListener("pointerenter",stopReel);
  view.addEventListener("pointerleave",function(){if(!reelLocked){boldStage();}});
  /* swipe the phone */
  var x0=null;
  view.addEventListener("pointerdown",function(e){
    if(e.target.closest&&e.target.closest(".d-phone")){x0=e.clientX;}
  });
  view.addEventListener("pointerup",function(e){
    if(x0===null){return;}
    var dx=e.clientX-x0;x0=null;
    if(Math.abs(dx)<40){return;}
    reelLocked=true;stopReel();
    var b=view.querySelector('.d-reelnav [data-reel="'+(dx<0?1:-1)+'"]');
    if(b){b.click();}
  });
  boldStage();
})();

/* ---------- language changes rebuild text, so re-arm ---------- */
document.addEventListener("click",function(e){
  if(e.target.closest&&e.target.closest("[data-lang]")){
    setTimeout(function(){
      armTells();armHeadings();
      if(window.__boldMarquee){window.__boldMarquee();}
      if(window.__boldPills){window.__boldPills();}
      if(window.__boldMagnet){window.__boldMagnet();}
    },30);
  }
},true);

/* the hero swaps its sentence on its own timer too */
(function(){
  var stack=document.querySelector(".tells");
  if(!stack){return;}
  new MutationObserver(function(){armTells();}).observe(stack,{childList:true,subtree:true});
})();

armTells();armHeadings();tint();
})();
</script>
"""

out = src.replace("</head>", CSS.strip() + "\n</head>", 1)
out = out.replace("</body>", JS.strip() + "\n</body>", 1)
out = out.replace('<meta name="theme-color" content="#E7E7E1">',
                  '<meta name="theme-color" content="#0B0C0D">', 1)
(_out / "index.html").write_text(out, encoding="utf-8")
(_root / "index.html").write_text(out, encoding="utf-8")   # die gewaehlte Fassung
print("written", len(out), "bytes -> versions/bold/index.html + index.html")
