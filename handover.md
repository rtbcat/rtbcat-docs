# Handover — SEO / AEO work on docs.rtb.cat

**Date:** 2026-06-11
**Repo:** `rtbcat/rtbcat-docs` (MkDocs Material site → GitHub Pages → https://docs.rtb.cat)
**Working clone:** `/home/jen/Documents/rtbcat-docs`
**gcloud / GCP context:** active account `jen@rtb.cat`, project `gmail-company-os`

> This file documents in-progress work. It is internal scratch — **delete it (or exclude it) before/at the public commit** if you don't want it on the live repo. It is NOT linked from any nav.

---

## TL;DR of where things stand

1. **DONE & LIVE:** "Explainers" section (10 articles + index) — PR #1, merged, live at https://docs.rtb.cat/explainers/.
2. **DONE (uncommitted):** AEO `title:` + `description:` front-matter added to **all 34 English pages**. Verified the built HTML emits unique, optimized meta tags.
3. **DONE (uncommitted):** Fixed a real bug in the in-progress `mkdocs.yml` + added a `<title>` override (details below).
4. **⚠️ PENDING:** Final local build verification of the title override + freshness hook was **interrupted before it completed** — re-run it (exact command below) before committing.
5. **DECIDED, NOT YET EXECUTED:** Bundle **everything** into one branch + PR, then merge → auto-deploys.
6. **OPEN:** Google Search Console API access (one gcloud command from Jen), robots.txt, Open Graph/JSON-LD, translations.

---

## 1. What is committed / live already

- **PR #1** (merged): `docs/explainers/` (11 files) + nav in `mkdocs.yml` + callout/TOC in `docs/index.md`. Live and verified (all pages 200, cross-links resolve). The GitHub Pages deploy workflow (`.github/workflows/deploy.yml`) runs `mkdocs gh-deploy --force` on push to `main`.

## 2. Uncommitted changes in the working tree (this is the bundle to ship)

Run `git status` to see them. They are:

**a) Title + description front-matter on 34 pages** (the main task — see `seo/AGENT_PROMPT_optimize_titles_descriptions.md` for the original spec):
- 11 explainers: `docs/explainers/*.md`
- 23 manual/reference: `docs/index.md`, `docs/00..17-*.md`, `docs/api-reference.md`, `docs/faq.md`, `docs/glossary.md`
- Each file now starts with:
  ```yaml
  ---
  title: "<= 65 chars, head-term-first, e.g. 'QPS Funnel for Google Authorized Buyers | Cat-Scan'"
  description: "140-160 chars, atomic fact first, ends with a value cue"
  ---
  ```
- Applied by 4 parallel sub-agents over disjoint file sets. All titles ≤65, descriptions 140–160. Body text and H1s were **not** touched.
- **Verified:** built the site and confirmed each page emits unique `<title>` and `<meta name="description">`. This also fixed the earlier bug where every page shared the site-level description.

**b) `<title>` double-branding fix** (NEW file + 1 mkdocs.yml line):
- Problem: MkDocs Material auto-appends ` - {site_name}`, so our titles rendered as
  `QPS Funnel for Google Authorized Buyers | Cat-Scan - Cat-Scan Documentation` (redundant, ~73 chars).
- Fix: `overrides/main.html` overrides the `htmltitle` block so pages **with** a front-matter `title:` render it **verbatim** (no suffix); others keep default behaviour.
- Enabled via `theme.custom_dir: overrides` in `mkdocs.yml`.
- ⚠️ `custom_dir` is resolved **relative to the config file's directory** — keep any throwaway test configs in the repo root, not `/tmp`, or this path breaks.

**c) `mkdocs.yml` config-bug fix (IMPORTANT — was silently broken):**
- The concurrent edit had placed `git-revision-date-localized:` and a `- hooks:` block **after `nav:` at nav-indentation**, so YAML parsed them as **nav entries, not plugins/hooks**. MkDocs confirmed this with repeated `A reference to 'hooks/freshness.py' is included in the 'nav' configuration` warnings. Net effect: freshness badges, commit-SHA injection, and the enriched sitemap were **NOT running** (build still succeeded, features just inert).
- Fix applied:
  - Moved `git-revision-date-localized:` up into the `plugins:` block (after `- search`).
  - Removed the misplaced duplicate block that followed `nav:`.
  - Added `hooks/freshness.py` to the **top-level `hooks:`** list (next to `hooks/abbreviations.py`).
