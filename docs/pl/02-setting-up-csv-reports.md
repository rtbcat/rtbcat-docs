---
title: "Raporty CSV Authorized Buyers: 5 raportów dla Cat-Scan"
description: "Google Authorized Buyers nie ma API raportowania, więc Cat-Scan odbudowuje lejek z pięciu zaplanowanych raportów CSV. Pełne metryki i wymiary oraz instrukcja konfiguracji."
---

# Konfiguracja raportów CSV

*Odbiorcy: nabywcy mediów, menedżerowie kont*

Zanim Cat-Scan będzie mógł cokolwiek analizować, potrzebuje danych. Google Authorized Buyers
nie ma API raportowania, więc wszystkie dane przepływają przez **pięć zaplanowanych raportów CSV**,
które tworzysz jednorazowo na swoim koncie Google AB.

!!! warning "Dlaczego pięć oddzielnych raportów?"
    Kolumny raportowania Google nie są ze sobą wszystkie kompatybilne. Na przykład
    „Bid requests" nie może pojawić się w tym samym raporcie co „Mobile app ID"
    lub „Creative ID + Billing ID". Aby uzyskać pełną widoczność lejka, potrzebnych jest pięć
    raportów, które Cat-Scan łączy automatycznie.

## Pięć raportów w skrócie

| # | Nazwa raportu | Co przekazuje Cat-Scan | Kluczowe kolumny |
|---|---------------|------------------------|------------------|
| 1 | **Quality** | Wydajność na poziomie kreacji z widocznością | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Lejek ofert na poziomie kreacji (bids -> wins) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Pełny lejek bidstream według kraju | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Pełny lejek bidstream według wydawcy | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Dlaczego Google odrzuca Twoje oferty | Filtering reason, Bids, Opportunity cost |

---

## Kompletny przewodnik po metrykach

Każda metryka, którą Cat-Scan przetwarza, jej znaczenie i który raport ją zawiera.

### Metryki lejka (potok bidstream)

Śledzą one postęp żądania oferty przez system aukcyjny Google.
Dostępne w raportach **Pipeline -- Geo** i **Pipeline -- Publisher**.

| Metryka | Definicja | Jednostka | Raporty |
|---------|-----------|-----------|---------|
| **Bid requests** | Łączna liczba żądań ofert wysłanych przez Google do Twojego endpointu licytującego. To surowy wolumen przychodzący — szczyt lejka. Obejmuje żądania, na które Twój licytant mógł nie odpowiedzieć na czas. | liczba | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Żądania ofert, które faktycznie dotarły do Twojego licytanta i uzyskały odpowiedź (pomyślną lub nie). Niższe niż „Bid requests", jeśli Twój licytant ma problemy z opóźnieniami lub przekroczeniami czasu. | liczba | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Żądania, dla których Twój licytant znalazł pasujące zasoby reklamowe (kreację pasującą do żądania). To pierwszy filtr: jeśli nie masz kreacji dla żądanego rozmiaru/formatu, tu się kończy. | liczba | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Żądania, dla których Twój licytant zwrócił prawidłową, możliwą do przetworzenia odpowiedź na ofertę (HTTP 200 z poprawnie sformułowaną ofertą). Wyklucza przekroczenia czasu, błędy i odpowiedzi bez oferty. | liczba | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Faktyczne odpowiedzi ofertowe złożone przez Twojego licytanta. Podzbiór pomyślnych odpowiedzi — Twój licytant może odpowiedzieć pomyślnie, ale wybrać, że nie złoży oferty (odpowiedź bez oferty). | liczba | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Oferty zaakceptowane przez Google do aukcji. Oferty mogą być odrzucone przed wejściem do aukcji z powodu reguł filtrowania (odrzucenie kreacji, naruszenia zasad, cena minimalna, wykluczenia pretargeting). Różnica między „Bids" a „Bids in auction" jest widoczna w raporcie Bid Filtering. | liczba | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Oferty, które wygrały aukcję. Za nie płacisz. Różnica między „Bids in auction" a „Auctions won" to konkurencja — inni kupujący przelicytowali Cię. | liczba | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Reklamy faktycznie wyświetlone w przeglądarce lub aplikacji użytkownika po wygraniu aukcji. Nieco mniej niż „Auctions won" z powodu błędów renderowania reklam, nawigacji po stronie przed renderowaniem i interferencji blokady reklam. | liczba | Wszystkie pięć raportów |
| **Clicks** | Interakcje użytkowników (kliknięcia/dotknięcia) z wyświetlanymi reklamami. | liczba | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Metryki wydatków i kosztów

