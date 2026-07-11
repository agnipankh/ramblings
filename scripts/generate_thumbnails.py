"""Generate web-sized WebP derivatives for every image under content/images.

content/images/<relpath>.<ext>  ->  content/images/thumbs/<profile>/<relpath>.webp

Profiles match the templates that reference them: `card` for masonry grid
tiles, `featured` for the homepage panel, `cover` for article headers.
Originals are never touched; thumbs are regenerated only when the source
is newer, so re-runs are cheap. Run automatically by `make html`.
"""

from pathlib import Path

from PIL import Image

CONTENT_IMAGES = Path(__file__).resolve().parent.parent / "content" / "images"
THUMBS = CONTENT_IMAGES / "thumbs"

PROFILES = {"card": 720, "featured": 1120, "cover": 1600}
SOURCE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
WEBP_QUALITY = 82


def iter_sources():
    for path in sorted(CONTENT_IMAGES.rglob("*")):
        if THUMBS in path.parents:
            continue
        if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES:
            yield path


def thumb_path(source, profile):
    rel = source.relative_to(CONTENT_IMAGES)
    return THUMBS / profile / rel.with_suffix(".webp")


def build_thumb(source, dest, max_width):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
        if image.width > max_width:
            ratio = max_width / image.width
            image = image.resize(
                (max_width, round(image.height * ratio)), Image.Resampling.LANCZOS
            )
        image.save(dest, "WEBP", quality=WEBP_QUALITY, method=4)


def generate():
    built = 0
    for source in iter_sources():
        for profile, max_width in PROFILES.items():
            dest = thumb_path(source, profile)
            if dest.exists() and dest.stat().st_mtime >= source.stat().st_mtime:
                continue
            build_thumb(source, dest, max_width)
            built += 1
    return built


if __name__ == "__main__":
    print(f"thumbnails: {generate()} generated")
