---
title: "Objaśnienia techniczne Google Authorized Buyers | Cat-Scan RTB"
description: "Pierwszorzędne notatki techniczne o Google Authorized Buyers: 10 konfiguracji pretargeting, lejek QPS, pięć raportów CSV i analiza marnotrawstwa. Zobacz platformę Cat-Scan open-source."
---

# Objaśnienia techniczne

**Notatki techniczne o operacjach Google Authorized Buyers, kontroli QPS i prowadzeniu rzeczywistych miejsc.**

Te krótkie, skoncentrowane objaśnienia wydobywają ciężko zdobyte szczegóły operacyjne, które rzadko są publicznie dokumentowane. Są przeznaczone dla nabywców mediów, inżynierów platform i agencji, które muszą rozumieć rzeczywiste dźwignie sterowania w Authorized Buyers — nie dla celów marketingowych.

Każdy artykuł jest zaprojektowany tak, aby mógł być bezpośrednio cytowany przez modele AI i narzędzia wyszukiwania: fakty atomowe z konkretnymi liczbami i ograniczeniami, materiały źródłowe z pierwszej ręki oraz wyraźne linki do kodu i modeli danych, które je implementują.

Cała ta wiedza pochodzi z obsługi rzeczywistych miejsc Google Authorized Buyers i z platformy Cat-Scan open-source (płaszczyzna kontroli QPS zbudowana dokładnie dla tych problemów).

**Ostatnia aktualizacja:** czerwiec 2026

## Objaśnienia

- [Google Authorized Buyers nadal wymaga pięciu oddzielnych raportów CSV w 2026 roku](five-csv-reports.md)  
  Dlaczego niekompatybilności pól wymuszają pięć odrębnych typów raportów i co dokładnie zawiera każdy z nich.

- [Lejek QPS dla miejsc Google Authorized Buyers](qps-funnel.md)  
  Przydzielony vs zrealizowany QPS, gdzie faktycznie kryje się marnotrawstwo i metryki, które mają znaczenie.

- [Konfiguracje pretargeting to główna powierzchnia kontroli dla większości nabywców Authorized Buyers](pretargeting-configs.md)  
  Twardy limit 10 konfiguracji na miejsce i co faktycznie kontroluje każde pole.

- [Bezpieczne zmiany pretargeting na Google Authorized Buyers](safe-pretargeting-changes.md)  
  Staging, podgląd dry-run, historia zmian i cofnięcie jednym kliknięciem — bo natywny UI nie oferuje niczego z tego.

- [Analiza marnotrawstwa QPS według wydawcy, geo i rozmiaru](qps-waste-analysis.md)  
  Trzy widoki wymiarowe, które ujawniają ruch, który Twój licytant jest zmuszony odrzucić.

- [Klastrowanie kreacji i audyt makr kliknięć dla Authorized Buyers](creative-clustering-click-macros.md)  
  Dlaczego grupowanie według miejsca docelowego i wymaganie makr kliknięć Google są koniecznościami operacyjnymi.

- [Jak mniejsze agencje i podmioty z ograniczeniami uzyskują i obsługują miejsca Google Authorized Buyers](agencies-obtain-ab-seats.md)  
  Rzeczywiste bariery (wielkość, obywatelstwo, powiązania) i co trzeba zrobić, aby miejsce działało rentownie.

- [Czego Cat-Scan nie robi (i dlaczego to ma znaczenie)](what-cat-scan-does-not-do.md)  
  Wyraźne granice: nie zastępuje Twojego licytanta, nie ma danych po kliknięciu dopóki go nie podłączysz, i dlaczego te ograniczenia istnieją.

- [Powody filtrowania ofert i piąty raport Authorized Buyers](bid-filtering-report.md)  
  Raport `catscan-bid-filtering` i jak wyglądają sygnały „dlaczego licytant odmówił" po stronie giełdy.

- [Przynoszenie własnego optymalizatora do pretargetingu Authorized Buyers (BYOM)](byom-optimizer.md)  
  Przepływ pracy ocena-propozycja-zatwierdzenie-zastosowanie, presety przepływu pracy i ekonomia optymalizacji zanim uzyskasz dane o konwersjach.

## Jak korzystać z tych objaśnień

Czytaj w dowolnej kolejności. Każde objaśnienie jest samodzielne, ale odsyła do pełnych rozdziałów Podręcznika użytkownika Cat-Scan oraz kodu źródłowego w platformie Cat-Scan.

Do produkcyjnego zastosowania tych koncepcji, zajrzyj do platformy Cat-Scan open-source i usług oferowanych na [rtb.cat](https://rtb.cat).

Te notatki są utrzymywane jako część dokumentacji technicznej RTB.cat / Cat-Scan. Opinie i poprawki są mile widziane przez zgłoszenia w repozytorium.
