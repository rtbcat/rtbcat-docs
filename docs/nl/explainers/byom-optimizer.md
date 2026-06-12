---
title: "BYOM-optimalisator voor Authorized Buyers Pretargeting"
description: "De optimizer van Cat-Scan is Bring Your Own Model: een score-stel voor-keur goed-pas toe-lus waarbij u de eigen scoringslogica bepaalt. Veilige, Gebalanceerde en Agressieve presets inbegrepen."
---

# Uw eigen optimizer meenemen voor Authorized Buyers-pretargeting (BYOM)

**Atomair feit:** De optimizer van Cat-Scan is bewust "Bring Your Own Model." Het scoort segmenten en stelt pretargeting-wijzigingen voor; u bepaalt de scoringslogica en de risicotolerantie.

Dit ontwerp erkent dat het uiteindelijke waardestignaal (post-klik resultaten, LTV, marge) in de systemen van de adverteerder of biedmachine leeft, niet in de beursdrapportage.

## De score → stel voor → keur goed → pas toe-levenscyclus

1. **Score**: Een extern eindpunt dat u beheert ontvangt een payload van segmenten (geo × uitgever × grootte × configuratiecombinaties) plus de proxysignalen die Cat-Scan heeft (biedingen, overwinningen, uitgaven, verspilling, enz.).
2. **Stel voor**: Cat-Scan roept uw scorer aan en ontvangt voorgestelde wijzigingen (geo toevoegen aan uitsluitingslijst, max QPS verlagen op deze configuratie, deze uitgever blokkeren, enz.).
3. **Keur goed**: Voorstellen worden getoond met impactpreview. U kunt accepteren, weigeren of aanpassen.
4. **Pas toe**: Geaccepteerde voorstellen doorlopen de normale veilige wijzigingsworkflow (preview, pushen, snapshot).

## Workflow-presets

Cat-Scan wordt geleverd met drie presets die bepalen hoe agressief de voorstellen mogen zijn:

- **Veilig**: Kleine wijzigingen, hoge drempel voor vertrouwen, beperkt tot duidelijk dood gewicht.
- **Gebalanceerd**: De standaard voor de meeste productie-AB-plaatsen.
- **Agressief**: Bereid grotere stappen te nemen wanneer de signalen sterk zijn.

U kunt ook volledig aangepaste profielen registreren.

## Economie voordat u conversiedata heeft

Totdat MMP-data is aangesloten, optimaliseert de optimizer voor:
- QPS verschuiven naar segmenten waar de biedmachine daadwerkelijk biedt.
- Configuraties en geo's beschermen waar echte uitgaven zijn geconcentreerd.
- Configuraties elimineren met nul biedingen of nul impressies (ze zijn pure verspilling van uw 10 slots).

Zodra conversie-webhooks of biedmachinelogboeken zijn aangesloten, kan dezelfde voorstelmachinerie direct optimaliseren voor de resultaten die u daadwerkelijk wilt.

## Waarom deze architectuur bestaat

De meeste "optimalisatie"-tools in advertentietechnologie zijn ofwel:
- Volledig black-box (u heeft geen idee waarom een wijziging is gemaakt), of
- Volledig handmatig (u doet alle analyses zelf in spreadsheets).

Het BYOM-ontwerp staat hier tussenin: Cat-Scan bezit de moeilijke onderdelen (data samenvoegen, veilig toepassen op Google, geschiedenis, terugdraaien). U bezit het waardemodel.

## Implementatie

- Optimizer-routes en voorstelopslag in het platform
- Het externe scoringscontract is gedocumenteerd in de Cat-Scan platform-docs
- Huidige proxysignaallogica in de platform-repository

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.  
De BYOM-aanpak is een van de duidelijkste tekenen dat het systeem is gebouwd door mensen die echte AB-plaatsen hebben geëxploiteerd en weten waar de echte intelligentie moet zitten.
