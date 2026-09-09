#!/usr/bin/env python3
# Variant C — the saga. A scroll-driven prologue: the fire, Uruk, the long
# separation of ledger and telling, today's unopened envelope, and the handover
# into the site itself.
import pathlib, json, random

_root = pathlib.Path(__file__).resolve().parent
if _root.name == "source":
    _root = _root.parent
src = (_root / "versions" / "quiet" / "index.html").read_text(encoding="utf-8")
_out = _root / "versions" / "story"
_out.mkdir(parents=True, exist_ok=True)

rnd = random.Random(1794)

# ---------------------------------------------------------------- generated bits
sparks = "".join(
    '<i style="left:%.1f%%;--d:%.2fs;--t:%.2fs;--x:%.0fpx;--s:%.1fpx"></i>' % (
        rnd.uniform(18, 82), rnd.uniform(0, 5.5), rnd.uniform(3.4, 7.2),
        rnd.uniform(-70, 70), rnd.uniform(1.4, 3.4))
    for _ in range(38))

tallies = "".join('<i style="--i:%d"></i>' % i for i in range(13))

signs = []
for row in range(9):
    for col in range(7):
        wedges = "".join(
            '<b style="--r:%ddeg;--x:%dpx;--y:%dpx"></b>' % (
                rnd.choice([-90, -45, 0, 45, 90, 135]), rnd.randint(0, 7), rnd.randint(0, 6))
            for _ in range(rnd.randint(2, 4)))
        signs.append('<span class="sg" style="--i:%d">%s</span>' % (row * 7 + col, wedges))
signs_html = "".join(signs)

LEDGER = [
 "8 gur she         3 udu         2 gud",
 "12 gur she        1 udu         5 gud",
 "5 gur she         9 udu         1 gud",
 "21 gur she        4 udu         7 gud",
 "3 gur she        11 udu         2 gud",
 "17 gur she        6 udu         4 gud",
]
MODERN = [
 "Altersguthaben per 31.12.2026                    301 661.50",
 "Altersgutschrift 2027        15.0 %               13 791.00",
 "Zinssatz obligatorisch  1.25 %   ueberobl.  1.00 %",
 "Voraussichtliche Altersrente ab 65                18 099.70",
 "Voraussichtliche Altersrente ab 62                14 902.30",
 "Koordinationsabzug                               -26 460.00",
 "Versicherter Lohn                                 91 940.00",
 "Moeglicher Einkauf per 01.01.2027                 64 209.00",
 "Freizuegigkeitsleistung Art. 15 / 17 FZG         301 661.50",
 "Deckungsgrad der Kasse 31.12.2026        108.4 %",
]
modern_block = "\n".join(MODERN * 4)
ledger_block = "\n".join(LEDGER * 3)

