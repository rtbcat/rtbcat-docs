---
title: "Cat-Scan Architecture: API, MCP and Postgres"
description: "Cat-Scan runs on Hetzner. The dashboard and MCP server use the API. A separate Postgres host supplies reporting data. Google supplies external services."
---

# Chapter 11: Architecture

*Audience: System administrators and developers*

Production runs on Hetzner after the cutover on 1 August 2026.
The app host runs the API, dashboard and MCP containers.
A separate database host runs Postgres.
The previous GCP app and Cloud SQL source remain frozen.
Keep their writers, timers and schedulers stopped.

## Request paths

| Client | Path | Access control |
|---|---|---|
| Browser | HTTPS edge → dashboard and API → Postgres | App session and user permissions |
| MCP client | HTTPS edge → MCP server → Agent API | Agent token and current buyer permissions |
| Direct Agent API client | HTTPS edge → Agent API | Agent token and current buyer permissions |
| Publisher lookup | API → app stores, publisher websites and Google Marketplace | Buyer permission and the selected service account |

The [Grok connection diagram](20-grok-bot.md#connection-path) shows the command-based connector path.

## Service boundaries

| Service | Function |
|---|---|
| HTTPS edge | TLS termination and request routing |
| `rtbcat-dashboard` | Next.js user interface |
| `rtbcat-api` | Authentication, buyer permissions, data access and external requests |
| `rtbcat-mcp` | Eight read tools that use the Agent API |
| Postgres | Application data, reporting totals and calculated summaries |

The MCP process has no database connection or stored Google credential.
It sends the caller's token to the Agent API for each tool call.
The API applies both token limits and current user permissions.

The production Compose file binds service ports to the app host's loopback interface.
It uses verified TLS for the private Postgres connection.
Google service credentials remain on the API side of the connection.

## Data processing

The API uses calculated reporting tables for analytics requests.
Batch requests must not aggregate the large raw `rtb_daily` table.
Creative performance uses calculated creative data.
Canonical daily spend uses buyer totals.

The scheduler adds refresh requests to a job queue.
A worker processes one refresh job at a time under a database lock.
A scheduler response means that the queue accepted the request.
Use `/precompute/health` and the refresh ledger to determine completion.

BigQuery can hold raw archives and support batch operations.
It is not the database for interactive dashboard requests.
Publisher lookup gets current evidence from external sources.
It does not automatically save a publisher directory.

## Release controls

Production uses images with fixed digests for an exact source commit.
The build workflow produces the images and the release manifest.
The deployment script applies that manifest to the app host.
The API and MCP must come from the same release.

Do not deploy the old GCP application or start its writers.
Do not edit files inside production containers.
Use the current [Hetzner deployment scripts](https://github.com/jenbrannstrom/rtbcat-platform/tree/main/scripts/hetzner) for release and rollback operations.
Older deployment chapters can contain commands for the previous GCP system.

## Source directories

| Directory | Content |
|---|---|
| `api/routers/` | HTTP routes |
| `services/` | Application operations |
| `storage/` | Database access |
| `mcp_server/` | MCP tools and transport |
| `integrations/grok/` | Repository bridge in the release candidate |
| `dashboard/src/` | User interface |
| `deploy/hetzner/` | Production container configuration |
| `scripts/hetzner/` | Deployment and rollback commands |

See [MCP access](19-agent-access.md), [Publisher research](18-publisher-research.md) and [Integrations](17-integrations.md).
