# Chapter 1: Login Errors

*Audience: everyone*

Cat-Scan supports three login methods: **Google OAuth** (most users),
**Authing OIDC** (organizations using Authing), and **email/password**
(local accounts created by an admin). If login works, there's nothing to
read here. This page is for when it doesn't.

## The seat selector

After logging in, the sidebar shows a **seat selector** at the top.

- **Single seat**: shows your seat name and ID directly.
- **Multiple seats**: a dropdown lets you switch. Each entry shows the buyer
  display name, the `buyer_account_id`, and a creative count.
- **"Sync All" button**: refreshes creatives, endpoints, and pretargeting
  configs from Google's API for the selected seat.

## Diagnosing login failures

| Symptom | Likely cause | What to do |
|---------|-------------|------------|
| Redirect loop (page keeps reloading) | Database unreachable — the auth check fails silently, returns `{authenticated: false}`, frontend redirects back to login | Check Cloud SQL Proxy container. See [Troubleshooting](15-troubleshooting.md). |
| "Server unavailable" (502 / 503 / 504) | API or nginx container is down | Contact your DevOps team. See [Health Monitoring](13-health-monitoring.md). |
| "Authentication required" after being idle | Session expired or cookie cleared | Sign in again. Sessions expire after the configured TTL. |
| "You don't have access to this buyer account" | Your user exists but has no permissions for this seat | Ask your administrator to grant seat access. See [User Administration](16-user-admin.md). |
| Login button does nothing / blank page | OAuth2 Proxy misconfigured or unreachable | DevOps should verify `OAUTH2_PROXY_ENABLED=true` and that the proxy container is running. |
| "Invalid credentials" on email/password | Wrong password, or the local account doesn't exist | Reset via admin panel, or ask the admin who created the account. |

## The redirect-loop problem in detail

This is the most common login failure and deserves its own section.

**Root cause pattern:** Any database failure causes
`_get_or_create_oauth2_user()` to fail silently. `/auth/check` then returns
`{authenticated: false}`. The frontend redirects to `/oauth2/sign_in`. OAuth
succeeds, but the DB write fails again. Loop.

**How Cat-Scan detects it (since Feb 2026):**

1. The API propagates DB errors via `request.state.auth_error`.
2. `/auth/check` returns HTTP 503 (not 200) when the database is unreachable.
3. The frontend counts redirects (max 2 in 30 seconds) and shows an
   error/retry UI instead of looping forever.

**Common triggers:**

- Cloud SQL Proxy container died or was recreated without restarting the API.
- Network partition between the VM and Cloud SQL.
- Postgres connection limit exhausted.

**Fix:**

1. Check Cloud SQL Proxy: `sudo docker ps | grep cloudsql`
2. If it's not running: `sudo docker compose restart cloudsql-proxy`
3. Wait 10 seconds, then restart the API: `sudo docker compose restart api`
4. Verify: `curl -sS http://localhost:8000/health`

See [Troubleshooting: Login Loop](15-troubleshooting.md) for the full
diagnostic flowchart.

## Next steps

- [Setting Up CSV Reports](02-setting-up-csv-reports.md): create the five
  reports Cat-Scan needs
- [Admin Navigation](02-navigating-the-dashboard.md): sidebar layout,
  restricted users, setup checklist
