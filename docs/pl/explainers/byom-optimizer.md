---
title: "Optymalizator BYOM dla pretargetingu Authorized Buyers"
description: "Optymalizator Cat-Scan to Bring Your Own Model: pętla ocena-propozycja-zatwierdzenie-zastosowanie, w której posiadasz logikę oceniania. Dołączone presety Safe, Balanced i Aggressive."
---

# Przynoszenie własnego optymalizatora do pretargetingu Authorized Buyers (BYOM)

**Fakt atomowy:** Optymalizator Cat-Scan jest celowo oparty na zasadzie „Bring Your Own Model". Ocenia segmenty i proponuje zmiany pretargetingu; Ty decydujesz o logice oceniania i tolerancji ryzyka.

Ten projekt uznaje, że ostateczny sygnał wartości (wyniki po kliknięciu, LTV, marża) żyje w systemach reklamodawcy lub licytanta, a nie wewnątrz raportowania giełdowego.

## Cykl życia: ocena → propozycja → zatwierdzenie → zastosowanie

1. **Ocena**: Kontrolowany przez Ciebie zewnętrzny endpoint otrzymuje ładunek segmentów (kombinacje geo × wydawca × rozmiar × konfiguracja) plus sygnały proxy, które Cat-Scan posiada (oferty, wygrane, wydatki, marnotrawstwo itp.).
2. **Propozycja**: Cat-Scan wywołuje Twój kalkulator ocen i otrzymuje proponowane zmiany (dodaj geo do listy wykluczeń, obniż max QPS na tej konfiguracji, zablokuj tego wydawcę itp.).
3. **Zatwierdzenie**: Propozycje są wyświetlane z podglądem wpływu. Możesz akceptować, odrzucać lub modyfikować.
4. **Zastosowanie**: Zaakceptowane propozycje przechodzą przez normalny bezpieczny przepływ zmian (podgląd, wypchnięcie, migawka).

## Presety przepływu pracy

Cat-Scan jest dostarczany z trzema presetami, które kontrolują, jak agresywne mogą być propozycje:

- **Safe**: Małe zmiany, wysoki próg pewności, ograniczone do wyraźnych marnotrawnych elementów.
- **Balanced**: Domyślny dla większości miejsc produkcyjnych.
- **Aggressive**: Skłonny do większych ruchów, gdy sygnały są silne.

Możesz również zarejestrować całkowicie niestandardowe profile.

## Ekonomia przed posiadaniem danych o konwersjach

Dopóki dane MMP nie są podłączone, optymalizator optymalizuje pod kątem:
- Przesunięcia QPS ku segmentom, gdzie licytant faktycznie składa oferty.
- Ochrony konfiguracji i geo, gdzie koncentrują się rzeczywiste wydatki.
- Eliminacji konfiguracji z zerowymi ofertami lub zerowymi wyświetleniami (to czyste marnotrawstwo Twoich 10 slotów).

Po podłączeniu webhooków konwersji lub logów licytanta ta sama maszyneria propozycji może optymalizować bezpośrednio pod kątem wyników, na których Ci faktycznie zależy.

## Dlaczego ta architektura istnieje

Większość narzędzi „optymalizacyjnych" w ad tech to albo:
- Całkowicie czarna skrzynka (nie masz pojęcia, dlaczego zmiana została wprowadzona), albo
- Całkowicie manualne (sam robisz całą analizę w arkuszach kalkulacyjnych).

Projekt BYOM leży pośrodku: Cat-Scan jest właścicielem trudnych części (łączenie danych, bezpieczne stosowanie do Google, historia, cofnięcie). Ty jesteś właścicielem modelu wartości.

## Implementacja

- Trasy optymalizatora i przechowywanie propozycji na platformie
- Zewnętrzny kontrakt oceniania jest udokumentowany w dokumentacji platformy Cat-Scan
- Bieżąca logika sygnałów proxy w repozytorium platformy

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.  
Podejście BYOM to jeden z najwyraźniejszych znaków, że system został zbudowany przez osoby, które prowadziły rzeczywiste miejsca i wiedzą, gdzie musi żyć prawdziwa inteligencja.
