---
title: "Authorized Buyers Pretargeting: 10 Configuraties per AB-Plaats"
description: "U krijgt precies 10 pretargeting-configuraties per Google Authorized Buyers-plaats — het enige volumebeheer aan de beurszijde. Zie elk veld en het Cat-Scan platform."
---

# Pretargeting-configuraties zijn het belangrijkste bedieningsvlak voor de meeste Authorized Buyers-kopers

**Atomair feit:** U krijgt precies 10 pretargeting-configuraties per Google Authorized Buyers-plaats.

Al het andere (biedmachinelogica, creatieve selectie, frequentiecapping) vindt plaats nadat het verkeer al naar u is gestuurd. Pretargeting is de enige volumebeheersing die u aan de beurszijde heeft.

## Wat één pretargeting-configuratie werkelijk regelt

Elke configuratie is een regelset die Google vertelt: "stuur mij alleen biedverzoeken die aan deze criteria voldoen."

| Veld                | Effect                                                                 | Veelgemaakte fout |
|---------------------|------------------------------------------------------------------------|--------------------|
| **Status**          | Actief of Gepauzeerd                                                   | Dode configuraties actief laten |
| **Max QPS**         | Harde limiet op queries per seconde voor deze regelset                 | Te hoog instellen "voor alle zekerheid" |
| **Geo's (opgenomen)** | Landen, regio's, steden (alleen grove segmenten)                    | Uitsluitend vertrouwen op breed "Europa" of "Azië" |
| **Geo's (uitgesloten)** | Expliciete blokkades die inclusies overschrijven                  | Exclusies niet agressief genoeg gebruiken |
| **Groottes (opgenomen)** | Specifieke advertentiegrootten of "alles"                       | "Alles" wanneer u alleen creatives van vaste grootte heeft |
| **Formaten**        | VIDEO, DISPLAY_IMAGE, DISPLAY_HTML, NATIVE                             | Formaten accepteren waarvoor u geen creatives heeft |
| **Platforms**       | DESKTOP, MOBILE_APP, MOBILE_WEB, CONNECTED_TV                          | Mobiel app-verkeer naar campagnes sturen die alleen voor desktop zijn |
| **Uitgevers**       | Toestaan/blokkeer-lijsten voor specifieke domeinen of app-bundles      | Beheren via de omslachtige CSV-upload/-downloadcyclus van Google |

**Atomair feit:** Google stelt nog steeds alleen grove geografische segmenten beschikbaar (Oost-VS, West-VS, Europa, Azië, enz.). Fijnmazige stad- of DMA-targeting binnen pretargeting is niet beschikbaar.

## Waarom de native UI zo omslachtig is

De Authorized Buyers pretargeting-interface vereist het downloaden van een CSV-sjabloon, offline bewerken en opnieuw uploaden, zelfs voor een wijziging van één regel. Er is geen geschiedenis, geen preview van impact en geen eenvoudige terugdraaioptie.

Dit is precies het probleem dat Cat-Scan is gebouwd om op te lossen.

## De veilige wijzigingsworkflow (wat een echte operator nodig heeft)

Een workflow die geschikt is voor productiegebruik moet ondersteunen:

1. Bewerken in de UI (of via API).
2. Dry-run / preview van de exacte delta vóórdat die naar Google wordt gepusht.
3. Staging van de wijziging.
4. Vastleggen wie wat heeft gewijzigd en wanneer (volledige audit).
5. Één-klik terugdraaien naar elke eerdere snapshot.

Cat-Scan implementeert precies deze workflow bovenop de Authorized Buyers API. Wijzigingen worden gepreviewed, vervolgens expliciet gepusht en daarna vastgelegd als snapshot voor directe terugdraaiing.

Zie de volledige beschrijving in het handboekhoofstuk en de implementatie in het platform.

## 10 configuraties is niet veel

Met slechts tien slots leert u snel om meedogenloos te zijn:

- Één of twee "breed maar veilig"-configuraties voor bewezen volume.
- Meerdere smalle, hoge-precisie configuraties voor specifieke geo's + groottes + formaten waar u sterke creatieve dekking heeft.
- Gepauzeerde configuraties die worden gebruikt als staginggebieden vóór promotie.

Alles wat niet actief biedingen of uitgaven produceert, verbruikt één van uw tien kostbare slots en moet worden gepauzeerd of verwijderd.

## Gerelateerd

- Volledig veldoverzicht en UI-schermafbeeldingen: [Pretargeting-configuratie](../06-pretargeting.md)
- Hoe te handelen op verspillingssignalen: [QPS-verspilling per dimensie analyseren](qps-waste-analysis.md)
- De veilige wijzigingsimplementatie in het Cat-Scan platform

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.  
De 10-configuraties-realiteit en de behoefte aan veilige bewerkingstools is waarom Cat-Scan bestaat.
