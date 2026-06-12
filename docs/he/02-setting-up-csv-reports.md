---
title: "הגדרת דוחות ה-CSV שלך"
description: "ל-Google Authorized Buyers אין Reporting API, ולכן Cat-Scan בונה מחדש את המשפך מחמישה דוחות CSV מתוזמנים. מדריך הגדרה עם הפניה מלאה למדדים ולממדים."
---

# הגדרת דוחות ה-CSV שלך

*קהל יעד: קוני מדיה, מנהלי חשבון*

לפני שCat-Scan יכול לנתח כל דבר, הוא זקוק לנתונים. ל-Google Authorized Buyers
אין Reporting API, ולכן כל הנתונים זורמים דרך **חמישה דוחות CSV מתוזמנים**
שאתם יוצרים פעם אחת בחשבון Google AB שלכם.

!!! warning "מדוע חמישה דוחות נפרדים?"
    עמודות הדיווח של Google אינן כולן תואמות זו לזו. לדוגמה,
    "Bid requests" לא יכולים להופיע באותו דוח כמו "Mobile app ID"
    או "Creative ID + Billing ID". כדי לקבל נראות מלאה של המשפך, נחוצים חמישה
    דוחות ש-Cat-Scan מאחד אותם אוטומטית.

## חמשת הדוחות במבט מהיר

| # | שם הדוח | מה הוא מוסר ל-Cat-Scan | עמודות מרכזיות |
|---|---------|------------------------|----------------|
| 1 | **Quality** | ביצועי יצירות ברמת Creative עם viewability | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | צינור הצעות ברמת Creative (הצעות -> ניצחונות) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | משפך bidstream מלא לפי מדינה | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | משפך bidstream מלא לפי מפרסם | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | מדוע Google דוחה את ההצעות שלכם | Filtering reason, Bids, Opportunity cost |

---

## הפניה מלאה למדדים

כל מדד שCat-Scan קולט, משמעותו, ואיזה דוח נושא אותו.

### מדדי משפך (צינור bidstream)

מדדים אלה עוקבים אחר התקדמות בקשת הצעה דרך מערכת המכרז של Google.
נמצאים בדוחות **Pipeline -- Geo** ו-**Pipeline -- Publisher**.

| מדד | הגדרה | יחידה | דוח/ות |
|-----|--------|-------|--------|
| **Bid requests** | סך בקשות ההצעות שGoogle שלח לנקודת הקצה של ה-bidder שלכם. זהו נפח הכניסה הגולמי — ראש המשפך. כולל בקשות שה-bidder שלכם אולי לא הגיב להן בזמן. | ספירה | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | בקשות הצעה שהגיעו בפועל ל-bidder שלכם וקיבלו תגובה (בהצלחה או לא). נמוך מ-"Bid requests" אם ל-bidder יש בעיות זמן תגובה או timeout. | ספירה | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | בקשות שבהן ה-bidder שלכם מצא inventory מתאים (יצירה שמתאימה לבקשה). זהו הסינון הראשון: אם אין לכם יצירה לגודל/פורמט המבוקש, זה נעצר כאן. | ספירה | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | בקשות שבהן ה-bidder שלכם החזיר תגובת הצעה תקפה וניתנת לניתוח (HTTP 200 עם הצעה בפורמט תקין). אינו כולל timeout, שגיאות ואי-הצעות. | ספירה | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | תגובות הצעה בפועל שה-bidder שלכם הגיש. תת-קבוצה של תגובות מוצלחות — ה-bidder עשוי להגיב בהצלחה אך לבחור שלא להציע (תגובת no-bid). | ספירה | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | הצעות שGoogle קיבל למכרז. הצעות עשויות להידחות לפני כניסה למכרז בגלל חוקי סינון (אי-אישור יצירות, הפרות מדיניות, מחיר רצפה, אי-הכללות pretargeting). הפער בין "Bids" ל-"Bids in auction" מוצג בדוח Bid Filtering. | ספירה | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | הצעות שזכו במכרז. אתם משלמים עבור אלה. הפער בין "Bids in auction" ל-"Auctions won" הוא תחרות — קונים אחרים הציעו יותר. | ספירה | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | מודעות שהוצגו בפועל בדפדפן או באפליקציה של משתמש לאחר זכייה במכרז. מעט פחות מ-"Auctions won" בשל כשלי עיבוד מודעות, ניווטי דף לפני עיבוד והפרעת חוסמי מודעות. | ספירה | כל חמשת הדוחות |
| **Clicks** | אינטראקציות משתמש (הקשות/קליקים) על המודעות שהצגתם. | ספירה | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### מדדי הוצאות ועלויות

