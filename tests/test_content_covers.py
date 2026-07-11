"""Every article must declare a cover image — the homepage renders each
post as an image card, so a missing cover degrades the grid. Pages
(About etc.) are exempt."""

import re
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"

COVER_LINE = re.compile(r"^cover:\s*(\S+)", re.IGNORECASE | re.MULTILINE)


def article_files():
    return [
        p
        for p in CONTENT.rglob("*.md")
        if "pages" not in p.parts and "extra" not in p.parts
    ]


def declared_cover(path):
    match = COVER_LINE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def test_articles_exist():
    assert len(article_files()) > 0


def test_every_article_declares_a_cover_image():
    missing = [
        str(p.relative_to(CONTENT)) for p in article_files() if not declared_cover(p)
    ]
    assert missing == [], f"Articles without a cover image: {missing}"


def test_declared_cover_files_exist():
    broken = []
    for path in article_files():
        cover = declared_cover(path)
        if cover and cover.startswith("/images"):
            if not (CONTENT / cover.lstrip("/")).exists():
                broken.append(f"{path.relative_to(CONTENT)} -> {cover}")
    assert broken == [], f"Covers pointing at missing files: {broken}"


def test_thumbnail_generator_covers_every_declared_cover():
    """Templates rewrite covers to images/thumbs/<profile>/<name>.webp;
    the generator must produce exactly those paths for every cover."""
    import importlib.util

    script = CONTENT.parent / "scripts" / "generate_thumbnails.py"
    spec = importlib.util.spec_from_file_location("generate_thumbnails", script)
    assert spec is not None and spec.loader is not None
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)

    sources = set(gen.iter_sources())
    for path in article_files():
        cover = declared_cover(path)
        if not (cover and cover.startswith("/images")):
            continue
        source = CONTENT / cover.lstrip("/")
        assert source in sources, f"{cover} not picked up by the generator"
        for profile in ("card", "featured", "cover"):
            expected = (
                CONTENT
                / "images"
                / "thumbs"
                / profile
                / source.relative_to(CONTENT / "images").with_suffix(".webp")
            )
            assert gen.thumb_path(source, profile) == expected