| Metryka | Definicja | Jednostka | Raporty |
|---------|-----------|-----------|---------|
| **Spend** | Łączna kwota wydana na wygranych wyświetleniach w danym okresie. To Twój rzeczywisty koszt mediów. Wyrażony w walucie Twojego konta (zazwyczaj USD). | waluta (mikro w surowych danych, dolary w UI) | Quality |
| **Opportunity cost** | Szacunkowy przychód utracony, ponieważ Google odfiltrował Twoje oferty zanim weszły do aukcji. Obliczany przez Google na podstawie historycznych wskaźników wygranych i CPM dla podobnych zasobów. Przydatny do ustalania priorytetów, które powody filtrowania naprawić w pierwszej kolejności. | waluta | Bid Filtering |

### Metryki jakości i widoczności

To metryki na poziomie kreacji z raportu **Quality**. Mierzą,
co dzieje się *po* wyświetleniu reklamy.

| Metryka | Definicja | Jednostka | Raporty |
|---------|-----------|-----------|---------|
| **Active View viewable** | Wyświetlenia, które spełniły standard widoczności MRC: co najmniej 50% pikseli reklamy znajdowało się w widocznym obszarze przeglądarki przez co najmniej 1 ciągłą sekundę (2 sekundy dla wideo). To branżowy standard dla „czy ta reklama faktycznie była widoczna". | liczba | Quality |
| **Active View measurable** | Wyświetlenia, dla których widoczność *mogła* być zmierzona. Niektóre środowiska (określone aplikacje, ramki iframe z różnych domen, starsze przeglądarki) blokują pomiar. Wskaźnik widoczności = Active View viewable / Active View measurable. | liczba | Quality |
| **Video starts** | Liczba razy, gdy kreacja wideo zaczęła się odtwarzać. Wypełniane tylko dla kreacji w formacie wideo. | liczba | Quality |
| **Video completions** | Liczba razy, gdy kreacja wideo odtworzyła się do 100% ukończenia (lub do punktu pomijania, jeśli można pominąć). Wskaźnik ukończenia wideo = completions / starts. | liczba | Quality |

### Metryki filtrowania ofert

Z raportu **Bid Filtering**. Informują, *dlaczego* oferty są
odrzucane zanim wejdą do aukcji.

| Metryka | Definicja | Jednostka | Raporty |
|---------|-----------|-----------|---------|
| **Bids** | Łączna liczba ofert złożonych przez Twojego licytanta (ta sama definicja co powyżej). W tym raporcie używana jako mianownik do obliczania wskaźników filtrowania. | liczba | Bid Filtering |
| **Bids in auction** | Oferty, które przeżyły filtrowanie i weszły do aukcji. `Bids - Bids in auction` = łączna liczba odfiltrowanych ofert. | liczba | Bid Filtering |
| **Opportunity cost** | Patrz metryki wydatków powyżej. W tym raporcie w podziale na powód filtrowania, abyś mógł zobaczyć, który powód kosztuje Cię najwięcej. | waluta | Bid Filtering |

### Wymiary (kolumny grupowania)

Wymiary to nie metryki — to osie, według których metryki są
rozkładane. Cat-Scan używa ich do fragmentowania danych.

