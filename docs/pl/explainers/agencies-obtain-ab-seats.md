---
title: "Jak agencje uzyskują miejsca Google Authorized Buyers"
description: "Google Authorized Buyers nie jest samoobsługowy; małe lub ograniczone agencje napotykają bariery wydatków, KYC i relacji. Jak RTB.cat dostarcza miejsce i narzędzia Cat-Scan."
---

# Jak mniejsze agencje i podmioty z ograniczeniami uzyskują i obsługują miejsca Google Authorized Buyers

**Fakt atomowy:** Wiele agencji, które są „zbyt małe", mają siedzibę w określonych jurysdykcjach (w tym obywatele i podmioty chińskie) lub po prostu nie mają istniejących relacji, nie może samodzielnie uzyskać bezpośredniej umowy Google Authorized Buyers.

To nie jest drobna kwestia papierkowa. To strukturalna bariera w programie Authorized Buyers.

## Rzeczywiste bariery

Google Authorized Buyers nie jest produktem samoobsługowym jak Google Ads. Zatwierdzenie obejmuje:

- Minimalne wymagania dotyczące wydatków i historii, których nowsze lub mniejsze agencje rzadko spełniają.
- Przeglądy zgodności i KYC, które mogą być trudne lub niemożliwe dla podmiotów w określonych krajach.
- Potrzebę istniejących relacji lub ciepłych rekomendacji.
- Kontrole gotowości technicznej i operacyjnej, o których większość agencji dowiaduje się dopiero po uzyskaniu miejsca.

Główną działalnością RTB.cat jest pomaganie dokładnie tym agencjom w uzyskaniu, a następnie skutecznym obsługiwaniu połączenia. Klienci przynoszą własnego licytanta. RTB.cat dostarcza rurociąg Authorized Buyers (a coraz częściej bezpośrednie endpointy OpenRTB, takie jak TrueCaller) i pobiera procent wydatków na media za zarządzanie i optymalizację.

## Co „obsługa miejsca" faktycznie wymaga po uzyskaniu umowy

Uzyskanie miejsca to tylko pierwszy krok. Codzienna obsługa ujawnia problemy udokumentowane w tych objaśnieniach:

- Pięć niekompatybilnych raportów CSV i potrzeba ich łączenia.
- Twardy limit 10 konfiguracji pretargetingu.
- Całkowity brak bezpiecznych narzędzi do wprowadzania zmian w natywnym UI.
- Pozyskiwanie identyfikatorów deal ID od wydawców (RTB.cat zabezpieczył identyfikatory deal ID u wydawców, w tym GCASH, Twitter i JAZZ w Pakistanie).
- Higiena kreacji na dużą skalę.
- Marnotrawstwo QPS, którego licytant nie może naprawić, ponieważ ruch nigdy nie powinien był być wysyłany.

Większość agencji, które w końcu otrzymują miejsce, jest zaskoczona ilością pracy operacyjnej, która pozostaje po ich stronie giełdy.

## Dlaczego platforma Cat-Scan istnieje

Cat-Scan (płaszczyzna kontroli QPS open-source) została zbudowana, ponieważ autor potrzebował tych możliwości podczas prowadzenia rzeczywistych miejsc i nie mógł ich znaleźć gdzie indziej. Celowo nie jest licytantem. Jest brakującą warstwą kontroli i widoczności na szczycie istniejącego połączenia Authorized Buyers (lub bezpośredniego OpenRTB).

Publikowanie platformy jako open source służy dwóm celom:
1. To konkretne, możliwe do zweryfikowania demonstrowanie głębokiej kompetencji operacyjnej.
2. To magnes dla leadów dokładnie dla klasy wyrafinowanych, ale ograniczonych agencji, które potrzebują zarówno połączenia, jak i narzędzi.

## Powiązane usługi

- Połączenie Google Authorized Buyers dla agencji, które nie mogą uzyskać go bezpośrednio.
- Bezpośrednie dostarczanie endpointu OpenRTB TrueCaller.
- Wprowadzenia i zarządzanie identyfikatorami deal ID wydawców.
- Bieżąca obsługa i optymalizacja miejsca (przy użyciu Cat-Scan lub równoważnych narzędzi).
- Doradztwo techniczne dla zespołów, które chcą budować lub ulepszać własne płaszczyzny kontroli.

Kontakt: [rtb.cat](https://rtb.cat) — WeChat: jenbrannstrom

**Ostatnia aktualizacja:** czerwiec 2026  
Część objaśnień technicznych RTB.cat / Cat-Scan.
