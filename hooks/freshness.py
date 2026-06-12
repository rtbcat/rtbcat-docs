"""
MkDocs hook for:
- Injecting current git commit SHA (global build freshness / traceability)
- Enhancing the generated sitemap.xml with ideal trimmings:
  * Accurate lastmod from git (or fallback)
  * Priorities (higher for Explainers for AEO)
  * changefreq
  * Image sitemaps for pages with screenshots
  * Clean AEO-friendly URLs

Run automatically on `mkdocs build`.
Requires: git available in the build env (works in GitHub Actions checkout).
"""

import os
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

def _run_git(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(cmd, cwd=Path(__file__).parent.parent, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""

def _get_commit_sha() -> str:
    # Works in GitHub Actions (GITHUB_SHA env) and local git checkout
    sha = os.environ.get("GITHUB_SHA") or _run_git(["git", "rev-parse", "HEAD"])
    return sha or "unknown"

def _get_file_lastmod(src_path: str) -> str:
    """Get last commit date for a specific file (ISO format)."""
    # src_path is relative to docs/ in the build
    date = _run_git(["git", "log", "-1", "--format=%cI", "--", f"docs/{src_path}"])
    if not date:
        # Fallback to now for new/untracked files
        return datetime.now(timezone.utc).isoformat()
    return date

def on_config(config):
    """Inject global build SHA (docs) and platform SHA (when dispatched from app commit) 
    so templates can show 'Built from docs abc1234 (platform def5678)'."""
    if "extra" not in config:
        config["extra"] = {}

    # Docs repo SHA (from this build)
    docs_sha = _get_commit_sha()
    config["extra"]["commit_sha"] = docs_sha
    config["extra"]["commit_sha_short"] = docs_sha[:7]

    # Platform SHA (passed via repository_dispatch payload from platform repo)
    platform_sha = os.environ.get("PLATFORM_SHA") or os.environ.get("PLATFORM_COMMIT_SHA")
    if platform_sha:
        config["extra"]["platform_commit_sha"] = platform_sha
        config["extra"]["platform_commit_sha_short"] = platform_sha[:7]
        platform_ref = os.environ.get("PLATFORM_REF", "")
        if platform_ref:
            config["extra"]["platform_ref"] = platform_ref
        print(f"[freshness hook] Platform SHA captured: {platform_sha[:7]}")
    else:
        # No platform SHA for this build
        config["extra"]["platform_commit_sha"] = "N/A"
        config["extra"]["platform_commit_sha_short"] = "N/A"

    return config

def on_post_build(config):
    """Enrich site/sitemap.xml with all the trimmings after MkDocs generates the basic one."""
    site_dir = Path(config["site_dir"])
    sitemap_path = site_dir / "sitemap.xml"
    if not sitemap_path.exists():
        return

    # Register namespaces for sitemap + image sitemap extension.
    # The empty-prefix registration keeps the standard default-namespace form
    # (<url>, <loc>, ...) instead of ElementTree's auto-assigned "ns0:" prefix.
    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    ET.register_namespace("xhtml", "http://www.w3.org/1999/xhtml")
    ET.register_namespace("image", "http://www.google.com/schemas/sitemap-image/1.1")

    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Common namespaces
    ns = {
        "": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "image": "http://www.google.com/schemas/sitemap-image/1.1",
    }

    base_url = config.get("site_url", "https://docs.rtb.cat").rstrip("/")

    # Priority and changefreq map (tuned for AEO + normal docs)
    # Higher priority on Explainers because that's the new high-signal content for AI models
    priority_map = {
        "index.md": "1.0",
        "explainers/index.md": "0.95",
    }
    # Boost all explainers
    for expl in [
        "explainers/five-csv-reports.md",
        "explainers/qps-funnel.md",
        "explainers/pretargeting-configs.md",
        "explainers/safe-pretargeting-changes.md",
        "explainers/qps-waste-analysis.md",
        "explainers/creative-clustering-click-macros.md",
        "explainers/agencies-obtain-ab-seats.md",
        "explainers/what-cat-scan-does-not-do.md",
        "explainers/bid-filtering-report.md",
        "explainers/byom-optimizer.md",
    ]:
        priority_map[expl] = "0.9"

    default_priority = "0.7"
    expl_changefreq = "weekly"   # AEO content should look fresh
    normal_changefreq = "monthly"

    # Locale prefixes (must match the i18n languages in mkdocs.yml). Used to map a
    # localized URL like /fr/explainers/qps-funnel/ back to the language-agnostic
    # priority key "explainers/qps-funnel.md" so every locale's explainers get boosted.
    locales = {"ar", "da", "es", "fr", "he", "nl", "pl", "ru", "uk", "zh"}

    # Source docs dir, used to resolve whether a directory URL is a leaf page
    # (foo.md) or a section index (foo/index.md).
    docs_dir = Path(config.get("docs_dir", "docs"))

    # Pages that have screenshots (for image sitemap extension). Keys are
    # language-agnostic source paths; images are shared across locales.
    image_pages = {
        "03-qps-funnel.md": ["images/screenshot-qps-home.png"],
        "04-analyzing-waste.md": [
            "images/screenshot-geo-qps.png",
            "images/screenshot-pub-qps.png",
            "images/screenshot-size-qps.png",
        ],
        "06-pretargeting.md": ["images/screenshot-pretargeting-configs.png"],
        "05-managing-creatives.md": ["images/screenshot-creatives.png"],
        # Add more as you add screenshots
    }

    def _resolve_src(path_part: str) -> str:
        """Map a sitemap URL path (sans base_url) to its source .md file,
        handling directory URLs (use_directory_urls) and section indexes."""
        if not path_part:
            return "index.md"
        leaf = f"{path_part}.md"
        index = f"{path_part}/index.md"
        if (docs_dir / leaf).exists():
            return leaf
        if (docs_dir / index).exists():
            return index
        return leaf  # best-effort fallback

    def _priority_key(src: str) -> str:
        """Strip a leading locale segment so localized pages share priority/changefreq."""
        first, _, rest = src.partition("/")
        return rest if first in locales and rest else src

    for url_elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_elem is None:
            continue

        loc = loc_elem.text or ""
        path_part = loc.replace(base_url, "").strip("/")
        src = _resolve_src(path_part)   # locale-specific source (for git lastmod)
        key = _priority_key(src)        # locale-agnostic key (for priority/changefreq/images)

        # lastmod from git (most accurate)
        lastmod = _get_file_lastmod(src)
        lastmod_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
        if lastmod_elem is None:
            lastmod_elem = ET.SubElement(url_elem, "lastmod")
        lastmod_elem.text = lastmod

        # changefreq
        cf = expl_changefreq if key.startswith("explainers/") else normal_changefreq
        cf_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq")
        if cf_elem is None:
            cf_elem = ET.SubElement(url_elem, "changefreq")
        cf_elem.text = cf

        # priority
        prio = priority_map.get(key, default_priority)
        prio_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}priority")
        if prio_elem is None:
            prio_elem = ET.SubElement(url_elem, "priority")
        prio_elem.text = prio

        # Image sitemap extension for pages with screenshots
        if key in image_pages:
            for img_path in image_pages[key]:
                img_url = f"{base_url}/{img_path}"
                img_elem = ET.SubElement(url_elem, "{http://www.google.com/schemas/sitemap-image/1.1}image")
                loc_img = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}loc")
                loc_img.text = img_url

    # Write back the enriched sitemap
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

    # Also write a human-friendly version note (optional)
    print(f"[freshness hook] Enriched sitemap with git lastmod + priorities + images. Commit: {_get_commit_sha()[:7]}")