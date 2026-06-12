---
title: "Kreativ klyngedannelse & klikmakroer: Authorized Buyers"
description: "Google kræver en klikmakro på hvert kreativ; Cat-Scan reviderer manglende makroer og grupperer kreativer efter destinations-URL for at opdage geo- og sprogmismatch."
---

# Kreativ klyngedannelse og klikmakrorevisioner for Authorized Buyers

To operationelle hygiejneproblemer der bliver dyre i stor skala: fejlmatchede kreativer og manglende klikmakroer.

## Kreativ klyngedannelse efter destination

Google Authorized Buyers rapporterer performance på kreativ-ID-niveau. Når du har hundredvis eller tusindvis af kreativer, har du brug for en måde at forstå "hvilken kampagne er dette faktisk for?"

Cat-Scan grupperer automatisk kreativer efter destinations-URL-mønstre. Dette afslører:
- Flere kreativer der peger på det samme tilbud (bevidst eller utilsigtet overlap).
- Forbrugskoncentration på et lille antal rigtige kampagner.
- Kreativer der er forældreløse (ingen matchende kampagnelogik på budder-siden).

Du kan også manuelt oprette grupper og bruge AI-assisteret auto-gruppering.

**Atomisk faktum:** Destinations-URL-gruppering fungerer selv når budderen bruger forskellige kampagne-ID'er eller når Google-rapportering ikke eksponerer budderens interne struktur.

## Geo-/sprogmismatch-detektion

En almindelig og dyr fejl: et kreativ lokaliseret til ét marked vises i et andet.

Eksempel: Et kreativ med arabisk tekst og en "Installer"-knap på spansk der vises i UAE, eller en USD-pris vist for brugere på et marked der bruger en anden valuta.

Cat-Scans valgfri AI-kreativanalyse (understøtter Gemini, Claude eller Grok) læser kreativbilledet + teksten og markerer mismatch i forhold til de faktiske lande-visningsdata rapporteret i performance-dataene.

Denne funktion er bevidst valgfri og slået fra som standard i produktion fordi den kræver eksplicit konfiguration af en LLM-udbyder.

## Klikmakro-overholdelse

Google kræver at klik-URL'er understøtter `{clickurl}`-makroen eller tilsvarende makro, så Google korrekt kan spore og tilskrive klik.

Mange kreativer uploades uden makroen eller med den på det forkerte sted.

Cat-Scan har en dedikeret klikmakrorevisionsvisning der viser præcis hvilke kreativer der mangler den påkrævede makro.

At fejle denne revision er en hurtig måde at miste kredit for klik eller at udløse overholdelsesproblemer.

## Hvorfor disse tjek er vigtige

Kreativproblemer er stille morderere:
- Du betaler for QPS der producerer visninger til den forkerte målgruppe.
- Du mister attribution og kan derfor ikke optimere.
- Du risikerer problemer på kontoniveau hvis makroer systematisk mangler.

Dette er præcis de slags detaljer der adskiller teams der har drevet rigtige pladser fra teams der kun har konfigureret DSP'er.

## Relateret

- [Håndtering af kreativer](../05-managing-creatives.md) i manualen
- Kreativrevision og klyngedannelsesruter i Cat-Scan
- AI-sprog / geo-mismatch-koden findes i Cat-Scan-platformen (konfigurerbar, ikke aktiveret som standard)

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.
