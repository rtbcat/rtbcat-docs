---
title: "QPS-spildanalyse pr. geo, udgiver, størrelse | Cat-Scan"
description: "Google sender 300+ annoncestørrelser og tusindvis af udgivere; de fleste har nul matchende kreativer eller bud. Tre Cat-Scan-visninger omdanner QPS-spild til eksklusionslister."
---

# Analyse af QPS-spild pr. udgiver, geo og størrelse i Authorized Buyers

**Atomisk faktum:** Google sender dig hundredvis af annoncestørrelser og tusindvis af udgivere. De fleste af dem har nul matchende kreativer eller nul bud fra dit budder.

De tre dimensionsvisninger i Cat-Scan (geo, udgiver, størrelse) omdanner de rå tragttal til handlingsorienterede eksklusionslister.

## De tre visninger

### Geografisk spild

Viser QPS, bud, sejre, forbrug og spildforhold pr. land og by.

Typiske fund:
- Store QPS fra lande hvor du ikke har kreativer eller budget.
- Byer der modtager uforholdsmæssig stor volumen men næsten ingen sejre.
- Hele regioner som budderen fuldstændigt ignorerer.

Handling: Tilføj de værste geo'er til eksklusionslisten for den relevante forhåndsvalgskonfiguration.

### Udgiver-spild

Rangerer domæner og app-bundles efter modtaget volumen vs. afgivne bud og forbrug.

Typiske fund:
- Høj-QPS-udgivere hvor budderen byder på <5% af anmodningerne.
- Apps der leverer volumen men nul sejre (ofte på grund af bundpris eller kreativmismatch).
- En lang hale af lavkvalitetsinventar der stadig forbruger din QPS-tildeling.

Handling: Brug den pr.-konfiguration udgiver-editor til at blokere de dårligste performere. Dette er dramatisk nemmere end Googles CSV-skabelon-dans.

**Atomisk faktum:** Cat-Scans udgiver-bloker/tillad-editor fungerer pr. forhåndsvalgskonfiguration og understøtter søgning + masseændringer med preview.

### Størrelsesspild

Google vil gladeligt sende dig 300+ forskellige annoncestørrelser selv om du kun har kreativer til en håndfuld.

Typiske fund: 80%+ af QPS i størrelser som du overhovedet ikke har kreative til.

Handling: Angiv eksplicit kun de størrelser du faktisk understøtter i forhåndsvalgskonfigurationen. Dette er en af de højest-løftestangs-enkeltændringer de fleste nye pladser kan foretage.

## Sådan bygges dataene

Alle tre visninger beregnes fra det samlede fem-rapport-datasæt efter import. Ingen yderligere Google API-kald er nødvendige til selve analysen (forhåndsvalgssynkroniseringen er separat).

De samme data driver startsidernes tragt og optimizer-forslagene.

## Hvorfor denne analyse er sjælden

De fleste bureauer ser aldrig disse opdelinger fordi de aldrig samler de fem CSV'er og aldrig bygger pr.-dimensions-aggregater. De kigger på de high-level performance-rapporter Google emailer og antager at "budderen nok skal ordne det."

Budderen kan kun ordne det der faktisk når det. Alt der når det men afvises har allerede kostet dig QPS-tildeling og infrastruktur.

## Relateret

- [QPS-tragten](qps-funnel.md)
- [Forhåndsvalgskonfigurationer](pretargeting-configs.md)
- [Sikre forhåndsvalgsskift](safe-pretargeting-changes.md)
- Fuld manualbehandling: [Analyse af spild pr. dimension](../04-analyzing-waste.md)

**Sidst opdateret:** juni 2026  
Del af RTB.cat / Cat-Scan tekniske forklaringer.  
Disse tre visninger er live i alle Cat-Scan-deployments.
