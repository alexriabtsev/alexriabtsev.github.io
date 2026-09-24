#!/usr/bin/env python3
"""
Конвертер Jekyll-постів (.md з YAML front matter) у org-mode файли
для системи org-publish (init-blog.el).

Використання:
    python3 jekyll2org.py <вхідна_тека_з_md> <вихідна_тека_org>

Що робить:
- Парсить YAML front matter
- Мапить title/date/categories/tags -> #+title / #+date / #+filetags
- Зберігає старий permalink як :OLD_PERMALINK: property (для редіректів)
- Конвертує markdown body -> org (жирний/курсив/посилання/картинки/заголовки/списки)
- Ім'я вихідного файлу = дата + slug (як у вихідному .md), розширення .org
"""

import sys
import re
import os
from pathlib import Path
import yaml


def split_front_matter(text):
    """Розділити файл на (front_matter_dict, body_text)."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body.lstrip("\n")


def normalize_tags(fm):
    """Зібрати категорії+теги в один список для #+filetags."""
    tags = []
    for key in ("categories", "tags"):
        val = fm.get(key)
        if not val:
            continue
        if isinstance(val, str):
            val = [val]
        tags.extend(val)
    # org-теги не люблять пробіли/коми -> замінюємо на підкреслення
    clean = []
    for t in tags:
        t = str(t).strip()
        t = re.sub(r"[,\s]+", "_", t)
        t = re.sub(r"[^\w\u0400-\u04FF_-]", "", t)  # лишаємо кирилицю/латиницю/цифри
        if t:
            clean.append(t)
    # унікальні, зберігаючи порядок
    seen = set()
    result = []
    for t in clean:
        if t not in seen:
            seen.add(t)
            result.append(t)
    return result


import subprocess


def md_to_org(body):
    """Конвертація Markdown -> Org через pandoc (надійніше за regex для
    таблиць, вкладених списків, цитат тощо)."""
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "org"],
        input=body,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc error: {result.stderr}")
    org = result.stdout

    # Прибираємо зайві :PROPERTIES: :CUSTOM_ID: :END: блоки, які pandoc
    # автоматично додає під кожним заголовком (не потрібні для постів блогу).
    org = re.sub(
        r'\n:PROPERTIES:\n:CUSTOM_ID:[^\n]*\n:END:\n',
        '\n',
        org,
    )
    return org.strip() + "\n"


def format_org_date(dt):
    """Jekyll date (datetime або рядок) -> org inactive timestamp [YYYY-MM-DD Day HH:MM]."""
    from datetime import datetime
    if isinstance(dt, str):
        try:
            dt = datetime.fromisoformat(dt)
        except ValueError:
            return None
    if hasattr(dt, "strftime"):
        return dt.strftime("[%Y-%m-%d %a %H:%M]")
    return None


def convert_file(src_path: Path, out_dir: Path):
    raw = src_path.read_text(encoding="utf-8")
    fm, body = split_front_matter(raw)

    title = fm.get("title", src_path.stem)
    date_val = fm.get("date")
    org_date = format_org_date(date_val) if date_val else None
    permalink = fm.get("permalink", "")
    tags = normalize_tags(fm)
    org_body = md_to_org(body)

    lines = []
    lines.append(f"#+title: {title}")
    if org_date:
        lines.append(f"#+date: {org_date}")
    if tags:
        lines.append(f"#+filetags: :{':'.join(tags)}:")
    if permalink:
        lines.append(f"#+property: OLD_PERMALINK {permalink}")
    lines.append("")
    lines.append(org_body)

    out_name = src_path.stem + ".org"
    out_path = out_dir / out_name
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main():
    if len(sys.argv) != 3:
        print("Використання: python3 jekyll2org.py <вхідна_тека> <вихідна_тека>")
        sys.exit(1)

    src_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(src_dir.glob("*.md"))
    if not md_files:
        print(f"У {src_dir} не знайдено .md файлів.")
        sys.exit(1)

    converted = 0
    errors = []
    for f in md_files:
        try:
            out = convert_file(f, out_dir)
            converted += 1
        except Exception as e:
            errors.append((f.name, str(e)))

    print(f"Конвертовано: {converted}/{len(md_files)}")
    if errors:
        print("Помилки:")
        for name, err in errors:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