SAGA_HTML = """
<a class="sg-skip" href="#top">Erzählung überspringen</a>
<section id="saga" aria-label="Prolog">
  <div class="sg-stage">
    <div class="sg-bg" aria-hidden="true"></div>
    <div class="sg-scrim" aria-hidden="true"></div>

    <!-- act 0 — the fire -->
    <div class="sg-act sg-a0" aria-hidden="true">
      <div class="sg-wall">
        <svg class="sg-bison" viewBox="0 0 100 132" fill="none" aria-hidden="true">
          <path d="M32 130C23 114 18 98 18 84V60c0-7 9-7 9 0v18h4V36c0-7 9-7 9 0v40h4V24c0-7 9-7 9 0v52h4V30c0-7 9-7 9 0v46h4V46c0-7 9-7 9 0v42c0 15-6 29-14 42Z"/>
        </svg>
        <div class="sg-tally">__TALLIES__</div>
      </div>
      <div class="sg-fire">
        <span class="sg-flame f1"></span><span class="sg-flame f2"></span><span class="sg-flame f3"></span>
        <span class="sg-log"></span><span class="sg-log b"></span>
      </div>
      <div class="sg-sparks">__SPARKS__</div>
      <div class="sg-figs">
        <span class="sg-fig" style="--o:-190px;--h:1"></span>
        <span class="sg-fig" style="--o:-110px;--h:.86"></span>
        <span class="sg-fig" style="--o:120px;--h:.94"></span>
        <span class="sg-fig" style="--o:200px;--h:.8"></span>
      </div>
    </div>

    <!-- act 1 — Uruk -->
    <div class="sg-act sg-a1" aria-hidden="true">
      <div class="sg-tablet">
        <div class="sg-signs">__SIGNS__</div>
        <pre class="sg-ledger">__LEDGER__</pre>
      </div>
    </div>

    <!-- act 2 — the long separation -->
    <div class="sg-act sg-a2" aria-hidden="true">
      <div class="sg-split">
        <div class="sg-col sg-left"><pre>__LEDGER__</pre><pre>__LEDGER__</pre></div>
        <div class="sg-rift"></div>
        <div class="sg-col sg-right">
          <span>·</span><span>·</span><span>·</span><span>·</span><span>·</span>
        </div>
      </div>
      <p class="sg-note" id="sgNote">Venedig, 1494: die doppelte Buchführung bekommt ihre Grammatik.</p>
    </div>

    <!-- act 3 — today -->
    <div class="sg-act sg-a3" aria-hidden="true">
      <pre class="sg-modern">__MODERN__</pre>
      <div class="sg-seal"></div>
    </div>

    <!-- act 4 — the handover -->
    <div class="sg-act sg-a4" aria-hidden="true">
      <div class="sg-aperture"><span></span></div>
    </div>

    <!-- words -->
    <div class="sg-words">
      <p class="sg-era" id="sgEra">vor vierzigtausend Jahren</p>
      <h2 class="sg-line" id="sgLine">Am Anfang sass jemand am Feuer und erzählte, was geschehen war.</h2>
    </div>

    <!-- the ruler -->
    <div class="sg-ruler" aria-hidden="true">
      <span class="sg-rail"><i id="sgDot"></i></span>
      <ol id="sgMarks"><li>40 000 v. Chr.</li><li>3400 v. Chr.</li><li>1494</li><li>heute</li></ol>
    </div>

    <div class="sg-hint" aria-hidden="true"><span></span></div>
  </div>
</section>
""".replace("__SPARKS__", sparks).replace("__TALLIES__", tallies).replace("__SIGNS__", signs_html) \
   .replace("__LEDGER__", ledger_block).replace("__MODERN__", modern_block)

