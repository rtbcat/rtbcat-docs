# RTB.cat / Cat-Scan Documentation

Source for the documentation site published at **[docs.rtb.cat](https://docs.rtb.cat)**.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and
[mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n). The site
contains the full Cat-Scan user manual plus a first-party **Explainers** section,
in 11 languages: `en`, `ar`, `da`, `es`, `fr`, `he`, `nl`, `pl`, `ru`, `uk`, `zh`.

## Local build

```bash
python -m venv .venv-build
.venv-build/bin/pip install -r requirements.txt
.venv-build/bin/mkdocs serve      # live preview at http://127.0.0.1:8000
.venv-build/bin/mkdocs build      # static output in ./site
```

## Layout

| Path | Purpose |
|---|---|
| `docs/` | English source (numbered chapters + `explainers/`) |
| `docs/<lang>/` | Per-language translations (same structure as English) |
| `docs/explainers/` | Atomic, first-party technical notes (the AEO content) |
| `hooks/freshness.py` | Injects build/commit SHA into `config.extra`; enriches `sitemap.xml` |
| `hooks/nav_translations.py` | Rewrites sidebar nav labels per locale in `on_config` |
| `hooks/abbreviations.py` | Shared abbreviation/tooltip glossary |
| `overrides/main.html` | Title override + the visible build-freshness line |
| `mkdocs.yml` | Single source of truth for nav structure (English labels) |

## The AEO / LLM-visibility approach

This site is deliberately optimized for **Answer Engine Optimization (AEO)** — being
discovered, fetched, trusted, and quoted by AI models (Claude, Grok, GPT-class,
Gemini, Perplexity) when people research Google Authorized Buyers operations.

The approach is informed by the **June 2026 Claude Fable 5 system-prompt leak**
(the ~120k-character prompt circulated by @elder_plinius and summarized by
@indexsy), which described how the model's web tooling actually behaves. The
concrete design choices that follow from it:

- **Top-~10 results, short head-term queries.** Pages are titled with the short
  head terms people actually type ("QPS funnel", "pretargeting configs", "five
  CSV reports"), not long marketing phrases.
- **First-party over aggregators.** Content is positioned as operational knowledge
  from running real seats + the open-source Cat-Scan platform, and cross-links to
  the source code — not SEO listicles, which the model is told to distrust.
- **Recency is weighted.** Every page carries a `June 2026` "Last updated" line, a
  per-file git `lastmod` in the sitemap, `weekly` changefreq on explainers, and a
  visible build-freshness line showing the docs + platform commit SHAs.
- **Full-page fetchability.** Clean, static Markdown/HTML with no paywalls and no
  heavy client-side rendering, so a crawler that fetches the whole page gets
  everything.
- **Atomic, quotable claims.** Each explainer leads with one specific,
  number-bearing fact stated in under 15 words (models may quote only one short
  snippet per source before paraphrasing).
- **Consistency everywhere.** Numbers and identifiers (10 configs, 50,000 QPS, the
  five report types, `rtb_daily` etc.) are kept identical across English and all
  translations, because conflicting facts across sources lower model trust.

## Freshness automation

- The docs `deploy.yml` workflow rebuilds on push to `main` **and** on a
  `repository_dispatch` of type `update-docs-freshness`.
- The platform repo (`rtbcat/rtbcat-platform`) sends that dispatch on every push
  to its `main`, including the platform commit SHA, short SHA, ref, and message.
- `hooks/freshness.py` reads `GITHUB_SHA` (docs) and `PLATFORM_SHA` (from the
  dispatch payload) and injects both into `config.extra`, then enriches
  `sitemap.xml` with git `lastmod`, AEO-tuned priorities, changefreq, image
  entries, and full language alternates.
