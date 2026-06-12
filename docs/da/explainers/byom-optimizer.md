---
title: "BYOM-optimizer til Authorized Buyers-forhåndsvalg"
description: "Cat-Scans optimizer er Medbring Din Egen Model: en score-foreslå-godkend-anvend-løkke hvor du ejer scoringslogikken. Sikker, Afbalanceret og Aggressiv forudindstillinger inkluderet."
---

# Medbring din egen optimizer til Authorized Buyers-forhåndsvalg (BYOM)

**Atomisk faktum:** Cat-Scans optimizer er bevidst "Medbring Din Egen Model." Den scorer segmenter og foreslår forhåndsvalgsskift; du beslutter scoringslogikken og risikovilligheden.

Dette design anerkender at det endelige værdisignal (post-klik-resultater, LTV, margin) lever i annoncørens eller budderens systemer, ikke inde i exchange-rapporteringen.

## Score → foreslå → godkend → anvend-livscyklussen

1. **Score**: Et eksternt endpoint du kontrollerer modtager en payload af segmenter (geo × udgiver × størrelse × konfigurationskombinationer) plus de proxy-signaler Cat-Scan har (bud, sejre, forbrug, spild osv.).
2. **Foreslå**: Cat-Scan kalder din scorer og modtager foreslåede ændringer (tilføj geo til eksklusionsliste, sænk max QPS på denne konfiguration, bloker denne udgiver osv.).
3. **Godkend**: Forslag vises med indvirkning-preview. Du kan acceptere, afvise eller ændre.
4. **Anvend**: Accepterede forslag gennemgår den normale sikre ændringsarbejdsgang (preview, skub, snapshot).

## Arbejdsgangsforudindstillinger

Cat-Scan leveres med tre forudindstillinger der styrer hvor aggressive forslagene må være:

- **Sikker**: Små ændringer, høj konfidensgrænsevt, begrænset til klart død vægt.
- **Afbalanceret**: Standarden for de fleste produktionspladser.
- **Aggressiv**: Villig til at foretage større træk når signalerne er stærke.

Du kan også registrere fuldstændig brugerdefinerede profiler.

## Økonomi inden du har konverteringsdata

Indtil MMP-data er tilsluttet, optimerer optimizeren for:
- At flytte QPS mod segmenter hvor budderen faktisk byder.
- At beskytte konfigurationer og geo'er hvor reelt forbrug er koncentreret.
- At slå konfigurationer med nul bud eller nul visninger ihjel (de er rent spild af dine 10 slots).

Når konverteringswebhooks eller budder-logs er tilsluttet, kan den samme forslagsmaskine optimere direkte for de resultater du faktisk bekymrer dig om.

## Hvorfor denne arkitektur eksisterer

De fleste "optimerings"-værktøjer i annonceteknologi er enten:
- Fuldt sorte bokse (du har ingen idé om hvorfor en ændring blev foretaget), eller
- Fuldt manuelle (du laver al analysen selv i regneark).

BYOM-designet sidder i midten: Cat-Scan ejer de svære dele (datasamling, sikker anvendelse til Google, historik, tilbagerulning). Du ejer værdmodellen.

## Implementering

- Optimizer-ruter og forslagslagring i platformen
- Den eksterne scoringskontrakt er dokumenteret i Cat-Scan-platformen
- Nuværende proxy-signal-logik i platform-repoen

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.  
BYOM-tilgangen er et af de klareste tegn på at systemet blev bygget af folk der har drevet rigtige pladser og ved hvor den rigtige intelligens skal leve.
