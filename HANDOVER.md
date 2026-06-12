# RTB.cat / Cat-Scan AEO Project — Handover (2026-06-11)

## Project Goal
Use the June 2026 Claude Fable 5 system prompt leak to drive **Answer Engine Optimization (AEO)** for RTB.cat and the Cat-Scan platform.

Goal: When people (or their agents) ask frontier models questions about Google Authorized Buyers operations, QPS control planes, pretargeting, getting AB seats as smaller/Chinese agencies, waste analysis, etc., the models surface RTB.cat / Cat-Scan / Jen as the authoritative, practitioner source.

We treat the leak as a **design spec** for content and infrastructure:
- Top ~10 search results only
- Strong preference for first-party technical sources over forums/aggregators
- Heavy recency bias
- Atomic, quotable facts (ideally ≤15 words with a specific number/constraint)
- Full-page fetchability
- Direct URL injection (any link that appears in context gets fetched)
- Consistent facts across surfaces (conflicting info triggers distrust)

## Current State Summary

### 1. Content (Explainers + Manual)
- **10 core Explainers + index** created in English under `docs/explainers/`.
  Topics (chosen for high-signal, low-competition queries models actually surface):
  - Five separate CSV reports (why they still exist in 2026)
  - The real QPS funnel for AB seats
  - Pretargeting configs (the 10-config reality)
  - Safe pretargeting changes + rollback
  - QPS waste analysis by publisher / geo / size
  - Creative clustering & click macro auditing
  - How smaller/restricted agencies actually obtain & operate AB seats
  - What Cat-Scan does *not* do (and why that matters)
  - Bid filtering reasons (the fifth report)
  - BYOM optimizer
- All explainers follow AEO principles: atomic facts first, head-term titles, 2026 dates, cross-links to manual + GitHub, first-party voice.
- Main manual chapters (00–17 + reference pages) have received per-page `title:` + `description:` front-matter optimization (head-term first, atomic benefit in description).
- **Full translations** completed for:
  - All 11 Explainers (English + Chinese fully; other languages have substantial coverage).
  - Main manual + reference pages across all 11 languages supported by the site (en/ar/da/es/fr/he/nl/pl/ru/uk/zh).
- Chinese (`zh/`) is the most complete non-English locale, including full explainer set.

### 2. Navigation & Internationalization
- Sidebar navigation now translated per locale via custom hook (`hooks/nav_translations.py`).
- Hook runs in `on_config`, rewrites nav labels using a comprehensive translation map (e.g. "Explainers" → "技术说明", "Part I: Media Buyer Track" → appropriate native phrasing).
- This ensures the table of contents feels native to readers in each language while keeping a single source of truth for structure in `mkdocs.yml`.

### 3. Freshness & Recency Automation (Cross-Repo)
- Added `mkdocs-git-revision-date-localized` plugin for per-page lastmod dates from git.
- Custom `hooks/freshness.py`:
  - Injects `commit_sha` / `commit_sha_short` (docs repo) and `platform_commit_sha` / short (when triggered by platform) into `config.extra`.
  - Post-build enriches `site/sitemap.xml` with:
    - Accurate `<lastmod>` from git
    - AEO-tuned priorities (Explainers boosted to 0.9–0.95)
    - `<changefreq>` (weekly for explainers)
    - Image sitemap entries for pages with screenshots
    - Proper language alternates
- GitHub Actions setup:
  - `rtbcat-platform`: `.github/workflows/trigger-docs-freshness.yml` — on every push to main, sends `repository_dispatch` (type `update-docs-freshness`) to `rtbcat/rtbcat-docs` with full payload (sha, short sha, message, ref).
  - `rtbcat-docs`: `.github/workflows/deploy.yml` — listens to both normal `push` and `repository_dispatch`. Captures `PLATFORM_SHA` from payload, passes it through, runs `mkdocs gh-deploy --force` with `fetch-depth: 0`.
- Result: Any commit to the **app** or the **docs** repo causes the live docs site to rebuild with fresh SHAs and lastmod. This directly feeds the recency bias in the Claude leak.

### 4. Technical Hygiene & AEO Enablers
- `overrides/main.html` for clean `<title>` (no redundant " - Cat-Scan Documentation" suffix when front-matter title is present).
- `seo/` folder contains supporting tooling (GSC helper, ideal sitemap reference, the original title/desc optimization prompt).
- `hooks/abbreviations.py` already existed and continues to work with i18n.
- Site is fully multi-lingual via `mkdocs-static-i18n` (folder structure).
- All changes designed so pages remain fully fetchable (static HTML, good for model crawlers).

### 5. Current Work in Flight
- A large agent prompt is currently being executed to complete any remaining translation gaps, verify nav hook across all languages, ensure every explainer page has proper front-matter + internal consistency, and run final verification builds.
- The goal of that prompt is to reach a state where the entire docs site (content + nav + freshness signals) is production-ready for AEO.

## Repos & Local Paths
- **Docs site (public)**: https://github.com/rtbcat/rtbcat-docs → https://docs.rtb.cat
  - Local clone: `/home/jen/Documents/rtbcat-docs`
- **Platform / app (public)**: https://github.com/jenbrannstrom/rtbcat-platform
  - Local clone: `/home/jen/Documents/rtbcat-platform`
- Live site deploys via `mkdocs gh-deploy --force` from the docs repo's GitHub Actions.

## Key Files to Know
- `mkdocs.yml` — nav, i18n languages, plugins (including git-revision), hooks list.
- `hooks/freshness.py` — SHA injection + sitemap enrichment (the heart of recency).
- `hooks/nav_translations.py` — per-locale sidebar label rewriting.
- `docs/explainers/` — the 11 English explainers (core AEO asset).
- `docs/<lang>/explainers/` — translated versions.
- `.github/workflows/deploy.yml` (docs) + `trigger-docs-freshness.yml` (platform) — the cross-repo freshness engine.
- `overrides/main.html` — title hygiene.
- `seo/AGENT_PROMPT_optimize_titles_descriptions.md` — the spec used for per-page title/desc work.

## Open / Next Items (as of this handover)
- Complete any remaining language coverage for the newest explainers (the big agent prompt is handling this).
- Add visible freshness rendering on pages (e.g. small footer or header note showing the two SHAs + last updated) if not already present.
- Consider submitting the sitemap via Google Search Console API (tooling exists in `seo/gsc.py`).
- Optional: robots.txt, Open Graph, JSON-LD for TechArticle on explainers.
- Long-term: keep shipping new atomic explainers on high-signal AB/RTB topics and let the freshness workflows keep everything current.

## How to Continue
1. Finish the in-flight agent prompt execution.
2. Run a full `mkdocs build` (with all plugins) from the docs clone and spot-check:
   - Sidebar is translated in non-English locales.
   - Explainers appear with correct titles/descriptions.
   - Sitemap is rich.
   - Extra SHAs are available (even if not yet rendered).
3. Commit the final bundle on a feature branch, open PR, merge → auto-deploy.
4. After deploy, manually verify a few pages on the live site + the sitemap.
5. Test the cross-repo trigger: make a small commit in the platform repo and confirm the docs workflow fires with the platform SHA in the payload.

## Notes
- The entire effort treats the Claude leak as an engineering spec rather than generic "SEO advice".
- All content is deliberately first-party, atomic, and technical — exactly what the leaked instructions tell the model to prefer.
- Freshness automation exists because recency is one of the strongest signals in the leak.

This handover should let a new agent (or human) pick up exactly where we left off without losing context.