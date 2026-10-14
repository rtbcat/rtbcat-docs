---
title: "Authorized Buyers RTB Glossary | Cat-Scan"
description: "Every RTB term in two views: how a media buyer sees it and how DevOps finds it in the system. Seat, QPS, waste, funnel, pretargeting, BYOM, and more."
---

# Glossary

Every term, two perspectives. The left column is how a media buyer thinks
about it. The right column is how a DevOps engineer finds it in the system.

| Term | Media buyer definition | DevOps / system definition |
|------|----------------------|---------------------------|
| **Seat** | A buyer account on Google Authorized Buyers. You scope your analysis and targeting per seat. | `buyer_account_id` in Postgres. Stored in `seats` table. Synced via `GET /seats`. |
| **QPS** | Queries Per Second: the maximum rate of bid requests you ask Google to send. Google throttles the actual volume based on your account tier. | Configured cap per pretargeting config. Actual inbound rate monitored via RTB funnel metrics in `rtb_daily`. |
| **Waste** | QPS consumed by bid requests your bidder rejects (wrong geos, wrong sizes, no matching creative). Money spent on nothing. | `(total_qps - bids_placed) / total_qps`. Computed from `rtb_daily` aggregates. Visible in funnel API. |
| **Pretargeting config** | The rules that control which bid requests reach your bidder. You get 10 per seat. Controls geos, sizes, formats, platforms, publishers. | Mutable entity synced from Google AB API. Stored in `pretargeting_configs`. Managed via `/settings/pretargeting`. Snapshots enable rollback. |
| **Funnel** | The progression from bid request to spend: QPS -> Bids -> Wins -> Impressions -> Clicks -> Spend. Each step has drop-off. | Computed from `rtb_daily` metrics. Served by `GET /analytics/rtb-funnel`. Frontend caches for 30 minutes. |
| **Creative** | An ad asset: image, video, HTML, or native. Has a format, size, destination URL, and performance history. | Row in `creatives` table. Thumbnails in blob storage. Synced from Google AB API. Performance from `rtb_daily` joins. |
| **Campaign** | A logical grouping of creatives. Used to organize analysis and reporting. | Row in `ai_campaigns` table. Many-to-many with creatives. Supports AI auto-clustering. |
| **Config card** | The UI panel showing a pretargeting config's state, max QPS, geos, sizes, formats, and platforms. | `PretargetingConfigCard` React component. Data from `GET /settings/pretargeting-configs`. |
| **Data freshness** | A grid showing which dates have imported data ("imported") vs. gaps ("missing") for each report type. | `GET /uploads/data-freshness`. Uses `generate_series + EXISTS` queries against `rtb_daily`, `rtb_bidstream`, `rtb_quality`, `rtb_bid_filtering`. 30s statement timeout. |
| **Import** | Getting CSV performance data into Cat-Scan, either by manual upload or Gmail auto-import. | CSV parsed, validated, deduplicated (via `row_hash` unique constraint), inserted into target tables. Chunked upload for files > 5MB. |
| **Rollback** | Reverting a pretargeting config change to its previous state. Preview with dry-run, then confirm. | Snapshot restore: reads `pretargeting_snapshots`, applies delta to Google AB API, records new snapshot. `POST /snapshots/rollback`. |
| **Optimizer / BYOM** | Automated system that scores segments and proposes config changes. Uses your own external model. | Score endpoint called via HTTP POST. Proposals stored in `optimizer_proposals`. Lifecycle: score -> propose -> approve -> apply. |
| **Workflow preset** | Safe, balanced, or aggressive. Controls how bold the optimizer's proposals are. | `canary_profile` parameter to score-and-propose API. Affects confidence thresholds and change magnitude limits. |
| **Effective CPM** | What you actually pay per thousand impressions, accounting for waste and infrastructure cost. | Computed in `OptimizerEconomicsService`. Combines spend data from `rtb_daily` with configured hosting cost. |
| **Conversion** | A valuable user action (purchase, signup) tracked after an impression. Fed back to optimize targeting. | Event ingested via pixel (`GET /conversions/pixel`) or webhook (`POST /conversions/webhook`). Stored in conversion tables. HMAC-verified for webhooks. |
| **Win rate** | Wins / Bids. How competitive your bids are in the auction. | `auction_wins / bids_placed` from `rtb_daily`. |
| **CTR** | Clicks / Impressions. How engaging your creatives are. | `clicks / impressions` from `rtb_daily`. |
| **Runtime health gate** | (Not a buyer term) | `v1-runtime-health-strict.yml` CI workflow. Runs end-to-end checks: API health, data health, conversions, optimizer, QPS SLO. Returns PASS/FAIL/BLOCKED per check. |
| **Contract check** | (Not a buyer term) | `scripts/contracts_check.py`. Validates data contracts (non-negotiable rules from import to API output). Runs post-deploy. Blocks release on failure. |
| **Cloud SQL Proxy** | (Not a buyer term) | Sidecar container providing authenticated access to Cloud SQL Postgres. Must be healthy before the API container starts. |
| **<AUTH_HEADER> header** | (Not a buyer term) | HTTP header set by OAuth2 Proxy after Google authentication. Trusted by the API when `OAUTH2_PROXY_ENABLED=true`. Stripped by nginx for external requests. |


## Agent access and publisher research terms

The new feature guides use these technical terms with the meanings below.

| Term | Meaning |
|---|---|
| **Agent API** | HTTP routes that give an external client access to specified Cat-Scan data. |
| **Agent token** | A secret credential that connects a client to a user identity and permitted operations. |
| **Token scope** | A permission for a specified group of API operations. |
| **Buyer permission** | A user's right to get data for a buyer account. |
| **MCP** | Model Context Protocol. A protocol that lets an AI client use specified application tools. |
| **Streamable HTTP** | The HTTP transport that this MCP server uses. |
| **Bridge** | Software that converts between two connector transports. |
| **Canonical spend** | Spend from the authoritative buyer reporting totals. |
| **Creative allocation** | The assignment of reporting totals to individual creatives. |
| **Reconciled allocation** | An allocation that agrees with the comparison totals under the service's rules. |
| **Cursor** | A value that identifies the next page of results. |
| **Publisher owner** | The organization declared as the owner of a publisher property. |
| **Publisher manager** | An organization declared as the manager of publisher inventory. |
| **Authorized seller** | A seller account listed in the publisher's ads file. |
| **Publisher profile** | Seller information visible through Google Marketplace. |
| **Partial result** | A result with missing or failed source sections. |
| **Truncation** | Omission of further entries because the result reached a stated limit. |
| **Revocation** | Removal of a token's ability to authorize a request. |
| **Release candidate** | A proposed release that has not passed all stable-release gates. |

For computer operations, **revoke** means to remove a token's access.
**Hash** means to calculate the stored digest of a token.
**Configure** means to set application parameters.
These meanings apply only to the stated computer operations.
