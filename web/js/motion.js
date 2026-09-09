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