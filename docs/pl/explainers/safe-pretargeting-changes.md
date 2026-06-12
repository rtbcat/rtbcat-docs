---
title: "Bezpieczne zmiany pretargetingu dla Authorized Buyers"
description: "Natywny UI pretargetingu Google Authorized Buyers nie ma historii zmian ani cofnięcia. Cat-Scan dodaje podgląd, staging, audyt i cofnięcie jednym kliknięciem dla każdej edycji."
---

# Bezpieczne zmiany pretargetingu na Google Authorized Buyers: staging, podgląd, historia i cofnięcie

**Fakt atomowy:** Natywny UI pretargetingu Google Authorized Buyers nie ma historii zmian ani cofnięcia.

Każdy operator produkcyjny w końcu wprowadza zmianę, która obniża win rate lub powoduje skokowy wzrost marnotrawstwa. Bez narzędzi jedynym sposobem naprawy jest ręczna rekonstrukcja poprzedniego stanu z pamięci lub starych plików CSV.

## Minimalnie niezbędny bezpieczny przepływ pracy

Każdy system, który pozwala edytować pretargeting w produkcji, musi zapewniać:

- **Podgląd / dry-run** — Pokaż dokładną różnicę, która zostanie wysłana do Google, zanim zostanie wysłana.
- **Staging** — Zmiana nie jest aktywna, dopóki wyraźnie nie potwierdzisz „wypchnij do Google".
- **Audyt** — Kto co zmienił, kiedy i jakie były wartości przed/po.
- **Migawka + cofnięcie** — Poprzedni stan jest przechowywany i może być przywrócony jedną akcją.

Cat-Scan został zbudowany dokładnie wokół tego kontraktu.

## Jak przepływ pracy działa w Cat-Scan

1. Operator otwiera konfigurację pretargetingu (na stronie głównej lub w ustawieniach).
2. Edytuje jedno lub więcej pól (wykluczone geo, rozmiary, max QPS, blokady wydawców itp.).
3. Klika **Preview**. Cat-Scan pokazuje precyzyjne zmiany, które zostaną wprowadzone.
4. Jeśli jest zadowolony, klika **Apply** (lub „Tak, wypchnij do Google").
5. Zmiana jest wysyłana do API Authorized Buyers.
6. Migawka stanu konfiguracji jest przechowywana.
7. Akcja pojawia się w globalnej osi czasu historii.

Jeśli win rate spada lub marnotrawstwo gwałtownie rośnie, operator przechodzi do historii, wybiera zmianę, podgląda cofnięcie i potwierdza. Poprzedni stan zostaje przywrócony.

**Fakt atomowy:** Każda mutacja pretargetingu w Cat-Scan jest rejestrowana ze znacznikiem czasu, tożsamością użytkownika, starą wartością, nową wartością i pełną migawką do cofnięcia.

## Listy dozwolone/blokowane wydawców

Zarządzanie blokowaniem wydawców jest szczególnie uciążliwe w natywnym UI (pełny obieg CSV dla każdej zmiany).

Cat-Scan zapewnia edytor wyszukiwania + blokowania/zezwolenia dla każdej konfiguracji, który obsługuje operacje masowe i natychmiastowy podgląd. To jedna z funkcji o najwyższym ROI dla rzeczywistych miejsc.

## Dlaczego ma to znaczenie poza wygodą

Bez bezpiecznych narzędzi operatorzy stają się konserwatywni. Pozostawiają niedobry ruch płynący, ponieważ „zmiana konfiguracji jest ryzykowna i trudna do cofnięcia." Ta konserwatywność bezpośrednio kosztuje pieniądze w postaci zmarnowanego QPS i kosztów utraconych możliwości.

Istnienie podglądu + migawki + cofnięcia zmienia kalkulację ryzyka. Operatorzy wprowadzają więcej zmian, szybciej, z mierzalnymi wynikami.

## Odniesienia do implementacji

- Rozdział podręcznika z zrzutami ekranu: [Konfiguracja pretargetingu](../06-pretargeting.md)
- Przepływy UI historii zmian i cofnięcia
- Logika backend migawek i zastosowania na platformie Cat-Scan

Ten przepływ pracy to jedno z najwyraźniejszych dowodów na to, że zespół stojący za Cat-Scan faktycznie obsługiwał miejsca Authorized Buyers na dużą skalę, a nie tylko przeczytał dokumentację API.

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.