| מדד | הגדרה | יחידה | דוח/ות |
|-----|--------|-------|--------|
| **Spend** | סך הכסף שהוצא על impressions שזכו בתקופה. זוהי עלות המדיה בפועל שלכם. מונמקת במטבע החשבון שלכם (בדרך כלל USD). | מטבע (micros בנתונים גולמיים, דולרים ב-UI) | Quality |
| **Opportunity cost** | הכנסה משוערת שהפסדתם כי Google סינן את ההצעות שלכם לפני שנכנסו למכרז. מחושב על ידי Google על בסיס שיעורי ניצחון היסטוריים ו-CPM לסוגי inventory דומים. שימושי לתעדוף אילו סיבות סינון לתקן תחילה. | מטבע | Bid Filtering |

### מדדי איכות ו-viewability

אלה מדדי יצירות ברמת Creative מדוח **Quality**. הם מודדים
מה קורה *לאחר* שה-impression מוצג.

| מדד | הגדרה | יחידה | דוח/ות |
|-----|--------|-------|--------|
| **Active View viewable** | Impressions שעמדו בתקן viewability של MRC: לפחות 50% מפיקסלי המודעה היו באזור הגלוי של הדפדפן למשך לפחות שנייה רצופה אחת (2 שניות לווידאו). זהו התקן התעשייתי ל-"האם המודעה אכן נראתה." | ספירה | Quality |
| **Active View measurable** | Impressions שבהם viewability *ניתן היה* למדידה. סביבות מסוימות (אפליקציות מסוימות, iframes cross-domain, דפדפנים ישנים) חוסמות מדידה. שיעור viewability = Active View viewable / Active View measurable. | ספירה | Quality |
| **Video starts** | מספר הפעמים שיצירת וידאו החלה לנגן. מאוכלס רק עבור יצירות בפורמט וידאו. | ספירה | Quality |
| **Video completions** | מספר הפעמים שיצירת וידאו נוגנה עד 100% השלמה (או עד נקודת הדילוג אם ניתן לדילוג). שיעור השלמת וידאו = completions / starts. | ספירה | Quality |

### מדדי סינון הצעות

מדוח **Bid Filtering**. אלה מספרים לכם *מדוע* הצעות נדחות
לפני שהן נכנסות למכרז.

| מדד | הגדרה | יחידה | דוח/ות |
|-----|--------|-------|--------|
| **Bids** | סך ההצעות שה-bidder שלכם הגיש (אותה הגדרה כמו לעיל). בדוח זה, משמש כמכנה לחישוב שיעורי סינון. | ספירה | Bid Filtering |
| **Bids in auction** | הצעות שעברו את הסינון ונכנסו למכרז. `Bids - Bids in auction` = סך ההצעות שסוננו. | ספירה | Bid Filtering |
| **Opportunity cost** | ראו מדדי הוצאות לעיל. בדוח זה, מפורט לפי סיבת סינון כדי שתוכלו לראות איזה סיבה עולה לכם הכי הרבה. | מטבע | Bid Filtering |

### ממדים (עמודות קיבוץ)

ממדים אינם מדדים — הם הצירים שלאורכם מדדים מפורטים.
Cat-Scan משתמש בהם כדי לפלח את הנתונים שלכם.

