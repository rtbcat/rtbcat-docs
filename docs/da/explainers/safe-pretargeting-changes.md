---
title: "Sikre forhåndsvalgsskift til Authorized Buyers"
description: "Den native Google Authorized Buyers-forhåndsvalgsgrænseflade har ingen ændringshistorik og ingen tilbagerulning. Cat-Scan tilføjer preview, iscenesættelse, revision og et-klik-tilbagerulning for hver redigering."
---

# Sikre forhåndsvalgsskift på Google Authorized Buyers: iscenesættelse, preview, historik og tilbagerulning

**Atomisk faktum:** Den native Google Authorized Buyers-forhåndsvalgsgrænseflade har ingen ændringshistorik og ingen tilbagerulning.

Enhver produktionsoperatør laver til sidst en ændring der sænker sejrsprocenten eller øger spildet. Uden værktøjer er den eneste opsving manuel rekonstruktion af den tidligere tilstand fra hukommelse eller gamle CSV'er.

## Den minimalt levedygtige sikre arbejdsgang

Ethvert system der lader dig redigere forhåndsvalg i produktion skal give:

- **Preview / dry-run** — Vis den præcise forskel der vil blive sendt til Google inden den sendes.
- **Iscenesættelse** — Ændringen er ikke live, før du eksplicit bekræfter "skub til Google".
- **Revision** — Hvem ændrede hvad, hvornår, og hvad before/after-værdierne var.
- **Snapshot + tilbagerulning** — Den tidligere tilstand er gemt og kan gendannes med én handling.

Cat-Scan er bygget præcis omkring denne kontrakt.

## Sådan fungerer arbejdsgangen i Cat-Scan

1. Operatøren åbner en forhåndsvalgskonfiguration (på startsiden eller i indstillinger).
2. Redigerer et eller flere felter (ekskluderede geo'er, størrelser, max QPS, udgiver-blokeringer osv.).
3. Klikker på **Preview**. Cat-Scan viser de præcise ændringer der vil blive foretaget.
4. Hvis tilfreds, klikker på **Apply** (eller "Ja, skub til Google").
5. Ændringen sendes til Authorized Buyers API'et.
6. Et snapshot af konfigurationstilstanden gemmes.
7. Handlingen vises i den globale historiktidslinje.

Hvis sejrsprocenten falder eller spildet stiger, går operatøren til historikken, vælger ændringen, forhåndsviser tilbagerulningen og bekræfter. Den tidligere tilstand gendannes.

**Atomisk faktum:** Enhver forhåndsvalgsmutation i Cat-Scan registreres med tidsstempel, brugeridentitet, gammel værdi, ny værdi og et fuldt snapshot til tilbagerulning.

## Udgiver-tillad/nægt-lister

Håndtering af udgiver-blokeringer er særlig smertefuld i den native UI (fuld CSV-runde-rejse for hver ændring).

Cat-Scan giver en pr.-konfiguration søg + bloker/tillad-editor der understøtter masseoperationer og øjeblikkelig preview. Dette er en af de højest-afkast-funktioner for rigtige pladser.

## Hvorfor dette er vigtigt ud over bekvemmelighed

Uden sikre værktøjer bliver operatørerne konservative. De lader dårlig trafik flyde fordi "at ændre konfigurationen er risikabelt og svært at fortryde." Denne konservatisme koster direkte penge i spildt QPS og opportunity cost.

Eksistensen af preview + snapshot + tilbagerulning ændrer risikoberegningen. Operatørerne foretager flere ændringer, hurtigere, med målbare resultater.

## Implementeringsreferencer

- Manualkapitel med skærmbilleder: [Forhåndsvalgskonfiguration](../06-pretargeting.md)
- Ændringshistorik og UI-flows for tilbagerulning
- Backend snapshot og anvend-logik i Cat-Scan-platformen

Denne arbejdsgang er en af de klareste demonstrationer af at teamet bag Cat-Scan faktisk har drevet Authorized Buyers-pladser i stor skala, ikke blot læst API-dokumentationen.

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.