- After the fix, building the real config errors with *only* `"git-revision-date-localized" plugin is not installed` — which **proves the plugin is now correctly registered** (it just can't be pip-installed in the sandbox; see gotcha below).

**d) Concurrent edits by Jen (review but keep — part of the bundle):**
- `.github/workflows/deploy.yml`: adds `fetch-depth: 0` to checkout — **correct & required** so `git-revision-date-localized` can read per-file commit dates (shallow clone would break it).
- `requirements.txt`: adds `mkdocs-git-revision-date-localized>=1.2` — correct; CI installs it fine.
- `hooks/freshness.py` (new): injects commit SHA (`on_config`) and enriches `site/sitemap.xml` (`on_post_build`) with git `lastmod`, priorities (Explainers boosted to 0.9–0.95), `changefreq`, and image entries for screenshot pages. Looks sound.
  - Minor known limitation: for localized URLs (`/zh/...`, `/es/...`) it maps `loc` back to a source `.md` that doesn't exist (translations are fallbacks), so those get `default_priority` + `lastmod=now`. Not broken, just not ideal. Refine later if desired.

**e) `seo/` (new, untracked) — tooling I created for GSC access + the AEO prompt:**
- `seo/gsc.py` — Search Console API helper (auth, sites, query, pages, sitemaps, submit-sitemap, inspect). Falls back to gcloud ADC.
- `seo/requirements.txt`, `seo/.gitignore` (ignores `client_secret*.json`, `token.json`, `.venv/`, `__pycache__/`), `seo/AGENT_PROMPT_optimize_titles_descriptions.md` (the spec for task **a**), `seo/ideal-sitemap.xml` (reference artifact, Jen-authored).
- `seo/.venv/` and `seo/__pycache__/` are gitignored. **Decide** whether `seo/` belongs in the public repo at all (it contains an internal "how to optimize for AI models" prompt). I'd lean toward keeping it OUT of the public commit, or moving it to a private location.

---

## 3. ⚠️ FINISH THIS FIRST: complete the interrupted build verification

The last verification build was rejected before finishing. Run it to confirm the override + hook work end-to-end. Because the sandbox can't pip-install `git-revision-date-localized`, build a variant with **only that plugin stripped** (everything else identical), from the repo root:

```bash
cd /home/jen/Documents/rtbcat-docs
python3 -m venv .venv-build && .venv-build/bin/pip install "mkdocs-material>=9.5" "mkdocs-static-i18n>=1.2"

# make a temp config with ONLY the git-revision plugin block removed (3 lines + its comment)
python3 - <<'PY'
s=open('mkdocs.yml').read()
block='''  # Per-page freshness from git commits (for "Last updated" badges + accurate sitemap lastmod)
  - git-revision-date-localized:
      type: datetime
      fallback_to_build_date: true
'''
open('mkdocs.nogit.yml','w').write(s.replace(block,''))
PY

# build from repo root (custom_dir: overrides resolves relative to config location)
.venv-build/bin/mkdocs build -f mkdocs.nogit.yml -d /tmp/site_strip

# EXPECTED RESULTS:
#  - "[freshness hook] Enriched sitemap ..." line in output   (hook runs)
#  - grep -c "included in the 'nav'" => 0                      (nav-bug gone)
#  - title verbatim, no " - Cat-Scan Documentation" suffix:
grep -oiE "<title>[^<]*</title>" /tmp/site_strip/explainers/qps-funnel/index.html   # -> QPS Funnel for Google Authorized Buyers | Cat-Scan
grep -oE "<priority>[^<]*</priority>|<changefreq>[^<]*</changefreq>" /tmp/site_strip/sitemap.xml | sort | uniq -c   # sitemap enriched
```

If the title still shows the ` - Cat-Scan Documentation` suffix, check that `theme.custom_dir: overrides` is present and `overrides/main.html` exists.

**On the real CI / production build, do NOT strip anything** — the full `mkdocs.yml` is correct and CI can install `git-revision-date-localized`.

---