| ממד | מה הוא | באילו דוחות |
|-----|---------|-------------|
| **Day** | תאריך לוח שנה (UTC). נדרש בכל הדוחות. Cat-Scan משתמש בזה לביטול כפילויות ולתצוגת סדרות זמן. | כל חמשת הדוחות |
| **Hour** | שעה ביום (0--23, UTC). מאפשר גרנולריות שעתית בניתוח צינור. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | קוד מדינה ISO דו-אותיות (לדוגמה, US, DE, IL). המקור הגאוגרפי של בקשת ההצעה. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (אופציונלי) |
| **Billing ID (Pretargeting config)** | מזהה מספרי של תצורת ה-pretargeting שקיבלה תעבורה זו. ממפה 1:1 לכרטיס תצורה ב-Cat-Scan. | Quality |
| **Creative ID** | מזהה מספרי של Google לנכס היצירה. מקושר לגלריית Creatives ב-Cat-Scan. | Quality, Bids in Auction, Bid Filtering (אופציונלי) |
| **Creative size** | מידות פיקסל של היצירה (לדוגמה, `300x250`, `728x90`). משמש לניתוח בזבוז מבוסס גודל. | Quality |
| **Creative format** | פורמט המודעה: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (אופציונלי) |
| **Platform** | פלטפורמת מכשיר: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (אופציונלי) |
| **Environment** | היכן הוצגה המודעה: `WEB`, `APP`. | Quality (אופציונלי) |
| **App ID** | מזהה Bundle של אפליקציה ניידת (לדוגמה, `com.example.app`). מאוכלס רק עבור inventory בתוך אפליקציה. | Quality (אופציונלי) |
| **App name** | שם אפליקציה קריא לאדם. | Quality (אופציונלי) |
| **Publisher ID** | מזהה מספרי של המפרסם (אתר או אפליקציה). | Quality (אופציונלי), Pipeline -- Publisher |
| **Publisher name** | שם מפרסם קריא לאדם. | Quality (אופציונלי), Pipeline -- Publisher |
| **Publisher domain** | הדומיין של אתר המפרסם (לדוגמה, `news.example.com`). | Quality (אופציונלי) |
| **Buyer account ID** | מזהה חשבון הקונה / מושב שלכם. נדרש כאשר אתם מפעילים מספר מושבים. | Bids in Auction, Bid Filtering (אופציונלי) |
| **Filtering reason** | קוד הסיבה של Google לסינון הצעה לפני כניסה למכרז (לדוגמה, `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## שלב אחר שלב: יצירת כל דוח

### 1. דוח Quality

זהו דוח הביצועים ברמת יצירה עם נתוני viewability והוצאות.

**ב-Google Authorized Buyers -> Reporting -> New Report:**

| הגדרה | ערך |
|-------|-----|
| סוג דוח | RTB |
| טווח זמן | Yesterday (מתוזמן יומי) |
| ממדים | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| ממדים אופציונליים | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| מדדים | Reached queries, Impressions, Clicks, Spend |
| מדדים אופציונליים | Video starts, Video completions, Active View viewable, Active View measurable |

**שם קובץ מוצע:** `catscan-quality`

!!! note
    דוח זה **לא** יכיל "Bid requests", "Bids", או "Bids in
    auction" — עמודות אלה אינן תואמות ל-"Billing ID" בדיווח של Google.

---

### 2. דוח Bids in Auction

דוח זה לוכד את צינור ההצעות ברמת היצירה, וממלא את
המדדים שדוח Quality אינו יכול לכלול.

| הגדרה | ערך |
|-------|-----|
| סוג דוח | RTB |
| טווח זמן | Yesterday (מתוזמן יומי) |
| ממדים | Day, Country, Creative ID, Buyer account ID |
| מדדים | Bids in auction, Auctions won, Bids, Impressions |

**שם קובץ מוצע:** `catscan-bidsinauction`

!!! info "כיצד Cat-Scan מאחד אותם"
    Quality + Bids in Auction מאוחדים על `(Day, Creative ID)` כדי לתת לכם
    את התמונה המלאה: מהצעות שהוגשו דרך impressions שהוצגו והוצאות שנצברו.

---

### 3. דוח Pipeline -- Geo

זהו דוח ראש המשפך שלכם: כמה בקשות הצעה Google שולח לכם
לפי מדינה, וכמה שורדות בכל שלב של המשפך.

| הגדרה | ערך |
|-------|-----|
| סוג דוח | RTB |
| טווח זמן | Yesterday (מתוזמן יומי) |
| ממדים | Day, Country, Hour |
| מדדים | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**שם קובץ מוצע:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **אל** תוסיפו Creative ID, Billing ID, או App ID לדוח זה. עמודות אלה
    אינן תואמות ל-"Bid requests".

---

### 4. דוח Pipeline -- Publisher

זהה ל-Pipeline -- Geo, אך מפורט לפי מפרסם במקום (או בנוסף ל-)
גיאוגרפיה.

| הגדרה | ערך |
|-------|-----|
| סוג דוח | RTB |
| טווח זמן | Yesterday (מתוזמן יומי) |
| ממדים | Day, Country, Hour, Publisher ID, Publisher name |
| מדדים | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**שם קובץ מוצע:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. דוח Bid Filtering

דוח זה מראה לכם *מדוע* Google מסנן את ההצעות שלכם לפני שהן נכנסות
למכרז — קריטי לאבחון בעיות pretargeting.

| הגדרה | ערך |
|-------|-----|
| סוג דוח | RTB |
| טווח זמן | Yesterday (מתוזמן יומי) |
| ממדים | Day, Filtering reason |
| ממדים אופציונליים | Country, Buyer account ID, Creative ID |
| מדדים | Bids, Bids in auction, Opportunity cost |

**שם קובץ מוצע:** `catscan-bid-filtering`

### סיבות סינון נפוצות

אלה הערכים שתראו בממד **Filtering reason**. כל אחד
מספר לכם סיבה ספציפית שבגללה Google דחה את ההצעה שלכם לפני כניסה למכרז.

| סיבת סינון | משמעות | מה לעשות |
|------------|---------|----------|
| `CREATIVE_NOT_APPROVED` | היצירה לא עברה את הסקירה של Google, או נדחתה | בדקו סטטוס יצירה ב-Google AB. תקנו הפרות מדיניות. |
| `BID_BELOW_AUCTION_FLOOR` | מחיר ההצעה שלכם נמוך ממינימום ה-CPM של המפרסם | העלו את ההצעה או הוציאו inventory בעל ערך נמוך דרך pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | מדיניות Exchange ברמת Google חסמה את ההצעה | סקרו את מדיניות המודעות של Google עבור היצירה הספציפית |
| `FILTERED_BY_PRETARGETING` | חוקי ה-pretargeting שלכם הוציאו את התעבורה הזו | מכוון אם החוקים שלכם נכונים; בדקו אם בלתי צפוי |
| `NO_MATCHING_CREATIVE` | בקשת ההצעה ביקשה גודל/פורמט שאין לכם | העלו יצירות לגדלים החסרים, או הוציאו גדלים אלה ב-pretargeting |
| `CREATIVE_SIZE_MISMATCH` | מידות היצירה אינן תואמות את חריץ המודעה | בדקו גודל יצירה מול מה שהמפרסם מבקש |
| `LANDING_PAGE_DISAPPROVED` | כתובת URL היעד נכשלה בסקירת Google | תקנו את דף הנחיתה או השתמשו בכתובת URL אחרת |
| `SSL_REQUIRED` | המפרסם דורש HTTPS אך היצירה או דף הנחיתה שלכם משתמשים ב-HTTP | העבירו את כל הנכסים וכתובות ה-URL ל-HTTPS |
| `FREQUENCY_CAPPED` | המשתמש כבר ראה יצירה זו יותר מדי פעמים | התנהגות צפויה; התאימו מגבלות תדירות אם אגרסיביות מדי |

---

## תזמון המסירה

עבור כל אחד מחמשת הדוחות:

1. לחצו **Schedule** ב-Google Authorized Buyers.
2. הגדירו תדירות ל-**Daily**.
3. הגדירו שיטת מסירה:
      - **Email** — שלחו לחשבון Gmail המחובר ל-Cat-Scan (מאפשר
        ייבוא אוטומטי). ראו [ייבוא נתונים](09-data-import.md) להגדרת
        ייבוא אוטומטי מ-Gmail.
      - **Manual** — אם אתם מעדיפים להוריד ולהעלות קבצי CSV בעצמכם דרך
        `/import`.

!!! tip "השתמשו בייבוא אוטומטי מ-Gmail"
    תזמון כל חמשת הדוחות לשלוח מייל לחשבון Gmail מחובר אומר
    ש-Cat-Scan מייבא אותם אוטומטית כל יום. אין צורך בהעלאות ידניות
    לאחר ההגדרה הראשונית.

## אימות ההגדרה שלכם

לאחר ייבוא קבוצת ה-CSV הראשונה שלכם (ידנית או דרך Gmail):

1. עברו ל-`/import` ב-Cat-Scan.
2. בדקו את **Data Freshness Grid** — אמורים לראות "imported" עבור כל חמשת
   סוגי הדוחות לתאריך של אתמול.
3. אם תאים כלשהם מציגים "missing", הדוח המקביל טרם התקבל.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

כאשר כל חמש העמודות מציגות ירוק עבור אתמול, ל-Cat-Scan יש נתונים מלאים
וכל תכונה (משפך, ניתוח בזבוז, המלצות, אופטימייזר) תעבוד.

## זיהוי אוטומטי

אינכם צריכים לומר ל-Cat-Scan איזה דוח אתם מעלים. מערכת הייבוא
מזהה את סוג הדוח אוטומטית מכותרות העמודות:

- יש **Bid filtering reason**? -> Bid Filtering
- יש **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- יש **Bid requests** (ללא Publisher ID)? -> Pipeline -- Geo
- יש **Creative ID** + **Billing ID**? -> Quality
- יש **Creative ID** + **Bids in auction**? -> Bids in Auction

## כיצד Cat-Scan משתמש בכל מדד

זה ממפה את המדדים הגולמיים של CSV למה שאתם רואים ב-UI של Cat-Scan.

| תכונת UI | מדדים בשימוש | דוח/ות מקור |
|-----------|-------------|-------------|
| **משפך QPS** (דף הבית) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (שניהם) + Quality |
| **חישוב % בזבוז** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **שיעור ניצחון** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | כל דוח עם שניהם |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **שיעור viewability** | `Active View viewable / Active View measurable` | Quality |
| **שיעור השלמת וידאו** | `Video completions / Video starts` | Quality |
| **ניתוח בזבוז גיאו** (`/qps/geo`) | Bid requests, Impressions, Spend לפי Country | Pipeline -- Geo + Quality |
| **בזבוז מפרסמים** (`/qps/publisher`) | Bid requests, Impressions, Spend לפי Publisher | Pipeline -- Publisher + Quality |
| **בזבוז גודל** (`/qps/size`) | Impressions, Spend לפי Creative size | Quality |
| **סיבות סינון** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost לפי Filtering reason | Bid Filtering |
| **מדדי כרטיס תצורה** | Reached queries, Impressions, Spend לפי Billing ID | Quality |
| **ביצועי יצירה** | Impressions, Clicks, Spend, Active View viewable לכל Creative ID | Quality |
| **דירוג אופטימייזר** | כל מדדי pipeline + quality, מצטברים לפי סגמנט | כל חמשת הדוחות |

## טעויות נפוצות

| טעות | מה קורה | תיקון |
|------|---------|--------|
| הוספת "Bid requests" לדוח Quality | Google מחזיר שגיאה או נתונים חלקיים | הסירו "Bid requests" — אינו תואם ל-"Billing ID" |
| שכחת דוח Bid Filtering | Cat-Scan לא יכול להראות לכם *מדוע* הצעות נדחות | צרו את הדוח החמישי עם ממד "Filtering reason" |
| שימוש ב-"Last 7 days" במקום "Yesterday" | נתונים חופפים, קבצים גדולים יותר, ייבוא איטי יותר | הגדירו ל-"Yesterday" ותזמנו יומי |
| אי-תזמון — ייצוא ידני בלבד | הנתונים מתיישנים, בדיקות תקינות נכשלות | תזמנו מסירה יומית דרך מייל |
| חסר ממד "Hour" בדוחות Pipeline | אין גרנולריות שעתית בניתוח QPS | הוסיפו Hour ל-Pipeline -- Geo וPipeline -- Publisher |
| מדדים אופציונליים חסרים בדוח Quality | אין נתוני viewability או וידאו ב-Cat-Scan | הוסיפו Active View viewable, Active View measurable, Video starts, Video completions |

## צעדים הבאים

- [ניווט ניהול](02-navigating-the-dashboard.md): פריסת סרגל צד
  ורשימת תיוג הגדרה
- [ייבוא נתונים](09-data-import.md): מכניקת ייבוא מפורטת, העלאות
  מחולקות ופתרון תקלות
- [משפך QPS](03-qps-funnel.md): ברגע שהנתונים זורמים, התחילו לנתח

**עודכן לאחרונה:** יוני 2026  
חלק מהתיעוד הטכני של RTB.cat / Cat-Scan.
