---
title: "تقارير CSV لـ Authorized Buyers: الخمسة التي تحتاجها Cat-Scan"
description: "لا توفر Google Authorized Buyers واجهة برمجية للتقارير، لذا تُعيد Cat-Scan بناء القمع من خمسة تقارير CSV مجدولة. مرجع كامل للمقاييس والأبعاد مع إرشادات الإعداد."
---

# إعداد تقارير CSV

*الجمهور المستهدف: مشترو الوسائط ومديرو الحسابات*

قبل أن تتمكن Cat-Scan من تحليل أي شيء، تحتاج إلى بيانات. لا توفر Google Authorized Buyers واجهة برمجية للتقارير (Reporting API)، لذا تتدفق جميع البيانات عبر **خمسة تقارير CSV مجدولة** تُنشئها مرة واحدة في حساب Google AB الخاص بك.

!!! warning "لماذا خمسة تقارير منفصلة؟"
    أعمدة التقارير في Google ليست متوافقة جميعها مع بعضها. فمثلاً، لا يمكن أن يظهر "Bid requests" في نفس التقرير مع "Mobile app ID" أو "Creative ID + Billing ID". للحصول على رؤية كاملة للقمع، تحتاج إلى خمسة تقارير تقوم Cat-Scan بربطها تلقائياً.

## الخمسة تقارير بنظرة عامة

| # | اسم التقرير | ما تخبره لـ Cat-Scan | الأعمدة الرئيسية |
|---|-------------|----------------------|------------------|
| 1 | **Quality** | الأداء على مستوى الإبداعية مع قابلية المشاهدة | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | مسار عروض الأسعار على مستوى الإبداعية (bids -> wins) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | قمع بيدستريم الكامل حسب الدولة | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | قمع بيدستريم الكامل حسب الناشر | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | سبب رفض Google لعروض أسعارك | Filtering reason, Bids, Opportunity cost |

---

## مرجع كامل للمقاييس

كل مقياس تستوعبه Cat-Scan، وما يعنيه، وأي تقرير يحمله.

### مقاييس القمع (مسار بيدستريم)

تتبع هذه المقاييس تقدم طلب عرض الأسعار عبر نظام مزاد Google. وهي موجودة في تقريري **Pipeline -- Geo** و**Pipeline -- Publisher**.

| المقياس | التعريف | الوحدة | التقرير/التقارير |
|---------|---------|--------|-----------------|
| **Bid requests** | إجمالي طلبات عروض الأسعار التي أرسلتها Google إلى نقطة نهاية مقدم العرض لديك. هذا هو الحجم الوارد الخام — أعلى القمع. يشمل الطلبات التي قد لا يكون مقدم العروض قد استجاب لها في الوقت المناسب. | عدد | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | طلبات عروض الأسعار التي وصلت فعلياً إلى مقدم العرض وحصلت على استجابة (ناجحة أم لا). أقل من "Bid requests" إذا كان مقدم العرض يعاني من مشكلات تأخر أو انتهاء مهلة. | عدد | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | الطلبات التي وجد فيها مقدم العرض مخزوناً إعلانياً مطابقاً (إبداعية تناسب الطلب). هذا هو المرشح الأول: إذا لم يكن لديك إبداعية للحجم/التنسيق المطلوب، يتوقف هنا. | عدد | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | الطلبات التي أعاد فيها مقدم العرض استجابة عرض أسعار صالحة وقابلة للتحليل (HTTP 200 بعرض أسعار منسق بشكل صحيح). يستثني انتهاء المهلة والأخطاء وعدم تقديم عروض. | عدد | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | استجابات عروض الأسعار الفعلية التي قدمها مقدم العرض. مجموعة فرعية من الاستجابات الناجحة — قد يستجيب مقدم العرض بنجاح لكنه يختار عدم تقديم عرض أسعار (استجابة no-bid). | عدد | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | العروض التي قبلتها Google في المزاد. يمكن رفض العروض قبل دخول المزاد بسبب قواعد التصفية (رفض الإبداعية، انتهاكات السياسات، سعر الحد الأدنى، استثناءات الاستهداف المسبق). الفجوة بين "Bids" و"Bids in auction" تظهر في تقرير Bid Filtering. | عدد | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | العروض التي فازت بالمزاد. أنت تدفع مقابل هذه. الفجوة بين "Bids in auction" و"Auctions won" هي المنافسة — مشترون آخرون تفوقوا عليك في العطاء. | عدد | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | الإعلانات التي عُرضت فعلياً في متصفح المستخدم أو تطبيقه بعد الفوز بالمزاد. أقل قليلاً من "Auctions won" بسبب فشل عرض الإعلان والتنقل في الصفحة قبل العرض وتدخل حاجب الإعلانات. | عدد | جميع التقارير الخمسة |
| **Clicks** | تفاعلات المستخدم (اللمس/النقر) على إعلاناتك المعروضة. | عدد | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### مقاييس الإنفاق والتكلفة

