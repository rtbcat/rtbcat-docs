---
title: "Analiza marnotrawstwa QPS według geo, wydawcy, rozmiaru | Cat-Scan"
description: "Google wysyła ponad 300 rozmiarów reklam i tysiące wydawców; większość z nich nie ma żadnych pasujących kreacji ani ofert. Trzy widoki Cat-Scan zamieniają marnotrawstwo QPS w listy wykluczeń."
---

# Analiza marnotrawstwa QPS według wydawcy, geo i rozmiaru w Authorized Buyers

**Fakt atomowy:** Google wysyła Ci setki rozmiarów reklam i tysiące wydawców. Większość z nich ma zerowe pasujące kreacje lub zerowe oferty od Twojego licytanta.

Trzy widoki wymiarów w Cat-Scan (geo, wydawca, rozmiar) zamieniają surowe liczby lejka w możliwe do zastosowania listy wykluczeń.

## Trzy widoki

### Marnotrawstwo geograficzne

Pokazuje QPS, oferty, wygrane, wydatki i wskaźnik marnotrawstwa według kraju i miasta.

Typowe ustalenia:
- Duży QPS z krajów, w których nie masz kreacji ani budżetu.
- Miasta otrzymujące nieproporcjonalny wolumen, ale prawie żadnych wygranych.
- Całe regiony, które licytant całkowicie ignoruje.

Działanie: Dodaj najgorsze geo do listy wykluczeń odpowiedniej konfiguracji pretargetingu.

### Marnotrawstwo wydawcy

Klasyfikuje domeny i pakiety aplikacji według otrzymanego wolumenu vs złożonych ofert i wydatków.

Typowe ustalenia:
- Wydawcy o wysokim QPS, gdzie licytant składa oferty na <5% żądań.
- Aplikacje dostarczające wolumen, ale zero wygranych (często z powodu ceny minimalnej lub niedopasowania kreacji).
- Długi ogon zasobów o niskiej jakości, który nadal zużywa Twoje przydzielone QPS.

Działanie: Użyj edytora wydawców dla każdej konfiguracji, aby zablokować najgorszych. To zdecydowanie łatwiejsze niż tańce z szablonami CSV Google.

**Fakt atomowy:** Edytor blokowania/zezwolenia wydawców Cat-Scan działa dla każdej konfiguracji pretargetingu i obsługuje wyszukiwanie + masowe zmiany z podglądem.

### Marnotrawstwo rozmiaru

Google chętnie wysyła Ci ponad 300 różnych rozmiarów reklam, nawet jeśli masz kreacje tylko dla kilku.

Typowe ustalenie: 80%+ QPS w rozmiarach, dla których w ogóle nie masz kreacji.

Działanie: Wyraźnie wymień w konfiguracji pretargetingu tylko te rozmiary, które faktycznie obsługujesz. To jedna z najbardziej opłacalnych pojedynczych zmian, jakie może wprowadzić większość nowych miejsc.

## Jak dane są budowane

Wszystkie trzy widoki są obliczane z połączonego zestawu danych pięciu raportów po imporcie. Do samej analizy nie są wymagane żadne dodatkowe wywołania API Google (synchronizacja pretargetingu jest oddzielna).

Te same dane zasilają lejek na stronie głównej i propozycje optymalizatora.

## Dlaczego ta analiza jest rzadka

Większość agencji nigdy nie widzi tych podziałów, ponieważ nigdy nie łączy pięciu plików CSV i nigdy nie buduje agregatów dla każdego wymiaru. Patrzą na wysokopoziomowe raporty wydajności, które Google wysyła e-mailem, i zakładają, że „licytant to posortuje."

Licytant może posortować tylko to, co do niego faktycznie dociera. Wszystko, co do niego dociera, ale jest odrzucane, już kosztowało Cię przydział QPS i infrastrukturę.

## Powiązane

- [Lejek QPS](qps-funnel.md)
- [Konfiguracje pretargetingu](pretargeting-configs.md)
- [Bezpieczne zmiany pretargetingu](safe-pretargeting-changes.md)
- Pełne omówienie w podręczniku: [Analiza marnotrawstwa według wymiarów](../04-analyzing-waste.md)

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.  
Te trzy widoki są dostępne na żywo w każdym wdrożeniu Cat-Scan.
