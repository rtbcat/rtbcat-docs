---
title: "CSV-звіти Authorized Buyers: 5 звітів для Cat-Scan"
description: "Google Authorized Buyers не має API звітності, тому Cat-Scan відновлює воронку з п'яти запланованих CSV-звітів. Повний довідник метрик, вимірів та налаштування."
---

# Налаштування CSV-звітів

*Аудиторія: медіа-байери, акаунт-менеджери*

Перш ніж Cat-Scan зможе щось аналізувати, йому потрібні дані. Google Authorized Buyers
не має API звітності, тому всі дані надходять через **п'ять запланованих CSV-звітів**,
які ви один раз створюєте у своєму акаунті Google AB.

!!! warning "Чому п'ять окремих звітів?"
    Стовпці звітності Google не всі сумісні між собою. Наприклад,
    «Bid requests» не може з'являтися в одному звіті з «Mobile app ID»
    або «Creative ID + Billing ID». Щоб отримати повну видимість воронки,
    потрібно п'ять звітів, які Cat-Scan об'єднує автоматично.

## П'ять звітів одним поглядом

| # | Назва звіту | Що повідомляє Cat-Scan | Ключові стовпці |
|---|-------------|------------------------|-----------------|
| 1 | **Quality** | Ефективність на рівні креативу з видимістю | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Конвеєр ставок на рівні креативу (ставки -> перемоги) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Повна воронка bidstream за країнами | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Повна воронка bidstream за видавцем | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Чому Google відхиляє ваші ставки | Filtering reason, Bids, Opportunity cost |

---

## Повний довідник метрик

Кожна метрика, яку отримує Cat-Scan, що вона означає та який звіт її містить.

### Метрики воронки (конвеєр bidstream)

Вони відстежують просування запиту ставки через аукціонну систему Google.
Присутні у звітах **Pipeline -- Geo** та **Pipeline -- Publisher**.

| Метрика | Визначення | Одиниця | Звіт(и) |
|---------|-----------|---------|---------|
| **Bid requests** | Загальна кількість запитів ставок, надісланих Google на ваш endpoint. Це вхідний обсяг — верхівка воронки. Включає запити, на які ваш bidder міг не відповісти вчасно. | кількість | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Запити ставок, що фактично досягли вашого bidder і отримали відповідь (успішну чи ні). Менше, ніж «Bid requests», якщо у bidder є проблеми з латентністю або тайм-аутами. | кількість | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Запити, для яких ваш bidder знайшов відповідний інвентар (креатив, що відповідає запиту). Це перший фільтр: якщо у вас немає креативу для запитуваного розміру/формату, обробка зупиняється тут. | кількість | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Запити, на які ваш bidder повернув дійсну, розпізнану відповідь ставки (HTTP 200 з коректно сформованою ставкою). Виключає тайм-аути, помилки та відмови від ставки. | кількість | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Фактичні відповіді зі ставками від вашого bidder. Підмножина успішних відповідей — bidder може відповісти успішно, але вирішити не ставити (відповідь без ставки). | кількість | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Ставки, прийняті Google до аукціону. Ставки можуть бути відхилені до входу в аукціон через правила фільтрації (незатверджений креатив, порушення правил, ціна підлоги, виключення pretargeting). Різниця між «Bids» і «Bids in auction» відображається у звіті Bid Filtering. | кількість | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Ставки, що виграли аукціон. Ви платите за них. Різниця між «Bids in auction» і «Auctions won» — це конкуренція: інші покупці перебили вас. | кількість | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Оголошення, фактично відображені в браузері або додатку користувача після перемоги в аукціоні. Дещо менше, ніж «Auctions won», через збої відображення реклами, переходи зі сторінки до відображення та блокувальники реклами. | кількість | Усі п'ять звітів |
| **Clicks** | Взаємодії користувача (натискання) з вашою показаною рекламою. | кількість | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Метрики витрат

| Метрика | Визначення | Одиниця | Звіт(и) |
|---------|-----------|---------|---------|
| **Spend** | Загальна сума, витрачена на виграні покази за період. Це ваші фактичні витрати на медіа. У валюті акаунту (зазвичай USD). | валюта (мікро в сирих даних, долари у UI) | Quality |
| **Opportunity cost** | Орієнтовний дохід, втрачений через те, що Google відфільтрував ваші ставки до входу в аукціон. Розраховується Google на основі історичних показників перемог і CPM для аналогічного інвентарю. Корисно для визначення пріоритетів, які причини фільтрації виправляти першими. | валюта | Bid Filtering |

