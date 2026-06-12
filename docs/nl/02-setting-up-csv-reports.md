---
title: "Authorized Buyers CSV-rapporten: 5 Die Cat-Scan Nodig Heeft"
description: "Google Authorized Buyers heeft geen Reporting API, dus Cat-Scan reconstrueert de trechter uit vijf geplande CSV-rapporten. Volledig metrisch en dimensiereferentie plus installatie."
---

# Uw CSV-rapporten instellen

*Doelgroep: media buyers, accountmanagers*

Voordat Cat-Scan iets kan analyseren, heeft het data nodig. Google Authorized Buyers
heeft geen Reporting API, dus alle data stroomt via **vijf geplande CSV-rapporten**
die u eenmalig aanmaakt in uw Google AB-account.

!!! warning "Waarom vijf afzonderlijke rapporten?"
    De rapportagekolommen van Google zijn niet allemaal compatibel met elkaar. Zo
    kan "Biedverzoeken" niet in hetzelfde rapport verschijnen als "Mobiele app-ID"
    of "Creative-ID + Facturerings-ID". Voor volledige trechtervisibiliteit heeft u
    vijf rapporten nodig die Cat-Scan automatisch samenvoegt.

## De vijf rapporten in één oogopslag

| # | Rapportnaam | Wat het Cat-Scan vertelt | Belangrijkste kolommen |
|---|-------------|--------------------------|------------------------|
| 1 | **Quality** | Prestaties op creative-niveau met zichtbaarheid | Billing ID, Creative ID, Impressies, Uitgaven, Active View |
| 2 | **Bids in Auction** | Biedpijplijn op creative-niveau (biedingen -> overwinningen) | Creative ID, Biedingen, Biedingen in veiling, Gewonnen veilingen |
| 3 | **Pipeline -- Geo** | Volledige biedstroom-trechter per land | Biedverzoeken, Land, Ontvangen queries, Impressies |
| 4 | **Pipeline -- Publisher** | Volledige biedstroom-trechter per uitgever | Biedverzoeken, Uitgever-ID, Uitgeversnaam |
| 5 | **Bid Filtering** | Waarom Google uw biedingen weigert | Filteringsreden, Biedingen, Opportuniteitskosten |

---

## Volledig metrieken-overzicht

Elke metriek die Cat-Scan verwerkt, wat die betekent en welk rapport die bevat.

### Trechtermetrieken (biedstroom-pipeline)

Deze volgen de progressie van een biedverzoek door het veilingsysteem van Google.
Aanwezig in de rapporten **Pipeline -- Geo** en **Pipeline -- Publisher**.

