---
title: "Budfliltringsrapport: Authorized Buyers femte CSV"
description: "Den femte rapport, catscan-bid-filtering, er det eneste sted Google fortæller dig hvorfor den afviste et bud før dit budder så det. Læs filtreringsårsagerne på exchange-siden."
---

# Budfliltringsårsager og den femte Authorized Buyers-rapport

**Atomisk faktum:** Den femte rapport (`catscan-bid-filtering`) er det eneste sted Google fortæller dig hvorfor den afviste et bud før det overhovedet nåede dit budder.

De fleste operatører kigger aldrig på den fordi den ankommer i sin egen CSV og ikke som standard samles med performance-dataene.

## Hvad budfliltringsrapporten indeholder

Den viser de årsager Google anvendte budfiltrering på exchange-siden for anmodninger der matchede dit forhåndsvalg men derefter blev filtreret fra inden de blev sendt.

Almindelige kategorier inkluderer:
- Kreativ- eller størrelsesmismatch (fra Googles perspektiv)
- Udgiver- eller inventarkvalitetssignaler
- Frekvens- eller andre politikfiltre
- Tekniske eller formatproblemer

Når den samles med de andre fire rapporter, forklarer den en del af faldet fra "reached queries" til "bids" der ikke er under dit budders kontrol.

## Hvorfor den er værdifuld

Dit budder ser kun hvad Google faktisk leverer. Budfliltringsrapporten er indsigten i det sidste filtreringslag der skete på Googles side.

Hvis en stor del af det potentielle volumen filtreres for "creative size not supported", er den rigtige løsning normalt i din forhåndsvalgsstørrelses-liste, ikke i budderen.

## Sådan bruger Cat-Scan den

Rapporten importeres til den relevante tabel. Den er tilgængelig til analyse ved siden af tragt- og spildvisningerne.

Det er et af de signaler der kan indføres i en brugerdefineret optimizer (se BYOM-forklaringen).

## Relateret kode og dokumentation

- Måltabel og formål i Cat-Scan-platformens datamodeldokumentation
- Den femte rapport er en del af det standard fem-rapport-importflow beskrevet i Dataimport-kapitlet

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.
