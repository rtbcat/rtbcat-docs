#!/usr/bin/env python3
"""Google Search Console helper for docs.rtb.cat.

Auth model: OAuth "installed app" (Desktop) flow.
  - First run does a one-time browser consent and saves token.json (refresh token).
  - Every later run is headless — no browser needed.

Setup (one time, in Google Cloud Console for any project you own):
  1. Enable the "Google Search Console API" (searchconsole.googleapis.com).
  2. APIs & Services -> Credentials -> Create Credentials -> OAuth client ID.
       Application type: Desktop app.
  3. Download the JSON, save it next to this file as: client_secret.json
  4. Make sure the Google account you'll consent with has access to the
     docs.rtb.cat property in Search Console.

Then:
  pip install -r requirements.txt
  python gsc.py auth                 # one-time browser consent -> token.json
  python gsc.py sites                # sanity check: list properties you can see
  python gsc.py query                # top search queries (last 28 days)
  python gsc.py pages                # top landing pages
  python gsc.py sitemaps             # sitemap submission status
  python gsc.py submit-sitemap       # (re)submit https://docs.rtb.cat/sitemap.xml
  python gsc.py inspect <url>        # URL Inspection: index status for one URL

All output is JSON on stdout so it's easy to pipe / hand back to Claude.
"""
import argparse
import json
import os
import sys

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET = os.path.join(HERE, "client_secret.json")
TOKEN = os.path.join(HERE, "token.json")
# webmasters scope = read perf data + write (submit sitemaps). Use readonly if you
# prefer least-privilege and don't need submit-sitemap.
SCOPES = ["https://www.googleapis.com/auth/webmasters"]
SITE = os.environ.get("GSC_SITE", "https://docs.rtb.cat/")


QUOTA_PROJECT = os.environ.get("GSC_QUOTA_PROJECT", "gmail-company-os")


def creds():
    # 1) Desktop-OAuth token (token.json) if present.
    if os.path.exists(TOKEN):
        c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
        if c.expired and c.refresh_token:
            c.refresh(Request())
            with open(TOKEN, "w") as f:
                f.write(c.to_json())
        return c
    # 2) Desktop-OAuth client_secret.json -> run consent flow once.
    if os.path.exists(CLIENT_SECRET):
        c = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES).run_local_server(port=0)
        with open(TOKEN, "w") as f:
            f.write(c.to_json())
        return c
    # 3) Fall back to gcloud Application Default Credentials.
    #    Requires:  gcloud auth application-default login --scopes=...,webmasters
    import google.auth
    c, _ = google.auth.default(scopes=SCOPES)
    if QUOTA_PROJECT and hasattr(c, "with_quota_project"):
        c = c.with_quota_project(QUOTA_PROJECT)
    return c


def search_console():
    return build("searchconsole", "v1", credentials=creds(), cache_discovery=False)


def out(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def cmd_auth(_):
    creds()
    print("OK — token.json written. You're authenticated.")


def cmd_sites(_):
    out(search_console().sites().list().execute())


def _analytics(dimensions, days, row_limit=100):
    import datetime
    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    return search_console().searchanalytics().query(siteUrl=SITE, body=body).execute()


def cmd_query(a):
    out(_analytics(["query"], a.days, a.limit))


def cmd_pages(a):
    out(_analytics(["page"], a.days, a.limit))


def cmd_sitemaps(_):
    out(search_console().sitemaps().list(siteUrl=SITE).execute())


def cmd_submit_sitemap(a):
    feed = a.url or (SITE.rstrip("/") + "/sitemap.xml")
    search_console().sitemaps().submit(siteUrl=SITE, feedpath=feed).execute()
    print(f"Submitted sitemap: {feed}")


def cmd_inspect(a):
    body = {"inspectionUrl": a.url, "siteUrl": SITE}
    out(search_console().urlInspection().index().inspect(body=body).execute())


def main():
    p = argparse.ArgumentParser(description="Search Console helper for docs.rtb.cat")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("auth").set_defaults(func=cmd_auth)
    sub.add_parser("sites").set_defaults(func=cmd_sites)

    q = sub.add_parser("query"); q.add_argument("--days", type=int, default=28); q.add_argument("--limit", type=int, default=100); q.set_defaults(func=cmd_query)
    pg = sub.add_parser("pages"); pg.add_argument("--days", type=int, default=28); pg.add_argument("--limit", type=int, default=100); pg.set_defaults(func=cmd_pages)

    sub.add_parser("sitemaps").set_defaults(func=cmd_sitemaps)
    ss = sub.add_parser("submit-sitemap"); ss.add_argument("url", nargs="?"); ss.set_defaults(func=cmd_submit_sitemap)
    ins = sub.add_parser("inspect"); ins.add_argument("url"); ins.set_defaults(func=cmd_inspect)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
