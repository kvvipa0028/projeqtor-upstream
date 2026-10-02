#!/usr/bin/env python3
"""Compare tool/i18n/nls/en/lang.js and tool/i18n/nls/zh/lang.js.

Checks:
- the two files have the same keys
- placeholders ${...}, HTML tags and &#NN; entities match
- Chinese values do not contain raw ASCII comma, colon or double quote
  (the PHP i18n loader splits lines on those characters)

Exit code is 1 when any check fails.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EN_PATH = ROOT / "tool/i18n/nls/en/lang.js"
ZH_PATH = ROOT / "tool/i18n/nls/zh/lang.js"
LINE = re.compile(r'^([A-Za-z0-9_]+)\s*:\s*"(.*)"\s*,?\s*$')
PLACEHOLDER = re.compile(r"\$\{[^}]+\}")
ENTITY = re.compile(r"&#\d+;?")
TAG = re.compile(r"</?[^>]+>")
CJK = re.compile(r"[\u4e00-\u9fff]")


def parse(path: Path):
    keys = {}
    order = []
    bad = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip() in ("{", "}", ""):
            continue
        match = LINE.match(line)
        if not match:
            bad.append((number, line[:160]))
            continue
        key, value = match.group(1), match.group(2)
        if key in keys:
            bad.append((number, f"duplicate key {key}"))
        keys[key] = value
        order.append(key)
    return keys, order, bad


def bag(pattern, value):
    return Counter(pattern.findall(value))


def main():
    en, en_order, en_bad = parse(EN_PATH)
    zh, zh_order, zh_bad = parse(ZH_PATH)
    errors = []
    if en_bad:
        errors.append(f"en/lang.js has {len(en_bad)} unparsed lines, first: {en_bad[0]}")
    if zh_bad:
        errors.append(f"zh/lang.js has {len(zh_bad)} unparsed lines, first: {zh_bad[0]}")

    missing = [key for key in en_order if key not in zh]
    extra = [key for key in zh_order if key not in en]
    if missing:
        errors.append(f"missing in zh ({len(missing)}): {', '.join(missing[:12])}")
    if extra:
        errors.append(f"extra in zh ({len(extra)}): {', '.join(extra[:12])}")

    placeholder_mismatch = []
    tag_mismatch = []
    entity_mismatch = []
    raw_punct = []
    still_english = []
    for key, value in en.items():
        zh_value = zh.get(key)
        if zh_value is None:
            continue
        if bag(PLACEHOLDER, value) != bag(PLACEHOLDER, zh_value):
            placeholder_mismatch.append(key)
        if bag(TAG, value) != bag(TAG, zh_value):
            tag_mismatch.append(key)
        if bag(ENTITY, value) != bag(ENTITY, zh_value):
            entity_mismatch.append(key)
        if any(ch in zh_value for ch in ',:"'):
            raw_punct.append(key)
        if key != "currentLocaleOfFile" and not CJK.search(zh_value) and re.search(r"[A-Za-z]{3,}", value):
            # Proper nouns and tokens may legitimately stay in Latin letters,
            # but a value with no Chinese at all is treated as untranslated.
            still_english.append(key)

    if placeholder_mismatch:
        errors.append(f"placeholder mismatch ({len(placeholder_mismatch)}): {', '.join(placeholder_mismatch[:12])}")
    if tag_mismatch:
        errors.append(f"HTML tag mismatch ({len(tag_mismatch)}): {', '.join(tag_mismatch[:12])}")
    if entity_mismatch:
        errors.append(f"HTML entity mismatch ({len(entity_mismatch)}): {', '.join(entity_mismatch[:12])}")
    if raw_punct:
        errors.append(f"raw comma/colon/quote in zh ({len(raw_punct)}): {', '.join(raw_punct[:12])}")
    if still_english:
        errors.append(f"zh values with no Chinese ({len(still_english)}): {', '.join(still_english[:12])}")

    print(f"en keys: {len(en)}")
    print(f"zh keys: {len(zh)}")
    print(f"placeholder mismatches: {len(placeholder_mismatch)}")
    print(f"HTML tag mismatches: {len(tag_mismatch)}")
    print(f"entity mismatches: {len(entity_mismatch)}")
    print(f"raw punctuation: {len(raw_punct)}")
    print(f"untranslated (no CJK): {len(still_english)}")
    if errors:
        print("FAILED")
        for error in errors:
            print("-", error)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