| المقياس | التعريف | الوحدة | التقرير/التقارير |
|---------|---------|--------|-----------------|
| **Spend** | إجمالي الأموال المنفقة على مرات الظهور الفائزة خلال الفترة. هذه هي تكلفة وسائطك الفعلية. مقومة بعملة حسابك (عادةً USD). | عملة (micros في البيانات الأولية، دولارات في واجهة المستخدم) | Quality |
| **Opportunity cost** | الإيرادات المقدرة التي خسرتها لأن Google صفّت عروض أسعارك قبل دخولها المزاد. تحسبها Google بناءً على معدلات الفوز التاريخية ومعدلات CPM لمخزون مماثل. مفيدة لتحديد أولويات أسباب التصفية التي يجب إصلاحها أولاً. | عملة | Bid Filtering |

### مقاييس الجودة وقابلية المشاهدة

هذه مقاييس على مستوى الإبداعية من تقرير **Quality**. تقيس ما يحدث *بعد* عرض مرة الظهور.

| المقياس | التعريف | الوحدة | التقرير/التقارير |
|---------|---------|--------|-----------------|
| **Active View viewable** | مرات الظهور التي استوفت معيار قابلية مشاهدة MRC: كانت 50% على الأقل من بكسلات الإعلان في المنطقة المرئية من المتصفح لمدة ثانية واحدة متواصلة على الأقل (ثانيتان للفيديو). هذا هو المعيار الصناعي لـ"هل شوهد هذا الإعلان فعلاً". | عدد | Quality |
| **Active View measurable** | مرات الظهور التي *أمكن* قياس قابلية مشاهدتها. بعض البيئات (تطبيقات معينة، iframes عبر النطاقات، متصفحات قديمة) تمنع القياس. معدل قابلية المشاهدة = Active View viewable / Active View measurable. | عدد | Quality |
| **Video starts** | عدد مرات بدء تشغيل إبداعية فيديو. لا يُملأ إلا لإبداعيات تنسيق الفيديو. | عدد | Quality |
| **Video completions** | عدد مرات تشغيل إبداعية الفيديو حتى الاكتمال 100% (أو حتى نقطة التخطي إذا كان قابلاً للتخطي). معدل اكتمال الفيديو = completions / starts. | عدد | Quality |

### مقاييس تصفية العروض

من تقرير **Bid Filtering**. هذه تخبرك *لماذا* يتم رفض العروض قبل دخولها المزاد.

| المقياس | التعريف | الوحدة | التقرير/التقارير |
|---------|---------|--------|-----------------|
| **Bids** | إجمالي العروض التي قدمها مقدم العرض (نفس التعريف السابق). في هذا التقرير، يُستخدم كمقام لحساب معدلات التصفية. | عدد | Bid Filtering |
| **Bids in auction** | العروض التي نجت من التصفية ودخلت المزاد. `Bids - Bids in auction` = إجمالي العروض المصفاة. | عدد | Bid Filtering |
| **Opportunity cost** | انظر مقاييس الإنفاق أعلاه. في هذا التقرير، مُفصَّل حسب سبب التصفية حتى تتمكن من رؤية أي سبب يكلفك أكثر. | عملة | Bid Filtering |

### الأبعاد (أعمدة التجميع)

الأبعاد ليست مقاييس — بل هي المحاور التي تُقسَّم عليها المقاييس. تستخدم Cat-Scan هذه الأبعاد لتقسيم بياناتك.

