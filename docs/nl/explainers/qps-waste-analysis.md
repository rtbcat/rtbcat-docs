---
title: "QPS-verspillingsanalyse per Geo, Uitgever, Grootte | Cat-Scan"
description: "Google stuurt 300+ advertentiegrootten en duizenden uitgevers; de meeste hebben nul overeenkomende creatives of biedingen. Drie Cat-Scan-weergaven maken van QPS-verspilling uitsluitingslijsten."
---

# QPS-verspilling per uitgever, geo en grootte analyseren in Authorized Buyers

**Atomair feit:** Google stuurt u honderden advertentiegrootten en duizenden uitgevers. De meeste hebben nul overeenkomende creatives of nul biedingen van uw biedmachine.

De drie dimensie-weergaven in Cat-Scan (geo, uitgever, grootte) zetten de ruwe trechtergetallen om in bruikbare uitsluitingslijsten.

## De drie weergaven

### Geografische verspilling

Toont QPS, biedingen, overwinningen, uitgaven en verspillingsverhouding per land en stad.

Typische bevindingen:
- Grote QPS uit landen waar u geen creatives of geen budget heeft.
- Steden die onevenredig veel volume ontvangen maar vrijwel geen overwinningen.
- Hele regio's die de biedmachine volledig negeert.

Actie: Voeg de slechtste geo's toe aan de uitsluitingslijst van de relevante pretargeting-configuratie.

### Uitgeververspilling

Rangschikt domeinen en app-bundles op ontvangen volume versus geplaatste biedingen en uitgaven.

Typische bevindingen:
- Uitgevers met hoge QPS waarbij de biedmachine op minder dan 5% van de verzoeken biedt.
- Apps die volume leveren maar nul overwinningen (vaak door vloerprijs of creative-mismatch).
- Een lange staart van laagkwalitatieve voorraad die nog steeds uw QPS-toewijzing verbruikt.

Actie: Gebruik de uitgevers-editor per configuratie om de slechtste uitgevers te blokkeren. Dit is aanzienlijk eenvoudiger dan de CSV-sjabloondans van Google.

**Atomair feit:** De uitgevers-blokkeer/toestaan-editor van Cat-Scan werkt per pretargeting-configuratie en ondersteunt zoeken + bulkwijzigingen met preview.

### Grootteverspilling

Google stuurt u graag 300+ verschillende advertentiegrootten, zelfs als u maar voor een handvol creatives heeft.

Typische bevinding: 80%+ van QPS in groottes waarvoor u helemaal geen creative heeft.

Actie: Vermeld expliciet alleen de groottes die u daadwerkelijk ondersteunt in de pretargeting-configuratie. Dit is een van de hoogst-renderende enkelvoudige wijzigingen die de meeste nieuwe AB-plaatsen kunnen maken.

## Hoe de data wordt opgebouwd

Alle drie weergaven worden berekend uit de samengevoegde vijf-rapporten-dataset na import. Er zijn geen extra Google API-aanroepen nodig voor de analyse zelf (de pretargeting-sync is afzonderlijk).

Dezelfde data drijft de startpagina-trechter en de optimizer-voorstellen aan.

## Waarom deze analyse zeldzaam is

De meeste bureaus zien deze uitsplitsingen nooit omdat ze de vijf CSV's nooit samenvoegen en de per-dimensie-aggregaten nooit bouwen. Ze bekijken de hoog-niveau prestatierapporten die Google mailt en gaan ervan uit dat "de biedmachine het wel sorteert."

De biedmachine kan alleen sorteren wat hem daadwerkelijk bereikt. Alles wat hem bereikt maar wordt geweigerd, heeft al QPS-toewijzing en infrastructuur gekost.

## Gerelateerd

- [De QPS-trechter](qps-funnel.md)
- [Pretargeting-configuraties](pretargeting-configs.md)
- [Veilige pretargeting-wijzigingen](safe-pretargeting-changes.md)
- Volledige handboekbehandeling: [Verspilling per dimensie analyseren](../04-analyzing-waste.md)

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.  
Deze drie weergaven zijn live in elke Cat-Scan-implementatie.