# ---------------------------------------------------------------- copy
S = {
"de": {"skip":"Erzählung überspringen",
 "e0":"vor vierzigtausend Jahren","l0":"Am Anfang sass jemand am Feuer und erzählte, was geschehen war.",
 "e1":"Uruk, 3400 v. Chr.","l1":"Die erste Schrift war keine Geschichte. Sie war eine Abrechnung über Gerste und Vieh.",
 "e2":"die folgenden fünftausend Jahre","l2":"Das Buch wurde immer genauer. Die Erzählung ging verloren.",
 "n2":"Venedig, 1494: die doppelte Buchführung bekommt ihre Grammatik.",
 "e3":"heute","l3":"Was bei Ihnen ankommt, ist genau, vollständig — und ungeöffnet.",
 "e4":"Tellingly","l4":"Wir setzen die beiden wieder zusammen.",
 "r":["40 000 v. Chr.","3400 v. Chr.","1494","heute"]},
"fr": {"skip":"Passer le récit",
 "e0":"il y a quarante mille ans","l0":"Au commencement, quelqu’un était assis près du feu et racontait ce qui s’était passé.",
 "e1":"Ourouk, 3400 av. J.-C.","l1":"La première écriture n’était pas un récit. C’était un décompte d’orge et de bétail.",
 "e2":"les cinq mille ans qui suivirent","l2":"Le registre est devenu toujours plus exact. Le récit s’est perdu.",
 "n2":"Venise, 1494 : la comptabilité en partie double reçoit sa grammaire.",
 "e3":"aujourd’hui","l3":"Ce qui vous parvient est exact, complet — et jamais ouvert.",
 "e4":"Tellingly","l4":"Nous remettons les deux ensemble.",
 "r":["40 000 av. J.-C.","3400 av. J.-C.","1494","aujourd’hui"]},
"it": {"skip":"Salta il racconto",
 "e0":"quarantamila anni fa","l0":"All’inizio qualcuno sedeva accanto al fuoco e raccontava che cosa era successo.",
 "e1":"Uruk, 3400 a.C.","l1":"La prima scrittura non era un racconto. Era un conteggio di orzo e bestiame.",
 "e2":"i cinquemila anni seguenti","l2":"Il registro è diventato sempre più esatto. Il racconto è andato perduto.",
 "n2":"Venezia, 1494: la partita doppia riceve la sua grammatica.",
 "e3":"oggi","l3":"Quello che le arriva è esatto, completo — e mai aperto.",
 "e4":"Tellingly","l4":"Rimettiamo insieme le due cose.",
 "r":["40 000 a.C.","3400 a.C.","1494","oggi"]},
"en": {"skip":"Skip the story",
 "e0":"forty thousand years ago","l0":"In the beginning someone sat by the fire and told what had happened.",
 "e1":"Uruk, 3400 BC","l1":"The first writing was not a story. It was a count of barley and cattle.",
 "e2":"the five thousand years that followed","l2":"The ledger grew ever more exact. The telling was lost.",
 "n2":"Venice, 1494: double-entry bookkeeping is given its grammar.",
 "e3":"today","l3":"What reaches you is exact, complete — and unopened.",
 "e4":"Tellingly","l4":"We put the two back together.",
 "r":["40,000 BC","3400 BC","1494","today"]}
}
CSS = r"""
<style>
/* ============================================================
   VARIANT C — the saga. Fire, clay, the long drift, today.
   ============================================================ */
#saga{position:relative;height:560vh;background:#0A0807}
.sg-stage{
  position:sticky;top:0;height:100vh;overflow:hidden;
  display:flex;align-items:center;justify-content:center;
  --p:0;
}
.sg-bg{position:absolute;inset:0;background:#0A0807;transition:background .1s linear}
.sg-act{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;padding-bottom:27vh}
.sg-scrim{position:absolute;left:0;right:0;bottom:0;height:52vh;z-index:4;pointer-events:none;
  background:linear-gradient(to top,var(--scrim,rgba(10,8,7,.9)) 22%,transparent)}

/* ---------- act 0 — the fire ---------- */
.sg-a0{flex-direction:column;transform:scale(var(--z,1))}
.sg-wall{
  position:absolute;left:50%;top:8%;width:min(760px,86vw);transform:translateX(-50%);
  display:flex;align-items:flex-end;justify-content:center;gap:clamp(20px,5vw,64px);
}
.sg-bison{width:clamp(96px,12vw,150px);stroke:#D08B4E;stroke-width:2.4;filter:drop-shadow(0 0 16px rgba(226,112,58,.35));stroke-linejoin:round;
  stroke-dasharray:var(--len,620);stroke-dashoffset:calc(var(--len,620) * (1 - var(--draw,0)))}
.sg-tally{display:flex;gap:9px;align-items:flex-end;padding-bottom:14px}
.sg-tally i{
  display:block;width:4px;height:44px;background:#D08B4E;box-shadow:0 0 14px rgba(226,112,58,.4);transform-origin:50% 100%;
  transform:scaleY(0) rotate(calc((var(--i) - 6) * 1.4deg));
  transition:transform .28s cubic-bezier(.2,.8,.3,1);
}
.sg-tally i.on{transform:scaleY(1) rotate(calc((var(--i) - 6) * 1.4deg))}
.sg-fire{position:absolute;bottom:24%;left:50%;transform:translateX(-50%) scale(1.55);width:220px;height:230px;transform-origin:50% 100%}
.sg-flame{
  position:absolute;left:50%;bottom:26px;border-radius:50% 50% 44% 44%;
  filter:blur(10px);mix-blend-mode:screen;transform-origin:50% 100%;
}
.sg-flame.f1{width:150px;height:190px;margin-left:-75px;background:radial-gradient(50% 60% at 50% 82%,#F0A247,#C4441B 62%,transparent 74%);animation:sg-fl 2.3s ease-in-out infinite}
.sg-flame.f2{width:96px;height:140px;margin-left:-48px;background:radial-gradient(50% 60% at 50% 80%,#FFD07A,#E2703A 60%,transparent 76%);animation:sg-fl 1.7s ease-in-out infinite .3s}
.sg-flame.f3{width:52px;height:88px;margin-left:-26px;background:radial-gradient(50% 60% at 50% 78%,#FFF0C4,#FFB758 58%,transparent 78%);animation:sg-fl 1.15s ease-in-out infinite .6s}
@keyframes sg-fl{
  0%,100%{transform:scale(1,1) skewX(0deg)}
  30%{transform:scale(.93,1.1) skewX(3deg)}
  60%{transform:scale(1.06,.94) skewX(-3deg)}
}
.sg-log{position:absolute;bottom:16px;left:50%;width:130px;height:11px;margin-left:-65px;border-radius:6px;background:#41230F;transform:rotate(-7deg)}
.sg-log.b{transform:rotate(9deg);background:#331B0B;width:118px;margin-left:-59px}
.sg-sparks{position:absolute;inset:0;pointer-events:none}
.sg-sparks i{
  position:absolute;bottom:29%;width:var(--s);height:var(--s);border-radius:50%;
  background:#FFC27A;opacity:0;box-shadow:0 0 8px 2px rgba(255,170,90,.55);animation:sg-sp var(--t) linear infinite var(--d);
}
@keyframes sg-sp{
  0%{opacity:0;transform:translate(0,0) scale(1)}
  12%{opacity:.95}
  100%{opacity:0;transform:translate(var(--x),-62vh) scale(.2)}
}
.sg-figs{position:absolute;bottom:21%;left:50%;width:0;height:0}
.sg-fig{
  position:absolute;bottom:0;left:var(--o);width:104px;height:calc(180px * var(--h));
  margin-left:-52px;border-radius:56px 56px 10px 10px;background:#040302;
  filter:drop-shadow(0 0 22px rgba(226,112,58,.30));transform-origin:50% 100%;
  animation:sg-breathe 4.6s ease-in-out infinite;
}
.sg-fig:before{
  content:"";position:absolute;top:-38px;left:50%;width:52px;height:52px;margin-left:-26px;
  border-radius:50%;background:#040302;
}
.sg-fig:nth-child(2){animation-delay:.9s}
.sg-fig:nth-child(3){animation-delay:1.8s}
.sg-fig:nth-child(4){animation-delay:2.6s}
@keyframes sg-breathe{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.018)}}

/* ---------- act 1 — Uruk ---------- */
.sg-tablet{
  position:relative;width:min(430px,80vw);max-height:62vh;aspect-ratio:4/5;border-radius:12px 12px 16px 16px;
  background:linear-gradient(168deg,#C9A379,#A9835A 62%,#8E6A45);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.28),inset 0 -14px 26px rgba(0,0,0,.28),0 50px 80px -40px rgba(0,0,0,.85);
  padding:clamp(20px,3.4vw,34px);overflow:hidden;
  transform:translateY(calc(60px * (1 - var(--t,0)))) rotateX(calc(12deg * (1 - var(--t,0))));
}
.sg-signs{display:grid;grid-template-columns:repeat(7,1fr);gap:clamp(8px,1.4vw,16px);height:100%}
.sg-signs .sg{position:relative;opacity:0;transform:scale(.4);transition:opacity .18s ease,transform .22s cubic-bezier(.2,.9,.3,1)}
.sg-signs .sg.on{opacity:1;transform:none}
.sg-signs .sg b{
  position:absolute;left:var(--x);top:var(--y);width:0;height:0;
  border-left:4px solid transparent;border-right:4px solid transparent;border-top:9px solid #5E4225;
  transform:rotate(var(--r));filter:drop-shadow(0 1px 0 rgba(255,255,255,.22));
}
.sg-ledger{
  position:absolute;inset:clamp(20px,3.4vw,34px);margin:0;overflow:hidden;
  font:400 10px/1.7 var(--mono);color:#5E4225;opacity:0;transition:opacity .5s ease;
  white-space:pre;
}
.sg-a1.late .sg-ledger{opacity:.85}
.sg-a1.late .sg-signs{opacity:.12}
.sg-signs{transition:opacity .5s ease}

/* ---------- act 2 — the drift ---------- */
.sg-split{position:relative;width:min(1000px,92vw);height:58vh;display:flex;align-items:stretch;justify-content:center}
.sg-col{flex:1;overflow:hidden;position:relative;display:flex;align-items:center;justify-content:center}
.sg-left{gap:26px;transform:translateX(calc(-16% * var(--t,0)))}
.sg-left pre{margin:0;font:400 9.5px/1.7 var(--mono);color:#C9A87E;white-space:pre;opacity:calc(.35 + .65 * var(--t,0))}
.sg-right{
  display:flex;flex-direction:column;align-items:center;justify-content:space-around;
  transform:translateX(calc(16% * var(--t,0)));opacity:calc(1 - var(--t,0));
}
.sg-right span{font-size:64px;color:#E2703A;line-height:.6;text-shadow:0 0 24px rgba(226,112,58,.7)}
.sg-rift{width:1px;background:linear-gradient(180deg,transparent,rgba(226,112,58,.5),transparent);flex:none}
.sg-note{
  position:absolute;top:11%;left:50%;transform:translate(-50%,-10px);
  margin:0;font:400 12.5px/1.6 var(--mono);letter-spacing:.04em;color:#C9A87E;
  opacity:0;transition:opacity .5s ease,transform .5s ease;text-align:center;max-width:80vw;
}
.sg-a2.mid .sg-note{opacity:.95;transform:translate(-50%,0)}
.sg-a2{position:absolute}

/* ---------- act 3 — today ---------- */
.sg-modern{
  margin:0;font:400 10px/1.62 var(--mono);color:#7E878D;white-space:pre;
  transform:scale(calc(1.06 - .06 * var(--t,0)));filter:blur(calc(3px * (1 - var(--t,0))));
  max-height:56vh;overflow:hidden;
}
.sg-seal{
  position:absolute;width:clamp(150px,20vw,220px);aspect-ratio:1;border:2px solid rgba(226,112,58,.6);
  border-radius:50%;transform:rotate(-14deg) scale(calc(.7 + .3 * var(--t,0)));opacity:calc(var(--t,0) * .9);
}
.sg-seal:after{
  content:"";position:absolute;inset:11px;border:1px solid rgba(226,112,58,.35);border-radius:50%;
}

/* ---------- act 4 — the handover ---------- */
.sg-aperture{
  width:min(760px,88vw);background:#F7F7F4;border-radius:2px;
  height:calc(6px + 300px * var(--t,0));max-height:44vh;
  box-shadow:0 0 0 1px rgba(0,0,0,.12),0 60px 100px -50px rgba(0,0,0,.7),0 0 120px -20px rgba(255,220,160,.35);
  transition:height .1s linear;
}

/* ---------- words ---------- */
.sg-words{
  position:absolute;left:50%;bottom:clamp(70px,10vh,120px);transform:translateX(-50%);
  width:min(1000px,88vw);text-align:center;z-index:5;pointer-events:none;
}
.sg-era{
  margin:0 0 14px;font:400 12px/1.5 var(--mono);letter-spacing:.16em;color:#D89B5E;
  opacity:0;transform:translateY(8px);transition:opacity .5s ease,transform .5s ease;
}
.sg-line{
  margin:0;font-size:clamp(23px,3.6vw,50px);line-height:1.12;letter-spacing:-0.025em;
  color:#F4EFE6;max-width:22ch;margin-inline:auto;font-weight:400;
  opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s cubic-bezier(.16,1,.3,1);
}
.sg-words.show .sg-era,.sg-words.show .sg-line{opacity:1;transform:none}
.sg-stage.finale .sg-line{color:#16191A}
.sg-stage.finale .sg-era{color:#2E5B49}

/* ---------- ruler ---------- */
.sg-ruler{position:absolute;right:clamp(16px,3vw,46px);top:50%;transform:translateY(-50%);display:flex;gap:14px;z-index:6}
.sg-rail{position:relative;width:1px;background:rgba(255,255,255,.16);height:clamp(180px,30vh,260px)}
.sg-rail i{position:absolute;left:-3px;width:7px;height:7px;border-radius:50%;background:#E2703A;top:calc(var(--p) * 100%);transition:top .12s linear}
.sg-ruler ol{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;justify-content:space-between;height:clamp(180px,30vh,260px)}
.sg-ruler li{font:400 10.5px/1 var(--mono);letter-spacing:.08em;color:rgba(255,255,255,.34);transition:color .3s ease}
.sg-ruler li.on{color:#F0C48A}
.sg-stage.finale .sg-ruler li{color:rgba(22,25,26,.32)}
.sg-stage.finale .sg-ruler li.on{color:#2E5B49}
.sg-stage.finale .sg-rail{background:rgba(22,25,26,.16)}
.sg-stage.finale .sg-hint{opacity:0}
.sg-hint{transition:opacity .4s ease}

/* ---------- scroll hint ---------- */
.sg-hint{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);width:1px;height:44px;background:rgba(255,255,255,.16);overflow:hidden;z-index:6}
.sg-hint span{position:absolute;inset:0;background:#E2703A;transform:translateY(-100%);animation:sg-hint 2.1s ease-in-out infinite}
@keyframes sg-hint{0%{transform:translateY(-100%)}60%,100%{transform:translateY(100%)}}

.sg-skip{position:absolute;left:-9999px}
.sg-skip:focus{left:14px;top:14px;z-index:80;background:#F7F7F4;color:#16191A;padding:10px 14px;border:1px solid #16191A}

/* the header stays usable through the prologue, it just gets out of the way */
.site{z-index:70;transition:background .4s ease,border-color .4s ease,color .4s ease}
body.sg-dark .site{background:transparent;backdrop-filter:none;border-bottom-color:transparent}
body.sg-dark .mark{color:#F4EFE6}
body.sg-dark .sections a{color:rgba(244,239,230,.5)}
body.sg-dark .sections a:hover{color:#F4EFE6}
body.sg-dark .langs button{color:rgba(244,239,230,.62)}
body.sg-dark .langs button:hover{color:#F4EFE6}
body.sg-dark .langs button[aria-pressed="true"]{background:#E2703A;border-color:#E2703A;color:#0A0807}

@media (max-width:760px){
  #saga{height:460vh}
  .sg-ruler{display:none}
  .sg-split{width:94vw}
}
@media (prefers-reduced-motion:reduce){
  #saga{height:auto}
  .sg-stage{position:static;height:auto;display:block;padding:60px 0}
  .sg-act,.sg-hint,.sg-ruler{display:none}
  .sg-words{position:static;transform:none;width:min(70ch,88vw);margin:0 auto;text-align:left}
  .sg-era,.sg-line{opacity:1;transform:none}
}
</style>
"""

