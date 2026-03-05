# Setting Up Your CSV Reports

*Audience: media buyers, account managers*

Before Cat-Scan can analyze anything, it needs data. Google Authorized Buyers
has no Reporting API, so all data flows through **five scheduled CSV reports**
that you create once in your Google AB account.

!!! warning "Why five separate reports?"
    Google's reporting columns are not all compatible with each other. For
    example, "Bid requests" cannot appear in the same report as "Mobile app ID"
    or "Creative ID + Billing ID". To get full funnel visibility, you need five
    reports that Cat-Scan joins together automatically.

## The five reports at a glance

| # | Report name | What it tells Cat-Scan | Key columns |
|---|-------------|----------------------|-------------|
| 1 | **Quality** | Creative-level performance with viewability | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Creative-level bid pipeline (bids → wins) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline – Geo** | Full bidstream funnel by country | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline – Publisher** | Full bidstream funnel by publisher | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Why Google is rejecting your bids | Filtering reason, Bids, Opportunity cost |

## Step-by-step: creating each report

### 1. Quality report

This is your creative-level performance report with viewability and spend data.

**In Google Authorized Buyers → Reporting → New Report:**

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Suggested filename:** `catscan-quality`

!!! note
    This report must **not** include "Bid requests", "Bids", or "Bids in
    auction" — those columns are incompatible with "Billing ID" in Google's
    reporting.

---

### 2. Bids in Auction report

This report captures the bid pipeline at the creative level, filling in the
metrics that the Quality report cannot include.

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Suggested filename:** `catscan-bidsinauction`

!!! info "How Cat-Scan joins these"
    Quality + Bids in Auction are joined on `(Day, Creative ID)` to give you
    the full picture: from bids placed through impressions served and spend
    incurred.

---

### 3. Pipeline – Geo report

This is your top-of-funnel report: how many bid requests Google is sending you
per country, and how many survive each stage of the funnel.

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Suggested filename:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    Do **not** add Creative ID, Billing ID, or App ID to this report. These
    columns are incompatible with "Bid requests".

---

### 4. Pipeline – Publisher report

Same as Pipeline – Geo, but broken down by publisher instead of (or in
addition to) geography.

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Suggested filename:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Bid Filtering report

This report shows you *why* Google is filtering your bids before they enter the
auction — critical for diagnosing pretargeting issues.

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Suggested filename:** `catscan-bid-filtering`

---

## Scheduling delivery

For each of the five reports:

1. Click **Schedule** in Google Authorized Buyers.
2. Set frequency to **Daily**.
3. Set delivery method:
      - **Email** — send to the Gmail account connected to Cat-Scan (enables
        auto-import). See [Data Import](09-data-import.md) for Gmail
        auto-import setup.
      - **Manual** — if you prefer to download and upload CSVs yourself via
        `/import`.

!!! tip "Use Gmail auto-import"
    Scheduling all five reports to email a connected Gmail account means
    Cat-Scan imports them automatically every day. No manual uploads needed
    after the initial setup.

## Verifying your setup

After importing your first set of CSVs (manually or via Gmail):

1. Go to `/import` in Cat-Scan.
2. Check the **Data Freshness Grid** — you should see "imported" for all five
   report types for yesterday's date.
3. If any cells show "missing", the corresponding report hasn't been received
   yet.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Once all five columns show green for yesterday, Cat-Scan has full data and
every feature (funnel, waste analysis, recommendations, optimizer) will work.

## Auto-detection

You don't need to tell Cat-Scan which report you're uploading. The import
system detects the report type automatically from the column headers:

- Has **Bid filtering reason**? → Bid Filtering
- Has **Bid requests** + **Publisher ID**? → Pipeline – Publisher
- Has **Bid requests** (no Publisher ID)? → Pipeline – Geo
- Has **Creative ID** + **Billing ID**? → Quality
- Has **Creative ID** + **Bids in auction**? → Bids in Auction

## Common mistakes

| Mistake | What happens | Fix |
|---------|-------------|-----|
| Adding "Bid requests" to the Quality report | Google errors or returns incomplete data | Remove "Bid requests" — it's incompatible with "Billing ID" |
| Forgetting the Bid Filtering report | Cat-Scan can't show you *why* bids are rejected | Create the 5th report with "Filtering reason" dimension |
| Using "Last 7 days" instead of "Yesterday" | Overlapping data, larger files, slower imports | Set to "Yesterday" and schedule daily |
| Not scheduling — only manual exports | Data goes stale, health checks fail | Schedule daily delivery via email |

## Next steps

- [Navigating the Dashboard](02-navigating-the-dashboard.md): find your way
  around the UI
- [Data Import](09-data-import.md): detailed import mechanics, chunked
  uploads, and troubleshooting
- [QPS Funnel](03-qps-funnel.md): once data is flowing, start analyzing
