---
title: "Pretargeting Authorized Buyers: 10 konfiguracji na miejsce"
description: "Masz dokładnie 10 konfiguracji pretargeting na miejsce Google Authorized Buyers — jedyna kontrola wolumenu po stronie giełdy. Zobacz każde pole i platformę Cat-Scan."
---

# Konfiguracje pretargeting to główna powierzchnia kontroli dla większości nabywców Authorized Buyers

**Fakt atomowy:** Masz dokładnie 10 konfiguracji pretargeting na miejsce Google Authorized Buyers.

Wszystko inne (logika licytanta, wybór kreacji, ograniczenie częstotliwości) następuje po tym, jak ruch już został do Ciebie wysłany. Pretargeting to jedyna kontrola wolumenu, którą masz po stronie giełdy.

## Co faktycznie kontroluje jedna konfiguracja pretargeting

Każda konfiguracja to zestaw reguł, który mówi Google: „wysyłaj mi tylko żądania ofert spełniające te kryteria."

| Pole                | Efekt                                                                 | Typowy błąd |
|---------------------|-----------------------------------------------------------------------|-------------|
| **State**           | Active lub Suspended                                                  | Pozostawianie martwych konfiguracji jako active |
| **Max QPS**         | Twardy limit zapytań na sekundę dla tego zestawu reguł               | Ustawianie zbyt wysoko „na wszelki wypadek" |
| **Geos (included)** | Kraje, regiony, miasta (tylko grube przedziały)                      | Poleganie wyłącznie na szerokim „Europa" lub „Azja" |
| **Geos (excluded)** | Wyraźne blokady, które zastępują włączenia                           | Niewystarczająco agresywne używanie wykluczeń |
| **Sizes (included)** | Konkretne rozmiary reklam lub „wszystkie"                            | „Wszystkie", gdy masz tylko kreacje o stałym rozmiarze |
| **Formats**         | VIDEO, DISPLAY_IMAGE, DISPLAY_HTML, NATIVE                           | Akceptowanie formatów, dla których nie masz kreacji |
| **Platforms**       | DESKTOP, MOBILE_APP, MOBILE_WEB, CONNECTED_TV                        | Wysyłanie ruchu z aplikacji mobilnych do kampanii tylko na desktop |
| **Publishers**      | Listy dozwolone/blokowane dla konkretnych domen lub pakietów aplikacji | Zarządzanie przez uciążliwy cykl przesyłania/pobierania CSV Google |

**Fakt atomowy:** Google nadal udostępnia tylko grube przedziały geograficzne (Wschodnie USA, Zachodnie USA, Europa, Azja itp.). Szczegółowe targetowanie na poziomie miasta lub DMA w pretargetingu nie jest dostępne.

## Dlaczego natywny UI jest uciążliwy

Interfejs pretargetingu Authorized Buyers wymaga pobrania szablonu CSV, edycji go offline i ponownego przesłania nawet dla zmiany jednej linii. Nie ma historii, podglądu wpływu ani łatwego cofnięcia.

To właśnie ten problem Cat-Scan został zbudowany, aby rozwiązać.

## Bezpieczny przepływ zmian (czego potrzebuje prawdziwy operator)

System klasy produkcyjnej, który pozwala edytować pretargeting w produkcji, musi obsługiwać:

1. Edycję w UI (lub przez API).
2. Dry-run / podgląd dokładnej różnicy przed wysłaniem czegokolwiek do Google.
3. Staging zmiany.
4. Rejestrację, kto co i kiedy zmienił (pełny audyt).
5. Cofnięcie jednym kliknięciem do dowolnej poprzedniej migawki.

Cat-Scan implementuje dokładnie ten przepływ na szczycie API Authorized Buyers. Zmiany są przeglądane, następnie wyraźnie wypychane, a następnie tworzą migawkę do natychmiastowego cofnięcia.

Zobacz pełny opis w rozdziale podręcznika i implementację na platformie.

## 10 konfiguracji to niewiele

Przy tylko dziesięciu slotach szybko uczysz się być bezwzględnym:

- Jedna lub dwie „szerokie, ale bezpieczne" konfiguracje dla sprawdzonego wolumenu.
- Kilka wąskich, precyzyjnych konfiguracji dla konkretnych kombinacji geo + rozmiary + formaty, gdzie masz silne pokrycie kreacjami.
- Zawieszone konfiguracje używane jako obszary staging przed awansem.

Cokolwiek, co aktywnie nie generuje ofert ani wydatków, zajmuje jeden z Twoich dziesięciu cennych slotów i powinno zostać zawieszone lub usunięte.

## Powiązane

- Pełne odniesienie do pól i zrzuty ekranu UI: [Konfiguracja pretargetingu](../06-pretargeting.md)
- Jak działać na podstawie sygnałów marnotrawstwa: [Analiza marnotrawstwa QPS według wymiarów](qps-waste-analysis.md)
- Implementacja bezpiecznych zmian na platformie Cat-Scan

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.  
Rzeczywistość 10 konfiguracji i potrzeba bezpiecznych narzędzi do edycji to powód istnienia Cat-Scan.
