#!/usr/bin/env python3
"""Check that skills/skill-map.md covers canonical root skills."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILL_MAP = SKILLS_DIR / "skill-map.md"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path}: unclosed YAML frontmatter")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def root_skills() -> list[Path]:
    return sorted(SKILLS_DIR.glob("crow-pet-*/SKILL.md"))


def check() -> list[str]:
    errors: list[str] = []
    skill_map_text = SKILL_MAP.read_text() if SKILL_MAP.exists() else ""
    rows = set(re.findall(r"\| `(crow-pet-[^`]+)` \|", skill_map_text))

    for path in root_skills():
        text = path.read_text()
        try:
            frontmatter = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not name:
            errors.append(f"{path}: missing frontmatter name")
        if not description:
            errors.append(f"{path}: missing frontmatter description")
        if name and name != path.parent.name:
            errors.append(f"{path}: frontmatter name {name!r} does not match folder {path.parent.name!r}")
        if "## Progressive Disclosure" not in text:
            errors.append(f"{path}: missing ## Progressive Disclosure")
        if "## Dependency Edges" not in text:
            errors.append(f"{path}: missing ## Dependency Edges")
        if name and name not in rows:
            errors.append(f"{SKILL_MAP}: missing routing table row for {name}")

    for row in sorted(rows):
        if not (SKILLS_DIR / row / "SKILL.md").exists():
            errors.append(f"{SKILL_MAP}: row references missing skill {row}")

    return errors


def print_summary() -> None:
    for path in root_skills():
        fm = parse_frontmatter(path)
        print(f"- `{fm.get('name', path.parent.name)}`: {fm.get('description', '').strip()}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when skill map drift is detected")
    args = parser.parse_args()

    errors = check()
    if args.check:
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        print("skill map ok")
        return 0

    print_summary()
    if errors:
        print("\nWarnings:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
