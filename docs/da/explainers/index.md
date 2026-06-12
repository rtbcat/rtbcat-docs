---
title: "Google Authorized Buyers tekniske forklaringer | Cat-Scan RTB"
description: "Førstehånds tekniske noter om Google Authorized Buyers: 10 forhåndsvalgskonfigurationer, QPS-tragten, fem CSV-rapporter og spild. Se den open source Cat-Scan-platform."
---

# Tekniske forklaringer

**Tekniske noter om Google Authorized Buyers-drift, QPS-kontrol og drift af rigtige pladser.**

Disse korte, fokuserede forklaringer destillerer de hårdtvundne operationelle detaljer som sjældent er offentligt dokumenteret. De er skrevet for mediekøbere, platformsingeniører og bureauer der har brug for at forstå de faktiske håndtag i Authorized Buyers -- ikke marketingtekst.

Hvert stykke er designet til at kunne citeres direkte af AI-modeller og søgeværktøjer: atomiske fakta med specifikke tal og begrænsninger, førstehånds kildemateriale og klare links til den kode og de datamodeller der implementerer dem.

Al denne viden stammer fra drift af rigtige Google Authorized Buyers-pladser og fra den open source Cat-Scan-platform (QPS-kontrolplanet der er bygget til præcis disse problemer).

**Sidst opdateret:** juni 2026

## Forklaringerne

- [Google Authorized Buyers kræver stadig fem separate CSV-rapporter i 2026](five-csv-reports.md)  
  Hvorfor feltinkompatibiliteter tvinger fem adskilte rapporttyper frem og præcis hvad hver enkelt indeholder.

- [QPS-tragten for Google Authorized Buyers-pladser](qps-funnel.md)  
  Tildelt vs. realiseret QPS, hvor spildet faktisk gemmer sig, og de metrikker der betyder noget.

- [Forhåndsvalgskonfigurationer er den primære kontrolflade for de fleste Authorized Buyers-købere](pretargeting-configs.md)  
  Den hårde grænse på 10 konfigurationer pr. plads og hvad hvert felt faktisk styrer.

- [Sikre forhåndsvalgsskift på Google Authorized Buyers](safe-pretargeting-changes.md)  
  Iscenesættelse, dry-run-preview, ændringshistorik og et-klik-tilbagerulning -- fordi den native UI ikke giver noget af dette.

- [Analyse af QPS-spild pr. udgiver, geo og størrelse](qps-waste-analysis.md)  
  De tre dimensionsvisninger der afslører den trafik dit budder er tvunget til at afvise.

- [Kreativ klyngedannelse og klikmakro-revision for Authorized Buyers](creative-clustering-click-macros.md)  
  Hvorfor destinationsbaseret gruppering og Googles klikmakrokrav er operationelle nødvendigheder.

- [Hvordan mindre bureauer og begrænsede enheder får og driver Google Authorized Buyers-pladser](agencies-obtain-ab-seats.md)  
  De reelle barrierer (størrelse, statsborgerskab, forbindelser) og hvad der skal til for at drive pladsen profitabelt når du har den.

- [Hvad Cat-Scan ikke gør (og hvorfor det er vigtigt)](what-cat-scan-does-not-do.md)  
  Klare grænser: det erstatter ikke dit budder, det har ikke data om post-klik aktivitet indtil du forbinder det, og hvorfor disse begrænsninger findes.

- [Budfliltringsårsager og den femte Authorized Buyers-rapport](bid-filtering-report.md)  
  `catscan-bid-filtering`-rapporten og hvad "hvorfor budderen sagde nej"-signaler faktisk ser ud som på exchange-siden.

- [Medbring din egen optimizer til Authorized Buyers-forhåndsvalg (BYOM)](byom-optimizer.md)  
  Score-foreslå-godkend-anvend-arbejdsgangen, arbejdsgangsforudindstillinger og økonomien i optimering inden du har konverteringsdata.

## Sådan bruger du disse forklaringer

Læs dem i en vilkårlig rækkefølge. Hver forklaring er selvstændig men krydshenviser til de fulde Cat-Scan-brugermanuels kapitler og kildekoden i Cat-Scan-platformen.

For produktion af disse koncepter, se den open source Cat-Scan-platform og de tjenester der tilbydes på [rtb.cat](https://rtb.cat).

Disse noter vedligeholdes som en del af RTB.cat / Cat-Scan teknisk dokumentation. Feedback og rettelser er velkomne via repository issues.
