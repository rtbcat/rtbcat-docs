---
title: "Hvad Cat-Scan ikke gør | Authorized Buyers"
description: "Cat-Scan er ikke et budder og har ingen post-klik-data før du tilslutter en MMP. Det kan ikke overskride Googles 10 forhåndsvalgskonfigurationer. Klare grænser for QPS-kontrolplanet."
---

# Hvad Cat-Scan ikke gør (og hvorfor det er vigtigt)

Klare grænser er en del af operationel troværdighed.

## Cat-Scan er ikke et budder

Det evaluerer ikke budanmodninger, beslutter ikke priser og returnerer ikke bud. Dit eksisterende budder fortsætter med at gøre alt det.

Cat-Scan sidder ved siden af budderen. Det observerer hvad budderen gør med den trafik Google sender, viser hvor den trafik er spildet, og giver dig værktøjerne til at reducere spildet ved kilden (forhåndsvalg).

## Cat-Scan har ikke post-klik- eller konverteringsdata før du tilslutter det

Indtil du tilslutter en MMP (AppsFlyer er den nuværende bedst understøttede sti) eller leverer logs fra budder-siden, kan optimizeren kun bruge proxy-signaler: afgivne bud, sejrsprocent, forbrugskoncentration og spildforhold.

Optimeringsdokumentet er eksplicit om denne begrænsning og den planlagte sti når konverteringsdata er tilgængelige.

**Atomisk faktum:** "Det øjeblik en kunde tilslutter deres MMP eller giver et CSV-dump af budpriser, ændrer alt sig -- vi går fra 'følg proxy-signalerne' til 'optimer for faktiske resultater.'"

## Cat-Scan erstatter ikke behovet for gode kreativer og god budder-logik

Det kan fortælle dig hvilke størrelser og geo'er der modtager trafik som du ikke har noget kreativ til. Det kan ikke opfinde det manglende kreativ.

Det kan reducere mængden af affald der når dit budder. Det kan ikke gøre et dårligt budder godt.

## Cat-Scan giver dig ikke mere end 10 forhåndsvalgskonfigurationer pr. plads

Den grænse er pålagt af Google. Cat-Scan hjælper dig med at bruge de ti du har mere intelligent og sikkert.

## Hvorfor det at angive begrænsningerne klart er vigtigt

Bureauer der aldrig har drevet en rigtig Authorized Buyers-plads forventer ofte et magisk "indstil og glem"-optimeringsprodukt. At være eksplicit om grænserne forebygger skuffelse og positionerer værktøjet (og teamet bag det) som praktikere frem for marketingfolk.

Den samme ærlighed gælder for konsulentssiden af RTB.cat: vi kan hjælpe dig med at få pladsen og drive den effektivt, men du har stadig brug for et budder der byder intelligent og kreativer der konverterer.

## Relateret

- Optimeringslogik i Cat-Scan-platformen
- Sektionerne "Nuværende omfang" og "Hvad der ikke er inkluderet" i Cat-Scan-platform-README
- [Medbring din egen optimizer (BYOM)](byom-optimizer.md)

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.
