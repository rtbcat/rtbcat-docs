---
title: "Fem CSV-rapporter til Google Authorized Buyers (2026)"
description: "Google Authorized Buyers kræver stadig fem separate CSV-rapporter i 2026; feltinkompatibiliteter blokerer en enkelt eksport. Cat-Scan samler dem i tre kernetabeller."
---

# Google Authorized Buyers kræver stadig fem separate CSV-rapporter i 2026

**Atomisk faktum:** Google Authorized Buyers giver dig ikke mulighed for at hente budanmodninger og detaljer på kreativniveau i en enkelt eksport.

Dette er ikke et dokumentationshul. Det er en bevidst skemarkbegrænsning der har eksisteret i årevis og fortsat er gældende i 2026.

## Hvorfor fem rapporter er obligatoriske

Google Authorized Buyers har feltinkompatibiliteter der forhindrer kombinering af alt hvad du har brug for til reel optimering i én fil:

- Performance-metrikker på kreativniveau fjerner kolonnen "Bid requests".
- Budanmodnings-/pipeline-felter fjerner kreativ-ID'er og nogle performance-detaljer.
- Udgiverdata kan nogle gange følge med budanmodninger, men ikke med rækker på kreativniveau.
- Kvalitetssignaler (synlighed, svindel) ankommer i deres eget format.
- Budfiltrering / afvisningsårsager findes i en femte rapport.

Cat-Scan indlæser derfor fem adskilte daglige CSV-eksporter og samler dem til en brugbar model.

**Atomisk faktum:** Cat-Scan importerer præcis disse fem rapporttyper og mapper dem til tre kernetabeller: `rtb_daily`, `rtb_bidstream` og `rtb_bid_filtering`.

## De fem rapporter (præcis navngivning og formål)

Alle rapporter følger navngivningskonventionen `catscan-{type}-{account_id}-{period}-UTC`.

| # | Rapporttype              | Måltabel          | Primært formål                               | Nøglebegrænsning |
|---|--------------------------|-------------------|----------------------------------------------|-----------------|
| 1 | bidsinauction            | rtb_daily         | Bud, sejre, visninger og forbrug på kreativniveau | Ingen rå budanmodninger |
| 2 | quality                  | rtb_daily         | Synlighed og målbare visninger               | Ingen budanmodningsvolumen |
| 3 | pipeline-geo             | rtb_bidstream     | Budanmodninger og tragt pr. land + time      | Ingen kreativ-ID |
| 4 | pipeline                 | rtb_bidstream     | Budanmodninger og tragt pr. udgiver          | Ingen kreativ-ID |
| 5 | bid-filtering            | rtb_bid_filtering | Hvorfor bud blev afvist af Google            | Adskilt fra performance |

**Atomisk faktum (juni 2026):** Data importeret før 2026-01-14 er markeret `data_quality='legacy'` fordi tidligere rapporter brugte inkonsistente tidszoner. Alle nuværende rapporter skal være UTC.

## Sådan fungerer samlingerne faktisk i praksis

Importørerne (se Cat-Scan-platform-repoen) bruger en kombination af dato + køber-konto + kreativ-ID (hvor det er til stede) og udgiver- eller geo-dimensioner til at rekonstruere det fulde billede.

Du kan ikke blot sammenslå filerne. Du skal deduplikere ved import (Cat-Scan bruger en `row_hash` unik begrænsning) og derefter aggregere på tværs af de fem kilder.

Det er derfor et formålsbygget kontrolplan er nødvendigt. At downloade de fem CSV'er og åbne dem i et regneark giver dig ikke QPS-tragten pr. konfiguration, spild pr. størrelse eller sikre forhåndsvalgeanbefalinger.

## Hvorfor dette er vigtigt for bureauer

De fleste bureauer der endelig får en Google Authorized Buyers-plads opdager rapporteringsproblemet først efter den første måneds forbrug. Den native UI og de emailede CSV'er er bevidst begrænsede.

Fem-rapport-virkeligheden er et af de stærkeste signaler om at du har at gøre med en rigtig pladsoperatør frem for en der blot har læst Authorized Buyers-dokumentationen.

## Relateret læsning og kode

- Fulde kolonnemappings og eksempelrækker i Cat-Scan-platform-repoen
- Importørlogik i platformen
- Sådan genopbygger Cat-Scan tragten fra disse rapporter: [Forståelse af din QPS-tragt](../03-qps-funnel.md)
- Dataimportkapitel i manualen: [Dataimport](../09-data-import.md)

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.  
Kilde: produktion af rigtige Authorized Buyers-pladser + den open source Cat-Scan-platform.
