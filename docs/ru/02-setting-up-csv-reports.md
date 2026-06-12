---
title: "CSV-отчёты Authorized Buyers: 5 отчётов для Cat-Scan"
description: "Google Authorized Buyers не имеет Reporting API, поэтому Cat-Scan восстанавливает воронку из пяти CSV-отчётов по расписанию. Полный справочник метрик, измерений и инструкция по настройке."
---

# Настройка CSV-отчётов

*Аудитория: медиа-байеры, менеджеры аккаунтов*

Прежде чем Cat-Scan сможет что-либо анализировать, ему нужны данные. Google Authorized Buyers не имеет Reporting API, поэтому все данные поступают через **пять CSV-отчётов по расписанию**, которые вы создаёте единожды в своём аккаунте Google AB.

!!! warning "Почему именно пять отдельных отчётов?"
    Столбцы отчётности Google не все совместимы друг с другом. Например, «Bid requests» не может появляться в одном отчёте вместе с «Mobile app ID» или «Creative ID + Billing ID». Чтобы получить полную видимость воронки, нужно пять отчётов, которые Cat-Scan автоматически объединяет.

## Пять отчётов в двух словах

| # | Название отчёта | Что он даёт Cat-Scan | Ключевые столбцы |
|---|-----------------|----------------------|------------------|
| 1 | **Quality** | Эффективность на уровне креатива с видимостью | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Воронка ставок на уровне креатива (bids → wins) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Полная воронка bidstream по странам | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Полная воронка bidstream по издателям | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Почему Google отклоняет ваши ставки | Filtering reason, Bids, Opportunity cost |

---

## Полный справочник метрик

Каждая метрика, которую Cat-Scan принимает, её значение и из какого отчёта она поступает.

### Метрики воронки (pipeline bidstream)

Они отслеживают прохождение bid request через аукционную систему Google. Присутствуют в отчётах **Pipeline -- Geo** и **Pipeline -- Publisher**.

| Метрика | Определение | Единица | Отчёт(ы) |
|---------|-------------|---------|-----------|
| **Bid requests** | Всего bid requests, которые Google отправил на ваш endpoint. Это входящий объём в сыром виде — вершина воронки. Включает запросы, на которые ваш bidder мог не успеть ответить. | кол-во | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Bid requests, которые фактически достигли вашего bidder и получили ответ (успешный или нет). Ниже «Bid requests», если у вашего bidder есть проблемы с задержкой или таймаутами. | кол-во | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Запросы, по которым ваш bidder нашёл подходящий инвентарь (креатив, соответствующий запросу). Это первый фильтр: если у вас нет креатива для запрошенного размера/формата, процесс останавливается здесь. | кол-во | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Запросы, на которые ваш bidder вернул корректный, разбираемый ответ (HTTP 200 с правильно сформированной ставкой). Исключает таймауты, ошибки и отказы от ставки. | кол-во | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Фактические ответы со ставками вашего bidder. Подмножество успешных ответов — bidder может ответить успешно, но не сделать ставку (no-bid response). | кол-во | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Ставки, которые Google допустил к аукциону. Ставки могут быть отклонены до входа в аукцион из-за правил фильтрации (отклонение креатива, нарушение политики, минимальная цена, исключения pretargeting). Разрыв между «Bids» и «Bids in auction» отображается в отчёте Bid Filtering. | кол-во | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Ставки, выигравшие аукцион. За них вы платите. Разрыв между «Bids in auction» и «Auctions won» — это конкуренция: другие покупатели перебили вас. | кол-во | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Объявления, фактически отображённые в браузере или приложении пользователя после выигрыша аукциона. Немного меньше «Auctions won» из-за сбоев рендеринга, навигации по страницам до рендеринга и вмешательства блокировщиков рекламы. | кол-во | Все пять отчётов |
| **Clicks** | Взаимодействия пользователей (касания/клики) с вашими показанными объявлениями. | кол-во | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Метрики расходов и стоимости

| Метрика | Определение | Единица | Отчёт(ы) |
|---------|-------------|---------|-----------|
| **Spend** | Общая сумма, потраченная на выигранные показы за период. Это ваша фактическая стоимость медиа. В валюте вашего аккаунта (обычно USD). | валюта (micros в сырых данных, доллары в интерфейсе) | Quality |
| **Opportunity cost** | Оценочный доход, упущенный из-за того, что Google отфильтровал ваши ставки до входа в аукцион. Рассчитывается Google на основе исторических показателей выигрышей и CPM для аналогичного инвентаря. Полезно для расстановки приоритетов при исправлении причин фильтрации. | валюта | Bid Filtering |

