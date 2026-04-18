#!/usr/bin/env python3
"""Merge index.template.html with partials/*.html into index.html."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "index.template.html"
PARTIALS = ROOT / "partials"
OUT = ROOT / "index.html"
PATTERN = re.compile(r"@@include:([a-z0-9-]+)@@")


def build() -> None:
    text = TEMPLATE.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        path = PARTIALS / f"{name}.html"
        if not path.is_file():
            raise FileNotFoundError(f"Missing partial: {path}")
        return path.read_text(encoding="utf-8")

    merged = PATTERN.sub(replace, text)
    OUT.write_text(merged, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
