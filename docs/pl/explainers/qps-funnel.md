---
title: "Lejek QPS dla Google Authorized Buyers | Cat-Scan"
description: "Miejsce żądające 50,000 QPS często otrzymuje znacznie mniej, a następnie licytant odrzuca większość tego, co faktycznie dociera. Zmapuj lejek QPS Authorized Buyers i wskaźnik marnotrawstwa z Cat-Scan."
---

# Lejek QPS dla miejsc Google Authorized Buyers

**Fakt atomowy:** Typowe miejsce żądające 50,000 QPS często otrzymuje znacznie mniej, a licytant następnie odrzuca większość tego, co faktycznie dociera.

Różnica między tym, o co poprosiłeś Google, aby wysłał, a tym, co Twój licytant faktycznie może wykorzystać, to centralny problem ekonomiczny prowadzenia miejsca Authorized Buyers.

## Etapy (co każda liczba faktycznie oznacza)

| Etap       | Definicja                                                                 | Kto płaci / kogo dotyczy          |
|------------|---------------------------------------------------------------------------|-----------------------------------|
| **QPS**    | Limit, który ustawiasz w pretargetingu. Google ogranicza przepustowość na podstawie poziomu Twojego konta i ostatnich wyników. | Ty płacisz za połączenie; Google decyduje, ile faktycznie przepływa |
| **Bid requests reached** | Zapytania, które faktycznie dotarły do Twojego endpointu | Koszt Twojej infrastruktury |
| **Bids**   | Żądania, na które Twój licytant zdecydował się złożyć ofertę             | Logika Twojego licytanta          |
| **Wins**   | Aukcje, które wygrałeś (płacisz tylko za te)                             | Twoje rzeczywiste wydatki na media |
| **Impressions** | Reklamy, które zostały wyświetlone po wygraniu                       | To, co użytkownik faktycznie zobaczył |
| **Clicks** | Interakcje użytkowników z Twoimi wyświetlonymi reklamami                 | Jakość kreacji + strony docelowej |
| **Spend**  | Pieniądze, które opuściły Twoje konto                                    | Jedyna liczba, która ostatecznie ma znaczenie |

**Fakt atomowy:** Największy pojedynczy spadek w większości miejsc następuje między QPS (lub dotartymi zapytaniami) a Bids. To marnotrawstwo, któremu Twoja konfiguracja pretargeting powinna zapobiegać.

## Wskaźnik marnotrawstwa

Wskaźnik marnotrawstwa = (QPS - Bids) / QPS

Jeśli Twój wskaźnik marnotrawstwa przekracza 50%, płacisz za wąż strażacki, który Twój licytant w większości ignoruje. Ten wolumen mógłby zostać przekierowany do konfiguracji, w których licytant faktycznie składa oferty i wygrywa.

Cat-Scan wyświetla to na stronie głównej jako główną diagnostykę.

## Dlaczego lejek jest trudniejszy w Authorized Buyers niż w większości DSP

- Jesteś ograniczony do 10 konfiguracji pretargeting na miejsce.
- Targetowanie geograficzne używa bardzo grubych przedziałów.
- Nie ma API raportowania w czasie rzeczywistym; wszystko pochodzi z pięciu dziennych plików CSV.
- Nie możesz zobaczyć „powodów braku oferty" po stronie licytanta, chyba że samodzielnie przetworzysz logi licytanta.

Google robi dużo filtrowania po swojej stronie, zanim ruch w ogóle do Ciebie dotrze. To, co pozostaje, nadal pełne jest szumów, które tylko Twoje reguły pretargetingu i pokrycie kreacjami mogą naprawić.

## Jak Cat-Scan sprawia, że lejek jest widoczny i możliwy do działania

- Odbudowuje pełny lejek z pięciu raportów.
- Rozkłada go według konfiguracji pretargetingu, geo, wydawcy, rozmiaru i kreacji.
- Pokazuje przydzielony QPS vs faktycznie zrealizowany wolumen na konfigurację.
- Pozwala edytować reguły pretargetingu kontrolujące górę lejka, z podglądem i możliwością cofnięcia.

Zobacz implementację na żywo w panelu Cat-Scan (strona główna + trasy `/qps/*`) i model danych zasilający obliczenia.

## Kluczowe metryki wywodzone z lejka

- Win rate = Wins / Bids
- CTR = Clicks / Impressions
- CPM (co faktycznie zapłaciłeś)
- Efektywne marnotrawstwo (QPS, o który prosiłeś, ale nigdy nie mogłeś zmonetyzować)

Gdy podłączysz dane po kliknięciu (AppsFlyer lub inne MMP), lejek zyskuje końcowy etap „zyskownego wyniku". Do tego czasu optymalizujesz na podstawie ofert + koncentracji wydatków + win rate.

## Powiązane

- [Rozumienie lejka QPS](../03-qps-funnel.md) (pełny rozdział podręcznika z zrzutami ekranu)
- [Analiza marnotrawstwa według wymiarów](qps-waste-analysis.md) w tych objaśnieniach
- [Konfiguracje pretargeting](pretargeting-configs.md)
- Logika optymalizacji używana w produkcji w repozytorium platformy Cat-Scan

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.  
Ten model lejka jest zaimplementowany i sprawdzony w produkcji na platformie Cat-Scan open-source.