### Метрики качества и видимости

Это метрики уровня креатива из отчёта **Quality**. Они измеряют то, что происходит *после* показа.

| Метрика | Определение | Единица | Отчёт(ы) |
|---------|-------------|---------|-----------|
| **Active View viewable** | Показы, соответствующие стандарту видимости MRC: не менее 50% пикселей объявления находились в видимой области браузера не менее 1 непрерывной секунды (2 секунды для видео). Это отраслевой стандарт «было ли объявление фактически увидено». | кол-во | Quality |
| **Active View measurable** | Показы, у которых видимость *можно было* измерить. Некоторые среды (определённые приложения, кросс-доменные iframe, старые браузеры) блокируют измерение. Коэффициент видимости = Active View viewable / Active View measurable. | кол-во | Quality |
| **Video starts** | Количество раз, когда видеокреатив начал воспроизводиться. Заполняется только для видеоформатов. | кол-во | Quality |
| **Video completions** | Количество раз, когда видеокреатив воспроизведён до 100% (или до точки пропуска, если пропуск доступен). Коэффициент завершения видео = completions / starts. | кол-во | Quality |

### Метрики фильтрации ставок

Из отчёта **Bid Filtering**. Они показывают *почему* ставки отклоняются до входа в аукцион.

| Метрика | Определение | Единица | Отчёт(ы) |
|---------|-------------|---------|-----------|
| **Bids** | Всего ставок вашего bidder (то же определение, что выше). В этом отчёте используется как знаменатель для расчёта показателей фильтрации. | кол-во | Bid Filtering |
| **Bids in auction** | Ставки, прошедшие фильтрацию и вошедшие в аукцион. `Bids - Bids in auction` = общее число отфильтрованных ставок. | кол-во | Bid Filtering |
| **Opportunity cost** | См. метрики расходов выше. В этом отчёте разбит по причинам фильтрации, чтобы вы могли видеть, какая причина обходится вам дороже всего. | валюта | Bid Filtering |

### Измерения (столбцы группировки)

Измерения — это не метрики, а оси, по которым метрики разбиваются. Cat-Scan использует их для нарезки данных.