JS = r"""
<script>
/* ============================================================
   VARIANT C — saga driver. Purely additive: without this script
   the prologue collapses to its five lines and the site works.
   ============================================================ */
(function(){
"use strict";
var COPY=__COPY__;
var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var saga=document.getElementById("saga");
if(!saga){return;}
var stage=saga.querySelector(".sg-stage");
var bg=saga.querySelector(".sg-bg");
var words=saga.querySelector(".sg-words");
var eraEl=document.getElementById("sgEra"),lineEl=document.getElementById("sgLine");
var noteEl=document.getElementById("sgNote"),marks=document.getElementById("sgMarks");
var skip=document.querySelector(".sg-skip");
var acts=[0,1,2,3,4].map(function(i){return saga.querySelector(".sg-a"+i);});
var tallies=saga.querySelectorAll(".sg-tally i");
var signs=saga.querySelectorAll(".sg-signs .sg");
var bison=saga.querySelector(".sg-bison");
var dot=document.getElementById("sgDot");

/* the ground colour walks from cave to paper */
var scrim=saga.querySelector(".sg-scrim");
var STOPS=[[0,[10,8,7]],[.26,[27,17,9]],[.5,[34,26,18]],[.74,[18,21,26]],[.93,[231,231,225]],[1,[231,231,225]]];
function mix(p){
  for(var i=1;i<STOPS.length;i++){
    if(p<=STOPS[i][0]){
      var a=STOPS[i-1],b=STOPS[i],k=(p-a[0])/((b[0]-a[0])||1),c=[0,0,0];
      for(var j=0;j<3;j++){c[j]=Math.round(a[1][j]+(b[1][j]-a[1][j])*k);}
      return c;
    }
  }
  return [231,231,225];
}

function lang(){
  var l=document.documentElement.lang||"de";
  return COPY[l]?l:"de";
}
function applyCopy(){
  var c=COPY[lang()];
  if(skip){skip.textContent=c.skip;}
  if(noteEl){noteEl.textContent=c.n2;}
  if(marks){
    var li=marks.children;
    for(var i=0;i<li.length&&i<c.r.length;i++){li[i].textContent=c.r[i];}
  }
  paintWords(true);
}

var shownAct=-1;
function paintWords(force){
  var c=COPY[lang()];
  if(shownAct<0){return;}
  if(force||eraEl.getAttribute("data-act")!=String(shownAct)){
    eraEl.textContent=c["e"+shownAct];
    lineEl.textContent=c["l"+shownAct];
    eraEl.setAttribute("data-act",shownAct);
  }
}

if(reduce){
  /* the prologue becomes five plain lines */
  var host=words.parentNode,c=COPY[lang()];
  var box=document.createElement("div");
  for(var i=0;i<5;i++){
    var p=document.createElement("p");
    p.className="sg-era";p.style.opacity=1;p.textContent=c["e"+i];
    var h=document.createElement("p");
    h.className="sg-line";h.style.opacity=1;h.style.margin="0 0 42px";h.textContent=c["l"+i];
    box.appendChild(p);box.appendChild(h);
  }
  words.innerHTML="";words.appendChild(box);
  document.body.classList.add("sg-done");
  new MutationObserver(function(){
    var cc=COPY[lang()],ps=words.querySelectorAll(".sg-era"),hs=words.querySelectorAll(".sg-line");
    for(var k=0;k<ps.length;k++){ps[k].textContent=cc["e"+k];hs[k].textContent=cc["l"+k];}
    if(skip){skip.textContent=cc.skip;}
  }).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
  return;
}

if(bison){
  try{var L=bison.querySelector("path").getTotalLength();bison.style.setProperty("--len",L);}catch(e){}
}

var SEG=[0,.22,.44,.64,.84,1];   /* act boundaries */
var lastTally=-1,lastSign=-1,ticking=false;

function frame(){
  ticking=false;
  var r=saga.getBoundingClientRect();
  var span=saga.offsetHeight-window.innerHeight;
  var p=span>0?Math.min(1,Math.max(0,-r.top/span)):0;
  stage.style.setProperty("--p",p);
  var g=mix(p);
  bg.style.background="rgb("+g[0]+","+g[1]+","+g[2]+")";
  if(scrim){
    scrim.style.setProperty("--scrim","rgba("+g[0]+","+g[1]+","+g[2]+",.92)");
    scrim.style.opacity=p>.86?Math.max(0,(1-p)/.14):1;
  }
  if(dot){dot.style.top=(p*100)+"%";}

  /* which act, and how far into it */
  var act=0;
  for(var i=0;i<5;i++){if(p>=SEG[i]){act=i;}}
  var t=(p-SEG[act])/(SEG[act+1]-SEG[act]);
  t=Math.min(1,Math.max(0,t));

  for(var j=0;j<5;j++){
    var el=acts[j];if(!el){continue;}
    var on=j===act;
    var o=on?Math.min(1,t<.12?t/.12:(t>.9?(1-t)/.1:1)):0;
    if(j===4&&on){o=Math.min(1,t/.2);}
    el.style.opacity=o;
    if(on){el.style.setProperty("--t",t);}
  }

  /* act 0: the camera leans in, the wall gets drawn, the tallies are cut */
  acts[0].style.setProperty("--z",1+(act===0?t:1)*0.16);
  if(bison){bison.style.setProperty("--draw",act===0?Math.min(1,t*1.6):1);}
  var wantT=act===0?Math.floor(Math.min(1,Math.max(0,(t-.35)/.5))*tallies.length):(act>0?tallies.length:0);
  if(wantT!==lastTally){
    for(var k=0;k<tallies.length;k++){tallies[k].classList.toggle("on",k<wantT);}
    lastTally=wantT;
  }

  /* act 1: the signs get pressed into the clay, then the ledger reads through */
  var wantS=act===1?Math.floor(Math.min(1,t/.62)*signs.length):(act>1?signs.length:0);
  if(wantS!==lastSign){
    var from=Math.min(wantS,lastSign<0?0:lastSign),to=Math.max(wantS,lastSign<0?0:lastSign);
    for(var m=0;m<signs.length;m++){signs[m].classList.toggle("on",m<wantS);}
    lastSign=wantS;
  }
  acts[1].classList.toggle("late",act===1&&t>.72);

  /* act 2: the note lands mid-drift */
  acts[2].classList.toggle("mid",act===2&&t>.42);

  /* words: swap on act change, and stand back during the transitions */
  if(act!==shownAct){shownAct=act;paintWords(true);}
  words.classList.toggle("show",t>.05&&t<.94);

  /* the ruler */
  if(marks){
    var mi=p<.28?0:(p<.5?1:(p<.72?2:3));
    for(var q=0;q<marks.children.length;q++){marks.children[q].classList.toggle("on",q===mi);}
  }

  stage.classList.toggle("finale",p>.9);
  document.body.classList.toggle("sg-done",p>.965);
  document.body.classList.toggle("sg-dark",p<.86);
}
function onScroll(){if(!ticking){ticking=true;requestAnimationFrame(frame);}}
addEventListener("scroll",onScroll,{passive:true});
addEventListener("resize",onScroll);
new MutationObserver(applyCopy).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
applyCopy();frame();
})();
</script>
"""

CSS = CSS.replace("__NOTHING__", "")
JS = JS.replace("__COPY__", json.dumps(S, ensure_ascii=False, separators=(",", ":")))

out = src.replace("</head>", CSS.strip() + "\n</head>", 1)
out = out.replace('<main id="main">\n<span id="top"></span>',
                  '<main id="main">\n' + SAGA_HTML.strip() + '\n<span id="top"></span>', 1)
out = out.replace("</body>", JS.strip() + "\n</body>", 1)
out = out.replace('<meta name="theme-color" content="#E7E7E1">',
                  '<meta name="theme-color" content="#0A0807">', 1)
(_out / "index.html").write_text(out, encoding="utf-8")
print("written", len(out), "bytes -> index-story.html")
