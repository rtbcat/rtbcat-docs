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
| 2 | **Bids in Auction** | Creative-level bid pipeline (bids -> wins) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Full bidstream funnel by country | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Full bidstream funnel by publisher | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Why Google is rejecting your bids | Filtering reason, Bids, Opportunity cost |

---

## Complete metrics reference

Every metric that Cat-Scan ingests, what it means, and which report carries it.

### Funnel metrics (bidstream pipeline)

These track the progression of a bid request through Google's auction system.
Present in the **Pipeline -- Geo** and **Pipeline -- Publisher** reports.

| Metric | Definition | Unit | Report(s) |
|--------|-----------|------|-----------|
| **Bid requests** | Total bid requests Google sent to your bidder endpoint. This is the raw inbound volume -- the top of the funnel. Includes requests your bidder may not have responded to in time. | count | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Bid requests that actually reached your bidder and got a response (successful or not). Lower than "Bid requests" if your bidder has latency issues or timeouts. | count | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Requests where your bidder found matching inventory (a creative that fits the request). This is the first filter: if you have no creative for the requested size/format, it stops here. | count | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Requests where your bidder returned a valid, parseable bid response (HTTP 200 with a well-formed bid). Excludes timeouts, errors, and no-bids. | count | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Actual bid responses your bidder placed. A subset of successful responses -- your bidder may respond successfully but choose not to bid (no-bid response). | count | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Bids that Google accepted into the auction. Bids can be rejected before auction entry due to filtering rules (creative disapproval, policy violations, floor price, pretargeting exclusions). The gap between "Bids" and "Bids in auction" is shown in the Bid Filtering report. | count | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Bids that won the auction. You pay for these. The gap between "Bids in auction" and "Auctions won" is competition -- other buyers outbid you. | count | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Ads actually rendered in a user's browser or app after winning the auction. Slightly less than "Auctions won" due to ad rendering failures, page navigations before render, and ad blocker interference. | count | All five reports |
| **Clicks** | User interactions (taps/clicks) on your served ads. | count | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Spend and cost metrics

| Metric | Definition | Unit | Report(s) |
|--------|-----------|------|-----------|
| **Spend** | Total money spent on won impressions for the period. This is your actual media cost. Denominated in your account's currency (usually USD). | currency (micros in raw data, dollars in UI) | Quality |
| **Opportunity cost** | Estimated revenue you lost because Google filtered your bids before they entered the auction. Calculated by Google based on historical win rates and CPMs for similar inventory. Useful for prioritizing which filtering reasons to fix first. | currency | Bid Filtering |

### Quality and viewability metrics

These are creative-level metrics from the **Quality** report. They measure
what happens *after* the impression is served.

| Metric | Definition | Unit | Report(s) |
|--------|-----------|------|-----------|
| **Active View viewable** | Impressions that met the MRC viewability standard: at least 50% of the ad's pixels were in the viewable area of the browser for at least 1 continuous second (2 seconds for video). This is the industry standard for "was this ad actually seen." | count | Quality |
| **Active View measurable** | Impressions where viewability *could* be measured. Some environments (certain apps, cross-domain iframes, older browsers) block measurement. Viewability rate = Active View viewable / Active View measurable. | count | Quality |
| **Video starts** | Number of times a video creative began playing. Only populated for video format creatives. | count | Quality |
| **Video completions** | Number of times a video creative played to 100% completion (or to the skip point if skippable). Video completion rate = completions / starts. | count | Quality |

### Bid filtering metrics

From the **Bid Filtering** report. These tell you *why* bids are being
rejected before they enter the auction.

| Metric | Definition | Unit | Report(s) |
|--------|-----------|------|-----------|
| **Bids** | Total bids your bidder placed (same definition as above). In this report, used as the denominator to calculate filtering rates. | count | Bid Filtering |
| **Bids in auction** | Bids that survived filtering and entered the auction. `Bids - Bids in auction` = total filtered bids. | count | Bid Filtering |
| **Opportunity cost** | See spend metrics above. In this report, broken down per filtering reason so you can see which reason costs you the most. | currency | Bid Filtering |

