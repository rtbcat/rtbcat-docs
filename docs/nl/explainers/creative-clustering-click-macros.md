---
title: "Creatieve Clustering & Klikmacro's: Authorized Buyers"
description: "Google vereist een klikmacro op elke creative; Cat-Scan controleert ontbrekende macro's en clustert creatives op bestemmings-URL om geo- en taalafwijkingen op te sporen."
---

# Creatieve clustering en klikmacro-audit voor Authorized Buyers

Twee operationele hygiëneproblemen die op schaal kostbaar worden: niet-overeenkomende creatives en ontbrekende klikmacro's.

## Creatieve clustering op bestemming

Google Authorized Buyers rapporteert prestaties op het niveau van creative-ID. Wanneer u honderden of duizenden creatives heeft, heeft u een manier nodig om te begrijpen "voor welke campagne is dit eigenlijk?"

Cat-Scan clustert creatives automatisch op bestemmings-URL-patronen. Dit onthult:
- Meerdere creatives die naar hetzelfde aanbod wijzen (opzettelijke of onbedoelde overlap).
- Uitgavenconcentratie op een klein aantal echte campagnes.
- Wezen-creatives (geen overeenkomende campagnelogica aan de biedmachine-zijde).

U kunt ook handmatig clusters aanmaken en gebruikmaken van AI-ondersteunde automatische clustering.

**Atomair feit:** Bestemmings-URL-clustering werkt zelfs wanneer de biedmachine verschillende campagne-ID's gebruikt of wanneer Google-rapportage de interne structuur van de biedmachine niet blootlegt.

## Geo-/taalafwijkingsdetectie

Een veelgemaakte en kostbare fout: een creative die is gelokaliseerd voor één markt, wordt weergegeven in een andere.

Voorbeeld: Een creative met Arabische tekst en een "Installeren"-knop in het Spaans die wordt weergegeven in de VAE, of een USD-prijs die wordt getoond aan gebruikers in een markt die een andere valuta gebruikt.

De optionele AI-creatieve analyse van Cat-Scan (ondersteunt Gemini, Claude of Grok) leest de creative-afbeelding en -tekst en markeert afwijkingen ten opzichte van de werkelijke weergavelanden die zijn gerapporteerd in de prestatiedata.

Deze functie is bewust optioneel en standaard uitgeschakeld in productie, omdat het expliciete configuratie van een LLM-provider vereist.

## Klikmacro-naleving

Google vereist dat klik-URL's de `{clickurl}` of equivalente macro ondersteunen, zodat Google klikken correct kan bijhouden en toewijzen.

Veel creatives worden geüpload zonder de macro of met de macro op de verkeerde plek.

Cat-Scan heeft een speciale klikmacro-auditweergave die precies laat zien welke creatives de vereiste macro missen.

Het mislukken van deze audit is een snelle manier om krediet voor klikken te verliezen of nalevingsproblemen te veroorzaken.

## Waarom deze controles belangrijk zijn

Creative-problemen zijn stille moordenaars:
- U betaalt voor QPS die impressies produceert voor het verkeerde publiek.
- U verliest attributie en kunt daardoor niet optimaliseren.
- U riskeert problemen op accountniveau als macro's stelselmatig ontbreken.

Dit zijn precies de details die teams scheiden die echte AB-plaatsen hebben geëxploiteerd van teams die alleen DSP's hebben geconfigureerd.

## Gerelateerd

- [Creatives beheren](../05-managing-creatives.md) in het handboek
- Creative-audit en clustering-routes in Cat-Scan
- De AI-taal-/geo-afwijkingscode bevindt zich in het Cat-Scan platform (configureerbaar, standaard niet ingeschakeld)

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.