| Wymiar | Co to jest | Które raporty |
|--------|-----------|---------------|
| **Day** | Data kalendarzowa (UTC). Wymagana we wszystkich raportach. Cat-Scan używa tego do deduplikacji i wyświetlania szeregów czasowych. | Wszystkie pięć |
| **Hour** | Godzina dnia (0--23, UTC). Umożliwia godzinową granularność w analizie potoku. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Dwuliterowy kod kraju ISO (np. US, DE, IL). Geograficzne pochodzenie żądania oferty. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (opcjonalnie) |
| **Billing ID (Pretargeting config)** | Numeryczny ID konfiguracji pretargeting, która zaakceptowała ten ruch. Mapuje 1:1 do karty konfiguracji w Cat-Scan. | Quality |
| **Creative ID** | Numeryczny ID Google dla zasobu kreacji. Łączy się z galerią kreacji w Cat-Scan. | Quality, Bids in Auction, Bid Filtering (opcjonalnie) |
| **Creative size** | Wymiary w pikselach kreacji (np. `300x250`, `728x90`). Używany do analizy marnotrawstwa według rozmiaru. | Quality |
| **Creative format** | Format reklamy: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (opcjonalnie) |
| **Platform** | Platforma urządzenia: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (opcjonalnie) |
| **Environment** | Gdzie reklama była wyświetlana: `WEB`, `APP`. | Quality (opcjonalnie) |
| **App ID** | Identyfikator pakietu aplikacji mobilnej (np. `com.example.app`). Wypełniane tylko dla zasobów reklamowych w aplikacji. | Quality (opcjonalnie) |
| **App name** | Czytelna dla człowieka nazwa aplikacji. | Quality (opcjonalnie) |
| **Publisher ID** | Numeryczny ID wydawcy (strony internetowej lub aplikacji). | Quality (opcjonalnie), Pipeline -- Publisher |
| **Publisher name** | Czytelna dla człowieka nazwa wydawcy. | Quality (opcjonalnie), Pipeline -- Publisher |
| **Publisher domain** | Domena strony internetowej wydawcy (np. `news.example.com`). | Quality (opcjonalnie) |
| **Buyer account ID** | ID Twojego konta kupującego / miejsca. Potrzebne, gdy prowadzisz wiele miejsc. | Bids in Auction, Bid Filtering (opcjonalnie) |
| **Filtering reason** | Kod powodu odrzucenia oferty przez Google przed wejściem do aukcji (np. `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Krok po kroku: tworzenie każdego raportu

### 1. Raport Quality

To Twój raport wydajności na poziomie kreacji z danymi o widoczności i wydatkach.

**W Google Authorized Buyers -> Reporting -> New Report:**

| Ustawienie | Wartość |
|------------|---------|
| Report type | RTB |
| Time range | Yesterday (zaplanowane codziennie) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Sugerowana nazwa pliku:** `catscan-quality`

!!! note
    Ten raport **nie** może zawierać „Bid requests", „Bids" ani
    „Bids in auction" — te kolumny są niekompatybilne z „Billing ID" w raportowaniu Google.

---

### 2. Raport Bids in Auction

Ten raport przechwytuje lejek ofert na poziomie kreacji, wypełniając
metryki, których raport Quality nie może zawierać.

| Ustawienie | Wartość |
|------------|---------|
| Report type | RTB |
| Time range | Yesterday (zaplanowane codziennie) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Sugerowana nazwa pliku:** `catscan-bidsinauction`

!!! info "Jak Cat-Scan łączy te raporty"
    Quality + Bids in Auction są łączone po `(Day, Creative ID)`, aby dać
    pełny obraz: od złożonych ofert przez wyświetlone reklamy i poniesione wydatki.

---

### 3. Raport Pipeline -- Geo

To Twój raport z góry lejka: ile żądań ofert Google wysyła Ci
według kraju i ile przeżywa każdy etap lejka.

| Ustawienie | Wartość |
|------------|---------|
| Report type | RTB |
| Time range | Yesterday (zaplanowane codziennie) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Sugerowana nazwa pliku:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **Nie** dodawaj Creative ID, Billing ID ani App ID do tego raportu. Te
    kolumny są niekompatybilne z „Bid requests".

---

### 4. Raport Pipeline -- Publisher

Taki sam jak Pipeline -- Geo, ale w podziale według wydawcy zamiast (lub
oprócz) geografii.

| Ustawienie | Wartość |
|------------|---------|
| Report type | RTB |
| Time range | Yesterday (zaplanowane codziennie) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Sugerowana nazwa pliku:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Raport Bid Filtering

Ten raport pokazuje, *dlaczego* Google filtruje Twoje oferty przed wejściem do
aukcji — kluczowe do diagnozowania problemów z pretargetingiem.

| Ustawienie | Wartość |
|------------|---------|
| Report type | RTB |
| Time range | Yesterday (zaplanowane codziennie) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Sugerowana nazwa pliku:** `catscan-bid-filtering`

### Typowe powody filtrowania

To wartości, które zobaczysz w wymiarze **Filtering reason**. Każda
informuje o konkretnym powodzie odrzucenia oferty przez Google przed wejściem do aukcji.

| Powód filtrowania | Co oznacza | Co zrobić |
|-------------------|-----------|-----------|
| `CREATIVE_NOT_APPROVED` | Kreacja nie przeszła recenzji Google lub została odrzucona | Sprawdź status kreacji w Google AB. Napraw naruszenia zasad. |
| `BID_BELOW_AUCTION_FLOOR` | Cena Twojej oferty była poniżej minimalnego CPM wydawcy | Podnieś ofertę lub wyklucz zasoby o niskiej wartości przez pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | Zasady Google na poziomie giełdy zablokowały ofertę | Przejrzyj zasady reklamowe Google dla konkretnej kreacji |
| `FILTERED_BY_PRETARGETING` | Twoje własne reguły pretargeting wykluczyły ten ruch | Celowe, jeśli Twoje reguły są poprawne; sprawdź, jeśli nieoczekiwane |
| `NO_MATCHING_CREATIVE` | Żądanie oferty wymagało rozmiaru/formatu, którego nie masz | Prześlij kreacje dla brakujących rozmiarów lub wyklucz te rozmiary w pretargetingu |
| `CREATIVE_SIZE_MISMATCH` | Wymiary kreacji nie pasują do miejsca reklamy | Sprawdź rozmiar kreacji względem tego, o co prosi wydawca |
| `LANDING_PAGE_DISAPPROVED` | Docelowy URL nie przeszedł recenzji Google | Napraw stronę docelową lub użyj innego URL |
| `SSL_REQUIRED` | Wydawca wymaga HTTPS, ale Twoja kreacja lub strona docelowa używa HTTP | Przełącz wszystkie zasoby i URL na HTTPS |
| `FREQUENCY_CAPPED` | Użytkownik widział już tę kreację zbyt wiele razy | Oczekiwane zachowanie; dostosuj limity częstotliwości, jeśli są zbyt agresywne |

---

## Planowanie dostarczania

Dla każdego z pięciu raportów:

1. Kliknij **Schedule** w Google Authorized Buyers.
2. Ustaw częstotliwość na **Daily**.
3. Ustaw metodę dostarczania:
      - **Email** — wyślij na konto Gmail połączone z Cat-Scan (umożliwia
        automatyczny import). Zobacz [Import danych](09-data-import.md) w celu
        konfiguracji automatycznego importu Gmail.
      - **Manual** — jeśli wolisz pobierać i przesyłać pliki CSV samodzielnie przez
        `/import`.

!!! tip "Użyj automatycznego importu Gmail"
    Zaplanowanie wszystkich pięciu raportów do wysyłania e-mailem na połączone konto Gmail oznacza,
    że Cat-Scan importuje je automatycznie każdego dnia. Po początkowej konfiguracji
    nie są potrzebne ręczne przesyłanie.

## Weryfikacja konfiguracji

Po zaimportowaniu pierwszego zestawu plików CSV (ręcznie lub przez Gmail):

1. Przejdź do `/import` w Cat-Scan.
2. Sprawdź **Data Freshness Grid** — powinieneś zobaczyć „imported" dla wszystkich pięciu
   typów raportów dla daty wczorajszej.
3. Jeśli którekolwiek komórki pokazują „missing", odpowiedni raport nie został jeszcze odebrany.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Gdy wszystkie pięć kolumn pokaże zielony dla wczoraj, Cat-Scan ma pełne dane i
każda funkcja (lejek, analiza marnotrawstwa, rekomendacje, optymalizator) będzie działać.

## Automatyczne wykrywanie

Nie musisz informować Cat-Scan, który raport przesyłasz. System importu
wykrywa typ raportu automatycznie na podstawie nagłówków kolumn:

- Ma **Bid filtering reason**? -> Bid Filtering
- Ma **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- Ma **Bid requests** (bez Publisher ID)? -> Pipeline -- Geo
- Ma **Creative ID** + **Billing ID**? -> Quality
- Ma **Creative ID** + **Bids in auction**? -> Bids in Auction

## Jak Cat-Scan używa każdej metryki

Mapuje surowe metryki CSV na to, co widzisz w UI Cat-Scan.

| Funkcja UI | Używane metryki | Raporty źródłowe |
|-----------|----------------|-----------------|
| **Lejek QPS** (strona główna) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (oba) + Quality |
| **Obliczanie % marnotrawstwa** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Win rate** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Dowolny raport z obydwoma |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Wskaźnik widoczności** | `Active View viewable / Active View measurable` | Quality |
| **Wskaźnik ukończenia wideo** | `Video completions / Video starts` | Quality |
| **Analiza marnotrawstwa geo** (`/qps/geo`) | Bid requests, Impressions, Spend według Country | Pipeline -- Geo + Quality |
| **Marnotrawstwo wydawcy** (`/qps/publisher`) | Bid requests, Impressions, Spend według Publisher | Pipeline -- Publisher + Quality |
| **Marnotrawstwo rozmiaru** (`/qps/size`) | Impressions, Spend według Creative size | Quality |
| **Powody filtrowania** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost według Filtering reason | Bid Filtering |
| **Metryki karty konfiguracji** | Reached queries, Impressions, Spend według Billing ID | Quality |
| **Wydajność kreacji** | Impressions, Clicks, Spend, Active View viewable na Creative ID | Quality |
| **Punktacja optymalizatora** | Wszystkie metryki potoku + jakości, zagregowane według segmentu | Wszystkie pięć |

## Typowe błędy

| Błąd | Co się dzieje | Naprawa |
|------|--------------|---------|
| Dodanie „Bid requests" do raportu Quality | Google zwraca błąd lub niepełne dane | Usuń „Bid requests" — jest niekompatybilny z „Billing ID" |
| Pominięcie raportu Bid Filtering | Cat-Scan nie może pokazać, *dlaczego* oferty są odrzucane | Utwórz 5. raport z wymiarem „Filtering reason" |
| Użycie „Last 7 days" zamiast „Yesterday" | Nakładające się dane, większe pliki, wolniejszy import | Ustaw na „Yesterday" i zaplanuj codziennie |
| Brak planowania — tylko ręczne eksporty | Dane tracą aktualność, sprawdzenia stanu nie przechodzą | Zaplanuj codzienne dostarczanie przez e-mail |
| Brak wymiaru „Hour" w raportach Pipeline | Brak godzinowej granularności w analizie QPS | Dodaj Hour do Pipeline -- Geo i Pipeline -- Publisher |
| Brak opcjonalnych metryk w raporcie Quality | Brak danych widoczności lub wideo w Cat-Scan | Dodaj Active View viewable, Active View measurable, Video starts, Video completions |

## Kolejne kroki

- [Nawigacja administracyjna](02-navigating-the-dashboard.md): układ paska bocznego i
  lista kontrolna konfiguracji
- [Import danych](09-data-import.md): szczegółowa mechanika importu, przesyłanie
  porcjami i rozwiązywanie problemów
- [Lejek QPS](03-qps-funnel.md): gdy dane już płyną, zacznij analizować