### Dimensions (grouping columns)

Dimensions are not metrics -- they are the axes along which metrics are broken
down. Cat-Scan uses these to slice your data.

| Dimension | What it is | Which reports |
|-----------|-----------|---------------|
| **Day** | Calendar date (UTC). Required in all reports. Cat-Scan uses this for deduplication and time-series display. | All five |
| **Hour** | Hour of day (0--23, UTC). Enables hourly granularity in pipeline analysis. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Two-letter ISO country code (e.g., US, DE, IL). The geographic origin of the bid request. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (optional) |
| **Billing ID (Pretargeting config)** | Numeric ID of the pretargeting config that accepted this traffic. Maps 1:1 to a config card in Cat-Scan. | Quality |
| **Creative ID** | Google's numeric ID for the creative asset. Links to the Creatives gallery in Cat-Scan. | Quality, Bids in Auction, Bid Filtering (optional) |
| **Creative size** | Pixel dimensions of the creative (e.g., `300x250`, `728x90`). Used for size-based waste analysis. | Quality |
| **Creative format** | The ad format: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (optional) |
| **Platform** | Device platform: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (optional) |
| **Environment** | Where the ad was served: `WEB`, `APP`. | Quality (optional) |
| **App ID** | Mobile app bundle ID (e.g., `com.example.app`). Only populated for in-app inventory. | Quality (optional) |
| **App name** | Human-readable app name. | Quality (optional) |
| **Publisher ID** | Numeric ID of the publisher (website or app). | Quality (optional), Pipeline -- Publisher |
| **Publisher name** | Human-readable publisher name. | Quality (optional), Pipeline -- Publisher |
| **Publisher domain** | The domain of the publisher's website (e.g., `news.example.com`). | Quality (optional) |
| **Buyer account ID** | Your buyer account / seat ID. Needed when you run multiple seats. | Bids in Auction, Bid Filtering (optional) |
| **Filtering reason** | Google's reason code for why a bid was filtered out before entering the auction (e.g., `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Step-by-step: creating each report

### 1. Quality report

This is your creative-level performance report with viewability and spend data.

**In Google Authorized Buyers -> Reporting -> New Report:**

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
    auction" -- those columns are incompatible with "Billing ID" in Google's
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

### 3. Pipeline -- Geo report

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

### 4. Pipeline -- Publisher report

