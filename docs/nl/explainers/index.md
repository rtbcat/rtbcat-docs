---
title: "Google Authorized Buyers Technische Toelichtingen | Cat-Scan RTB"
description: "Eerste-hands technische notities over Google Authorized Buyers: 10 pretargeting-configuraties, de QPS-trechter, vijf CSV-rapporten en verspilling. Zie het open-source Cat-Scan platform."
---

# Technische toelichtingen

**Technische notities over Google Authorized Buyers-operaties, QPS-beheer en het runnen van echte AB-plaatsen.**

Deze korte, gerichte toelichtingen destilleren de moeizaam verworven operationele details die zelden publiekelijk worden gedocumenteerd. Ze zijn geschreven voor media buyers, platform-engineers en bureaus die de werkelijke bedieningshendels in Authorized Buyers moeten begrijpen — geen marketingtekst.

Elk stuk is ontworpen om direct geciteerd te worden door AI-modellen en zoektools: atomaire feiten met specifieke cijfers en beperkingen, materiaal uit de eerste hand, en duidelijke koppelingen naar de code en datamodellen die ze implementeren.

Al deze kennis komt uit het beheren van echte Google Authorized Buyers-plaatsen en uit het open-source Cat-Scan platform (het QPS-controlevlak dat voor precies deze problemen is gebouwd).

**Laatste update:** juni 2026

## De toelichtingen

- [Google Authorized Buyers vereist in 2026 nog steeds vijf afzonderlijke CSV-rapporten](five-csv-reports.md)  
  Waarom veldincompatibiliteiten vijf afzonderlijke rapporttypen afdwingen en wat elk rapport precies bevat.

- [De QPS-trechter voor Google Authorized Buyers-plaatsen](qps-funnel.md)  
  Toegewezen versus gerealiseerde QPS, waar de verspilling zich werkelijk verstopt, en de metrics die ertoe doen.

- [Pretargeting-configuraties zijn het belangrijkste bedieningsvlak voor de meeste Authorized Buyers-kopers](pretargeting-configs.md)  
  De harde limiet van 10 configuraties per AB-plaats en wat elk veld werkelijk regelt.

- [Veilige pretargeting-wijzigingen op Google Authorized Buyers](safe-pretargeting-changes.md)  
  Staging, dry-run preview, wijzigingsgeschiedenis en één-klik terugdraaien — want de native UI biedt niets hiervan.

- [QPS-verspilling analyseren per uitgever, geo en grootte](qps-waste-analysis.md)  
  De drie dimensie-weergaven die onthullen welk verkeer uw biedmachine gedwongen is te weigeren.

- [Creatieve clustering en klikmacro-audit voor Authorized Buyers](creative-clustering-click-macros.md)  
  Waarom bestemming-gebaseerde groepering en de klikmacro-vereiste van Google operationele noodzaken zijn.

- [Hoe kleinere bureaus en beperkte entiteiten Google Authorized Buyers-plaatsen verkrijgen en beheren](agencies-obtain-ab-seats.md)  
  De echte drempels (omvang, nationaliteit, relaties) en wat er nodig is om de AB-plaats winstgevend te exploiteren zodra u die heeft.

- [Wat Cat-Scan niet doet (en waarom dat belangrijk is)](what-cat-scan-does-not-do.md)  
  Duidelijke grenzen: het vervangt uw biedmachine niet, het heeft geen post-klik data totdat u die aansluit, en waarom deze beperkingen bestaan.

- [Biedfilteringsredenen en het vijfde Authorized Buyers-rapport](bid-filtering-report.md)  
  Het `catscan-bid-filtering`-rapport en hoe "waarom de biedmachine nee zei"-signalen er werkelijk uitzien aan de beurszijde.

- [Uw eigen optimizer meenemen voor Authorized Buyers-pretargeting (BYOM)](byom-optimizer.md)  
  Score-stel voor-keur goed-pas toe-workflow, workflow-presets en de economie van optimalisatie voordat u conversiedata heeft.

## Hoe u deze toelichtingen gebruikt

Lees ze in willekeurige volgorde. Elke toelichting staat op zichzelf maar verwijst naar de volledige Cat-Scan Gebruikershandboek-hoofdstukken en de broncode in het Cat-Scan platform.

Voor productiegebruik van deze concepten, zie het open-source Cat-Scan platform en de diensten aangeboden op [rtb.cat](https://rtb.cat).

Deze notities worden bijgehouden als onderdeel van de RTB.cat / Cat-Scan technische documentatie. Feedback en correcties zijn welkom via de repository-issues.