## 4. Cleanup before committing

- **Delete** `mkdocs.nogit.yml` (throwaway test config, repo root) — must NOT be committed.
- **Delete** `.venv-build/` (gitignored as `.venv/`? NO — it's `.venv-build`, so it is NOT ignored; remove it manually).
- Confirm `seo/.venv/` and `seo/__pycache__/` are not staged (they're covered by `seo/.gitignore`).
- Decide on `seo/` inclusion (see 2e).

## 5. Commit / deploy plan (decided: bundle everything)

```bash
cd /home/jen/Documents/rtbcat-docs
git checkout -b seo-titles-descriptions
git add docs/ mkdocs.yml requirements.txt .github/workflows/deploy.yml hooks/freshness.py overrides/
#   (+ `git add seo/` ONLY if you decided to publish it — see 2e)
git commit -m "AEO: per-page titles+descriptions, verbatim <title> override, fix git-revision/freshness plugin wiring"
git push -u origin seo-titles-descriptions
gh pr create ...
# merge → .github/workflows/deploy.yml runs `mkdocs gh-deploy --force` → live in ~1 min (+ GitHub Pages CDN lag)
```
After merge, verify a couple of pages' `<title>`/`<meta description>` on the live site, and confirm `https://docs.rtb.cat/sitemap.xml` now carries `<priority>`/`<changefreq>`/`<lastmod>`.

---

## 6. Open items / backlog

1. **Google Search Console API access (waiting on Jen, ~1 command).** The property `docs.rtb.cat` is added & verified. gcloud is `jen@rtb.cat` but its token lacks the `webmasters` scope. Jen needs to run, interactively:
   ```bash
   gcloud auth application-default login --scopes=openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters
   gcloud auth application-default set-quota-project gmail-company-os
   ```
   Then confirm + use:
   ```bash
   cd seo && .venv/bin/python gsc.py sites          # should list docs.rtb.cat
   .venv/bin/python gsc.py submit-sitemap           # submit https://docs.rtb.cat/sitemap.xml
   .venv/bin/python gsc.py query                     # top queries (will be near-empty for weeks — site is new)
   ```
   API gives: Search Analytics, sitemap status, URL inspection (~2k/day). It does NOT give full Index Coverage or field Core Web Vitals (export CSV for those).
2. **`robots.txt` is still missing** (`https://docs.rtb.cat/robots.txt` → 404). Add one referencing the sitemap (e.g. a `docs/robots.txt` copied verbatim, or via a hook). Quick win.
3. **Open Graph / Twitter Card / JSON-LD** not yet added (social sharing + AEO). Material's `social` plugin generates OG images (needs `pillow`+`cairosvg`); `TechArticle` JSON-LD on explainers is a nice-to-have.
4. **Weak H1s.** Many manual chapters still have generic `# Chapter X: ...` H1s. The sub-agents reported recommended head-term H1s but did NOT apply them (report-only). The recommendations are in the chat transcript; applying them changes visible headings (and anchor IDs) so do it deliberately.
5. **Thin pages in sitemap.** The `includes/abbreviations.*` partials build across all 11 locales and land in the sitemap. Consider `noindex`/excluding them.
6. **Translations.** Explainers are English-only (fallback) across the 10 non-English locales. Optional later work.

## 7. Environment gotchas (will save you time)

- **Sandbox pip CANNOT fetch `mkdocs-git-revision-date-localized`** ("No matching distribution / from versions: none"). `mkdocs-material` and `mkdocs-static-i18n` ARE available (pip cache). So local full builds must strip git-revision (see §3); CI is fine.
- **`pip install -r requirements.txt` fails entirely** in the sandbox because of the one unfetchable package (pip aborts all). Install `mkdocs-material` + `mkdocs-static-i18n` explicitly for local work.
- **`custom_dir` is relative to the config file** — test configs must live in the repo root.
- **Non-fatal build noise (safe to ignore):** a red Material "MkDocs 2.0" notice (vendor gag), the i18n language-switcher-vs-`navigation.instant` warning, and `abbreviations.*` "not in nav" notices. `--strict` fails on these, but the deploy uses non-strict `gh-deploy`, so they don't block.
- Build venv used this session: `.venv-build` (material + i18n only).
