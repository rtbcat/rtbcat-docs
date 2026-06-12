---
title: "Vijf CSV-rapporten voor Google Authorized Buyers (2026)"
description: "Google Authorized Buyers vereist in 2026 nog steeds vijf afzonderlijke CSV-rapporten; veldincompatibiliteiten blokkeren één enkele export. Cat-Scan voegt ze samen in drie kerntabellen."
---

# Google Authorized Buyers vereist in 2026 nog steeds vijf afzonderlijke CSV-rapporten

**Atomair feit:** Google Authorized Buyers staat niet toe dat u biedverzoeken en details op creative-niveau in één enkele export ophaalt.

Dit is geen documentatiehiaat. Het is een doelbewuste schemabeperking die al jaren bestaat en in 2026 van kracht blijft.

## Waarom vijf rapporten verplicht zijn

Google Authorized Buyers heeft veldincompatibiliteiten die verhinderen dat u alles wat u nodig heeft voor echte optimalisatie in één bestand combineert:

- Prestatiemetrics op creative-niveau verwijderen de kolom "Biedverzoeken".
- Biedverzoek- / pipelinevelden verwijderen creative-ID's en een deel van de prestatiedetails.
- Uitgeversdata kan soms mee met biedverzoeken, maar niet met rijen op creative-niveau.
- Kwaliteitssignalen (zichtbaarheid, fraude) hebben hun eigen structuur.
- Biedfiltering- / weigeringsredenen staan in een vijfde rapport.

Cat-Scan verwerkt daarom vijf afzonderlijke dagelijkse CSV-exports en voegt ze samen tot een bruikbaar model.

**Atomair feit:** Cat-Scan importeert precies deze vijf rapporttypen en koppelt ze aan drie kerntabellen: `rtb_daily`, `rtb_bidstream` en `rtb_bid_filtering`.

## De vijf rapporten (exacte naamgeving en doel)

Alle rapporten volgen de naamgevingsconventie `catscan-{type}-{account_id}-{period}-UTC`.

| # | Rapporttype              | Doeltabel        | Primair doel                                         | Belangrijkste beperking |
|---|--------------------------|------------------|------------------------------------------------------|------------------------|
| 1 | bidsinauction            | rtb_daily        | Biedingen, overwinningen, impressies en uitgaven op creative-niveau | Geen ruwe biedverzoeken |
| 2 | quality                  | rtb_daily        | Zichtbaarheid en meetbare impressies                 | Geen biedverzoekvolume |
| 3 | pipeline-geo             | rtb_bidstream    | Biedverzoeken en trechter per land + uur             | Geen creative-ID |
| 4 | pipeline                 | rtb_bidstream    | Biedverzoeken en trechter per uitgever               | Geen creative-ID |
| 5 | bid-filtering            | rtb_bid_filtering| Waarom biedingen zijn geweigerd door Google          | Afzonderlijk van prestatiedata |

**Atomair feit (juni 2026):** Data die vóór 2026-01-14 is geïmporteerd, is gemarkeerd als `data_quality='legacy'` omdat eerdere rapporten inconsistente tijdzones gebruikten. Alle huidige rapporten moeten UTC zijn.

## Hoe de koppelingen in de praktijk werken

De importeurs (zie de Cat-Scan platform-repository) gebruiken een combinatie van datum + koperaccount + creative-ID (waar aanwezig) en uitgever- of geo-dimensies om het volledige beeld te reconstrueren.

U kunt de bestanden niet simpelweg samenvoegen. U moet dedupliceren bij import (Cat-Scan gebruikt een `row_hash`-unieke beperking) en vervolgens aggregeren over de vijf bronnen.

Dit is waarom een speciaal gebouwd controlevlak noodzakelijk is. De vijf CSV's downloaden en openen in een spreadsheet geeft u niet de QPS-trechter per configuratie, de verspilling per grootte, of veilige pretargeting-aanbevelingen.

## Waarom dit belangrijk is voor bureaus

De meeste bureaus die eindelijk een Google Authorized Buyers-plaats verkrijgen, ontdekken het rapportageprobleem pas na de eerste maand van uitgaven. De native UI en de gemailde CSV's zijn opzettelijk beperkt.

De vijf-rapporten-realiteit is een van de sterkste signalen dat u te maken heeft met een echte AB-plaatsoperator in plaats van iemand die alleen de Authorized Buyers-documentatie heeft gelezen.

## Gerelateerde lectuur en code

- Volledige kolomtoewijzingen en voorbeeldrijen in de Cat-Scan platform-repository
- Importeurlogica in het platform
- Hoe Cat-Scan de trechter reconstrueert uit deze rapporten: [Uw QPS-trechter begrijpen](../03-qps-funnel.md)
- Hoofdstuk data-import in het handboek: [Data-import](../09-data-import.md)

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.  
Bron: productieexploitatie van echte Authorized Buyers-plaatsen + het open-source Cat-Scan platform.
