---
title: "MCP and Agent API Access | Cat-Scan"
description: "Connect an AI client to eight read tools. Set buyer permissions, create an agent token, inspect data quality and remove access."
---

# MCP and Agent API access

Cat-Scan has an MCP server at `https://mcp.rtb.cat/mcp`.
MCP is the connection protocol that lets an AI client use specified application tools.
The server has eight read tools.
These tools cannot change bids, deals or pretargeting settings.
They do not give arbitrary SQL access.

The MCP server sends each request to the Agent API with the client's agent token.
The Agent API examines the token permissions and the user's current buyer permissions.
The MCP server does not store Google credentials or connect directly to the database.

## Available tools

| Tool | Function |
|---|---|
| `rtbcat_list_buyers` | Get the permitted buyers and their currencies. |
| `rtbcat_search_creatives` | Find creatives for one buyer. |
| `rtbcat_get_creative` | Get creative details and destination diagnostics. |
| `rtbcat_get_creative_asset` | Get asset reference URLs. The tool does not download the assets. |
| `rtbcat_get_daily_spend` | Get canonical daily spend for one buyer. |
| `rtbcat_get_creative_performance` | Get performance evidence for 1 to 100 creatives. |
| `rtbcat_check_data_quality` | Compare canonical spend with creative allocation. |
| `rtbcat_lookup_publisher` | Get current publisher, manager, seller and contact evidence. |

Reporting requests have a maximum date range of 90 days, including both end dates.
Creative search gives a maximum of 100 rows per page.
Use the returned cursor without changes to get the next page.

## Create an agent token

You need a Cat-Scan administrator session with the `sudo` role.
Create a separate token for each client or workflow.

1. Open **Admin → Agent tokens** at `/admin/agent-tokens`.
2. Select the user identity for the token.
3. Select the permitted buyer accounts.
4. Select the necessary permissions from the table below.
5. Set the expiry period.
6. Create the token.
7. Put the token in the client's secret store.

| Permission | Access |
|---|---|
| `agent:stats:read` | Buyer statistics, daily spend and data quality |
| `agent:creatives:read` | Creative search and details |
| `agent:creative-performance:read` | Creative performance |
| `agent:assets:read` | Creative asset references |
| `agent:publishers:read` | Publisher research |

The app shows the full token once.
Do not put the token in chat messages, source files or command arguments.
The database stores a hash of the token.

An explicit buyer list remains fixed.
Create a replacement token to add a buyer to that list.
For a user without the `sudo` role, `all_granted_buyers` follows the user's current buyer permissions.
Both modes apply the user's current permissions on each request.

## Connect a client

Use a client that supports authenticated Streamable HTTP.
Set the server URL to `https://mcp.rtb.cat/mcp`.
Configure the `Authorization` header with `Bearer` followed by the token.
Use the client's secret substitution function for the token value.

Client configuration formats can differ.
For a command-based Grok connector, use [Grok setup](20-grok-bot.md).

1. Ask the client to list the MCP tools.
2. Make sure that the list has the eight tools shown above.
3. Call `rtbcat_list_buyers`.
4. Make sure that the returned buyers agree with the token's permitted buyers.
5. Request data for one permitted buyer.

A tool list alone does not prove data access.
The result of an authenticated tool call supplies that evidence.

## Interpret reporting results

Keep each buyer's currency with its values.
Examine data freshness and missing dates before you use spend figures.
A buyer's `last_synced` value is not evidence of report freshness.

Canonical daily spend comes from the buyer's reporting totals.
Creative spend comes from allocation to individual creatives.
The MCP server withholds creative spend figures when that allocation is not reconciled.
The result then contains `spend_figures_withheld: true` and the allocation evidence.
Do not substitute zero for a withheld or missing value.

Creative performance does not include clicks.
It gives `clicks_available: false` and `total_clicks: null`.
Daily buyer totals can include clicks, but those clicks do not identify individual creatives.

Publisher research uses current external sources.
See [Publisher research](18-publisher-research.md) for source limits and partial results.

## Replace or remove access

For planned token replacement:

1. Create a replacement token before the old token expires.
2. Replace the token in the client's secret store.
3. Restart the client connector if necessary.
4. Call `rtbcat_list_buyers` to test access.
5. Revoke the old token in **Admin → Agent tokens**.

If a token is exposed, revoke that token immediately.
Revocation stops access on the next tool call.
It does not require a server restart.

## Fault isolation

| Result | Action |
|---|---|
| No tools | Examine the endpoint URL and client transport configuration. |
| Authentication failure | Examine token expiry and revocation status. |
| Access denied | Examine the token permissions and the user's buyer permissions. |
| HTTP 503 | Examine `CATSCAN_MCP_ENABLED` on the MCP service. |
| Public publisher evidence without Google evidence | Examine the Google status in the result. |

`GET /health` on the MCP host shows the service's enabled state.
A successful health response does not prove that the token can get data.

See the [API reference](https://docs.rtb.cat/api-reference/#agent-api-and-publisher-research) for direct HTTP routes.
