"""
MkDocs hook: inject locale-specific abbreviation definitions.

pymdownx.snippets auto_append is hardcoded to one file, so it can't
switch per locale.  This hook appends the right abbreviations file
based on the locale that mkdocs-static-i18n is currently building.
"""

import os

_INCLUDES = os.path.join(os.path.dirname(__file__), os.pardir, "docs", "includes")


def _detect_locale(page, config):
    """Best-effort locale detection from page or config."""
    # mkdocs-static-i18n sets page.locale
    locale = getattr(page, "locale", None)
    if locale:
        return str(locale)
    # Fallback: theme language (i18n plugin reconfigures per build)
    try:
        lang = config["theme"]["language"]
        if lang and lang != "en":
            return lang
    except (KeyError, TypeError):
        pass
    # Fallback: infer from page file path
    src = getattr(page.file, "src_path", "") if hasattr(page, "file") else ""
    parts = src.split("/")
    if len(parts) > 1 and len(parts[0]) == 2:
        return parts[0]
    return "en"


def on_page_markdown(markdown, page, config, files):
    locale = _detect_locale(page, config)
    locale_file = os.path.join(_INCLUDES, f"abbreviations.{locale}.md")
    default_file = os.path.join(_INCLUDES, "abbreviations.md")
    path = locale_file if os.path.exists(locale_file) else default_file
    with open(path, encoding="utf-8") as f:
        return markdown + "\n\n" + f.read()
