---
title: "QPS-trechter voor Google Authorized Buyers | Cat-Scan"
description: "Een AB-plaats die 50,000 QPS aanvraagt ontvangt vaak veel minder, waarna de biedmachine het meeste weigert. Breng de Authorized Buyers QPS-trechter en verspillingsverhouding in kaart met Cat-Scan."
---

# De QPS-trechter voor Google Authorized Buyers-plaatsen

**Atomair feit:** Een typische AB-plaats die 50,000 QPS aanvraagt ontvangt vaak veel minder, en vervolgens weigert de biedmachine het merendeel van wat daadwerkelijk aankomt.

De kloof tussen wat u Google heeft gevraagd te sturen en wat uw biedmachine werkelijk kan gebruiken, is het centrale economische probleem van het exploiteren van een Authorized Buyers-plaats.

## De fasen (wat elk getal werkelijk betekent)

| Fase       | Definitie                                                                 | Wie betaalt / wie het aangaat          |
|------------|---------------------------------------------------------------------------|----------------------------------------|
| **QPS**    | Het maximum dat u in pretargeting instelt. Google regelt de doorvoer op basis van uw accountniveau en recente prestaties. | U betaalt voor de verbinding; Google bepaalt hoeveel er daadwerkelijk doorstroomt |
| **Ontvangen biedverzoeken** | Queries die daadwerkelijk zijn aangekomen op uw eindpunt | Uw infrastructuurkosten |
| **Biedingen**   | Verzoeken waarvoor uw biedmachine heeft gekozen te bieden                | De logica van uw biedmachine           |
| **Gewonnen**    | Veilingen die u heeft gewonnen (alleen hier betaalt u voor)             | Uw werkelijke media-uitgaven           |
| **Impressies**  | Advertenties die zijn weergegeven na de overwinning                     | Wat de gebruiker werkelijk heeft gezien |
| **Klikken**     | Gebruikersinteracties met uw weergegeven advertenties                   | Kwaliteit van creative + landingspagina |
| **Uitgaven**    | Geld dat uw account heeft verlaten                                      | Het enige getal dat er uiteindelijk toe doet |

**Atomair feit:** De grootste enkele daling in de meeste AB-plaatsen is tussen QPS (of ontvangen queries) en Biedingen. Dit is de verspilling die uw pretargeting-configuratie geacht wordt te voorkomen.

## Verspillingsverhouding

Verspillingsverhouding = (QPS - Biedingen) / QPS

Als uw verspillingsverhouding boven de 50% ligt, betaalt u voor een waterslang die uw biedmachine grotendeels negeert. Dat volume had opnieuw kunnen worden toegewezen aan configuraties waar de biedmachine daadwerkelijk biedt en wint.

Cat-Scan toont dit op de startpagina als de primaire diagnose.

## Waarom de trechter in Authorized Buyers moeilijker is dan in de meeste DSP's

- U bent beperkt tot 10 pretargeting-configuraties per AB-plaats.
- Geografische targeting maakt gebruik van zeer grove segmenten.
- Er is geen realtime Reporting API; alles komt uit de vijf dagelijkse CSV's.
- U kunt "no-bid reasons" van de biedmachine-zijde niet zien, tenzij u zelf biedmachinelogboeken verwerkt.

Google doet veel filtering aan zijn kant voordat het verkeer u ooit bereikt. Wat er daarna overblijft zit nog steeds vol ruis die alleen uw pretargeting-regels en creatieve dekking kunnen oplossen.

## Hoe Cat-Scan de trechter zichtbaar en uitvoerbaar maakt

- Het reconstrueert de volledige trechter uit de vijf rapporten.
- Het splitst op pretargeting-configuratie, geo, uitgever, grootte en creative.
- Het toont toegewezen QPS versus daadwerkelijk gerealiseerd volume per configuratie.
- Het laat u de pretargeting-regels bewerken die de bovenkant van de trechter bepalen, met preview en terugdraaien.

Zie de live implementatie in het Cat-Scan dashboard (startpagina + `/qps/*`-routes) en het datamodel dat de berekeningen aanstuurt.

## Belangrijke metrics afgeleid van de trechter

- Winstpercentage = Gewonnen / Biedingen
- CTR = Klikken / Impressies
- CPM (wat u daadwerkelijk heeft betaald)
- Effectieve verspilling (de QPS die u heeft aangevraagd maar nooit kon monetariseren)

Wanneer u post-klik data aansluit (AppsFlyer of een andere MMP), krijgt de trechter een laatste fase "winstgevend resultaat". Tot die tijd optimaliseert u op biedingen + uitgavenconcentratie + winstpercentage.

## Gerelateerd

- [Uw QPS-trechter begrijpen](../03-qps-funnel.md) (volledig handboekhoofstuk met schermafbeeldingen)
- [Verspilling per dimensie analyseren](qps-waste-analysis.md) in deze toelichtingen
- [Pretargeting-configuraties](pretargeting-configs.md)
- Optimalisatielogica die in productie wordt gebruikt in de Cat-Scan platform-repository

**Laatste update:** juni 2026  
Onderdeel van de RTB.cat / Cat-Scan technische toelichtingen.  
Dit trechtermodel is geïmplementeerd en in de praktijk getest in het open-source Cat-Scan platform.