### Метрики якості та видимості

Це метрики рівня креативу зі звіту **Quality**. Вони вимірюють те,
що відбувається *після* показу оголошення.

| Метрика | Визначення | Одиниця | Звіт(и) |
|---------|-----------|---------|---------|
| **Active View viewable** | Покази, що відповідали стандарту видимості MRC: принаймні 50% пікселів оголошення знаходилися у видимій зоні браузера принаймні 1 безперервну секунду (2 секунди для відео). Це галузевий стандарт для «чи була реклама насправді побачена». | кількість | Quality |
| **Active View measurable** | Покази, де видимість *можна* виміряти. Деякі середовища (певні додатки, крос-доменні iframe, старіші браузери) блокують вимірювання. Рівень видимості = Active View viewable / Active View measurable. | кількість | Quality |
| **Video starts** | Кількість разів, коли відеокреатив починав відтворення. Заповнюється лише для відеоформатів. | кількість | Quality |
| **Video completions** | Кількість разів, коли відеокреатив відтворився до 100% завершення (або до точки пропуску, якщо він пропускається). Рівень завершення відео = completions / starts. | кількість | Quality |

### Метрики фільтрації ставок

Зі звіту **Bid Filtering**. Вони повідомляють *чому* ставки відхиляються
до входу в аукціон.

| Метрика | Визначення | Одиниця | Звіт(и) |
|---------|-----------|---------|---------|
| **Bids** | Загальна кількість ставок від вашого bidder (те саме визначення, що вище). У цьому звіті використовується як знаменник для розрахунку коефіцієнтів фільтрації. | кількість | Bid Filtering |
| **Bids in auction** | Ставки, що пережили фільтрацію і потрапили до аукціону. `Bids - Bids in auction` = загальна кількість відфільтрованих ставок. | кількість | Bid Filtering |
| **Opportunity cost** | Дивіться метрики витрат вище. У цьому звіті деталізовано за причиною фільтрації, щоб ви бачили, яка причина коштує вам найбільше. | валюта | Bid Filtering |

### Виміри (стовпці групування)

Виміри — це не метрики; це осі, за якими розбиваються метрики.
Cat-Scan використовує їх для сегментації ваших даних.

