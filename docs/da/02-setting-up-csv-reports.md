---
title: "Authorized Buyers CSV-rapporter: 5 rapporter Cat-Scan har brug for"
description: "Google Authorized Buyers har ingen Reporting API, så Cat-Scan genopbygger tragten fra fem planlagte CSV-rapporter. Komplet reference for metrikker og dimensioner samt opsætningsvejledning."
---

# Opsætning af dine CSV-rapporter

*Målgruppe: mediekøbere, account managers*

Før Cat-Scan kan analysere noget som helst, har den brug for data. Google Authorized Buyers
har ingen Reporting API, så alle data strømmer igennem **fem planlagte CSV-rapporter**,
som du opretter én gang i din Google AB-konto.

!!! warning "Hvorfor fem separate rapporter?"
    Googles rapporteringskolonner er ikke alle kompatible med hinanden. For
    eksempel kan "Bid requests" ikke optræde i samme rapport som "Mobile app ID"
    eller "Creative ID + Billing ID". For at opnå fuld tragtsigt skal du bruge fem
    rapporter, som Cat-Scan samler automatisk.

## De fem rapporter på et øjeblik

| # | Rapportnavn | Hvad den fortæller Cat-Scan | Nøglekolonner |
|---|-------------|---------------------------|---------------|
| 1 | **Quality** | Performance på kreativniveau med synlighed | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Budpipeline på kreativniveau (bud -> sejre) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Fuld bidstream-tragt pr. land | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Fuld bidstream-tragt pr. udgiver | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Hvorfor Google afviser dine bud | Filtering reason, Bids, Opportunity cost |

---

## Komplet metrikreference

Alle metrikker som Cat-Scan indlæser, hvad de betyder, og hvilken rapport der indeholder dem.

### Tragtmetrikker (bidstream-pipeline)

Disse sporer forløbet for en budanmodning igennem Googles auktionssystem.
Findes i rapporterne **Pipeline -- Geo** og **Pipeline -- Publisher**.

| Metrik | Definition | Enhed | Rapport(er) |
|--------|-----------|-------|-------------|
| **Bid requests** | Samlede budanmodninger Google sendte til dit budder-endpoint. Dette er det rå indgående volumen -- toppen af tragten. Inkluderer anmodninger dit budder muligvis ikke nåede at svare på til tiden. | antal | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Budanmodninger der faktisk nåede dit budder og fik et svar (succesfuldt eller ej). Lavere end "Bid requests" hvis dit budder har latency-problemer eller timeouts. | antal | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Anmodninger hvor dit budder fandt matchende inventar (et kreativ der passer til anmodningen). Dette er det første filter: hvis du ikke har et kreativ til den ønskede størrelse/format, stopper det her. | antal | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Anmodninger hvor dit budder returnerede et gyldigt, parserbart budsvar (HTTP 200 med et korrekt formateret bud). Ekskluderer timeouts, fejl og no-bids. | antal | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Faktiske budsvar dit budder afgav. Et delmængde af succesfulde svar -- dit budder kan svare succesfuldt men vælge ikke at byde (no-bid-svar). | antal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Bud som Google godtog ind i auktionen. Bud kan afvises før auktionsdeltagelse på grund af filtreringsregler (kreativafvisning, politikovertrædelser, bundpris, forhåndsvalgsudelukkelser). Forskellen mellem "Bids" og "Bids in auction" vises i Bid Filtering-rapporten. | antal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Bud der vandt auktionen. Du betaler for disse. Forskellen mellem "Bids in auction" og "Auctions won" er konkurrence -- andre købere oversteg dit bud. | antal | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Annoncer der faktisk blev vist i en brugers browser eller app efter at have vundet auktionen. Lidt færre end "Auctions won" på grund af fejl i annoncerenderingen, sidenavigation inden rendering og annonceblokerende interferens. | antal | Alle fem rapporter |
| **Clicks** | Brugerinteraktioner (tryk/klik) på dine viste annoncer. | antal | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Forbrugs- og omkostningsmetrikker

| Metrik | Definition | Enhed | Rapport(er) |
|--------|-----------|-------|-------------|
| **Spend** | Samlet pengebrug på vundne visninger i perioden. Dette er dine faktiske medieomkostninger. Denomineret i din kontos valuta (normalt USD). | valuta (mikros i rådata, dollars i UI) | Quality |
| **Opportunity cost** | Estimeret omsætning du tabte fordi Google filtrede dine bud fra inden de kom ind i auktionen. Beregnet af Google baseret på historiske sejrsprocenter og CPM'er for lignende inventar. Nyttigt til at prioritere hvilke filtreringsårsager der skal rettes først. | valuta | Bid Filtering |

