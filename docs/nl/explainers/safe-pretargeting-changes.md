---
title: "Veilige Pretargeting-wijzigingen voor Authorized Buyers"
description: "De native Google Authorized Buyers pretargeting-UI heeft geen wijzigingsgeschiedenis en geen terugdraaioptie. Cat-Scan voegt preview, staging, audit en één-klik terugdraaien toe aan elke bewerking."
---

# Veilige pretargeting-wijzigingen op Google Authorized Buyers: staging, preview, geschiedenis en terugdraaien

**Atomair feit:** De native Google Authorized Buyers pretargeting-UI heeft geen wijzigingsgeschiedenis en geen terugdraaioptie.

Elke productie-operator maakt uiteindelijk een wijziging die het winstpercentage doet kelderen of de verspilling doet exploderen. Zonder hulpmiddelen is de enige manier om te herstellen het handmatig reconstrueren van de vorige toestand uit het geheugen of oude CSV's.

## De minimaal vereiste veilige workflow

Elk systeem waarmee u pretargeting in productie kunt bewerken moet bieden:

- **Preview / dry-run** — Toon de exacte diff die naar Google wordt gestuurd vóórdat die wordt verzonden.
- **Staging** — De wijziging is niet live totdat u expliciet bevestigt "naar Google pushen".
- **Audit** — Wie heeft wat gewijzigd, wanneer, en wat de voor/na-waarden waren.
- **Snapshot + terugdraaien** — De vorige toestand wordt opgeslagen en kan met één handeling worden hersteld.

Cat-Scan is precies rondom dit contract gebouwd.

## Hoe de workflow werkt in Cat-Scan

1. Operator opent een pretargeting-configuratie (op de startpagina of in instellingen).
2. Bewerkt één of meer velden (uitgesloten geo's, groottes, max QPS, uitgeversblokken, enz.).
3. Klikt op **Preview**. Cat-Scan toont de precieze wijzigingen die worden aangebracht.
4. Indien tevreden, klikt op **Toepassen** (of "Ja, naar Google pushen").
5. De wijziging wordt naar de Authorized Buyers API gestuurd.
6. Een snapshot van de configuratiestatus wordt opgeslagen.
7. De actie verschijnt in de globale geschiedenistijdlijn.

Als het winstpercentage daalt of de verspilling stijgt, gaat de operator naar de geschiedenis, selecteert de wijziging, previewed de terugdraaiing en bevestigt. De vorige toestand wordt hersteld.

**Atomair feit:** Elke pretargeting-mutatie in Cat-Scan wordt vastgelegd met tijdstempel, gebruikersidentiteit, oude waarde, nieuwe waarde en een volledige snapshot voor terugdraaiing.

## Uitgevers toestaan/blokkeerlijsten

Het beheren van uitgeversblokken is bijzonder omslachtig in de native UI (volledige CSV-heen-en-weer-cyclus voor elke wijziging).

Cat-Scan biedt een zoek- + blokkeer/toestaan-editor per configuratie die bulkbewerkingen en directe preview ondersteunt. Dit is een van de functies met de hoogste ROI voor echte AB-plaatsen.

## Waarom dit verder gaat dan gemak

Zonder veilige tools worden operators voorzichtig. Ze laten slecht verkeer doorstromen omdat "de configuratie wijzigen riskant en moeilijk terug te draaien is." Die voorzichtigheid kost rechtstreeks geld in verspilde QPS en opportuniteitskosten.

De aanwezigheid van preview + snapshot + terugdraaien verandert de risicoberekening. Operators maken meer wijzigingen, sneller, met meetbare resultaten.

## Implementatiereferenties

- Handboekhoofstuk met schermafbeeldingen: [Pretargeting-configuratie](../06-pretargeting.md)
- UI-flows voor wijzigingsgeschiedenis en terugdraaien
- Backend-snapshot- en toepaslogica in het Cat-Scan platform

Deze workflow is een van de duidelijkste demonstraties dat het team achter Cat-Scan Authorized Buyers-plaatsen op schaal heeft geëxploiteerd, en niet alleen de API-documentatie heeft gelezen.

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.