| Вимір | Що це | Які звіти |
|-------|-------|-----------|
| **Day** | Календарна дата (UTC). Обов'язкова у всіх звітах. Cat-Scan використовує її для дедублікації та відображення часових рядів. | Усі п'ять |
| **Hour** | Година дня (0--23, UTC). Забезпечує погодинну деталізацію в аналізі конвеєра. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Дволітерний код країни ISO (наприклад, US, DE, IL). Географічне походження запиту ставки. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (необов'язково) |
| **Billing ID (Pretargeting config)** | Числовий ідентифікатор конфігурації pretargeting, що прийняла цей трафік. Відображається 1:1 на картку конфігурації в Cat-Scan. | Quality |
| **Creative ID** | Числовий ідентифікатор Google для рекламного матеріалу. Посилається на галерею креативів у Cat-Scan. | Quality, Bids in Auction, Bid Filtering (необов'язково) |
| **Creative size** | Розміри в пікселях креативу (наприклад, `300x250`, `728x90`). Використовується для аналізу втрат за розміром. | Quality |
| **Creative format** | Формат оголошення: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (необов'язково) |
| **Platform** | Платформа пристрою: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (необов'язково) |
| **Environment** | Де було показано оголошення: `WEB`, `APP`. | Quality (необов'язково) |
| **App ID** | Ідентифікатор пакету мобільного додатку (наприклад, `com.example.app`). Заповнюється лише для in-app інвентарю. | Quality (необов'язково) |
| **App name** | Зрозуміла людині назва додатку. | Quality (необов'язково) |
| **Publisher ID** | Числовий ідентифікатор видавця (вебсайту або додатку). | Quality (необов'язково), Pipeline -- Publisher |
| **Publisher name** | Зрозуміла людині назва видавця. | Quality (необов'язково), Pipeline -- Publisher |
| **Publisher domain** | Домен вебсайту видавця (наприклад, `news.example.com`). | Quality (необов'язково) |
| **Buyer account ID** | Ідентифікатор вашого акаунту покупця / місця. Потрібен при роботі з кількома місцями. | Bids in Auction, Bid Filtering (необов'язково) |
| **Filtering reason** | Код причини Google, чому ставка була відфільтрована до входу в аукціон (наприклад, `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Покрокове керівництво: створення кожного звіту

### 1. Звіт Quality

Це ваш звіт ефективності на рівні креативу з даними про видимість і витрати.

**У Google Authorized Buyers -> Reporting -> New Report:**

| Налаштування | Значення |
|-------------|---------|
| Report type | RTB |
| Time range | Yesterday (запланований щоденно) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Пропонована назва файлу:** `catscan-quality`

!!! note
    Цей звіт **не повинен** включати «Bid requests», «Bids» або «Bids in
    auction» — ці стовпці несумісні з «Billing ID» у звітності Google.

---

### 2. Звіт Bids in Auction

Цей звіт фіксує конвеєр ставок на рівні креативу, заповнюючи
метрики, які звіт Quality не може включати.

| Налаштування | Значення |
|-------------|---------|
| Report type | RTB |
| Time range | Yesterday (запланований щоденно) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Пропонована назва файлу:** `catscan-bidsinauction`

!!! info "Як Cat-Scan їх об'єднує"
    Quality + Bids in Auction об'єднуються за `(Day, Creative ID)`, щоб дати
    повну картину: від розміщених ставок до показів та понесених витрат.

---

### 3. Звіт Pipeline -- Geo

Це ваш звіт верхньої частини воронки: скільки запитів ставок Google надсилає вам
за країнами та скільки з них проходить кожен етап воронки.

| Налаштування | Значення |
|-------------|---------|
| Report type | RTB |
| Time range | Yesterday (запланований щоденно) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Пропонована назва файлу:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **Не** додавайте Creative ID, Billing ID або App ID до цього звіту. Ці
    стовпці несумісні з «Bid requests».

---

### 4. Звіт Pipeline -- Publisher

Аналогічний до Pipeline -- Geo, але деталізований за видавцем, а не (або
на додаток до) географії.

| Налаштування | Значення |
|-------------|---------|
| Report type | RTB |
| Time range | Yesterday (запланований щоденно) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Пропонована назва файлу:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Звіт Bid Filtering

Цей звіт показує *чому* Google фільтрує ваші ставки до входу в аукціон —
критично для діагностики проблем з pretargeting.

| Налаштування | Значення |
|-------------|---------|
| Report type | RTB |
| Time range | Yesterday (запланований щоденно) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Пропонована назва файлу:** `catscan-bid-filtering`

### Поширені причини фільтрації

Це значення, які ви побачите у вимірі **Filtering reason**. Кожне
повідомляє конкретну причину, чому Google відхилив вашу ставку до входу в аукціон.

| Причина фільтрації | Що означає | Що робити |
|-------------------|-----------|-----------|
| `CREATIVE_NOT_APPROVED` | Креатив не пройшов перевірку Google або був відхилений | Перевірте статус креативу в Google AB. Виправте порушення правил. |
| `BID_BELOW_AUCTION_FLOOR` | Ціна вашої ставки нижча за мінімальний CPM видавця | Підвищіть ставку або виключіть малоцінний інвентар через pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | Правила рівня біржі Google заблокували ставку | Перегляньте рекламні правила Google для конкретного креативу |
| `FILTERED_BY_PRETARGETING` | Ваші власні правила pretargeting виключили цей трафік | Навмисне, якщо ваші правила коректні; перегляньте, якщо несподіване |
| `NO_MATCHING_CREATIVE` | Запит ставки запитав розмір/формат, якого у вас немає | Завантажте креативи для відсутніх розмірів або виключіть ці розміри в pretargeting |
| `CREATIVE_SIZE_MISMATCH` | Розміри креативу не відповідають рекламному місцю | Перевірте розмір креативу порівняно з тим, що запитує видавець |
| `LANDING_PAGE_DISAPPROVED` | URL призначення не пройшов перевірку Google | Виправте цільову сторінку або використайте інший URL |
| `SSL_REQUIRED` | Видавець вимагає HTTPS, але ваш креатив або цільова сторінка використовує HTTP | Перенесіть усі ресурси та URL на HTTPS |
| `FREQUENCY_CAPPED` | Користувач вже бачив цей креатив надто багато разів | Очікувана поведінка; відрегулюйте обмеження частоти, якщо вони надто агресивні |

---

## Планування доставки

Для кожного з п'яти звітів:

1. Натисніть **Schedule** у Google Authorized Buyers.
2. Встановіть частоту **Daily**.
3. Встановіть спосіб доставки:
      - **Email** — надсилайте на обліковий запис Gmail, підключений до Cat-Scan (дозволяє
        автоматичний імпорт). Дивіться [Імпорт даних](09-data-import.md) для налаштування
        автоматичного імпорту Gmail.
      - **Manual** — якщо ви надаєте перевагу самостійному завантаженню та вивантаженню
        CSV через `/import`.

!!! tip "Використовуйте автоматичний імпорт Gmail"
    Планування всіх п'яти звітів для надсилання на підключений обліковий запис Gmail означає,
    що Cat-Scan імпортує їх автоматично щодня. Після початкового налаштування ручне
    завантаження не потрібне.

## Перевірка налаштування

Після імпорту першого набору CSV (вручну або через Gmail):

1. Перейдіть до `/import` у Cat-Scan.
2. Перевірте **Data Freshness Grid** — ви повинні побачити «imported» для всіх п'яти
   типів звітів за вчорашню дату.
3. Якщо будь-які клітинки показують «missing», відповідний звіт ще не було отримано.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Коли всі п'ять стовпців показують зелений за вчора, Cat-Scan має повні дані і
кожна функція (воронка, аналіз втрат, рекомендації, оптимізатор) працюватиме.

## Автоматичне визначення

Вам не потрібно повідомляти Cat-Scan, який звіт ви завантажуєте. Система
імпорту автоматично визначає тип звіту за заголовками стовпців:

- Є **Bid filtering reason**? -> Bid Filtering
- Є **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- Є **Bid requests** (без Publisher ID)? -> Pipeline -- Geo
- Є **Creative ID** + **Billing ID**? -> Quality
- Є **Creative ID** + **Bids in auction**? -> Bids in Auction

## Як Cat-Scan використовує кожну метрику

Це відображення сирих CSV-метрик на те, що ви бачите в UI Cat-Scan.

| Функція UI | Використані метрики | Вихідний звіт(и) |
|-----------|---------------------|-----------------|
| **Воронка QPS** (головна сторінка) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (обидва) + Quality |
| **Розрахунок % втрат** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Коефіцієнт перемог** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Будь-який звіт з обома |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Рівень видимості** | `Active View viewable / Active View measurable` | Quality |
| **Рівень завершення відео** | `Video completions / Video starts` | Quality |
| **Аналіз втрат за гео** (`/qps/geo`) | Bid requests, Impressions, Spend за Country | Pipeline -- Geo + Quality |
| **Втрати за видавцем** (`/qps/publisher`) | Bid requests, Impressions, Spend за Publisher | Pipeline -- Publisher + Quality |
| **Втрати за розміром** (`/qps/size`) | Impressions, Spend за Creative size | Quality |
| **Причини фільтрації** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost за Filtering reason | Bid Filtering |
| **Метрики картки конфігурації** | Reached queries, Impressions, Spend за Billing ID | Quality |
| **Ефективність креативу** | Impressions, Clicks, Spend, Active View viewable за Creative ID | Quality |
| **Оцінювання оптимізатора** | Усі метрики конвеєра + якості, агреговані за сегментом | Усі п'ять |

## Типові помилки

| Помилка | Що відбувається | Виправлення |
|---------|----------------|-------------|
| Додавання «Bid requests» до звіту Quality | Google видає помилку або повертає неповні дані | Видаліть «Bid requests» — він несумісний з «Billing ID» |
| Відсутність звіту Bid Filtering | Cat-Scan не може показати *чому* ставки відхиляються | Створіть 5-й звіт з виміром «Filtering reason» |
| Використання «Last 7 days» замість «Yesterday» | Дані, що перекриваються, більші файли, повільніший імпорт | Встановіть «Yesterday» і плануйте щоденно |
| Без планування — лише ручний експорт | Дані застарівають, перевірки справності не проходять | Плануйте щоденну доставку через email |
| Відсутній вимір «Hour» у звітах Pipeline | Немає погодинної деталізації в аналізі QPS | Додайте Hour до Pipeline -- Geo і Pipeline -- Publisher |
| Відсутні необов'язкові метрики у звіті Quality | Немає даних видимості або відео в Cat-Scan | Додайте Active View viewable, Active View measurable, Video starts, Video completions |

## Наступні кроки

- [Адмін-навігація](02-navigating-the-dashboard.md): розміщення бічної панелі та
  контрольний список налаштування
- [Імпорт даних](09-data-import.md): детальна механіка імпорту, завантаження
  по частинах та усунення несправностей
- [Воронка QPS](03-qps-funnel.md): коли дані надходять, починайте аналіз