| Metriek | Definitie | Eenheid | Rapport(en) |
|---------|-----------|---------|-------------|
| **Biedverzoeken** | Totaal aantal biedverzoeken dat Google naar uw biedmachine-eindpunt heeft gestuurd. Dit is het ruwe inkomende volume — de bovenkant van de trechter. Inclusief verzoeken waarop uw biedmachine mogelijk niet op tijd heeft gereageerd. | aantal | Pipeline -- Geo, Pipeline -- Publisher |
| **Ontvangen queries** | Biedverzoeken die uw biedmachine daadwerkelijk hebben bereikt en een respons hebben gekregen (succesvol of niet). Lager dan "Biedverzoeken" als uw biedmachine latentieproblemen of time-outs heeft. | aantal | Pipeline -- Geo, Pipeline -- Publisher |
| **Voorraadovereenkomsten** | Verzoeken waarbij uw biedmachine overeenkomende voorraad heeft gevonden (een creative die bij het verzoek past). Dit is het eerste filter: als u geen creative heeft voor de gevraagde grootte/formaat, stopt het hier. | aantal | Pipeline -- Geo, Pipeline -- Publisher |
| **Succesvolle responsen** | Verzoeken waarbij uw biedmachine een geldige, parseerbare biedrespons heeft geretourneerd (HTTP 200 met een goed gevormde bieding). Exclusief time-outs, fouten en geen-biedingen. | aantal | Pipeline -- Geo, Pipeline -- Publisher |
| **Biedingen** | Werkelijke biedresponsen die uw biedmachine heeft geplaatst. Een subset van succesvolle responsen — uw biedmachine kan succesvol reageren maar er toch voor kiezen niet te bieden (geen-bieding-respons). | aantal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Biedingen in veiling** | Biedingen die Google in de veiling heeft geaccepteerd. Biedingen kunnen worden geweigerd vóór toelating tot de veiling vanwege filteringregels (creative-afkeuring, beleidsschendingen, vloerprijs, pretargeting-uitsluitingen). Het verschil tussen "Biedingen" en "Biedingen in veiling" wordt weergegeven in het Bid Filtering-rapport. | aantal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Gewonnen veilingen** | Biedingen die de veiling hebben gewonnen. U betaalt hiervoor. Het verschil tussen "Biedingen in veiling" en "Gewonnen veilingen" is concurrentie — andere kopers hebben u overboden. | aantal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressies** | Advertenties die daadwerkelijk zijn weergegeven in de browser of app van een gebruiker na het winnen van de veiling. Iets minder dan "Gewonnen veilingen" door weergavefouten van advertenties, paginanavigaties vóór weergave en interferentie van advertentieblokkers. | aantal | Alle vijf rapporten |
| **Klikken** | Gebruikersinteracties (tikken/klikken) op uw weergegeven advertenties. | aantal | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Uitgaven- en kostenmetrieken

| Metriek | Definitie | Eenheid | Rapport(en) |
|---------|-----------|---------|-------------|
| **Uitgaven** | Totaal besteed geld aan gewonnen impressies voor de periode. Dit zijn uw werkelijke mediakosten. Uitgedrukt in de valuta van uw account (meestal USD). | valuta (micros in ruwe data, dollars in UI) | Quality |
| **Opportuniteitskosten** | Geschatte inkomsten die u heeft misgelopen doordat Google uw biedingen heeft gefilterd voordat ze de veiling ingingen. Berekend door Google op basis van historische winstpercentages en CPM's voor vergelijkbare voorraad. Nuttig om te prioriteren welke filteringsredenen u als eerste aanpakt. | valuta | Bid Filtering |

### Kwaliteits- en zichtbaarheidsmetrieken

Dit zijn metrieken op creative-niveau uit het **Quality**-rapport. Ze meten
wat er *na* de impressieweergave gebeurt.

| Metriek | Definitie | Eenheid | Rapport(en) |
|---------|-----------|---------|-------------|
| **Active View zichtbaar** | Impressies die voldeden aan de MRC-zichtbaarheidsnorm: ten minste 50% van de pixels van de advertentie was gedurende ten minste 1 aaneengesloten seconde (2 seconden voor video) in het zichtbare gebied van de browser. Dit is de industriestandaard voor "was deze advertentie daadwerkelijk gezien." | aantal | Quality |
| **Active View meetbaar** | Impressies waarbij zichtbaarheid *kon* worden gemeten. Sommige omgevingen (bepaalde apps, cross-domain iframes, oudere browsers) blokkeren meting. Zichtbaarheidspercentage = Active View zichtbaar / Active View meetbaar. | aantal | Quality |
| **Video-starts** | Aantal keren dat een video-creative begon af te spelen. Alleen ingevuld voor video-format creatives. | aantal | Quality |
| **Video-voltooiingen** | Aantal keren dat een video-creative tot 100% voltooiing is afgespeeld (of tot het overslaan-punt indien overslaan mogelijk is). Video-voltooiingspercentage = voltooiingen / starts. | aantal | Quality |

### Biedfilteringsmetrieken

Uit het **Bid Filtering**-rapport. Deze vertellen u *waarom* biedingen worden
geweigerd voordat ze de veiling ingaan.

