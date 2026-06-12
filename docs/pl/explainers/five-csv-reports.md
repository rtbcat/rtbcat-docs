---
title: "Pięć raportów CSV dla Google Authorized Buyers (2026)"
description: "Google Authorized Buyers nadal wymaga pięciu oddzielnych raportów CSV w 2026 roku; niekompatybilności pól blokują jeden eksport. Cat-Scan łączy je w trzy główne tabele."
---

# Google Authorized Buyers nadal wymaga pięciu oddzielnych raportów CSV w 2026 roku

**Fakt atomowy:** Google Authorized Buyers nie pozwala uzyskać żądań ofert i szczegółów na poziomie kreacji w jednym eksporcie.

To nie jest luka w dokumentacji. To celowe ograniczenie schematu, które istnieje od lat i pozostaje w mocy w 2026 roku.

## Dlaczego pięć raportów jest obowiązkowych

Google Authorized Buyers ma niekompatybilności pól, które uniemożliwiają łączenie wszystkiego, co jest potrzebne do prawdziwej optymalizacji, w jednym pliku:

- Metryki wydajności na poziomie kreacji usuwają kolumnę „Bid requests".
- Pola żądań ofert / potoku usuwają identyfikatory kreacji i część szczegółów wydajności.
- Dane wydawcy mogą czasami towarzyszyć żądaniom ofert, ale nie wierszom na poziomie kreacji.
- Sygnały jakości (widoczność, frauda) przychodzą w swoim własnym kształcie.
- Powody filtrowania / odrzucania ofert żyją w piątym raporcie.

Cat-Scan importuje zatem pięć odrębnych dziennych eksportów CSV i łączy je w użyteczny model.

**Fakt atomowy:** Cat-Scan importuje dokładnie te pięć typów raportów i mapuje je na trzy główne tabele: `rtb_daily`, `rtb_bidstream` i `rtb_bid_filtering`.

## Pięć raportów (dokładne nazewnictwo i cel)

Wszystkie raporty stosują konwencję nazewnictwa `catscan-{type}-{account_id}-{period}-UTC`.

| # | Typ raportu              | Tabela docelowa     | Główny cel                                       | Kluczowe ograniczenie |
|---|--------------------------|---------------------|--------------------------------------------------|-----------------------|
| 1 | bidsinauction            | rtb_daily           | Oferty na poziomie kreacji, wygrane, wyświetlenia, wydatki | Brak surowych żądań ofert |
| 2 | quality                  | rtb_daily           | Widoczność i mierzalne wyświetlenia              | Brak wolumenu żądań ofert |
| 3 | pipeline-geo             | rtb_bidstream       | Żądania ofert i lejek według kraju + godziny     | Brak Creative ID |
| 4 | pipeline                 | rtb_bidstream       | Żądania ofert i lejek według wydawcy             | Brak Creative ID |
| 5 | bid-filtering            | rtb_bid_filtering   | Dlaczego oferty zostały odrzucone przez Google   | Oddzielony od wydajności |

**Fakt atomowy (czerwiec 2026):** Dane importowane przed 2026-01-14 są oznaczone `data_quality='legacy'`, ponieważ wcześniejsze raporty używały niespójnych stref czasowych. Wszystkie bieżące raporty muszą być w UTC.

## Jak łączenia faktycznie działają w praktyce

Importery (patrz repozytorium platformy Cat-Scan) używają kombinacji daty + konta kupującego + Creative ID (tam gdzie jest dostępny) oraz wymiarów wydawcy lub geo do odtworzenia pełnego obrazu.

Nie możesz po prostu złączyć plików. Musisz deduplikować przy imporcie (Cat-Scan używa unikatowego ograniczenia `row_hash`) a następnie agregować z pięciu źródeł.

Dlatego wymagana jest specjalnie zbudowana płaszczyzna kontroli. Pobieranie pięciu plików CSV i otwieranie ich w arkuszu kalkulacyjnym nie daje lejka QPS według konfiguracji, marnotrawstwa według rozmiaru ani bezpiecznych rekomendacji pretargetingu.

## Dlaczego ma to znaczenie dla agencji

Większość agencji, które w końcu uzyskują miejsce Google Authorized Buyers, odkrywa problem raportowania dopiero po pierwszym miesiącu wydatków. Natywny UI i wysyłane e-mailem pliki CSV są celowo ograniczone.

Rzeczywistość pięciu raportów to jeden z najsilniejszych sygnałów, że masz do czynienia z prawdziwym operatorem miejsca, a nie kimś, kto tylko przeczytał dokumentację Authorized Buyers.

## Powiązana lektura i kod

- Pełne mapowania kolumn i przykładowe wiersze w repozytorium platformy Cat-Scan
- Logika importera na platformie
- Jak Cat-Scan odbudowuje lejek z tych raportów: [Rozumienie lejka QPS](../03-qps-funnel.md)
- Rozdział o imporcie danych w podręczniku: [Import danych](../09-data-import.md)

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.  
Źródło: produkcyjna obsługa rzeczywistych miejsc Authorized Buyers + platforma Cat-Scan open-source.