| Измерение | Что это | В каких отчётах |
|-----------|---------|-----------------|
| **Day** | Календарная дата (UTC). Обязательна во всех отчётах. Cat-Scan использует это для дедупликации и отображения временных рядов. | Все пять |
| **Hour** | Час дня (0--23, UTC). Обеспечивает почасовую детализацию в анализе воронки. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Двухбуквенный код страны ISO (например, US, DE, IL). Географическое происхождение bid request. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (опционально) |
| **Billing ID (Pretargeting config)** | Числовой ID конфигурации pretargeting, принявшей этот трафик. Соответствует карточке конфигурации в Cat-Scan 1:1. | Quality |
| **Creative ID** | Числовой ID Google для ресурса креатива. Ссылается на галерею креативов в Cat-Scan. | Quality, Bids in Auction, Bid Filtering (опционально) |
| **Creative size** | Пиксельные размеры креатива (например, `300x250`, `728x90`). Используется для анализа потерь по размерам. | Quality |
| **Creative format** | Формат объявления: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (опционально) |
| **Platform** | Платформа устройства: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (опционально) |
| **Environment** | Где было показано объявление: `WEB`, `APP`. | Quality (опционально) |
| **App ID** | Идентификатор пакета мобильного приложения (например, `com.example.app`). Заполняется только для in-app инвентаря. | Quality (опционально) |
| **App name** | Человекочитаемое название приложения. | Quality (опционально) |
| **Publisher ID** | Числовой ID издателя (сайта или приложения). | Quality (опционально), Pipeline -- Publisher |
| **Publisher name** | Человекочитаемое имя издателя. | Quality (опционально), Pipeline -- Publisher |
| **Publisher domain** | Домен сайта издателя (например, `news.example.com`). | Quality (опционально) |
| **Buyer account ID** | ID вашего покупательского аккаунта / места. Нужен при управлении несколькими местами. | Bids in Auction, Bid Filtering (опционально) |
| **Filtering reason** | Код причины Google, по которой ставка была отфильтрована до входа в аукцион (например, `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Пошаговое создание каждого отчёта

### 1. Отчёт Quality

Это отчёт об эффективности на уровне креатива с данными о видимости и расходах.

**В Google Authorized Buyers → Reporting → New Report:**

| Настройка | Значение |
|-----------|----------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Рекомендуемое имя файла:** `catscan-quality`

!!! note
    Этот отчёт **не должен** включать «Bid requests», «Bids» или «Bids in
    auction» — эти столбцы несовместимы с «Billing ID» в отчётности Google.

---

### 2. Отчёт Bids in Auction

Этот отчёт фиксирует воронку ставок на уровне креатива, заполняя метрики, которые не может включить отчёт Quality.

| Настройка | Значение |
|-----------|----------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Рекомендуемое имя файла:** `catscan-bidsinauction`

!!! info "Как Cat-Scan объединяет их"
    Quality + Bids in Auction объединяются по `(Day, Creative ID)`, что даёт
    полную картину: от размещённых ставок до показанных impressions и понесённых расходов.

---

### 3. Отчёт Pipeline -- Geo

Это отчёт верхней части воронки: сколько bid requests Google отправляет вам по странам и сколько из них проходит каждый этап воронки.

| Настройка | Значение |
|-----------|----------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Рекомендуемое имя файла:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **Не** добавляйте Creative ID, Billing ID или App ID в этот отчёт. Эти
    столбцы несовместимы с «Bid requests».

---

### 4. Отчёт Pipeline -- Publisher

То же, что Pipeline -- Geo, но разбито по издателям вместо (или в дополнение к) географии.

| Настройка | Значение |
|-----------|----------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Рекомендуемое имя файла:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Отчёт Bid Filtering

Этот отчёт показывает *почему* Google фильтрует ваши ставки до входа в аукцион — критично для диагностики проблем pretargeting.

| Настройка | Значение |
|-----------|----------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Рекомендуемое имя файла:** `catscan-bid-filtering`

### Распространённые причины фильтрации

Это значения, которые вы увидите в измерении **Filtering reason**. Каждое из них указывает конкретную причину, по которой Google отклонил вашу ставку до входа в аукцион.

| Причина фильтрации | Что означает | Что делать |
|--------------------|-------------|------------|
| `CREATIVE_NOT_APPROVED` | Креатив не прошёл проверку Google или был отклонён | Проверьте статус креатива в Google AB. Устраните нарушения политики. |
| `BID_BELOW_AUCTION_FLOOR` | Цена ставки ниже минимального CPM издателя | Повысьте ставку или исключите малоценный инвентарь через pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | Политика Google на уровне биржи заблокировала ставку | Проверьте рекламные политики Google для конкретного креатива |
| `FILTERED_BY_PRETARGETING` | Ваши собственные правила pretargeting исключили этот трафик | Намеренно, если правила верны; проверьте при неожиданном результате |
| `NO_MATCHING_CREATIVE` | Bid request запросил размер/формат, которого у вас нет | Загрузите креативы для недостающих размеров или исключите их в pretargeting |
| `CREATIVE_SIZE_MISMATCH` | Размеры креатива не соответствуют рекламному блоку | Проверьте размер креатива против того, что запрашивает издатель |
| `LANDING_PAGE_DISAPPROVED` | Целевой URL не прошёл проверку Google | Исправьте лендинг или используйте другой URL |
| `SSL_REQUIRED` | Издатель требует HTTPS, но ваш креатив или лендинг использует HTTP | Переведите все ресурсы и URL на HTTPS |
| `FREQUENCY_CAPPED` | Пользователь уже видел этот креатив слишком много раз | Ожидаемое поведение; скорректируйте частотные ограничения, если они слишком агрессивны |

---

## Настройка расписания доставки

Для каждого из пяти отчётов:

1. Нажмите **Schedule** в Google Authorized Buyers.
2. Установите частоту — **Daily**.
3. Установите метод доставки:
      - **Email** — отправить на Gmail-аккаунт, подключённый к Cat-Scan (включает
        авто-импорт). Подробнее о настройке авто-импорта Gmail см. в разделе [Импорт данных](09-data-import.md).
      - **Manual** — если вы предпочитаете самостоятельно скачивать и загружать CSV через
        `/import`.

!!! tip "Используйте авто-импорт Gmail"
    Настройка доставки всех пяти отчётов на email подключённого аккаунта Gmail означает,
    что Cat-Scan импортирует их автоматически каждый день. После первоначальной настройки
    ручные загрузки не нужны.

## Проверка настройки

После импорта первого комплекта CSV (вручную или через Gmail):

1. Перейдите в `/import` в Cat-Scan.
2. Проверьте **Data Freshness Grid** — вы должны увидеть «imported» для всех пяти
   типов отчётов за вчерашнюю дату.
3. Если какие-либо ячейки показывают «missing», соответствующий отчёт ещё не получен.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Когда все пять столбцов показывают зелёный цвет за вчерашнюю дату, у Cat-Scan есть полные данные и
каждая функция (воронка, анализ потерь, рекомендации, оптимизатор) будет работать.

## Автодетекция

Вам не нужно сообщать Cat-Scan, какой отчёт вы загружаете. Система импорта
автоматически определяет тип отчёта по заголовкам столбцов:

- Есть **Bid filtering reason**? → Bid Filtering
- Есть **Bid requests** + **Publisher ID**? → Pipeline -- Publisher
- Есть **Bid requests** (без Publisher ID)? → Pipeline -- Geo
- Есть **Creative ID** + **Billing ID**? → Quality
- Есть **Creative ID** + **Bids in auction**? → Bids in Auction

## Как Cat-Scan использует каждую метрику

Это сопоставление сырых CSV-метрик с тем, что вы видите в интерфейсе Cat-Scan.

| Функция интерфейса | Используемые метрики | Исходный отчёт(ы) |
|-------------------|----------------------|-------------------|
| **Воронка QPS** (главная страница) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (оба) + Quality |
| **Расчёт % потерь** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Win rate** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Любой отчёт с обоими показателями |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Viewability rate** | `Active View viewable / Active View measurable` | Quality |
| **Video completion rate** | `Video completions / Video starts` | Quality |
| **Анализ потерь по гео** (`/qps/geo`) | Bid requests, Impressions, Spend по Country | Pipeline -- Geo + Quality |
| **Потери по издателям** (`/qps/publisher`) | Bid requests, Impressions, Spend по Publisher | Pipeline -- Publisher + Quality |
| **Потери по размерам** (`/qps/size`) | Impressions, Spend по Creative size | Quality |
| **Причины фильтрации** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost по Filtering reason | Bid Filtering |
| **Метрики карточки конфига** | Reached queries, Impressions, Spend по Billing ID | Quality |
| **Эффективность креатива** | Impressions, Clicks, Spend, Active View viewable по Creative ID | Quality |
| **Скоринг оптимизатора** | Все метрики pipeline + quality, агрегированные по сегменту | Все пять |

## Распространённые ошибки

| Ошибка | Что происходит | Исправление |
|--------|----------------|-------------|
| Добавление «Bid requests» в отчёт Quality | Google выдаёт ошибку или возвращает неполные данные | Удалите «Bid requests» — он несовместим с «Billing ID» |
| Отсутствие отчёта Bid Filtering | Cat-Scan не может показать *почему* ставки отклоняются | Создайте 5-й отчёт с измерением «Filtering reason» |
| Использование «Last 7 days» вместо «Yesterday» | Пересекающиеся данные, большие файлы, медленный импорт | Установите «Yesterday» и настройте ежедневное расписание |
| Только ручной экспорт без расписания | Данные устаревают, проверки работоспособности не проходят | Настройте ежедневную доставку по email |
| Отсутствие измерения «Hour» в отчётах Pipeline | Нет почасовой детализации в анализе QPS | Добавьте Hour в Pipeline -- Geo и Pipeline -- Publisher |
| Отсутствие опциональных метрик в отчёте Quality | Нет данных о видимости или видео в Cat-Scan | Добавьте Active View viewable, Active View measurable, Video starts, Video completions |

## Дальнейшие шаги

- [Админ-навигация](02-navigating-the-dashboard.md): структура боковой панели и
  чеклист настройки
- [Импорт данных](09-data-import.md): подробная механика импорта, фрагментированные
  загрузки и устранение неисправностей
- [Воронка QPS](03-qps-funnel.md): как только данные начнут поступать, приступите к анализу