### Kvalitets- og synlighedsmetrikker

Disse er metrikker på kreativniveau fra **Quality**-rapporten. De måler
hvad der sker *efter* at visningen er leveret.

| Metrik | Definition | Enhed | Rapport(er) |
|--------|-----------|-------|-------------|
| **Active View viewable** | Visninger der opfyldte MRC-synlighedsstandarden: mindst 50% af annoncens pixels var i det synlige område af browseren i mindst 1 sammenhængende sekund (2 sekunder for video). Dette er branchens standard for "var denne annonce faktisk set." | antal | Quality |
| **Active View measurable** | Visninger hvor synlighed *kunne* måles. Nogle miljøer (visse apps, cross-domain iframes, ældre browsere) blokerer måling. Synlighedsrate = Active View viewable / Active View measurable. | antal | Quality |
| **Video starts** | Antal gange et videokreativ begyndte at afspille. Kun udfyldt for kreative i videoformat. | antal | Quality |
| **Video completions** | Antal gange et videokreativ afspillede til 100% afslutning (eller til skipppunktet hvis det kan springes over). Videoafslutningsrate = afslutninger / starter. | antal | Quality |

### Budfliltringsmetrikker

Fra **Bid Filtering**-rapporten. Disse fortæller dig *hvorfor* bud afvises
inden de kommer ind i auktionen.

| Metrik | Definition | Enhed | Rapport(er) |
|--------|-----------|-------|-------------|
| **Bids** | Samlede bud dit budder afgav (samme definition som ovenfor). I denne rapport brugt som nævner til beregning af filtreringsrater. | antal | Bid Filtering |
| **Bids in auction** | Bud der overlevede filtrering og kom ind i auktionen. `Bids - Bids in auction` = samlede filtrerede bud. | antal | Bid Filtering |
| **Opportunity cost** | Se forbrugsmetrikker ovenfor. I denne rapport opdelt pr. filtreringsårsag så du kan se hvilken årsag der koster dig mest. | valuta | Bid Filtering |

### Dimensioner (grupperingskolonner)

Dimensioner er ikke metrikker -- de er akserne langs hvilke metrikker opdeles.
Cat-Scan bruger disse til at skære dine data.

