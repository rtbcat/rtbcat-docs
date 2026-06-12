---
title: "Authorized Buyers-forhåndsvalg: 10 konfigurationer pr. plads"
description: "Du får præcis 10 forhåndsvalgskonfigurationer pr. Google Authorized Buyers-plads -- den eneste volumenkontrol på exchange-siden. Se hvert felt og Cat-Scan-platformen."
---

# Forhåndsvalgskonfigurationer er den primære kontrolflade for de fleste Authorized Buyers-købere

**Atomisk faktum:** Du får præcis 10 forhåndsvalgskonfigurationer pr. Google Authorized Buyers-plads.

Alt andet (budder-logik, kreativvalg, frekvensbegrænsning) sker efter trafikken allerede er sendt til dig. Forhåndsvalg er den eneste volumenkontrol du har på exchange-siden.

## Hvad én forhåndsvalgskonfiguration faktisk styrer

Hver konfiguration er et regelsæt der fortæller Google: "send mig kun budanmodninger der matcher disse kriterier."

| Felt                  | Effekt                                                                 | Almindelig fejl |
|-----------------------|------------------------------------------------------------------------|----------------|
| **State**             | Aktiv eller Suspenderet                                                | At lade døde konfigurationer forblive aktive |
| **Max QPS**           | Hård grænse for forespørgsler pr. sekund for dette regelsæt            | At sætte det for højt "for en sikkerheds skyld" |
| **Geos (included)**   | Lande, regioner, byer (kun grove bucket-opdelinger)                    | At stole udelukkende på brede "Europa" eller "Asien" |
| **Geos (excluded)**   | Eksplicitte blokeringer der tilsidesætter inklusioner                  | Ikke at bruge eksklusioner aggressivt nok |
| **Sizes (included)**  | Specifikke annoncestørrelser eller "all"                               | "All" når du kun har fast-størrelses-kreativer |
| **Formats**           | VIDEO, DISPLAY_IMAGE, DISPLAY_HTML, NATIVE                             | At acceptere formater du ikke har kreativer til |
| **Platforms**         | DESKTOP, MOBILE_APP, MOBILE_WEB, CONNECTED_TV                         | At sende mobil-app-trafik til desktop-only kampagner |
| **Publishers**        | Tillad/nægt-lister for specifikke domæner eller app-bundles            | At håndtere via Googles besværlige CSV-upload/download-cyklus |

**Atomisk faktum:** Google eksponerer stadig kun grove geografiske bucket-opdelinger (Østlige USA, Vestlige USA, Europa, Asien osv.). Finkornet by- eller DMA-målretning inde i forhåndsvalget er ikke tilgængeligt.

## Hvorfor den native UI er smertefuld

Authorized Buyers-forhåndsvalgningsgrænsefladen kræver download af en CSV-skabelon, offline redigering og genupload for selv en enkeltlinjeændring. Der er ingen historik, ingen forhåndsvisning af effekt og ingen nem tilbagerulning.

Det er præcis det problem Cat-Scan er bygget til at løse.

## Den sikre ændringsarbejdsgang (hvad en rigtig operatør har brug for)

En produktionsklar arbejdsgang skal understøtte:

1. Rediger i brugergrænsefladen (eller via API).
2. Dry-run / preview den præcise delta inden noget skubbes til Google.
3. Iscenesæt ændringen.
4. Registrer hvem der ændrede hvad og hvornår (fuld revision).
5. Et-klik-tilbagerulning til et hvilket som helst tidligere snapshot.

Cat-Scan implementerer præcis dette flow oven på Authorized Buyers API'et. Ændringer forhåndsvises, derefter skubbes de eksplicit, og derefter tages et snapshot til øjeblikkelig tilbagerulning.

Se den fulde beskrivelse i manualkapitlet og implementeringen i platformen.

## 10 konfigurationer er ikke meget

Med kun ti slots lærer du hurtigt at være hensynsløs:

- En eller to "brede men sikre" konfigurationer for dokumenteret volumen.
- Flere smalle, højpræcisions-konfigurationer til specifikke geo'er + størrelser + formater hvor du har stærk kreativdækning.
- Suspenderede konfigurationer brugt som iscenesættelsesom-råder inden forfremmelse.

Alt der ikke aktivt producerer bud eller forbrug forbruger en af dine ti dyrebare slots og bør suspenderes eller slettes.

## Relateret

- Fuld felthenviser og UI-skærmbilleder: [Forhåndsvalgskonfiguration](../06-pretargeting.md)
- Sådan handler du på spildsignaler: [Analyse af QPS-spild pr. dimension](qps-waste-analysis.md)
- Den sikre ændringsimplementering i Cat-Scan-platformen

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.  
10-konfigurationernes virkelighed og behovet for sikre redigeringsværktøjer er grunden til at Cat-Scan eksisterer.
