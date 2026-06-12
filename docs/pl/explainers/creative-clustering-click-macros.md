---
title: "Klastrowanie kreacji i makra kliknięć: Authorized Buyers"
description: "Google wymaga makra kliknięć na każdej kreacji; Cat-Scan audytuje brakujące makra i klastruje kreacje według docelowego URL, aby wykryć niedopasowania geo i języka."
---

# Klastrowanie kreacji i audyt makr kliknięć dla Authorized Buyers

Dwa problemy higieny operacyjnej, które stają się kosztowne na dużą skalę: niedopasowane kreacje i brakujące makra kliknięć.

## Klastrowanie kreacji według miejsca docelowego

Google Authorized Buyers raportuje wydajność na poziomie Creative ID. Gdy masz setki lub tysiące kreacji, potrzebujesz sposobu na zrozumienie „dla której kampanii to faktycznie jest?"

Cat-Scan automatycznie klastruje kreacje według wzorców docelowego URL. Ujawnia to:
- Wiele kreacji wskazujących na tę samą ofertę (zamierzone lub przypadkowe nakładanie się).
- Koncentrację wydatków na małej liczbie prawdziwych kampanii.
- Kreacje, które są osierocone (brak pasującej logiki kampanii po stronie licytanta).

Możesz również ręcznie tworzyć klastry i używać automatycznego klastrowania wspomaganego przez AI.

**Fakt atomowy:** Klastrowanie według docelowego URL działa nawet wtedy, gdy licytant używa różnych ID kampanii lub gdy raportowanie Google nie ujawnia wewnętrznej struktury licytanta.

## Wykrywanie niedopasowań geo / języka

Częsty i kosztowny błąd: kreacja zlokalizowana dla jednego rynku jest wyświetlana w innym.

Przykład: Kreacja z arabskim tekstem i przyciskiem „Zainstaluj" po hiszpańsku wyświetlana w ZEA, lub cena w USD pokazywana użytkownikom na rynku, który używa innej waluty.

Opcjonalna analiza kreacji AI Cat-Scan (obsługuje Gemini, Claude lub Grok) odczytuje obraz kreacji + tekst i oznacza niedopasowania względem rzeczywistych krajów wyświetlania zgłoszonych w danych wydajności.

Ta funkcja jest celowo opcjonalna i domyślnie wyłączona w produkcji, ponieważ wymaga wyraźnej konfiguracji dostawcy LLM.

## Zgodność makr kliknięć

Google wymaga, aby klikalne URL obsługiwały makro `{clickurl}` lub równoważne, tak aby Google mógł prawidłowo śledzić i przypisywać kliknięcia.

Wiele kreacji jest przesyłanych bez makra lub z makrem w niewłaściwym miejscu.

Cat-Scan ma dedykowany widok audytu makr kliknięć, który pokazuje dokładnie, które kreacje mają brakujące wymagane makro.

Nieprzejście tego audytu to szybki sposób na utratę kredytów za kliknięcia lub wywołanie problemów ze zgodnością.

## Dlaczego te sprawdzenia mają znaczenie

Problemy z kreacjami to ciche zabójcy:
- Płacisz za QPS, który generuje wyświetlenia dla niewłaściwej grupy odbiorców.
- Tracisz atrybucję i dlatego nie możesz optymalizować.
- Ryzykujesz problemy na poziomie konta, jeśli makra systematycznie brakuje.

To właśnie takie szczegóły odróżniają zespoły, które prowadziły rzeczywiste miejsca, od zespołów, które tylko konfigurowały DSP.

## Powiązane

- [Zarządzanie kreacjami](../05-managing-creatives.md) w podręczniku
- Trasy audytu i klastrowania kreacji w Cat-Scan
- Kod analizy niedopasowań języka / geo AI żyje na platformie Cat-Scan (konfigurowalny, domyślnie nieaktywny)

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.