| البُعد | ما هو | التقارير التي تتضمنه |
|--------|-------|---------------------|
| **Day** | تاريخ التقويم (UTC). مطلوب في جميع التقارير. تستخدمه Cat-Scan لإزالة التكرار وعرض السلاسل الزمنية. | الخمسة جميعاً |
| **Hour** | ساعة اليوم (0--23، UTC). تتيح دقة ساعية في تحليل المسار. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | رمز الدولة المكون من حرفين وفق ISO (مثل US, DE, IL). المنشأ الجغرافي لطلب عرض الأسعار. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (اختياري) |
| **Billing ID (Pretargeting config)** | المعرّف الرقمي لتكوين الاستهداف المسبق الذي قبل هذه الحركة. يُعيّن 1:1 لبطاقة تكوين في Cat-Scan. | Quality |
| **Creative ID** | المعرّف الرقمي لـ Google للمادة الإبداعية. يرتبط بمعرض الإبداعيات في Cat-Scan. | Quality, Bids in Auction, Bid Filtering (اختياري) |
| **Creative size** | أبعاد البكسل للإبداعية (مثل `300x250`, `728x90`). يُستخدم لتحليل الهدر حسب الحجم. | Quality |
| **Creative format** | تنسيق الإعلان: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (اختياري) |
| **Platform** | منصة الجهاز: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (اختياري) |
| **Environment** | مكان عرض الإعلان: `WEB`, `APP`. | Quality (اختياري) |
| **App ID** | معرّف حزمة التطبيق المحمول (مثل `com.example.app`). لا يُملأ إلا للمخزون داخل التطبيق. | Quality (اختياري) |
| **App name** | اسم التطبيق مقروءاً للإنسان. | Quality (اختياري) |
| **Publisher ID** | المعرّف الرقمي للناشر (موقع ويب أو تطبيق). | Quality (اختياري), Pipeline -- Publisher |
| **Publisher name** | اسم الناشر مقروءاً للإنسان. | Quality (اختياري), Pipeline -- Publisher |
| **Publisher domain** | النطاق لموقع الناشر (مثل `news.example.com`). | Quality (اختياري) |
| **Buyer account ID** | معرّف حسابك / مقعدك كمشتري. مطلوب عند تشغيل مقاعد متعددة. | Bids in Auction, Bid Filtering (اختياري) |
| **Filtering reason** | رمز سبب رفض Google لعرض أسعارك قبل دخول المزاد (مثل `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## خطوة بخطوة: إنشاء كل تقرير

### 1. تقرير Quality

هذا هو تقرير أداء مستوى الإبداعية مع بيانات قابلية المشاهدة والإنفاق.

**في Google Authorized Buyers -> Reporting -> New Report:**

| الإعداد | القيمة |
|---------|--------|
| Report type | RTB |
| Time range | Yesterday (مجدول يومياً) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**اسم الملف المقترح:** `catscan-quality`

!!! note
    يجب أن **لا** يتضمن هذا التقرير "Bid requests" أو "Bids" أو "Bids in auction" — هذه الأعمدة غير متوافقة مع "Billing ID" في تقارير Google.

---

### 2. تقرير Bids in Auction

يلتقط هذا التقرير مسار عروض الأسعار على مستوى الإبداعية، ويملأ المقاييس التي لا يستطيع تقرير Quality تضمينها.

| الإعداد | القيمة |
|---------|--------|
| Report type | RTB |
| Time range | Yesterday (مجدول يومياً) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**اسم الملف المقترح:** `catscan-bidsinauction`

!!! info "كيف تربط Cat-Scan هذه التقارير"
    يتم ربط Quality + Bids in Auction على `(Day, Creative ID)` لمنحك الصورة الكاملة: من العروض المقدمة إلى مرات الظهور المقدمة والإنفاق المتكبد.

---

### 3. تقرير Pipeline -- Geo

هذا هو تقرير أعلى القمع: عدد طلبات عروض الأسعار التي ترسلها Google لك حسب الدولة، وكم منها يتجاوز كل مرحلة في القمع.

| الإعداد | القيمة |
|---------|--------|
| Report type | RTB |
| Time range | Yesterday (مجدول يومياً) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**اسم الملف المقترح:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **لا** تضف Creative ID أو Billing ID أو App ID إلى هذا التقرير. هذه الأعمدة غير متوافقة مع "Bid requests".

---

### 4. تقرير Pipeline -- Publisher

مثل Pipeline -- Geo، لكنه مُقسَّم حسب الناشر بدلاً من (أو بالإضافة إلى) الجغرافيا.

| الإعداد | القيمة |
|---------|--------|
| Report type | RTB |
| Time range | Yesterday (مجدول يومياً) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**اسم الملف المقترح:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. تقرير Bid Filtering

يُظهر هذا التقرير *لماذا* تُصفّي Google عروض أسعارك قبل دخولها المزاد — وهو أمر بالغ الأهمية لتشخيص مشكلات الاستهداف المسبق.

| الإعداد | القيمة |
|---------|--------|
| Report type | RTB |
| Time range | Yesterday (مجدول يومياً) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**اسم الملف المقترح:** `catscan-bid-filtering`

### أسباب التصفية الشائعة

هذه هي القيم التي ستراها في بُعد **Filtering reason**. كل منها يخبرك بسبب محدد لرفض Google لعرض أسعارك قبل دخول المزاد.

| سبب التصفية | ما يعنيه | ما يجب فعله |
|------------|---------|------------|
| `CREATIVE_NOT_APPROVED` | الإبداعية لم تجتز مراجعة Google، أو تم رفضها | تحقق من حالة الإبداعية في Google AB. أصلح انتهاكات السياسات. |
| `BID_BELOW_AUCTION_FLOOR` | سعر عرضك كان أدنى من الحد الأدنى لـ CPM لدى الناشر | ارفع العرض أو استبعد المخزون منخفض القيمة عبر الاستهداف المسبق |
| `DISAPPROVED_BY_EXCHANGE` | سياسة Google على مستوى التبادل حجبت العرض | راجع سياسات إعلانات Google للإبداعية المحددة |
| `FILTERED_BY_PRETARGETING` | قواعد استهدافك المسبق الخاصة استبعدت هذه الحركة | مقصود إذا كانت قواعدك صحيحة؛ راجع إذا كان غير متوقع |
| `NO_MATCHING_CREATIVE` | طلب عرض الأسعار يطلب حجماً/تنسيقاً لا تمتلكه | ارفع إبداعيات للأحجام المفقودة، أو استبعد تلك الأحجام في الاستهداف المسبق |
| `CREATIVE_SIZE_MISMATCH` | أبعاد الإبداعية لا تتطابق مع مساحة الإعلان | تحقق من حجم الإبداعية مقابل ما يطلبه الناشر |
| `LANDING_PAGE_DISAPPROVED` | عنوان URL الوجهة فشل في مراجعة Google | أصلح الصفحة المقصودة أو استخدم URL مختلفاً |
| `SSL_REQUIRED` | الناشر يتطلب HTTPS لكن إبداعيتك أو صفحتك المقصودة تستخدم HTTP | حوّل جميع الأصول وعناوين URL إلى HTTPS |
| `FREQUENCY_CAPPED` | رأى المستخدم هذه الإبداعية مرات كثيرة جداً | سلوك متوقع؛ اضبط حدود التكرار إذا كانت مقيدة جداً |

---

## جدولة التسليم

لكل واحد من التقارير الخمسة:

1. انقر على **Schedule** في Google Authorized Buyers.
2. اضبط التكرار على **Daily**.
3. اضبط طريقة التسليم:
      - **Email** — أرسل إلى حساب Gmail المتصل بـ Cat-Scan (يتيح الاستيراد التلقائي). انظر [استيراد البيانات](09-data-import.md) لإعداد الاستيراد التلقائي عبر Gmail.
      - **Manual** — إذا كنت تفضل تنزيل ورفع ملفات CSV بنفسك عبر `/import`.

!!! tip "استخدم الاستيراد التلقائي عبر Gmail"
    جدولة جميع التقارير الخمسة لإرسالها بالبريد الإلكتروني إلى حساب Gmail متصل يعني أن Cat-Scan تستوردها تلقائياً كل يوم. لا حاجة لرفع يدوي بعد الإعداد الأولي.

## التحقق من إعدادك

بعد استيراد مجموعتك الأولى من ملفات CSV (يدوياً أو عبر Gmail):

1. اذهب إلى `/import` في Cat-Scan.
2. تحقق من **Data Freshness Grid** — يجب أن تتعرف على "imported" لجميع أنواع التقارير الخمسة لتاريخ الأمس.
3. إذا أظهرت أي خلايا "missing"، فإن التقرير المقابل لم يُستلم بعد.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

بمجرد أن تعرض جميع الأعمدة الخمسة اللون الأخضر لتاريخ الأمس، تمتلك Cat-Scan بيانات كاملة وستعمل كل ميزة (القمع، تحليل الهدر، التوصيات، المحسّن).

## الاكتشاف التلقائي

لست بحاجة لإخبار Cat-Scan بالتقرير الذي تُحمّله. يكتشف نظام الاستيراد نوع التقرير تلقائياً من رؤوس الأعمدة:

- يحتوي على **Bid filtering reason**؟ -> Bid Filtering
- يحتوي على **Bid requests** + **Publisher ID**؟ -> Pipeline -- Publisher
- يحتوي على **Bid requests** (بدون Publisher ID)؟ -> Pipeline -- Geo
- يحتوي على **Creative ID** + **Billing ID**؟ -> Quality
- يحتوي على **Creative ID** + **Bids in auction**؟ -> Bids in Auction

## كيف تستخدم Cat-Scan كل مقياس

يربط هذا المقاييس الأولية لملفات CSV بما تراه في واجهة مستخدم Cat-Scan.

| ميزة واجهة المستخدم | المقاييس المستخدمة | تقرير/تقارير المصدر |
|--------------------|-------------------|---------------------|
| **قمع QPS** (الصفحة الرئيسية) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (كلاهما) + Quality |
| **حساب نسبة الهدر %** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **معدل الفوز** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | أي تقرير يحتوي على كليهما |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **معدل قابلية المشاهدة** | `Active View viewable / Active View measurable` | Quality |
| **معدل اكتمال الفيديو** | `Video completions / Video starts` | Quality |
| **تحليل الهدر الجغرافي** (`/qps/geo`) | Bid requests, Impressions, Spend by Country | Pipeline -- Geo + Quality |
| **هدر الناشر** (`/qps/publisher`) | Bid requests, Impressions, Spend by Publisher | Pipeline -- Publisher + Quality |
| **هدر الحجم** (`/qps/size`) | Impressions, Spend by Creative size | Quality |
| **أسباب التصفية** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost by Filtering reason | Bid Filtering |
| **مقاييس بطاقة التكوين** | Reached queries, Impressions, Spend by Billing ID | Quality |
| **أداء الإبداعية** | Impressions, Clicks, Spend, Active View viewable per Creative ID | Quality |
| **تسجيل نقاط المحسّن** | جميع مقاييس pipeline + quality، مُجمَّعة حسب الشريحة | الخمسة جميعاً |

## الأخطاء الشائعة

| الخطأ | ما يحدث | الحل |
|------|---------|------|
| إضافة "Bid requests" إلى تقرير Quality | تُعيد Google أخطاءً أو بيانات غير مكتملة | احذف "Bid requests" — فهو غير متوافق مع "Billing ID" |
| نسيان تقرير Bid Filtering | لا تستطيع Cat-Scan إظهار *لماذا* تُرفض العروض | أنشئ التقرير الخامس مع بُعد "Filtering reason" |
| استخدام "Last 7 days" بدلاً من "Yesterday" | بيانات متداخلة، ملفات أكبر، استيرادات أبطأ | اضبط على "Yesterday" وجدوله يومياً |
| عدم الجدولة — التصدير اليدوي فقط | تصبح البيانات قديمة، تفشل فحوصات الصحة | جدول التسليم اليومي عبر البريد الإلكتروني |
| غياب بُعد "Hour" في تقارير Pipeline | لا دقة ساعية في تحليل QPS | أضف Hour إلى Pipeline -- Geo وPipeline -- Publisher |
| غياب المقاييس الاختيارية في تقرير Quality | لا بيانات قابلية مشاهدة أو فيديو في Cat-Scan | أضف Active View viewable, Active View measurable, Video starts, Video completions |

## الخطوات التالية

- [التنقل الإداري](02-navigating-the-dashboard.md): تخطيط الشريط الجانبي وقائمة مراجعة الإعداد
- [استيراد البيانات](09-data-import.md): آليات الاستيراد التفصيلية والرفع المجزأ واستكشاف الأخطاء
- [قمع QPS](03-qps-funnel.md): بمجرد تدفق البيانات، ابدأ التحليل
