(function(){
"use strict";
var LANGS=["de","fr","it","en"];

var I18N={
de:{
"meta.title":"Tellingly — Daten, erzählt.",
"meta.desc":"Tellingly macht aus institutionellen Daten eine Erzählung, die Menschen zu Ende lesen. Vorsorge, Portfolio, Schule, Gesundheit, Team. Kreuzlingen, Schweiz.",
"a11y.skip":"Zum Inhalt springen",
"nav.argument":"Argument","nav.formats":"Formate","nav.verticals":"Bereiche","nav.who":"Abgrenzung",
"nav.contact":"Kontakt",
"nav.try":"Ausprobieren",
"try.h":"Sehen Sie es sich an.",
"try.sub":"Wählen Sie einen Bereich und ein Format. Der Inhalt bleibt derselbe — nur die Zustellung ändert sich.",
"stage.unbranded":"Ohne Marke. Farbe, Schrift und Logo kommen von Ihnen.",
"stage.motion":"Reel und Brief bewegen sich, die Edition steht still — sie ist gedruckt. Animation nur dort, wo sie eine Kennzahl erklärt: der Betrag zählt hoch, die Differenz wächst als zweiter Balken, der Laborwert fährt in seinen Referenzbereich.",
"stage.prev":"Zurück",
"stage.next":"Weiter",
"stage.figures":"Kennzahlen",
"hero.line0":"Ihre Bank hat Ihnen im Januar einen Portfolioauszug geschickt.<br><span class=\"quiet\">Sie haben ihn nicht geöffnet.</span>",
"hero.line1":"Ihre Pensionskasse hat Ihnen im Januar den Vorsorgeausweis geschickt.<br><span class=\"quiet\">Sie wissen nicht, was er bedeutet.</span>",
"hero.line2":"Die Schule hat Ihnen im Februar das Zeugnis Ihres Kindes geschickt.<br><span class=\"quiet\">Sie haben die Zahlen gesehen, nicht das Jahr.</span>",
"hero.line3":"Ihre Ärztin hat Ihnen im März einen Befund geschickt.<br><span class=\"quiet\">Sie haben die Hälfte davon gegoogelt.</span>",
"hero.line4":"Ihr Arbeitgeber hat Ihnen im Dezember die Beurteilung geschickt.<br><span class=\"quiet\">Sie haben sie einmal überflogen.</span>",
"hero.navlabel":"Dokument",
"hero.tab0":"Portfolioauszug",
"hero.tab1":"Vorsorgeausweis",
"hero.tab2":"Zeugnis",
"hero.tab3":"Befund",
"hero.tab4":"Beurteilung",
"hero.sub":"Tellingly nimmt dieselben Daten und erzählt sie. Institutionen verschicken sie. Menschen lesen sie zu Ende.",
"hero.cta":"Sprechen Sie mit uns",
"arg.h":"Die Buchhaltung kam vor der Literatur.",
"arg.p1":"Die Schrift wurde um 3400 v. Chr. in Uruk erfunden, um Getreide und Vieh zu zählen. Die ersten Dokumente waren Verzeichnisse. Die Literatur kam tausend Jahre später.",
"arg.p2":"Irgendwann in den folgenden fünftausend Jahren hörten die Zahlen auf, zu jemandem zu sprechen. Dabei sind ein Vorsorgeausweis und ein Schulzeugnis derselbe menschliche Vorgang: Jemand erzählt Ihnen, was mit etwas geschehen ist, das Ihnen wichtig ist. Wir stellen die Verbindung zwischen dem Buch und der Erzählung wieder her.",
"arg.pull":"Wir vereinfachen Ihre Daten nicht. Wir geben ihnen einen Erzähler.",
"fmt.h":"Dieselben Daten, dreimal erzählt.",
"fmt.sub":"Jeder Bereich erscheint in allen drei Formaten. Derselbe Rückblick, dreimal anders zugestellt.",
"fmt.eg":"Beispiel",
"fmt.brief.medium":"Digital, im Browser",
"fmt.brief.body":"Der ganze Rückblick zum Scrollen. Ein Link, keine Anmeldung, kein PDF.",
"fmt.brief.note":"Auf Deutsch ist ein Brief ein Brief: ein Bericht, der ankommt wie Post.",
"fmt.edition.medium":"Gedruckt",
"fmt.edition.body":"Lang, gehaltvoll, hochwertig. Etwas, das man behält — keine Postwurfsendung.",
"ver.h":"Fünf Branchen. Ein Handwerk.",
"ver.sub":"Tellingly Studio schreibt, Tellingly Engine erzeugt. Darunter liegen fünf Bereiche — und jeder Bereich erscheint in jedem Format.",
"ver.c0":"Bereich","ver.c1":"Kunde","ver.c2":"Was die Empfängerin erhält","ver.c3":"Rhythmus",
"ver.portfolio.cust":"Banken und Vermögensverwalter",
"ver.portfolio.gets":"Eine Anlageübersicht, die Kundinnen und Kunden lesen statt ablegen",
"ver.portfolio.cad":"Quartalsweise oder jährlich",
"ver.pension.cust":"Pensionskassen und Sammelstiftungen",
"ver.pension.gets":"Ein Vorsorgeausweis, den man versteht",
"ver.pension.cad":"Jährlich",
"ver.school.cust":"Schulen und Bildungsbehörden",
"ver.school.gets":"Ein Semester- und Jahresbericht für Eltern",
"ver.school.cad":"Zweimal jährlich",
"ver.health.cust":"Ärztenetze und Krankenversicherer",
"ver.health.gets":"Eine Jahresübersicht zur Gesundheit, die Patientinnen und Patienten verstehen",
"ver.health.cad":"Jährlich",
"ver.team.cust":"HR-Abteilungen",
"ver.team.gets":"Eine Leistungs- und Entwicklungsbeurteilung",
"ver.team.cad":"Jährlich",
"comb.hint":"Bereich plus Format ergibt das Produkt. Wählen Sie eines von jedem.",
"comb.lblV":"Bereich","comb.lblF":"Format",
"who.h":"Dashboards sind für Analysten.",
"who.p1":"Ein BI-Werkzeug bedient Menschen, deren Beruf es ist, auf Daten zu schauen. Tellingly bedient die Person, die das Dokument erhält und sich für Daten überhaupt nicht interessiert: die Rentnerin, den Vater, die Kundin.",
"who.p2":"Wir sind kein Dashboard, kein BI-Werkzeug, keine Visualisierungsbibliothek. Wenn Ihre Empfänger Zahlen erkunden wollen, kaufen Sie ein Dashboard. Wenn sie verstehen sollen, was geschehen ist, sprechen Sie mit uns.",
"contact.h":"Sprechen Sie mit uns.",
"contact.p":"Die Dokumente für 2027 entstehen jetzt. Wenn Ihre dabei sein sollen, sprechen wir darüber. Ein Gespräch, keine Demo.",
"contact.cta":"Schreiben Sie uns",
"foot.legal":"Tellingly GmbH — Kreuzlingen, Schweiz",
"mail.subject":"Anfrage über tellingly.ch",
"fmt.reel.medium":"Mobil, hochkant, getaktet",
"fmt.reel.body":"Neunzig Sekunden auf dem Telefon. Das Jahr als Folge von Karten, die man weiterschickt.",
"pv.kicker":"Portfolio 2026",
"pv.num":"&#8722;3.12&#8201;%",
"pv.numlabel":"Ergebnis 2026",
"pv.h":"Ihr Jahr in dreissig Sekunden",
"pv.p":"Eine klare Strategie schützt nicht vor jeder Schwankung. Sie gibt Orientierung, wenn Märkte, Zinsen und Nachrichten schnell wechseln.",
"pv.short":"Eine klare Strategie schützt nicht vor jeder Schwankung.",
"pv.h2":"Was Ihr Portfolio bewegte"
},
fr:{
"meta.title":"Tellingly — les données, racontées.",
"meta.desc":"Tellingly transforme les données institutionnelles en un récit que les gens lisent jusqu’au bout. Prévoyance, portefeuille, école, santé, équipe. Kreuzlingen, Suisse.",
"a11y.skip":"Aller au contenu",
"nav.argument":"Argument","nav.formats":"Formats","nav.verticals":"Domaines","nav.who":"Distinction",
"nav.contact":"Contact",
"nav.try":"Essayer",
"try.h":"Voyez par vous-même.",
"try.sub":"Choisissez un domaine et un format. Le contenu reste le même — seule la livraison change.",
"stage.unbranded":"Sans marque. Couleur, typographie et logo viennent de vous.",
"stage.motion":"Le Reel et le Brief bougent, l’Edition reste immobile — c’est de l’imprimé. Du mouvement uniquement là où il explique un chiffre : le montant s’additionne, l’écart pousse en seconde barre, la valeur de laboratoire glisse dans sa plage de référence.",
"stage.prev":"Retour",
"stage.next":"Suivant",
"stage.figures":"Chiffres clés",
"hero.line0":"Votre banque vous a envoyé un relevé de portefeuille en janvier.<br><span class=\"quiet\">Vous ne l’avez pas ouvert.</span>",
"hero.line1":"Votre caisse de pension vous a envoyé le certificat en janvier.<br><span class=\"quiet\">Vous ne savez pas ce qu’il signifie.</span>",
"hero.line2":"L’école vous a remis le bulletin de votre enfant en février.<br><span class=\"quiet\">Vous avez vu les notes, pas l’année.</span>",
"hero.line3":"Votre médecin vous a envoyé un rapport de laboratoire en mars.<br><span class=\"quiet\">Vous en avez cherché la moitié sur Google.</span>",
"hero.line4":"Votre employeur vous a remis votre évaluation en décembre.<br><span class=\"quiet\">Vous l’avez parcourue une fois.</span>",
"hero.navlabel":"Document",
"hero.tab0":"Relevé de portefeuille",
"hero.tab1":"Certificat de prévoyance",
"hero.tab2":"Bulletin scolaire",
"hero.tab3":"Rapport de laboratoire",
"hero.tab4":"Évaluation",
"hero.sub":"Tellingly reprend les mêmes données et les raconte. Les institutions les envoient. Les gens les lisent jusqu’au bout.",
"hero.cta":"Parlons-en",
"arg.h":"La comptabilité est venue avant la littérature.",
"arg.p1":"L’écriture est née à Ourouk vers 3400 av. J.-C. pour compter le grain et le bétail. Les premiers documents étaient des registres. La littérature est arrivée mille ans plus tard.",
"arg.p2":"Quelque part au cours des cinq mille ans suivants, les chiffres ont cessé de parler à quiconque. Pourtant, un certificat de prévoyance et un bulletin scolaire relèvent du même geste humain : quelqu’un vous raconte ce qui est arrivé à une chose qui compte pour vous. Nous rétablissons le lien entre le registre et le récit.",
"arg.pull":"Nous ne simplifions pas vos données. Nous leur donnons un narrateur.",
"fmt.h":"Les mêmes données, racontées de trois façons.",
"fmt.sub":"Chaque domaine paraît dans les trois formats. Le même bilan, livré de trois façons.",
"fmt.eg":"Exemple",
"fmt.brief.medium":"Numérique, dans le navigateur",
"fmt.brief.body":"Le bilan complet, à faire défiler. Un lien, sans compte, sans PDF.",
"fmt.brief.note":"En allemand, « Brief » veut dire lettre : un bilan qui arrive comme du courrier.",
"fmt.edition.medium":"Imprimé",
"fmt.edition.body":"Long, substantiel, soigné. Un objet que l’on garde — pas un envoi de plus.",
"ver.h":"Cinq secteurs. Un seul métier.",
"ver.sub":"Tellingly Studio écrit, Tellingly Engine produit. En dessous, cinq domaines — et chaque domaine existe dans chaque format.",
"ver.c0":"Domaine","ver.c1":"Client","ver.c2":"Ce que reçoit le destinataire","ver.c3":"Rythme",
"ver.portfolio.cust":"Banques et gérants de fortune",
"ver.portfolio.gets":"Un bilan de placement que les clients lisent au lieu de le classer",
"ver.portfolio.cad":"Trimestriel ou annuel",
"ver.pension.cust":"Caisses de pension et fondations collectives",
"ver.pension.gets":"Un certificat de prévoyance que l’on comprend",
"ver.pension.cad":"Annuel",
"ver.school.cust":"Écoles et autorités scolaires",
"ver.school.gets":"Un bilan semestriel et annuel pour les parents",
"ver.school.cad":"Deux fois par an",
"ver.health.cust":"Réseaux de médecins et assureurs maladie",
"ver.health.gets":"Un bilan de santé annuel que les patients comprennent",
"ver.health.cad":"Annuel",
"ver.team.cust":"Départements RH",
"ver.team.gets":"Un bilan de performance et de développement",
"ver.team.cad":"Annuel",
"comb.hint":"Un domaine plus un format donnent le produit. Choisissez-en un de chaque.",
"comb.lblV":"Domaine","comb.lblF":"Format",
"who.h":"Les tableaux de bord sont faits pour les analystes.",
"who.p1":"Un outil de BI sert celles et ceux dont le métier est de regarder des données. Tellingly sert la personne qui reçoit le document et qui ne s’intéresse pas du tout aux données : la retraitée, le père, la cliente.",
"who.p2":"Nous ne sommes ni un tableau de bord, ni un outil de BI, ni une bibliothèque de visualisation. Si vos destinataires veulent explorer les chiffres, achetez un tableau de bord. S’ils doivent comprendre ce qui s’est passé, parlons-en.",
"contact.h":"Parlons-en.",
"contact.p":"Les documents pour 2027 se préparent maintenant. Si les vôtres doivent en faire partie, parlons-en. Un entretien, pas une démo.",
"contact.cta":"Écrivez-nous",
"foot.legal":"Tellingly GmbH — Kreuzlingen, Suisse",
"mail.subject":"Demande via tellingly.ch",
"fmt.reel.medium":"Mobile, vertical, rythmé",
"fmt.reel.body":"Quatre-vingt-dix secondes sur le téléphone. L’année en cartes que l’on fait suivre.",
"pv.kicker":"Portfolio 2026",
"pv.num":"&#8722;3.12&#8201;%",
"pv.numlabel":"Résultat 2026",
"pv.h":"Votre année en trente secondes",
"pv.p":"Une stratégie claire ne protège pas de chaque secousse. Elle donne un repère quand les marchés, les taux et les nouvelles changent vite.",
"pv.short":"Une stratégie claire ne protège pas de chaque secousse.",
"pv.h2":"Ce qui a fait bouger votre portefeuille"
},
it:{
"meta.title":"Tellingly — i dati, raccontati.",
"meta.desc":"Tellingly trasforma i dati istituzionali in un racconto che le persone leggono fino in fondo. Previdenza, portafoglio, scuola, salute, team. Kreuzlingen, Svizzera.",
"a11y.skip":"Vai al contenuto",
"nav.argument":"Argomento","nav.formats":"Formati","nav.verticals":"Ambiti","nav.who":"Distinzione",
"nav.contact":"Contatto",
"nav.try":"Provare",
"try.h":"Lo guardi lei stesso.",
"try.sub":"Scelga un ambito e un formato. Il contenuto resta lo stesso — cambia solo la consegna.",
"stage.unbranded":"Senza marchio. Colore, carattere e logo arrivano da lei.",
"stage.motion":"Reel e Brief si muovono, l’Edition resta ferma — è stampa. Movimento solo dove spiega una cifra: l’importo sale contando, la differenza cresce come seconda barra, il valore di laboratorio scivola nel suo intervallo.",
"stage.prev":"Indietro",
"stage.next":"Avanti",
"stage.figures":"Cifre chiave",
"hero.line0":"La sua banca le ha inviato un estratto di portafoglio in gennaio.<br><span class=\"quiet\">Non l’ha aperto.</span>",
"hero.line1":"La sua cassa pensioni le ha inviato il certificato in gennaio.<br><span class=\"quiet\">Non sa che cosa significhi.</span>",
"hero.line2":"La scuola le ha consegnato la pagella di suo figlio in febbraio.<br><span class=\"quiet\">Ha visto i voti, non l’anno.</span>",
"hero.line3":"Il suo medico le ha inviato un referto di laboratorio in marzo.<br><span class=\"quiet\">Ne ha cercato metà su Google.</span>",
"hero.line4":"Il suo datore di lavoro le ha consegnato la valutazione in dicembre.<br><span class=\"quiet\">L’ha scorsa una volta.</span>",
"hero.navlabel":"Documento",
"hero.tab0":"Estratto di portafoglio",
"hero.tab1":"Certificato di previdenza",
"hero.tab2":"Pagella",
"hero.tab3":"Referto di laboratorio",
"hero.tab4":"Valutazione",
"hero.sub":"Tellingly prende gli stessi dati e li racconta. Le istituzioni li spediscono. Le persone li leggono fino in fondo.",
"hero.cta":"Parliamone",
"arg.h":"La contabilità è venuta prima della letteratura.",
"arg.p1":"La scrittura nacque a Uruk intorno al 3400 a.C. per contare grano e bestiame. I primi documenti erano registri. La letteratura arrivò mille anni dopo.",
"arg.p2":"Da qualche parte, nei cinquemila anni successivi, i numeri hanno smesso di parlare a qualcuno. Eppure un certificato di previdenza e una pagella sono lo stesso gesto umano: qualcuno le racconta che cosa è successo a qualcosa che le sta a cuore. Noi ricostruiamo il legame tra il registro e il racconto.",
"arg.pull":"Non semplifichiamo i suoi dati. Diamo loro un narratore.",
"fmt.h":"Gli stessi dati, raccontati in tre modi.",
"fmt.sub":"Ogni ambito esce in tutti e tre i formati. Lo stesso resoconto, recapitato in tre modi.",
"fmt.eg":"Esempio",
"fmt.brief.medium":"Digitale, nel browser",
"fmt.brief.body":"Il resoconto completo, da scorrere. Un link, senza registrazione, senza PDF.",
"fmt.brief.note":"In tedesco «Brief» significa lettera: un resoconto che arriva come posta.",
"fmt.edition.medium":"Stampato",
"fmt.edition.body":"Lungo, sostanzioso, curato. Un oggetto da tenere — non l’ennesimo invio.",
"ver.h":"Cinque settori. Un solo mestiere.",
"ver.sub":"Tellingly Studio scrive, Tellingly Engine produce. Sotto, cinque ambiti — e ogni ambito esiste in ogni formato.",
"ver.c0":"Ambito","ver.c1":"Cliente","ver.c2":"Che cosa riceve il destinatario","ver.c3":"Ritmo",
"ver.portfolio.cust":"Banche e gestori patrimoniali",
"ver.portfolio.gets":"Un resoconto d’investimento che i clienti leggono invece di archiviare",
"ver.portfolio.cad":"Trimestrale o annuale",
"ver.pension.cust":"Casse pensioni e fondazioni collettive",
"ver.pension.gets":"Un certificato di previdenza che si capisce",
"ver.pension.cad":"Annuale",
"ver.school.cust":"Scuole e autorità scolastiche",
"ver.school.gets":"Un resoconto semestrale e annuale per i genitori",
"ver.school.cad":"Due volte l’anno",
"ver.health.cust":"Reti di medici e assicuratori malattia",
"ver.health.gets":"Un riepilogo annuale sulla salute che i pazienti capiscono",
"ver.health.cad":"Annuale",
"ver.team.cust":"Reparti HR",
"ver.team.gets":"Una valutazione delle prestazioni e dello sviluppo",
"ver.team.cad":"Annuale",
"comb.hint":"Un ambito più un formato danno il prodotto. Ne scelga uno per parte.",
"comb.lblV":"Ambito","comb.lblF":"Formato",
"who.h":"I dashboard sono per gli analisti.",
"who.p1":"Uno strumento di BI serve chi guarda i dati per mestiere. Tellingly serve la persona che riceve il documento e dei dati non si interessa affatto: la pensionata, il padre, la cliente.",
"who.p2":"Non siamo un dashboard, né uno strumento di BI, né una libreria di visualizzazione. Se i suoi destinatari vogliono esplorare i numeri, compri un dashboard. Se devono capire che cosa è successo, parliamone.",
"contact.h":"Parliamone.",
"contact.p":"I documenti per il 2027 si preparano adesso. Se i suoi devono farne parte, ne parliamo. Un colloquio, non una demo.",
"contact.cta":"Ci scriva",
"foot.legal":"Tellingly GmbH — Kreuzlingen, Svizzera",
"mail.subject":"Richiesta da tellingly.ch",
"fmt.reel.medium":"Mobile, verticale, ritmato",
"fmt.reel.body":"Novanta secondi sul telefono. L’anno come una sequenza di carte da inoltrare.",
"pv.kicker":"Portfolio 2026",
"pv.num":"&#8722;3.12&#8201;%",
"pv.numlabel":"Risultato 2026",
"pv.h":"Il suo anno in trenta secondi",
"pv.p":"Una strategia chiara non protegge da ogni oscillazione. Dà un orientamento quando mercati, tassi e notizie cambiano in fretta.",
"pv.short":"Una strategia chiara non protegge da ogni oscillazione.",
"pv.h2":"Che cosa ha mosso il suo portafoglio"
},
en:{
"meta.title":"Tellingly — data, told.",
"meta.desc":"Tellingly turns institutional data into a story people finish. Pension, portfolio, school, health, team. Kreuzlingen, Switzerland.",
"a11y.skip":"Skip to content",
"nav.argument":"Argument","nav.formats":"Formats","nav.verticals":"Verticals","nav.who":"Distinction",
"nav.contact":"Contact",
"nav.try":"Try it",
"try.h":"See it for yourself.",
"try.sub":"Pick a vertical and a format. The content stays the same — only the delivery changes.",
"stage.unbranded":"Unbranded. Colour, type and logo come from you.",
"stage.motion":"Reel and Brief move; the Edition stays still — it is print. Motion only where it explains a figure: the amount counts up, the shortfall grows as a second bar, the lab value slides into its reference range.",
"stage.prev":"Back",
"stage.next":"Next",
"stage.figures":"Key figures",
"hero.line0":"Your bank sent you a portfolio statement in January.<br><span class=\"quiet\">You have not opened it.</span>",
"hero.line1":"Your pension fund sent you the statement in January.<br><span class=\"quiet\">You do not know what it means.</span>",
"hero.line2":"Your child’s school sent you the report in February.<br><span class=\"quiet\">You saw the grades, not the year.</span>",
"hero.line3":"Your doctor sent you a lab result in March.<br><span class=\"quiet\">You googled half of it.</span>",
"hero.line4":"Your employer sent you the review in December.<br><span class=\"quiet\">You skimmed it once.</span>",
"hero.navlabel":"Document",
"hero.tab0":"Portfolio statement",
"hero.tab1":"Pension statement",
"hero.tab2":"School report",
"hero.tab3":"Lab result",
"hero.tab4":"Performance review",
"hero.sub":"Tellingly takes the same data and tells it. Institutions send it. People finish it.",
"hero.cta":"Talk to us",
"arg.h":"Accounting came before literature.",
"arg.p1":"Writing was invented in Uruk around 3400 BC to count grain and livestock. The first documents were ledgers. Literature arrived a thousand years later.",
"arg.p2":"Somewhere in the next five thousand years the numbers stopped speaking to anyone. Yet a pension statement and a school report are the same human act: someone telling you what happened to something you care about. We rebuild the connection between the ledger and the telling.",
"arg.pull":"We do not simplify your data. We give it a narrator.",
"fmt.h":"The same data, told three ways.",
"fmt.sub":"Every vertical comes in all three formats. The same review, delivered three ways.",
"fmt.eg":"Example",
"fmt.brief.medium":"Digital, in the browser",
"fmt.brief.body":"The whole review, scrolled. One link, no login, no PDF.",
"fmt.brief.note":"In German a Brief is a letter: a review that arrives like post.",
"fmt.edition.medium":"Print",
"fmt.edition.body":"Long, substantial, considered. Something kept — not another mailing.",
"ver.h":"Five industries. One craft.",
"ver.sub":"Tellingly Studio writes, Tellingly Engine generates. Beneath them sit five verticals — and every vertical exists in every format.",
"ver.c0":"Vertical","ver.c1":"Customer","ver.c2":"What the recipient gets","ver.c3":"Cadence",
"ver.portfolio.cust":"Banks and wealth managers",
"ver.portfolio.gets":"An investment review clients read instead of file",
"ver.portfolio.cad":"Quarterly or annual",
"ver.pension.cust":"Pension funds and collective foundations",
"ver.pension.gets":"An occupational pension statement people understand",
"ver.pension.cad":"Annual",
"ver.school.cust":"Schools and education authorities",
"ver.school.gets":"A semester and year-end review for parents",
"ver.school.cad":"Twice yearly",
"ver.health.cust":"Physician networks and health insurers",
"ver.health.gets":"An annual health summary patients understand",
"ver.health.cad":"Annual",
"ver.team.cust":"HR departments",
"ver.team.gets":"A performance and development review",
"ver.team.cad":"Annual",
"comb.hint":"A vertical plus a format is the product. Pick one of each.",
"comb.lblV":"Vertical","comb.lblF":"Format",
"who.h":"Dashboards are for analysts.",
"who.p1":"A BI tool serves people whose job is to look at data. Tellingly serves the person who receives the document and has no interest in data at all: the pensioner, the father, the client.",
"who.p2":"We are not a dashboard, not a BI tool, not a visualisation library. If your recipients want to explore the numbers, buy a dashboard. If they need to understand what happened, talk to us.",
"contact.h":"Talk to us.",
"contact.p":"The 2027 documents are being built now. If yours should be among them, let us talk. A conversation, not a demo.",
"contact.cta":"Write to us",
"foot.legal":"Tellingly GmbH — Kreuzlingen, Switzerland",
"mail.subject":"Enquiry via tellingly.ch",
"fmt.reel.medium":"Mobile, vertical, paced",
"fmt.reel.body":"Ninety seconds on a phone. The year as a run of cards people forward.",
"pv.kicker":"Portfolio 2026",
"pv.num":"&#8722;3.12&#8201;%",
"pv.numlabel":"Result 2026",
"pv.h":"Your year in thirty seconds",
"pv.p":"A clear strategy does not protect you from every swing. It gives you a bearing when markets, rates and news move quickly.",
"pv.short":"A clear strategy does not protect you from every swing.",
"pv.h2":"What moved your portfolio"
}
};

var nodes=document.querySelectorAll("[data-i18n]");
var langBtns=document.querySelectorAll("[data-lang]");
var mailBtn=document.getElementById("mailBtn");
var metaDesc=document.querySelector('meta[name="description"]');
var current="de";

function applyLang(l,writeUrl){
  var d=I18N[l]; if(!d){return;}
  current=l;
  document.documentElement.lang=l;
  for(var i=0;i<nodes.length;i++){
    var v=d[nodes[i].getAttribute("data-i18n")];
    if(v!=null){nodes[i].innerHTML=v;}
  }
  document.title=d["meta.title"];
  if(metaDesc){metaDesc.setAttribute("content",d["meta.desc"]);}
  for(var j=0;j<langBtns.length;j++){
    langBtns[j].setAttribute("aria-pressed",String(langBtns[j].getAttribute("data-lang")===l));
  }
  if(mailBtn){mailBtn.setAttribute("href","mailto:hallo@tellingly.ch?subject="+encodeURIComponent(d["mail.subject"]));}
  var tn=document.getElementById("tellnav");
  if(tn&&d["hero.navlabel"]){tn.setAttribute("aria-label",d["hero.navlabel"]);}
  if(typeof renderStage==="function"){renderStage();}
  var th=document.querySelectorAll(".verts th");
  var map=["ver.c0","ver.c1","ver.c2","ver.c3"];
  var cells=document.querySelectorAll(".verts td[data-h]");
  for(var k=0;k<cells.length;k++){
    cells[k].setAttribute("data-h",d[map[(k%3)+1]]);
  }
  if(writeUrl&&window.history&&history.replaceState){
    try{
      var u=new URL(window.location.href);
      u.searchParams.set("lang",l);
      history.replaceState(null,"",u.toString());
    }catch(e){}
  }
}

for(var b=0;b<langBtns.length;b++){
  langBtns[b].addEventListener("click",function(){
    applyLang(this.getAttribute("data-lang"),true);
  });
}

/* first paint: honour ?lang=, else the browser's preference, else German */
(function(){
  var q="";
  try{q=(new URLSearchParams(window.location.search).get("lang")||"").toLowerCase();}catch(e){}
  if(LANGS.indexOf(q)>-1){applyLang(q,false);return;}
  var prefs=navigator.languages||[navigator.language||"de"];
  for(var i=0;i<prefs.length;i++){
    var c=String(prefs[i]).slice(0,2).toLowerCase();
    if(LANGS.indexOf(c)>-1){if(c!=="de"){applyLang(c,false);}else{applyLang("de",false);}return;}
  }
  applyLang("de",false);
})();

/* the window: five documents, five tellings */
var tells=document.querySelectorAll(".tell");
var docsEl=document.querySelectorAll(".field .doc");
var tabsEl=document.querySelectorAll(".tellnav button");
var tellIdx=0,tellTimer=null,tellLocked=false;
var reduceMotion=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function showTell(i){
  tellIdx=i;
  for(var a=0;a<tells.length;a++){tells[a].classList.toggle("is-on",a===i);}
  for(var b2=0;b2<docsEl.length;b2++){docsEl[b2].classList.toggle("is-on",b2===i);}
  for(var c=0;c<tabsEl.length;c++){tabsEl[c].setAttribute("aria-pressed",String(c===i));}
}
function tellStart(){
  if(reduceMotion||tellLocked||tellTimer||tells.length<2){return;}
  tellTimer=setInterval(function(){showTell((tellIdx+1)%tells.length);},5400);
}
function tellStop(){if(tellTimer){clearInterval(tellTimer);tellTimer=null;}}

(function(){
  for(var i=0;i<tabsEl.length;i++){
    (function(n){
      tabsEl[n].addEventListener("click",function(){tellLocked=true;tellStop();showTell(n);});
    })(i);
  }
  var env=document.querySelector(".envelope");
  if(env){
    env.addEventListener("mouseenter",tellStop);
    env.addEventListener("mouseleave",tellStart);
    env.addEventListener("focusin",tellStop);
  }
  document.addEventListener("visibilitychange",function(){
    if(document.hidden){tellStop();}else{tellStart();}
  });
  tellStart();
})();

var DEMO={"de":{"portfolio":{"kicker":"Portfolio 2026","title":"Ihr Anlagejahr 2026","beats":[{"l":"Ergebnis","v":"−3.12 %","t":"Ein Jahr, das im Februar zu wackeln begann und im Oktober zurückkam. Sie haben nichts falsch gemacht."},{"l":"Depotwert per 31.12.","v":"CHF 459’047"},{"l":"Was gehalten hat","v":"Obligationen","t":"Der ruhigste Teil Ihres Depots hat die beiden schwachen Quartale abgefedert. Genau dafür ist er da."},{"l":"Kosten","v":"0.65 % p.a."}],"close":"Drei Fragen für Ihr nächstes Gespräch. Ihre Beraterin bringt sie mit."},"pension":{"kicker":"Vorsorge 2026","title":"Ihre Vorsorge, in Zahlen und in Worten","beats":[{"l":"Altersguthaben","v":"CHF 301’662","t":"Dieses Jahr sind CHF 17’345 dazugekommen. CHF 3’554 davon sind Zins — Geld, das Sie nicht einzahlen mussten."},{"l":"Rente ab 65","v":"CHF 18’100 im Jahr"},{"l":"Wenn Sie mit 62 aufhören","v":"CHF 14’902","t":"Drei Jahre früher kosten rund ein Sechstel der Rente — lebenslang. Das ist eine Entscheidung, keine Nebenwirkung."},{"l":"Möglicher Einkauf","v":"CHF 64’209"}],"close":"Was Sie jetzt entscheiden können — und was Zeit hat."},"school":{"kicker":"Schuljahr 2026/27","title":"Das erste Semester von Lea","beats":[{"l":"Gesamtdurchschnitt","v":"4.96","t":"Von 4.77 im Vorjahr. Der Sprung kommt aus den Naturwissenschaften, nicht aus mehr Aufwand in allen Fächern."},{"l":"Stärkstes Fach","v":"Englisch 5.5"},{"l":"Grösster Fortschritt","v":"Biologie +0.5","t":"Zwei Fächer haben zugelegt, eines ist zurückgegangen. Mathematik braucht im zweiten Semester Aufmerksamkeit."},{"l":"Absenzen","v":"4 Lektionen"}],"close":"Worüber wir am Elterngespräch sprechen sollten."},"health":{"kicker":"Gesundheit 2026","title":"Ihre Werte, erklärt","beats":[{"l":"Im Normbereich","v":"9 von 15","t":"Die meisten Werte sind unauffällig. Sechs weichen ab — und vier davon hängen miteinander zusammen."},{"l":"LDL-Cholesterin","v":"3.9 mmol/l"},{"l":"Langzeitzucker HbA1c","v":"5.9 %","t":"Noch kein Diabetes, aber die Vorstufe. Dieser Wert bewegt sich schneller als jeder andere, wenn sich Alltag und Ernährung ändern."},{"l":"Nächste Kontrolle","v":"in 3 Monaten"}],"close":"Zwei Dinge, die bis dahin am meisten bringen."},"team":{"kicker":"Jahr 2026","title":"Ihr Jahr im Team","beats":[{"l":"Zielerreichung","v":"101.4 %","t":"Fünf Ziele, vier erreicht oder übertroffen. Das eine, das offen blieb, hing von anderen ab."},{"l":"Gesamtbewertung","v":"3 von 5"},{"l":"Grösster Zuwachs","v":"Kommunikation","t":"Ihre Selbsteinschätzung und die Ihrer Vorgesetzten lagen dieses Jahr zum ersten Mal gleichauf."},{"l":"Weiterbildung","v":"12 Tage"}],"close":"Drei Themen für das Entwicklungsgespräch im Januar."}},"en":{"portfolio":{"kicker":"Portfolio 2026","title":"Your investment year 2026","beats":[{"l":"Result","v":"−3.12 %","t":"A year that started wobbling in February and came back in October. You did nothing wrong."},{"l":"Portfolio value on 31 Dec","v":"CHF 459,047"},{"l":"What held","v":"Bonds","t":"The quietest part of your portfolio absorbed both weak quarters. That is exactly what it is there for."},{"l":"Costs","v":"0.65 % p.a."}],"close":"Three questions for your next meeting. Your adviser will bring them."},"pension":{"kicker":"Pension 2026","title":"Your pension, in figures and in words","beats":[{"l":"Retirement savings","v":"CHF 301,662","t":"CHF 17,345 was added this year. CHF 3,554 of it is interest — money you did not have to pay in."},{"l":"Pension from 65","v":"CHF 18,100 a year"},{"l":"If you stop at 62","v":"CHF 14,902","t":"Three years early costs about a sixth of the pension, for life. That is a decision, not a side effect."},{"l":"Voluntary purchase possible","v":"CHF 64,209"}],"close":"What you can decide now — and what can wait."},"school":{"kicker":"School year 2026/27","title":"Lea’s first semester","beats":[{"l":"Overall average","v":"4.96","t":"Up from 4.77 last year. The jump comes from the sciences, not from more effort across every subject."},{"l":"Strongest subject","v":"English 5.5"},{"l":"Biggest gain","v":"Biology +0.5","t":"Two subjects improved, one slipped. Mathematics needs attention in the second semester."},{"l":"Absences","v":"4 lessons"}],"close":"What we should talk about at the parents’ meeting."},"health":{"kicker":"Health 2026","title":"Your results, explained","beats":[{"l":"Within range","v":"9 of 15","t":"Most of your values are unremarkable. Six are off — and four of those are connected to each other."},{"l":"LDL cholesterol","v":"3.9 mmol/l"},{"l":"Long-term sugar HbA1c","v":"5.9 %","t":"Not diabetes, but the stage before it. This value moves faster than any other when daily habits change."},{"l":"Next check-up","v":"in 3 months"}],"close":"Two things that will help most before then."},"team":{"kicker":"Year 2026","title":"Your year on the team","beats":[{"l":"Goal attainment","v":"101.4 %","t":"Five goals, four met or beaten. The one left open depended on other people."},{"l":"Overall rating","v":"3 of 5"},{"l":"Biggest gain","v":"Communication","t":"Your own assessment and your manager’s landed at the same level for the first time this year."},{"l":"Training","v":"12 days"}],"close":"Three topics for the development conversation in January."}},"fr":{"portfolio":{"kicker":"Portefeuille 2026","title":"Votre année de placement 2026","beats":[{"l":"Résultat","v":"−3.12 %","t":"Une année qui a vacillé en février et qui est revenue en octobre. Vous n’avez rien fait de faux."},{"l":"Valeur au 31.12.","v":"CHF 459 047"},{"l":"Ce qui a tenu","v":"Obligations","t":"La partie la plus calme de votre portefeuille a amorti les deux trimestres faibles. C’est exactement son rôle."},{"l":"Coûts","v":"0.65 % p.a."}],"close":"Trois questions pour votre prochain entretien. Votre conseillère les apportera."},"pension":{"kicker":"Prévoyance 2026","title":"Votre prévoyance, en chiffres et en mots","beats":[{"l":"Avoir de vieillesse","v":"CHF 301 662","t":"CHF 17 345 se sont ajoutés cette année. CHF 3 554 sont des intérêts — de l’argent que vous n’avez pas versé."},{"l":"Rente dès 65 ans","v":"CHF 18 100 par an"},{"l":"Si vous arrêtez à 62 ans","v":"CHF 14 902","t":"Trois ans plus tôt coûtent environ un sixième de la rente, à vie. C’est une décision, pas un effet secondaire."},{"l":"Rachat possible","v":"CHF 64 209"}],"close":"Ce que vous pouvez décider maintenant — et ce qui peut attendre."},"school":{"kicker":"Année scolaire 2026/27","title":"Le premier semestre de Lea","beats":[{"l":"Moyenne générale","v":"4.96","t":"Contre 4.77 l’an dernier. Le progrès vient des sciences, pas d’un effort accru dans toutes les branches."},{"l":"Branche la plus forte","v":"Anglais 5.5"},{"l":"Plus grand progrès","v":"Biologie +0.5","t":"Deux branches ont progressé, une a reculé. Les mathématiques demanderont de l’attention au second semestre."},{"l":"Absences","v":"4 leçons"}],"close":"Ce dont nous devrions parler lors de l’entretien avec les parents."},"health":{"kicker":"Santé 2026","title":"Vos valeurs, expliquées","beats":[{"l":"Dans la norme","v":"9 sur 15","t":"La plupart de vos valeurs sont sans particularité. Six s’écartent — et quatre d’entre elles sont liées."},{"l":"Cholestérol LDL","v":"3.9 mmol/l"},{"l":"Glycémie HbA1c","v":"5.9 %","t":"Pas encore un diabète, mais le stade qui précède. C’est la valeur qui bouge le plus vite quand le quotidien change."},{"l":"Prochain contrôle","v":"dans 3 mois"}],"close":"Deux choses qui aideront le plus d’ici là."},"team":{"kicker":"Année 2026","title":"Votre année dans l’équipe","beats":[{"l":"Atteinte des objectifs","v":"101.4 %","t":"Cinq objectifs, quatre atteints ou dépassés. Le seul resté ouvert dépendait des autres."},{"l":"Évaluation globale","v":"3 sur 5"},{"l":"Plus forte progression","v":"Communication","t":"Votre auto-évaluation et celle de votre responsable se sont rejointes pour la première fois cette année."},{"l":"Formation","v":"12 jours"}],"close":"Trois sujets pour l’entretien de développement en janvier."}},"it":{"portfolio":{"kicker":"Portafoglio 2026","title":"Il suo anno d’investimento 2026","beats":[{"l":"Risultato","v":"−3.12 %","t":"Un anno che ha vacillato in febbraio ed è tornato in ottobre. Lei non ha sbagliato nulla."},{"l":"Valore al 31.12.","v":"CHF 459’047"},{"l":"Che cosa ha tenuto","v":"Obbligazioni","t":"La parte più tranquilla del suo portafoglio ha attutito i due trimestri deboli. È esattamente il suo compito."},{"l":"Costi","v":"0.65 % p.a."}],"close":"Tre domande per il prossimo colloquio. La sua consulente le porterà con sé."},"pension":{"kicker":"Previdenza 2026","title":"La sua previdenza, in cifre e in parole","beats":[{"l":"Avere di vecchiaia","v":"CHF 301’662","t":"Quest’anno si sono aggiunti CHF 17’345. Di questi, CHF 3’554 sono interessi — denaro che lei non ha versato."},{"l":"Rendita dai 65 anni","v":"CHF 18’100 all’anno"},{"l":"Se smette a 62 anni","v":"CHF 14’902","t":"Tre anni prima costano circa un sesto della rendita, a vita. È una decisione, non un effetto collaterale."},{"l":"Riscatto possibile","v":"CHF 64’209"}],"close":"Che cosa può decidere ora — e che cosa può aspettare."},"school":{"kicker":"Anno scolastico 2026/27","title":"Il primo semestre di Lea","beats":[{"l":"Media generale","v":"4.96","t":"Da 4.77 dell’anno scorso. Il salto arriva dalle scienze, non da più impegno in tutte le materie."},{"l":"Materia più forte","v":"Inglese 5.5"},{"l":"Progresso maggiore","v":"Biologia +0.5","t":"Due materie sono migliorate, una è arretrata. La matematica richiederà attenzione nel secondo semestre."},{"l":"Assenze","v":"4 lezioni"}],"close":"Di che cosa dovremmo parlare al colloquio con i genitori."},"health":{"kicker":"Salute 2026","title":"I suoi valori, spiegati","beats":[{"l":"Nella norma","v":"9 su 15","t":"La maggior parte dei valori non presenta particolarità. Sei si discostano — e quattro di questi sono collegati fra loro."},{"l":"Colesterolo LDL","v":"3.9 mmol/l"},{"l":"Glicemia HbA1c","v":"5.9 %","t":"Non è diabete, ma lo stadio che lo precede. È il valore che si muove più in fretta quando cambiano abitudini e alimentazione."},{"l":"Prossimo controllo","v":"fra 3 mesi"}],"close":"Due cose che da qui ad allora servono di più."},"team":{"kicker":"Anno 2026","title":"Il suo anno nel team","beats":[{"l":"Raggiungimento obiettivi","v":"101.4 %","t":"Cinque obiettivi, quattro raggiunti o superati. L’unico rimasto aperto dipendeva da altri."},{"l":"Valutazione complessiva","v":"3 su 5"},{"l":"Crescita maggiore","v":"Comunicazione","t":"La sua autovalutazione e quella della sua responsabile quest’anno hanno coinciso per la prima volta."},{"l":"Formazione","v":"12 giorni"}],"close":"Tre temi per il colloquio di sviluppo di gennaio."}}};
var WHY={"de":{"portfolio":{"h":"Wofür Banken und Vermögensverwalter das einsetzen","p":"Der Quartals- oder Jahresauszug ist der einzige garantierte Kontaktpunkt mit jedem einzelnen Kunden. Heute wird er abgelegt. Gelesen wird er, wenn er erzählt, was im Depot passiert ist — und er endet mit einer Frage, die ein Gespräch auslöst.","o":["Höhere Lesequote statt ungeöffneter Auszüge","Mehr Beratungstermine, ausgelöst vom Versand selbst","Persönlicher Bezug statt Standardreporting"]},"pension":{"h":"Wofür Pensionskassen das einsetzen","p":"Der Vorsorgeausweis ist gesetzlich vorgeschrieben und wird trotzdem nicht gelesen. Wer versteht, was er besitzt, fragt seltener nach, entscheidet bewusster und traut seiner Kasse mehr.","o":["Weniger Rückfragen nach dem Versand","Bewusstere Entscheide zu Einkauf, Kapitalbezug und Rentenalter","Vertrauen in eine Institution, die man sonst nie sieht"]},"school":{"h":"Wofür Schulen und Bildungsbehörden das einsetzen","p":"Eltern lesen Noten und übersehen den Verlauf. Ein Bericht, der die Entwicklung erzählt, macht das Elterngespräch kürzer und besser — weil beide Seiten mit demselben Bild hineingehen.","o":["Eltern, die vorbereitet ins Gespräch kommen","Weniger Diskussionen über einzelne Noten","Fortschritt wird sichtbar, nicht nur das Niveau"]},"health":{"h":"Wofür Ärztenetze und Krankenversicherer das einsetzen","p":"Ein Befund, den niemand versteht, erzeugt Angst oder Gleichgültigkeit. Beides kostet. Eine erklärte Jahresübersicht bringt Patientinnen und Patienten zur nächsten Kontrolle — und nimmt Anrufe aus der Praxis.","o":["Höhere Termintreue bei Nachkontrollen","Weniger beunruhigte Anrufe nach dem Versand","Prävention, die ankommt statt vorbeigeht"]},"team":{"h":"Wofür HR-Abteilungen das einsetzen","p":"Die Jahresbeurteilung wird geschrieben, unterschrieben und vergessen. Bleibt sie im Kopf, beginnt das Entwicklungsgespräch nicht mehr bei null.","o":["Beurteilungen, an die man sich im März noch erinnert","Bessere Entwicklungs- und Lohngespräche","Ein Signal an Mitarbeitende, dass genau hingeschaut wurde"]}},"en":{"portfolio":{"h":"What banks and wealth managers use it for","p":"The quarterly or annual statement is the one guaranteed touchpoint with every single client. Today it gets filed. It gets read when it tells what actually happened in the portfolio — and it ends with a question that starts a conversation.","o":["Statements that are read instead of filed","More advisory meetings, triggered by the mailing itself","A personal relationship instead of standard reporting"]},"pension":{"h":"What pension funds use it for","p":"The pension statement is legally mandated and still goes unread. People who understand what they own ask fewer questions, decide more deliberately, and trust their fund more.","o":["Fewer support enquiries after the mailing","More deliberate decisions on buy-ins, capital and retirement age","Trust in an institution nobody ever sees"]},"school":{"h":"What schools and education authorities use it for","p":"Parents read grades and miss the trajectory. A report that tells the development makes the parents’ meeting shorter and better — because both sides walk in with the same picture.","o":["Parents who arrive prepared","Fewer arguments about individual grades","Progress becomes visible, not just the level"]},"health":{"h":"What physician networks and health insurers use it for","p":"A result nobody understands produces either fear or indifference. Both are expensive. An explained annual summary brings patients back for the next check-up — and takes calls off the practice.","o":["Better attendance at follow-up appointments","Fewer anxious calls after the mailing","Prevention that lands instead of passing by"]},"team":{"h":"What HR departments use it for","p":"The annual review is written, signed and forgotten. When it stays in mind, the development conversation no longer starts from zero.","o":["Reviews people still remember in March","Better development and salary conversations","A signal to employees that someone actually looked closely"]}},"fr":{"portfolio":{"h":"À quoi cela sert aux banques et aux gérants de fortune","p":"Le relevé trimestriel ou annuel est le seul point de contact garanti avec chaque client. Aujourd’hui, il est classé. Il est lu lorsqu’il raconte ce qui s’est passé dans le portefeuille — et il se termine par une question qui déclenche un entretien.","o":["Des relevés lus au lieu d’être classés","Davantage de rendez-vous, déclenchés par l’envoi lui-même","Une relation personnelle plutôt qu’un reporting standard"]},"pension":{"h":"À quoi cela sert aux caisses de pension","p":"Le certificat de prévoyance est prescrit par la loi et reste malgré tout non lu. Qui comprend ce qu’il possède pose moins de questions, décide plus consciemment et fait davantage confiance à sa caisse.","o":["Moins de demandes après l’envoi","Des décisions plus réfléchies sur le rachat, le capital et l’âge de la retraite","La confiance envers une institution que l’on ne voit jamais"]},"school":{"h":"À quoi cela sert aux écoles et aux autorités scolaires","p":"Les parents lisent les notes et manquent la trajectoire. Un bilan qui raconte l’évolution rend l’entretien plus court et meilleur — parce que les deux parties arrivent avec la même image.","o":["Des parents qui arrivent préparés","Moins de discussions sur telle ou telle note","Le progrès devient visible, pas seulement le niveau"]},"health":{"h":"À quoi cela sert aux réseaux de médecins et aux assureurs","p":"Un résultat que personne ne comprend produit soit de l’angoisse, soit de l’indifférence. Les deux coûtent cher. Un bilan annuel expliqué ramène les patients au contrôle suivant — et décharge le cabinet.","o":["Une meilleure présence aux contrôles de suivi","Moins d’appels inquiets après l’envoi","Une prévention qui arrive au lieu de passer à côté"]},"team":{"h":"À quoi cela sert aux départements RH","p":"L’évaluation annuelle est rédigée, signée et oubliée. Lorsqu’elle reste en tête, l’entretien de développement ne repart plus de zéro.","o":["Des évaluations dont on se souvient encore en mars","De meilleurs entretiens de développement et de salaire","Un signal aux collaborateurs qu’on a vraiment regardé de près"]}},"it":{"portfolio":{"h":"A che cosa serve a banche e gestori patrimoniali","p":"Il resoconto trimestrale o annuale è l’unico punto di contatto garantito con ogni singolo cliente. Oggi viene archiviato. Viene letto quando racconta che cosa è successo nel portafoglio — e si chiude con una domanda che apre un colloquio.","o":["Resoconti letti invece che archiviati","Più appuntamenti di consulenza, generati dall’invio stesso","Una relazione personale al posto del reporting standard"]},"pension":{"h":"A che cosa serve alle casse pensioni","p":"Il certificato di previdenza è prescritto dalla legge e resta comunque non letto. Chi capisce che cosa possiede chiede meno, decide con più consapevolezza e si fida di più della propria cassa.","o":["Meno richieste dopo l’invio","Decisioni più consapevoli su riscatto, capitale ed età di pensionamento","Fiducia in un’istituzione che non si vede mai"]},"school":{"h":"A che cosa serve a scuole e autorità scolastiche","p":"I genitori leggono i voti e perdono di vista il percorso. Un resoconto che racconta lo sviluppo rende il colloquio più breve e migliore — perché entrambe le parti arrivano con la stessa immagine.","o":["Genitori che arrivano preparati","Meno discussioni sui singoli voti","Il progresso diventa visibile, non solo il livello"]},"health":{"h":"A che cosa serve a reti di medici e assicuratori malattia","p":"Un referto che nessuno capisce produce paura o indifferenza. Entrambe costano. Un riepilogo annuale spiegato riporta i pazienti al controllo successivo — e alleggerisce lo studio medico.","o":["Maggiore puntualità ai controlli di follow-up","Meno telefonate preoccupate dopo l’invio","Prevenzione che arriva invece di passare accanto"]},"team":{"h":"A che cosa serve ai reparti HR","p":"La valutazione annuale viene scritta, firmata e dimenticata. Se resta in mente, il colloquio di sviluppo non riparte più da zero.","o":["Valutazioni che a marzo si ricordano ancora","Colloqui di sviluppo e di salario migliori","Un segnale ai collaboratori che qualcuno ha guardato davvero"]}}};


/* Motion is an argument, not decoration: it runs where it explains a figure,
   never on the Edition (print), never under prefers-reduced-motion. */
var VIS={"portfolio":[{"k":"delta","spark":[0,3,-5,-9,-4,-2,-6,-11,-7,-2,1,-3]},{"k":"num"},{"k":"name"},{"k":"num"}],"pension":[{"k":"num","parts":[79.5,20.5]},{"k":"num"},{"k":"gap","a":18100,"b":14902},{"k":"num"}],"school":[{"k":"from","from":4.77},{"k":"name"},{"k":"gap","a":5.0,"b":5.5},{"k":"ticks","n":4}],"health":[{"k":"share","n":15,"on":9},{"k":"range","min":0,"max":6.5,"band":[0,3.0],"val":3.9},{"k":"range","min":4.5,"max":7.5,"band":[4.5,5.7],"val":5.9},{"k":"ticks","n":3}],"team":[{"k":"meter","val":101.4,"target":100,"max":125},{"k":"share","n":5,"on":3},{"k":"name"},{"k":"ticks","n":12}]};
var reduceUI=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function numParts(str){
  var m=String(str).match(/([-\u2212]?)(\d[\d'\u2019.,\u00a0 ]*)/);
  if(!m){return null;}
  var raw=m[2],pre=String(str).slice(0,m.index),post=String(str).slice(m.index+m[0].length);
  var dm=raw.match(/[.,](\d{1,2})$/);
  var dec=dm?dm[1].length:0;
  var decSep=dm?raw.charAt(raw.length-dm[1].length-1):".";
  var body=dec?raw.slice(0,raw.length-dm[1].length-1):raw;
  var gm=body.match(/['\u2019.,\u00a0 ]/);
  var val=parseFloat(body.replace(/['\u2019.,\u00a0 ]/g,"")+(dec?"."+raw.slice(-dec):""));
  if(m[1]){val=-val;}
  return {pre:pre,post:post,dec:dec,decSep:decSep,grp:gm?gm[0]:"",val:val};
}
function fmtNum(v,p){
  var neg=v<0;v=Math.abs(v);
  var s=v.toFixed(p.dec),ip=p.dec?s.slice(0,s.length-p.dec-1):s,fp=p.dec?s.slice(s.length-p.dec):"";
  if(p.grp){ip=ip.replace(/\B(?=(\d{3})+(?!\d))/g,p.grp);}
  return p.pre+(neg?"\u2212":"")+ip+(p.dec?p.decSep+fp:"")+p.post;
}
function countUp(el,animate){
  var target=el.getAttribute("data-target")||el.textContent;
  el.setAttribute("data-target",target);
  var p=numParts(target);
  if(!p){return;}
  var from=parseFloat(el.getAttribute("data-from"));
  if(isNaN(from)){from=0;}
  if(!animate){el.textContent=target;return;}
  var t0=null,dur=850;
  el.textContent=fmtNum(from,p);
  function step(t){
    if(t0===null){t0=t;}
    var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
    el.textContent=fmtNum(from+(p.val-from)*e,p);
    if(k<1){requestAnimationFrame(step);}else{el.textContent=target;}
  }
  requestAnimationFrame(step);
}
function reveal(el,animate){
  var counts=el.querySelectorAll("[data-count]");
  if(!animate){
    el.classList.add("no-motion");
    el.classList.add("is-on");
    for(var i=0;i<counts.length;i++){countUp(counts[i],false);}
    return;
  }
  el.classList.remove("no-motion");
  el.classList.remove("is-on");
  void el.offsetWidth;
  el.classList.add("is-on");
  for(var j=0;j<counts.length;j++){countUp(counts[j],true);}
}
function startMotion(view){
  var animate=!reduceUI&&fSel!=="Edition";
  if(fSel==="Reel"){
    var card=view.querySelector(".d-rcard");
    if(card){reveal(card,animate);}
    return;
  }
  var secs=view.querySelectorAll(".d-sec");
  if(fSel==="Edition"||!animate||!("IntersectionObserver" in window)){
    for(var i=0;i<secs.length;i++){reveal(secs[i],false);}
    if(fSel==="Edition"){reveal(view,false);}
    return;
  }
  var scroller=view.querySelector(".d-scroll");
  var io=new IntersectionObserver(function(entries){
    for(var k=0;k<entries.length;k++){
      if(entries[k].isIntersecting){reveal(entries[k].target,true);io.unobserve(entries[k].target);}
    }
  },{root:scroller,threshold:0.55});
  for(var m2=0;m2<secs.length;m2++){io.observe(secs[m2]);}
}

var VKEY={Portfolio:"portfolio",Pension:"pension",School:"school",Health:"health",Team:"team"};
var FNOTE={Reel:["fmt.reel.medium","fmt.reel.body"],Brief:["fmt.brief.medium","fmt.brief.body"],Edition:["fmt.edition.medium","fmt.edition.body"]};
var vSel="Pension",fSel="Brief",reelIdx=0;

function tx(k){var d=I18N[current];return (d&&d[k])||"";}
function esc(x){return String(x).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

function cardsOf(d){
  var out=[{k:"open"}];
  for(var i=0;i<d.beats.length;i++){out.push({k:"beat",b:d.beats[i]});}
  out.push({k:"close"});
  return out;
}
function pct(x){return Math.max(0,Math.min(100,x));}
function metricHTML(v){
  if(!v){return "";}
  var h="",i;
  if(v.k==="num"&&v.parts){
    h='<div class="m-bar">';
    for(i=0;i<v.parts.length;i++){h+='<i style="--w:'+v.parts[i]+'%"></i>';}
    h+='</div>';
  }else if(v.k==="gap"){
    var mx=Math.max(v.a,v.b);
    h='<div class="m-gap"><i style="--w:'+pct(v.a/mx*100)+'%"></i>'+
      '<i class="b" style="--w:'+pct(v.b/mx*100)+'%"></i></div>';
  }else if(v.k==="share"){
    h='<div class="m-dots" style="--cols:'+(v.n<=6?v.n:5)+'">';
    for(i=0;i<v.n;i++){h+='<i class="'+(i<v.on?"on":"")+'" style="--i:'+i+'"></i>';}
    h+='</div>';
  }else if(v.k==="ticks"){
    h='<div class="m-ticks">';
    for(i=0;i<v.n;i++){h+='<i style="--i:'+i+'"></i>';}
    h+='</div>';
  }else if(v.k==="range"){
    var sp=v.max-v.min;
    h='<div class="m-range"><span class="band" style="--bl:'+pct((v.band[0]-v.min)/sp*100)+
      '%;--bw:'+pct((v.band[1]-v.band[0])/sp*100)+'%"></span>'+
      '<span class="mark" style="--l:'+pct((v.val-v.min)/sp*100)+'%"></span></div>';
  }else if(v.k==="meter"){
    h='<div class="m-meter"><i style="--w:'+pct(v.val/v.max*100)+'%"></i>'+
      '<span class="target" style="--t:'+pct(v.target/v.max*100)+'%"></span></div>';
  }else if(v.k==="delta"){
    var pts=v.spark,lo=Math.min.apply(null,pts),hi=Math.max.apply(null,pts),rg=(hi-lo)||1,d="";
    for(i=0;i<pts.length;i++){
      d+=(i?"L":"M")+(i/(pts.length-1)*100).toFixed(2)+","+(26-(pts[i]-lo)/rg*22).toFixed(2);
    }
    var zy=(26-(0-lo)/rg*22).toFixed(2);
    h='<svg class="m-spark" viewBox="0 0 100 30" preserveAspectRatio="none" aria-hidden="true">'+
      '<line x1="0" y1="'+zy+'" x2="100" y2="'+zy+'"></line><path d="'+d+'"></path></svg>';
  }
  return h?'<div class="d-metric">'+h+'</div>':"";
}
function beatBlock(b,v){
  var val=esc(b.v);
  if(v&&v.k==="name"){val='<span class="m-wipe">'+val+'</span>';}
  var from=(v&&v.k==="from")?' data-from="'+v.from+'"':"";
  return '<p class="d-label">'+esc(b.l)+'</p><p class="d-value" data-count="1"'+from+'>'+val+'</p>'+
         metricHTML(v)+
         (b.t?'<p class="d-text">'+esc(b.t)+'</p>':'');
}
function viewReel(d,vis){
  var cards=cardsOf(d),n=cards.length;
  if(reelIdx<0){reelIdx=0;} if(reelIdx>=n){reelIdx=n-1;}
  var c=cards[reelIdx],inner;
  if(c.k==="open"){inner='<p class="d-kicker">'+esc(d.kicker)+'</p><p class="d-title">'+esc(d.title)+'</p>';}
  else if(c.k==="beat"){inner=beatBlock(c.b,vis[reelIdx-1]);}
  else{inner='<p class="d-close">'+esc(d.close)+'</p>';}
  var bar="";
  for(var i=0;i<n;i++){bar+='<i class="'+(i<=reelIdx?"on":"")+'"></i>';}
  return '<div class="d-reelwrap"><div class="d-phone" data-reel="1" style="cursor:pointer">'+
    '<div class="d-rbar" aria-hidden="true">'+bar+'</div>'+
    '<div class="d-rcard">'+inner+'</div>'+
    '<div class="d-phonefoot" aria-hidden="true"><span class="d-slot" aria-hidden="true"></span></div></div>'+
    '<div class="d-reelnav">'+
      '<button type="button" data-reel="-1">'+esc(tx("stage.prev"))+'</button>'+
      '<span class="d-count">'+(reelIdx+1)+' / '+n+'</span>'+
      '<button type="button" data-reel="1">'+esc(tx("stage.next"))+'</button>'+
    '</div></div>';
}
function viewBrief(d,vis){
  var s='<div class="d-page"><div class="d-pagehead"><span class="d-slot" aria-hidden="true"></span>'+
        '<span class="d-kicker">'+esc(d.kicker)+'</span></div>'+
        '<h4 class="d-h1">'+esc(d.title)+'</h4>';
  for(var i=0;i<d.beats.length;i++){s+='<section class="d-sec">'+beatBlock(d.beats[i],vis[i])+'</section>';}
  s+='<div class="d-rule"></div><p class="d-close">'+esc(d.close)+'</p></div>';
  return '<div class="d-briefwrap"><div class="d-scroll" tabindex="0" role="region" aria-label="'+esc(d.title)+'">'+s+'</div></div>';
}
function viewEdition(d,vis){
  var figs="";
  for(var i=0;i<d.beats.length;i++){
    figs+='<li><span class="d-figrow"><span>'+esc(d.beats[i].l)+'</span><span>'+esc(d.beats[i].v)+
            '</span></span>'+metricHTML(vis[i])+'</li>';
  }
  return '<div class="d-spread">'+
   '<div class="d-leaf"><div class="d-pagehead"><span class="d-slot" aria-hidden="true"></span>'+
     '<span class="d-kicker">'+esc(d.kicker)+'</span></div>'+
     '<h4 class="d-h1">'+esc(d.title)+'</h4>'+
     '<p class="d-text" style="margin-top:0">'+esc(d.beats[0].t||"")+'</p>'+
     '<p class="d-text">'+esc(d.beats[2].t||"")+'</p>'+
     '<div class="d-folio">1</div></div>'+
   '<div class="d-leaf">'+
     '<p class="d-label">'+esc(tx("stage.figures"))+'</p>'+
     '<ul class="d-figs">'+figs+'</ul>'+
     '<p class="d-close" style="margin-top:auto">'+esc(d.close)+'</p>'+
     '<div class="d-folio">2</div></div></div>';
}

function renderStage(){
  var view=document.getElementById("stageview");
  if(!view||typeof DEMO==="undefined"||!DEMO||!DEMO[current]){return;}
  if(!vSel||!fSel||!VKEY[vSel]){return;}
  var key=VKEY[vSel],d=DEMO[current][key],w=WHY[current][key];
  if(!d){return;}
  var vis=(typeof VIS!=="undefined"&&VIS[key])?VIS[key]:[];
  view.innerHTML = fSel==="Reel"?viewReel(d,vis):(fSel==="Edition"?viewEdition(d,vis):viewBrief(d,vis));
  startMotion(view);

  var name=document.getElementById("comboName");
  var token=document.getElementById("comboToken");
  if(name){name.textContent=vSel+" "+fSel;}
  if(token){token.innerHTML=vSel.toLowerCase()+'<span class="dot">.</span>'+fSel.toLowerCase();}

  var note=document.getElementById("stagenote");
  if(note){note.textContent=tx(FNOTE[fSel][0])+" — "+tx(FNOTE[fSel][1]);}

  var h=document.getElementById("whyH"),pp=document.getElementById("whyP"),ul=document.getElementById("whyO");
  if(h&&w){h.textContent=w.h;pp.textContent=w.p;
    var li="";for(var i=0;i<w.o.length;i++){li+="<li>"+esc(w.o[i])+"</li>";}
    ul.innerHTML=li;}
}

(function(){
  var vChips=document.querySelectorAll("[data-v]");
  var fChips=document.querySelectorAll("[data-f]");
  function bind(list,attr,set){
    for(var i=0;i<list.length;i++){
      (function(el){
        el.addEventListener("click",function(){
          for(var j=0;j<list.length;j++){list[j].setAttribute("aria-pressed","false");}
          el.setAttribute("aria-pressed","true");
          set(el.getAttribute(attr));reelIdx=0;renderStage();
        });
      })(list[i]);
    }
  }
  bind(vChips,"data-v",function(v){vSel=v;});
  bind(fChips,"data-f",function(f){fSel=f;});
  var view=document.getElementById("stageview");
  if(view){
    view.addEventListener("click",function(e){
      var b=e.target.closest?e.target.closest("[data-reel]"):null;
      if(!b){return;}
      var dir=b.getAttribute("data-reel");
      var wasButton=b.tagName==="BUTTON";
      reelIdx+=parseInt(dir,10);
      renderStage();
      if(wasButton){
        var again=view.querySelector('.d-reelnav [data-reel="'+dir+'"]');
        if(again){try{again.focus();}catch(err){}}
      }
    });
  }
  renderStage();
})();

})();