| Metriek | Definitie | Eenheid | Rapport(en) |
|---------|-----------|---------|-------------|
| **Biedingen** | Totaal aantal biedingen dat uw biedmachine heeft geplaatst (zelfde definitie als hierboven). In dit rapport gebruikt als noemer voor het berekenen van filteringspercentages. | aantal | Bid Filtering |
| **Biedingen in veiling** | Biedingen die filtrering hebben overleefd en de veiling zijn ingegaan. `Biedingen - Biedingen in veiling` = totaal gefilterde biedingen. | aantal | Bid Filtering |
| **Opportuniteitskosten** | Zie uitgavenmetrieken hierboven. In dit rapport uitgesplitst per filteringsreden zodat u kunt zien welke reden u het meest kost. | valuta | Bid Filtering |

### Dimensies (groeperingskolommen)

Dimensies zijn geen metrieken — het zijn de assen waarlangs metrieken worden
uitgesplitst. Cat-Scan gebruikt deze om uw data te segmenteren.

| Dimensie | Wat het is | Welke rapporten |
|----------|-----------|-----------------|
| **Dag** | Kalenderdatum (UTC). Vereist in alle rapporten. Cat-Scan gebruikt dit voor deduplicatie en tijdreeksweergave. | Alle vijf |
| **Uur** | Uur van de dag (0--23, UTC). Maakt uurlijkse granulariteit mogelijk in pipelineanalyse. | Pipeline -- Geo, Pipeline -- Publisher |
| **Land** | Tweeletter ISO-landcode (bijv. US, DE, IL). De geografische oorsprong van het biedverzoek. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (optioneel) |
| **Billing ID (Pretargeting-configuratie)** | Numeriek ID van de pretargeting-configuratie die dit verkeer heeft geaccepteerd. Koppelt 1:1 aan een configuratiekaart in Cat-Scan. | Quality |
| **Creative-ID** | Het numerieke ID van Google voor het creative-bestand. Koppelt aan de Creatives-galerij in Cat-Scan. | Quality, Bids in Auction, Bid Filtering (optioneel) |
| **Creative-grootte** | Pixelafmetingen van de creative (bijv. `300x250`, `728x90`). Gebruikt voor analyse van verspilling per grootte. | Quality |
| **Creative-formaat** | Het advertentieformaat: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (optioneel) |
| **Platform** | Apparaatplatform: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (optioneel) |
| **Omgeving** | Waar de advertentie is weergegeven: `WEB`, `APP`. | Quality (optioneel) |
| **App-ID** | Mobiele app bundle-ID (bijv. `com.example.app`). Alleen ingevuld voor in-app-voorraad. | Quality (optioneel) |
| **App-naam** | Leesbare naam van de app. | Quality (optioneel) |
| **Uitgever-ID** | Numeriek ID van de uitgever (website of app). | Quality (optioneel), Pipeline -- Publisher |
| **Uitgeversnaam** | Leesbare naam van de uitgever. | Quality (optioneel), Pipeline -- Publisher |
| **Uitgeversdomein** | Het domein van de website van de uitgever (bijv. `news.example.com`). | Quality (optioneel) |
| **Koperaccount-ID** | Uw koperaccount / AB-plaatsen-ID. Nodig als u meerdere AB-plaatsen beheert. | Bids in Auction, Bid Filtering (optioneel) |
| **Filteringsreden** | De redencode van Google waarom een bieding is gefilterd vóór toelating tot de veiling (bijv. `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Stap voor stap: elk rapport aanmaken

### 1. Quality-rapport

Dit is uw prestatiesrapport op creative-niveau met zichtbaarheids- en uitgavendata.

**In Google Authorized Buyers -> Rapportage -> Nieuw rapport:**

| Instelling | Waarde |
|------------|--------|
| Rapporttype | RTB |
| Tijdperiode | Gisteren (dagelijks gepland) |
| Dimensies | Dag, Billing ID (Pretargeting-configuratie), Creative-ID, Creative-grootte, Land |
| Optionele dimensies | Uur, Creative-formaat, Platform, Omgeving, App-ID, App-naam, Uitgever-ID, Uitgeversnaam, Uitgeversdomein |
| Metrieken | Ontvangen queries, Impressies, Klikken, Uitgaven |
| Optionele metrieken | Video-starts, Video-voltooiingen, Active View zichtbaar, Active View meetbaar |

**Voorgestelde bestandsnaam:** `catscan-quality`

!!! note
    Dit rapport mag **niet** "Biedverzoeken", "Biedingen" of "Biedingen in
    veiling" bevatten — die kolommen zijn incompatibel met "Billing ID" in
    de rapportage van Google.

---

### 2. Bids in Auction-rapport

Dit rapport legt de biedpijplijn vast op creative-niveau en vult de
metrieken in die het Quality-rapport niet kan bevatten.

| Instelling | Waarde |
|------------|--------|
| Rapporttype | RTB |
| Tijdperiode | Gisteren (dagelijks gepland) |
| Dimensies | Dag, Land, Creative-ID, Koperaccount-ID |
| Metrieken | Biedingen in veiling, Gewonnen veilingen, Biedingen, Impressies |

**Voorgestelde bestandsnaam:** `catscan-bidsinauction`

!!! info "Hoe Cat-Scan deze samenvoegt"
    Quality + Bids in Auction worden samengevoegd op `(Dag, Creative-ID)` om
    het volledige beeld te geven: van geplaatste biedingen tot weergegeven
    impressies en gemaakte uitgaven.

---

### 3. Pipeline -- Geo-rapport

Dit is uw bovenkant-van-trechter-rapport: hoeveel biedverzoeken Google u per
land stuurt en hoeveel er elke fase van de trechter overleven.

| Instelling | Waarde |
|------------|--------|
| Rapporttype | RTB |
| Tijdperiode | Gisteren (dagelijks gepland) |
| Dimensies | Dag, Land, Uur |
| Metrieken | Biedverzoeken, Ontvangen queries, Voorraadovereenkomsten, Succesvolle responsen, Biedingen, Biedingen in veiling, Gewonnen veilingen, Impressies, Klikken |

**Voorgestelde bestandsnaam:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    Voeg **geen** Creative-ID, Billing ID of App-ID toe aan dit rapport. Deze
    kolommen zijn incompatibel met "Biedverzoeken".

---

### 4. Pipeline -- Publisher-rapport

Hetzelfde als Pipeline -- Geo, maar uitgesplitst per uitgever in plaats van (of
naast) geografie.

| Instelling | Waarde |
|------------|--------|
| Rapporttype | RTB |
| Tijdperiode | Gisteren (dagelijks gepland) |
| Dimensies | Dag, Land, Uur, Uitgever-ID, Uitgeversnaam |
| Metrieken | Biedverzoeken, Ontvangen queries, Voorraadovereenkomsten, Succesvolle responsen, Biedingen, Biedingen in veiling, Gewonnen veilingen, Impressies, Klikken |

**Voorgestelde bestandsnaam:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Bid Filtering-rapport

Dit rapport toont u *waarom* Google uw biedingen filtert voordat ze de veiling
ingaan — essentieel voor het diagnosticeren van pretargeting-problemen.

| Instelling | Waarde |
|------------|--------|
| Rapporttype | RTB |
| Tijdperiode | Gisteren (dagelijks gepland) |
| Dimensies | Dag, Filteringsreden |
| Optionele dimensies | Land, Koperaccount-ID, Creative-ID |
| Metrieken | Biedingen, Biedingen in veiling, Opportuniteitskosten |

**Voorgestelde bestandsnaam:** `catscan-bid-filtering`

### Veelvoorkomende filteringsredenen

Dit zijn de waarden die u ziet in de dimensie **Filteringsreden**. Elke
waarde geeft een specifieke reden waarom Google uw bieding heeft geweigerd vóór toelating tot de veiling.

| Filteringsreden | Wat het betekent | Wat te doen |
|----------------|-----------------|-------------|
| `CREATIVE_NOT_APPROVED` | De creative heeft de beoordeling van Google niet doorstaan, of is afgekeurd | Controleer de creative-status in Google AB. Los beleidsschendingen op. |
| `BID_BELOW_AUCTION_FLOOR` | Uw biedprijs lag onder de minimum-CPM van de uitgever | Verhoog de bieding of sluit laagwaardige voorraad uit via pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | Het beleid van Google op beursniveau heeft de bieding geblokkeerd | Bekijk het advertentiebeleid van Google voor de specifieke creative |
| `FILTERED_BY_PRETARGETING` | Uw eigen pretargeting-regels hebben dit verkeer uitgesloten | Opzettelijk als uw regels correct zijn; controleer als onverwacht |
| `NO_MATCHING_CREATIVE` | Het biedverzoek vroeg om een grootte/formaat dat u niet heeft | Upload creatives voor de ontbrekende groottes, of sluit die groottes uit in pretargeting |
| `CREATIVE_SIZE_MISMATCH` | Creative-afmetingen komen niet overeen met het advertentieslot | Controleer creative-grootte versus wat de uitgever vraagt |
| `LANDING_PAGE_DISAPPROVED` | De bestemmings-URL heeft de beoordeling van Google niet doorstaan | Herstel de landingspagina of gebruik een andere URL |
| `SSL_REQUIRED` | De uitgever vereist HTTPS maar uw creative of landingspagina gebruikt HTTP | Schakel alle assets en URL's over naar HTTPS |
| `FREQUENCY_CAPPED` | De gebruiker heeft deze creative al te vaak gezien | Verwacht gedrag; pas frequentiecaps aan als ze te agressief zijn |

---

## Levering plannen

Voor elk van de vijf rapporten:

1. Klik op **Plannen** in Google Authorized Buyers.
2. Stel de frequentie in op **Dagelijks**.
3. Stel de leveringsmethode in:
      - **E-mail** — stuur naar het Gmail-account dat is verbonden met Cat-Scan (maakt
        automatisch importeren mogelijk). Zie [Data-import](09-data-import.md) voor de
        Gmail-automatisch-importeren-instelling.
      - **Handmatig** — als u CSV's liever zelf downloadt en uploadt via
        `/import`.

!!! tip "Gebruik Gmail automatisch importeren"
    Het plannen van alle vijf rapporten om ze te e-mailen naar een verbonden Gmail-account betekent
    dat Cat-Scan ze elke dag automatisch importeert. Geen handmatige uploads meer nodig
    na de eerste installatie.

## Uw installatie verifiëren

Na het importeren van uw eerste set CSV's (handmatig of via Gmail):

1. Ga naar `/import` in Cat-Scan.
2. Controleer het **Datafreshness-raster** — u zou "imported" moeten zien voor alle vijf
   rapporttypen voor de datum van gisteren.
3. Als cellen "missing" tonen, is het bijbehorende rapport nog niet ontvangen.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Zodra alle vijf kolommen groen zijn voor gisteren, heeft Cat-Scan volledige data en
werken alle functies (trechter, verspillingsanalyse, aanbevelingen, optimizer).

## Automatische detectie

U hoeft Cat-Scan niet te vertellen welk rapport u uploadt. Het importsysteem
detecteert het rapporttype automatisch aan de hand van de kolomkoppen:

- Heeft **Bid filtering reason**? -> Bid Filtering
- Heeft **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- Heeft **Bid requests** (geen Publisher ID)? -> Pipeline -- Geo
- Heeft **Creative ID** + **Billing ID**? -> Quality
- Heeft **Creative ID** + **Bids in auction**? -> Bids in Auction

## Hoe Cat-Scan elke metriek gebruikt

Dit koppelt ruwe CSV-metrieken aan wat u ziet in de Cat-Scan UI.

| UI-functie | Gebruikte metrieken | Bronrapport(en) |
|-----------|---------------------|-----------------|
| **QPS-trechter** (startpagina) | Biedverzoeken, Ontvangen queries, Biedingen, Biedingen in veiling, Gewonnen veilingen, Impressies, Klikken, Uitgaven | Pipeline (beide) + Quality |
| **Verspillingspercentage berekening** | `(Biedverzoeken - Biedingen) / Biedverzoeken` | Pipeline |
| **Winstpercentage** | `Gewonnen veilingen / Biedingen` | Pipeline + Bids in Auction |
| **CTR** | `Klikken / Impressies` | Elk rapport met beide |
| **CPM** | `(Uitgaven / Impressies) * 1000` | Quality |
| **Zichtbaarheidspercentage** | `Active View zichtbaar / Active View meetbaar` | Quality |
| **Video-voltooiingspercentage** | `Video-voltooiingen / Video-starts` | Quality |
| **Geo-verspillingsanalyse** (`/qps/geo`) | Biedverzoeken, Impressies, Uitgaven per Land | Pipeline -- Geo + Quality |
| **Uitgeververspilling** (`/qps/publisher`) | Biedverzoeken, Impressies, Uitgaven per Uitgever | Pipeline -- Publisher + Quality |
| **Grootteverspilling** (`/qps/size`) | Impressies, Uitgaven per Creative-grootte | Quality |
| **Filteringsredenen** (`/qps/filtering`) | Biedingen, Biedingen in veiling, Opportuniteitskosten per Filteringsreden | Bid Filtering |
| **Configuratiekaartmetrieken** | Ontvangen queries, Impressies, Uitgaven per Billing ID | Quality |
| **Creative-prestaties** | Impressies, Klikken, Uitgaven, Active View zichtbaar per Creative-ID | Quality |
| **Optimizer-scoring** | Alle pipeline- + quality-metrieken, geaggregeerd per segment | Alle vijf |

## Veelgemaakte fouten

| Fout | Wat er gebeurt | Oplossing |
|------|---------------|-----------|
| "Biedverzoeken" toevoegen aan het Quality-rapport | Google geeft fouten of retourneert onvolledige data | Verwijder "Biedverzoeken" — het is incompatibel met "Billing ID" |
| Het Bid Filtering-rapport vergeten | Cat-Scan kan niet tonen *waarom* biedingen worden geweigerd | Maak het 5e rapport aan met de dimensie "Filteringsreden" |
| "Afgelopen 7 dagen" gebruiken in plaats van "Gisteren" | Overlappende data, grotere bestanden, langzamere imports | Stel in op "Gisteren" en plan dagelijks |
| Niet plannen — alleen handmatige exports | Data wordt verouderd, gezondheidscontroles mislukken | Plan dagelijkse levering via e-mail |
| Dimensie "Uur" mist in Pipeline-rapporten | Geen uurlijkse granulariteit in QPS-analyse | Voeg Uur toe aan Pipeline -- Geo en Pipeline -- Publisher |
| Optionele metrieken missen in Quality-rapport | Geen zichtbaarheids- of videodata in Cat-Scan | Voeg Active View zichtbaar, Active View meetbaar, Video-starts, Video-voltooiingen toe |

## Volgende stappen

- [Admin-navigatie](02-navigating-the-dashboard.md): zijbalkindeling en
  installatiechecklist
- [Data-import](09-data-import.md): gedetailleerde importmechanismen, gesegmenteerde
  uploads en probleemoplossing
- [QPS-trechter](03-qps-funnel.md): zodra data stroomt, beginnen met analyseren
