# Handover - RTB.cat Docs AEO Pipeline

**Date:** 2026-06-13
**Repo:** `rtbcat/rtbcat-docs`
**Live site:** https://docs.rtb.cat
**Local clone:** `/home/jen/Documents/rtbcat-docs`
**Primary purpose:** This docs site is a core marketing surface for RTB.cat / Cat-Scan. It is optimized for Answer Engine Optimization (AEO): static, crawlable, multilingual, fresh, and rich with first-party technical explainers.

## Critical Deployment Pipeline

This repo is hosted as a static GitHub Pages site on the `gh-pages` branch, but the site is built by GitHub Actions before it is published.

The normal pipeline is:

```text
push to main
  -> GitHub Actions workflow: .github/workflows/deploy.yml
  -> actions/checkout with fetch-depth: 0
  -> actions/setup-python@v5 using Python 3.12
  -> pip install -r requirements.txt from PyPI
  -> mkdocs gh-deploy --force
  -> generated static files are pushed to gh-pages
  -> GitHub Pages publishes https://docs.rtb.cat
```

This means PyPI is not used by the live website at runtime. PyPI is used only inside the GitHub Actions build job. GitHub Pages serves the generated HTML, CSS, JS, images, and sitemap from `gh-pages`.

The current PyPI dependencies are:

```text
mkdocs-material>=9.5
mkdocs-static-i18n>=1.2
mkdocs-git-revision-date-localized-plugin>=1.2
```

Important naming detail:

- The MkDocs plugin key in `mkdocs.yml` is `git-revision-date-localized`.
- The PyPI package in `requirements.txt` is `mkdocs-git-revision-date-localized-plugin`.

The current pipeline has been verified end-to-end:

- Source commit on `main`: `830edf8 Update docs freshness and translations`
- `Deploy docs to GitHub Pages` GitHub Actions run for `830edf8`: success
- Published `gh-pages` commit: `42a4c6a`
- Live site shows `Built from docs 830edf8`

## Cross-Repo Freshness Pipeline

Docs rebuild on two events:

1. A push to `main` in `rtbcat/rtbcat-docs`.
2. A `repository_dispatch` event of type `update-docs-freshness` from the platform repo.

The platform repo (`jenbrannstrom/rtbcat-platform`) sends dispatch payload fields such as `sha`, `sha_short`, `ref`, and `commit_message`. The docs workflow captures these into environment variables:

```text
PLATFORM_SHA
PLATFORM_SHA_SHORT
PLATFORM_REF
PLATFORM_MESSAGE
```

`hooks/freshness.py` reads the docs commit SHA and optional platform SHA, injects them into `config.extra`, and enriches the generated sitemap. This is important for AEO because model web tooling and search systems heavily weight recency and crawlable source metadata.

## Why This Matters

The docs site is not just product documentation. It is the main public technical proof surface for RTB.cat / Cat-Scan:

- First-party explainers establish authority for Google Authorized Buyers / ADX / RTB operations.
- Atomic technical claims make pages easy for LLMs and search engines to quote or summarize.
- Multilingual pages broaden reach across agencies and operators.
- Commit and sitemap freshness make the site look actively maintained.
- Static HTML keeps all content fetchable by crawlers and model browsing tools.

## Current State

- `main` is pushed and clean.
- `gh-pages` is deployed and live.
- GitHub Actions can install the PyPI dependencies and deploy successfully.
- The local `.venv-build` can also install `requirements.txt` and run `mkdocs build`.
- Generated `site/` output is ignored and should not be committed.

## Key Files

- `.github/workflows/deploy.yml` - GitHub Actions build and deploy pipeline.
- `requirements.txt` - PyPI packages used by the Actions build.
- `mkdocs.yml` - MkDocs Material config, i18n config, nav, plugins, hooks, extra assets.
- `hooks/freshness.py` - commit SHA injection and sitemap enrichment.
- `hooks/nav_translations.py` - localized sidebar/nav labels.
- `overrides/main.html` - page title override and visible build freshness line.
- `docs/explainers/` - English AEO explainer source pages.
- `docs/<lang>/explainers/` - translated explainer pages.
- `seo/` - supporting SEO/AEO tooling and reference artifacts.

## Local Build Commands

From `/home/jen/Documents/rtbcat-docs`:

```bash
python -m venv .venv-build
.venv-build/bin/pip install -r requirements.txt
.venv-build/bin/mkdocs build
.venv-build/bin/mkdocs serve
```

Manual deploy from local, when needed:

```bash
.venv-build/bin/mkdocs gh-deploy --force
```

Normally, do not need to deploy locally. Pushing `main` triggers the GitHub Actions pipeline.

## Verification Commands

Check source and deploy branches:

```bash
git status --short --branch
git ls-remote --heads origin main gh-pages
```

Check the latest Actions runs:

```bash
gh run list --repo rtbcat/rtbcat-docs --workflow "Deploy docs to GitHub Pages" --limit 5
gh run list --repo rtbcat/rtbcat-docs --workflow pages-build-deployment --limit 5
```

Check the live build SHA:

```bash
curl -L -sS https://docs.rtb.cat | rg "Built from docs"
```

## Non-Fatal Build Noise

These warnings are currently expected and do not block deploys:

- Material for MkDocs warning about future MkDocs 2.0 changes.
- `mkdocs-static-i18n` warning that the Material language switcher contextual link is not compatible with `navigation.instant`.
- `includes/abbreviations.*.md` pages reported as not included in nav.
- Some language search support notices for languages not supported by `lunr.js`.

The deploy workflow is intentionally non-strict, so these warnings do not fail deployment.

## Open / Next Items

- Add `robots.txt` referencing `https://docs.rtb.cat/sitemap.xml`.
- Consider Open Graph / Twitter Card / JSON-LD for high-value explainers.
- Consider exact dependency pins for fully reproducible builds.
- Submit or resubmit sitemap through Google Search Console.
- Keep publishing new focused explainers for high-signal AB / ADX / RTB topics.
- Periodically verify cross-repo freshness dispatch from the platform repo.

## Things Not To Reintroduce

- Do not use `mkdocs-git-revision-date-localized` as a PyPI package name. It is the plugin key, not the installable package.
- Do not strip `git-revision-date-localized` from `mkdocs.yml` for CI. The full GitHub Actions build can install the package correctly.
- Do not commit generated `site/` output.
- Do not treat GitHub Pages as a Python runtime. It is static hosting only; Python runs in Actions.