Same as Pipeline -- Geo, but broken down by publisher instead of (or in
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
auction -- critical for diagnosing pretargeting issues.

| Setting | Value |
|---------|-------|
| Report type | RTB |
| Time range | Yesterday (scheduled daily) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Suggested filename:** `catscan-bid-filtering`

### Common filtering reasons

These are the values you'll see in the **Filtering reason** dimension. Each
one tells you a specific reason Google rejected your bid before auction entry.

| Filtering reason | What it means | What to do |
|-----------------|--------------|------------|
| `CREATIVE_NOT_APPROVED` | The creative hasn't passed Google's review, or was disapproved | Check creative status in Google AB. Fix policy violations. |
| `BID_BELOW_AUCTION_FLOOR` | Your bid price was below the publisher's minimum CPM | Raise bid or exclude low-value inventory via pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | Google's exchange-level policy blocked the bid | Review Google's ad policies for the specific creative |
| `FILTERED_BY_PRETARGETING` | Your own pretargeting rules excluded this traffic | Intentional if your rules are correct; review if unexpected |
| `NO_MATCHING_CREATIVE` | The bid request asked for a size/format you don't have | Upload creatives for the missing sizes, or exclude those sizes in pretargeting |
| `CREATIVE_SIZE_MISMATCH` | Creative dimensions don't match the ad slot | Check creative size vs. what the publisher requests |
| `LANDING_PAGE_DISAPPROVED` | The destination URL failed Google's review | Fix the landing page or use a different URL |
| `SSL_REQUIRED` | Publisher requires HTTPS but your creative or landing page uses HTTP | Switch all assets and URLs to HTTPS |
| `FREQUENCY_CAPPED` | User has already seen this creative too many times | Expected behavior; adjust frequency caps if too aggressive |

---

## Scheduling delivery

For each of the five reports:

1. Click **Schedule** in Google Authorized Buyers.
2. Set frequency to **Daily**.
3. Set delivery method:
      - **Email** -- send to the Gmail account connected to Cat-Scan (enables
        auto-import). See [Data Import](09-data-import.md) for Gmail
        auto-import setup.
      - **Manual** -- if you prefer to download and upload CSVs yourself via
        `/import`.

!!! tip "Use Gmail auto-import"
    Scheduling all five reports to email a connected Gmail account means
    Cat-Scan imports them automatically every day. No manual uploads needed
    after the initial setup.

## Verifying your setup

After importing your first set of CSVs (manually or via Gmail):

1. Go to `/import` in Cat-Scan.
2. Check the **Data Freshness Grid** -- you should see "imported" for all five
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

- Has **Bid filtering reason**? -> Bid Filtering
- Has **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- Has **Bid requests** (no Publisher ID)? -> Pipeline -- Geo
- Has **Creative ID** + **Billing ID**? -> Quality
- Has **Creative ID** + **Bids in auction**? -> Bids in Auction

## How Cat-Scan uses each metric

This maps raw CSV metrics to what you see in the Cat-Scan UI.

| UI feature | Metrics used | Source report(s) |
|-----------|-------------|-----------------|
| **QPS funnel** (home page) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (both) + Quality |
| **Waste % calculation** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Win rate** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Any report with both |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Viewability rate** | `Active View viewable / Active View measurable` | Quality |
| **Video completion rate** | `Video completions / Video starts` | Quality |
| **Geo waste analysis** (`/qps/geo`) | Bid requests, Impressions, Spend by Country | Pipeline -- Geo + Quality |
| **Publisher waste** (`/qps/publisher`) | Bid requests, Impressions, Spend by Publisher | Pipeline -- Publisher + Quality |
| **Size waste** (`/qps/size`) | Impressions, Spend by Creative size | Quality |
| **Filtering reasons** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost by Filtering reason | Bid Filtering |
| **Config card metrics** | Reached queries, Impressions, Spend by Billing ID | Quality |
| **Creative performance** | Impressions, Clicks, Spend, Active View viewable per Creative ID | Quality |
| **Optimizer scoring** | All pipeline + quality metrics, aggregated by segment | All five |

## Common mistakes

| Mistake | What happens | Fix |
|---------|-------------|-----|
| Adding "Bid requests" to the Quality report | Google errors or returns incomplete data | Remove "Bid requests" -- it's incompatible with "Billing ID" |
| Forgetting the Bid Filtering report | Cat-Scan can't show you *why* bids are rejected | Create the 5th report with "Filtering reason" dimension |
| Using "Last 7 days" instead of "Yesterday" | Overlapping data, larger files, slower imports | Set to "Yesterday" and schedule daily |
| Not scheduling -- only manual exports | Data goes stale, health checks fail | Schedule daily delivery via email |
| Missing "Hour" dimension on Pipeline reports | No hourly granularity in QPS analysis | Add Hour to Pipeline -- Geo and Pipeline -- Publisher |
| Missing optional metrics on Quality report | No viewability or video data in Cat-Scan | Add Active View viewable, Active View measurable, Video starts, Video completions |

## Next steps

- [Admin Navigation](02-navigating-the-dashboard.md): sidebar layout and
  setup checklist
- [Data Import](09-data-import.md): detailed import mechanics, chunked
  uploads, and troubleshooting
- [QPS Funnel](03-qps-funnel.md): once data is flowing, start analyzing
