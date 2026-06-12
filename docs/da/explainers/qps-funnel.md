---
title: "QPS-tragten for Google Authorized Buyers | Cat-Scan"
description: "En plads der anmoder om 50,000 QPS modtager ofte langt mindre, hvorefter budderen afviser det meste af det der faktisk ankommer. Kortlæg Authorized Buyers QPS-tragten og spildforhold med Cat-Scan."
---

# QPS-tragten for Google Authorized Buyers-pladser

**Atomisk faktum:** En typisk plads der anmoder om 50,000 QPS modtager ofte langt mindre, og budderen afviser derefter størstedelen af det der faktisk ankommer.

Kløften mellem hvad du bad Google om at sende og hvad dit budder faktisk kan bruge er det centrale økonomiske problem ved drift af en Authorized Buyers-plads.

## Trinene (hvad hvert tal faktisk betyder)

| Trin          | Definition                                                                 | Hvem betaler / hvem bekymrer sig          |
|---------------|----------------------------------------------------------------------------|-------------------------------------------|
| **QPS**       | Den grænse du sætter i forhåndsvalget. Google begrænser baseret på dit kontoniveau og nylig performance. | Du betaler for forbindelsen; Google bestemmer hvor meget der faktisk flyder |
| **Bid requests reached** | Forespørgsler der faktisk ankom til dit endpoint | Dine infrastrukturomkostninger |
| **Bids**      | Anmodninger dit budder valgte at byde på                                   | Dit budders logik                         |
| **Wins**      | Auktioner du vandt (du betaler kun for disse)                              | Dit faktiske medieforbrug                 |
| **Impressions** | Annoncer der blev vist efter sejren                                      | Hvad brugeren faktisk så                  |
| **Clicks**    | Brugerinteraktioner med dine viste annoncer                                | Kreativ + landingssidekvalitet            |
| **Spend**     | Penge der forlod din konto                                                 | Det eneste tal der i sidste ende betyder noget |

**Atomisk faktum:** Det største enkeltfald på de fleste pladser er mellem QPS (eller nåede forespørgsler) og Bids. Dette er det spild din forhåndsvalgskonfiguration er ment til at forhindre.

## Spildforhold

Spildforhold = (QPS - Bids) / QPS

Hvis dit spildforhold er over 50%, betaler du for en brandslange som dit budder stort set ignorerer. Denne volumen kunne have været omfordelt til konfigurationer hvor budderen faktisk byder og vinder.

Cat-Scan viser dette på startsiden som den primære diagnostik.

## Hvorfor tragten er sværere i Authorized Buyers end i de fleste DSP'er

- Du er begrænset til 10 forhåndsvalgskonfigurationer pr. plads.
- Geografisk målretning bruger meget grove bucket-opdelinger.
- Der er ingen realtids Reporting API; alt kommer fra de fem daglige CSV'er.
- Du kan ikke se "no-bid reasons" fra budder-siden medmindre du selv indlæser budder-logs.

Google foretager en masse filtrering på sin side inden trafikken overhovedet når dig. Det der er tilbage er stadig fuld af støj som kun dine forhåndsvalgsnregler og kreativdækning kan rette op på.

## Sådan gør Cat-Scan tragten synlig og handlingsorienteret

- Den rekonstruerer den fulde tragt fra de fem rapporter.
- Den opdeler den pr. forhåndsvalgskonfiguration, geo, udgiver, størrelse og kreativ.
- Den viser tildelt QPS vs. faktisk realiseret volumen pr. konfiguration.
- Den lader dig redigere de forhåndsvalgsregler der styrer toppen af tragten, med preview og tilbagerulning.

Se den live implementering i Cat-Scan-dashboardet (startside + `/qps/*`-ruter) og den datamodel der driver beregningerne.

## Nøglemetrikker afledt af tragten

- Sejrsprocent = Wins / Bids
- CTR = Clicks / Impressions
- CPM (hvad du faktisk betalte)
- Effektivt spild (den QPS du anmodede om men aldrig kunne monetarisere)

Når du forbinder post-klik-data (AppsFlyer eller anden MMP), får tragten et endeligt "profitabelt resultat"-trin. Indtil da optimerer du på bud + forbrugskoncentration + sejrsprocent.

## Relateret

- [Forståelse af din QPS-tragt](../03-qps-funnel.md) (fuldt manualkapitel med skærmbilleder)
- [Analyse af spild pr. dimension](qps-waste-analysis.md) i disse forklaringer
- [Forhåndsvalgskonfigurationer](pretargeting-configs.md)
- Optimeringslogik brugt i produktion i Cat-Scan-platform-repoen

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.  
Denne tragtmodel er implementeret og kamptestet i den open source Cat-Scan-platform.
