---
title: "Raport filtrowania ofert: piąty plik CSV Authorized Buyers"
description: "Piąty raport, catscan-bid-filtering, to jedyne miejsce, gdzie Google informuje, dlaczego odrzucił ofertę zanim Twój licytant ją zobaczył. Odczytaj powody filtrowania po stronie giełdy."
---

# Powody filtrowania ofert i piąty raport Authorized Buyers

**Fakt atomowy:** Piąty raport (`catscan-bid-filtering`) to jedyne miejsce, gdzie Google informuje Cię, dlaczego odrzucił ofertę zanim w ogóle dotarła do Twojego licytanta.

Większość operatorów nigdy na niego nie patrzy, ponieważ przychodzi we własnym pliku CSV i domyślnie nie jest łączony z danymi o wydajności.

## Co zawiera raport filtrowania ofert

Ujawnia powody, dla których Google zastosował filtrowanie ofert po stronie giełdy dla żądań, które pasowały do Twojego pretargetingu, ale następnie zostały odfiltrowane przed wysłaniem.

Typowe kategorie obejmują:
- Niedopasowania kreacji lub rozmiaru (z perspektywy Google)
- Sygnały jakości wydawcy lub zasobów reklamowych
- Filtry częstotliwości lub inne filtry zasad
- Kwestie techniczne lub formatowe

Gdy jest połączony z pozostałymi czterema raportami, wyjaśnia część spadku z „reached queries" do „bids", który nie jest pod kontrolą Twojego licytanta.

## Dlaczego jest wartościowy

Twój licytant widzi tylko to, co Google faktycznie dostarcza. Raport filtrowania ofert to wgląd w ostatnią warstwę filtrowania, która miała miejsce po stronie Google.

Jeśli duża część potencjalnego wolumenu jest filtrowana z powodu „creative size not supported", poprawka jest zazwyczaj na Twojej liście rozmiarów pretargetingu, a nie w licytancie.

## Jak Cat-Scan go używa

Raport jest importowany do odpowiedniej tabeli. Jest dostępny do analizy obok widoków lejka i marnotrawstwa.

To jeden z sygnałów, które mogą być wprowadzone do niestandardowego optymalizatora (patrz objaśnienie BYOM).

## Powiązany kod i dokumentacja

- Tabela docelowa i cel w dokumentacji modelu danych platformy Cat-Scan
- Piąty raport jest częścią standardowego pięcioraportowego przepływu importu opisanego w rozdziale Import danych

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.