| Dimension | Hvad det er | Hvilke rapporter |
|-----------|-----------|-----------------|
| **Day** | Kalenderdato (UTC). Påkrævet i alle rapporter. Cat-Scan bruger dette til deduplication og tidsserievisning. | Alle fem |
| **Hour** | Time på dagen (0--23, UTC). Muliggør timegranularitet i pipeline-analyse. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Tocifret ISO-landekode (f.eks. US, DE, IL). Budanmodningens geografiske oprindelse. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (valgfrit) |
| **Billing ID (Pretargeting config)** | Numerisk ID for den forhåndsvalgskonfiguration der accepterede denne trafik. Mapper 1:1 til et konfigurationskort i Cat-Scan. | Quality |
| **Creative ID** | Googles numeriske ID for kreativaktiven. Links til Kreativgalleriet i Cat-Scan. | Quality, Bids in Auction, Bid Filtering (valgfrit) |
| **Creative size** | Pixeldimensioner for kreativet (f.eks. `300x250`, `728x90`). Bruges til størrelsesbaseret spildanalyse. | Quality |
| **Creative format** | Annonceformatet: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (valgfrit) |
| **Platform** | Enhedsplatform: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (valgfrit) |
| **Environment** | Hvor annoncen blev vist: `WEB`, `APP`. | Quality (valgfrit) |
| **App ID** | Mobil-app-bundle-ID (f.eks. `com.example.app`). Kun udfyldt for in-app-inventar. | Quality (valgfrit) |
| **App name** | Menneskelæsbart appnavn. | Quality (valgfrit) |
| **Publisher ID** | Numerisk ID for udgiveren (websted eller app). | Quality (valgfrit), Pipeline -- Publisher |
| **Publisher name** | Menneskelæseligt udgivernavn. | Quality (valgfrit), Pipeline -- Publisher |
| **Publisher domain** | Domænet for udgiverens websted (f.eks. `news.example.com`). | Quality (valgfrit) |
| **Buyer account ID** | Dit køber-konto / seat-ID. Nødvendigt når du kører flere pladser. | Bids in Auction, Bid Filtering (valgfrit) |
| **Filtering reason** | Googles årsagskode for hvorfor et bud blev filtreret fra inden det kom ind i auktionen (f.eks. `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Trin-for-trin: oprettelse af hver rapport

### 1. Quality-rapport

Dette er din performance-rapport på kreativniveau med synligheds- og forbrugsdata.

**I Google Authorized Buyers -> Reporting -> New Report:**

| Indstilling | Værdi |
|-------------|-------|
| Report type | RTB |
| Time range | Yesterday (planlagt dagligt) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Foreslået filnavn:** `catscan-quality`

!!! note
    Denne rapport må **ikke** inkludere "Bid requests", "Bids" eller "Bids in
    auction" -- disse kolonner er inkompatible med "Billing ID" i Googles
    rapportering.

---

### 2. Bids in Auction-rapport

Denne rapport fanger budpipelinen på kreativniveau og udfylder de
metrikker som Quality-rapporten ikke kan inkludere.

| Indstilling | Værdi |
|-------------|-------|
| Report type | RTB |
| Time range | Yesterday (planlagt dagligt) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Foreslået filnavn:** `catscan-bidsinauction`

!!! info "Sådan samler Cat-Scan disse"
    Quality + Bids in Auction samles på `(Day, Creative ID)` for at give dig
    det fulde billede: fra afgivne bud til leverede visninger og pådraget forbrug.

---

### 3. Pipeline -- Geo-rapport

Dette er din topp-af-tragt-rapport: hvor mange budanmodninger Google sender dig
pr. land, og hvor mange der overlever hvert trin i tragten.

| Indstilling | Værdi |
|-------------|-------|
| Report type | RTB |
| Time range | Yesterday (planlagt dagligt) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Foreslået filnavn:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    Tilføj **ikke** Creative ID, Billing ID eller App ID til denne rapport. Disse
    kolonner er inkompatible med "Bid requests".

---

### 4. Pipeline -- Publisher-rapport

Samme som Pipeline -- Geo, men opdelt pr. udgiver i stedet for (eller ud over)
geografi.

| Indstilling | Værdi |
|-------------|-------|
| Report type | RTB |
| Time range | Yesterday (planlagt dagligt) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Foreslået filnavn:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Bid Filtering-rapport

Denne rapport viser dig *hvorfor* Google filtrerer dine bud fra inden de
kommer ind i auktionen -- afgørende for diagnosticering af forhåndsvalgsproblemer.

| Indstilling | Værdi |
|-------------|-------|
| Report type | RTB |
| Time range | Yesterday (planlagt dagligt) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Foreslået filnavn:** `catscan-bid-filtering`

### Almindelige filtreringsårsager

Dette er de værdier du vil se i dimensionen **Filtering reason**. Hver
af dem fortæller dig en specifik årsag til at Google afviste dit bud inden auktionsdeltagelse.

| Filtreringsårsag | Hvad det betyder | Hvad du skal gøre |
|-----------------|-----------------|-------------------|
| `CREATIVE_NOT_APPROVED` | Kreativet har ikke bestået Googles gennemgang, eller blev afvist | Tjek kreativstatus i Google AB. Ret politikovertrædelser. |
| `BID_BELOW_AUCTION_FLOOR` | Din budpris var under udgiverens minimums-CPM | Hæv buddet eller ekskluder lavt-værdis inventar via forhåndsvalg |
| `DISAPPROVED_BY_EXCHANGE` | Googles exchange-niveau-politik blokerede buddet | Gennemgå Googles annoncepolitikker for det specifikke kreativ |
| `FILTERED_BY_PRETARGETING` | Dine egne forhåndsvalgsnregler udelukkede denne trafik | Intentionel hvis dine regler er korrekte; gennemgå hvis uventet |
| `NO_MATCHING_CREATIVE` | Budanmodningen bad om en størrelse/format du ikke har | Upload kreative til de manglende størrelser, eller ekskluder disse størrelser i forhåndsvalg |
| `CREATIVE_SIZE_MISMATCH` | Kreativdimensioner matcher ikke annoncepladsen | Tjek kreativstørrelse vs hvad udgiveren anmoder om |
| `LANDING_PAGE_DISAPPROVED` | Destinations-URL'en bestod ikke Googles gennemgang | Ret landingssiden eller brug en anden URL |
| `SSL_REQUIRED` | Udgiver kræver HTTPS men dit kreativ eller din landingsside bruger HTTP | Skift alle aktiver og URL'er til HTTPS |
| `FREQUENCY_CAPPED` | Brugeren har allerede set dette kreativ for mange gange | Forventet adfærd; juster frekvensbegrænsninger hvis for aggressive |

---

## Planlægning af levering

For hver af de fem rapporter:

1. Klik på **Schedule** i Google Authorized Buyers.
2. Sæt frekvens til **Daily**.
3. Indstil leveringsmetode:
      - **Email** -- send til Gmail-kontoen forbundet til Cat-Scan (muliggør
        auto-import). Se [Dataimport](09-data-import.md) for opsætning af Gmail
        auto-import.
      - **Manual** -- hvis du foretrækker at downloade og uploade CSV'er selv via
        `/import`.

!!! tip "Brug Gmail auto-import"
    At planlægge alle fem rapporter til at emaile en tilkoblet Gmail-konto betyder at
    Cat-Scan importerer dem automatisk hver dag. Ingen manuelle uploads nødvendige
    efter den indledende opsætning.

## Verificering af din opsætning

Efter import af dit første sæt CSV'er (manuelt eller via Gmail):

1. Gå til `/import` i Cat-Scan.
2. Tjek **Data Freshness Grid** -- du bør se "imported" for alle fem
   rapporttyper for gårsdagens dato.
3. Hvis nogen celler viser "missing", er den tilsvarende rapport endnu ikke modtaget.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Når alle fem kolonner viser grønt for i går, har Cat-Scan fulde data og
alle funktioner (tragt, spildanalyse, anbefalinger, optimizer) vil fungere.

## Automatisk detektion

Du behøver ikke at fortælle Cat-Scan hvilken rapport du uploader. Importsystemet
registrerer automatisk rapporttypen ud fra kolonneoverskrifterne:

- Har **Bid filtering reason**? -> Bid Filtering
- Har **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- Har **Bid requests** (ingen Publisher ID)? -> Pipeline -- Geo
- Har **Creative ID** + **Billing ID**? -> Quality
- Har **Creative ID** + **Bids in auction**? -> Bids in Auction

## Sådan bruger Cat-Scan hver metrik

Dette mapper rå CSV-metrikker til hvad du ser i Cat-Scan-brugergrænsefladen.

| UI-funktion | Anvendte metrikker | Kilderapport(er) |
|------------|-------------------|-----------------|
| **QPS-tragt** (startside) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (begge) + Quality |
| **Spild%-beregning** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Sejrsprocent** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Enhver rapport med begge |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Synlighedsrate** | `Active View viewable / Active View measurable` | Quality |
| **Videoafslutningsrate** | `Video completions / Video starts` | Quality |
| **Geo-spildanalyse** (`/qps/geo`) | Bid requests, Impressions, Spend pr. Country | Pipeline -- Geo + Quality |
| **Udgiver-spild** (`/qps/publisher`) | Bid requests, Impressions, Spend pr. Publisher | Pipeline -- Publisher + Quality |
| **Størrelsesspild** (`/qps/size`) | Impressions, Spend pr. Creative size | Quality |
| **Filtreringsårsager** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost pr. Filtering reason | Bid Filtering |
| **Konfigurationskortmetrikker** | Reached queries, Impressions, Spend pr. Billing ID | Quality |
| **Kreativperformance** | Impressions, Clicks, Spend, Active View viewable pr. Creative ID | Quality |
| **Optimizer-scoring** | Alle pipeline + quality-metrikker, aggregeret pr. segment | Alle fem |

## Almindelige fejl

| Fejl | Hvad der sker | Løsning |
|------|--------------|---------|
| Tilføjelse af "Bid requests" til Quality-rapporten | Google fejler eller returnerer ufuldstændige data | Fjern "Bid requests" -- det er inkompatibelt med "Billing ID" |
| Glemmer Bid Filtering-rapporten | Cat-Scan kan ikke vise dig *hvorfor* bud afvises | Opret den 5. rapport med "Filtering reason"-dimensionen |
| Brug af "Last 7 days" i stedet for "Yesterday" | Overlappende data, større filer, langsommere imports | Sæt til "Yesterday" og planlæg dagligt |
| Ingen planlægning -- kun manuelle eksporter | Data forældes, sundhedstjek fejler | Planlæg daglig levering via email |
| Manglende "Hour"-dimension på Pipeline-rapporter | Ingen timegranularitet i QPS-analyse | Tilføj Hour til Pipeline -- Geo og Pipeline -- Publisher |
| Manglende valgfrie metrikker på Quality-rapport | Ingen synligheds- eller videodata i Cat-Scan | Tilføj Active View viewable, Active View measurable, Video starts, Video completions |

## Næste trin

- [Admin-navigation](02-navigating-the-dashboard.md): sidepanel-layout og
  opsætningscheckliste
- [Dataimport](09-data-import.md): detaljeret importmekanik, chunked
  uploads og fejlfinding
- [QPS-tragt](03-qps-funnel.md): når data flyder, begynd at analysere
