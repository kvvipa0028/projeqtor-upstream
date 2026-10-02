#!/usr/bin/env python3
"""Compare tool/i18n/nls/en/lang.js and tool/i18n/nls/zh/lang.js.

Checks:
- the two files have the same keys
- placeholders ${...}, HTML tags and &#NN; entities match
- Chinese values do not contain raw ASCII comma, colon or double quote
  (the PHP i18n loader splits lines on those characters)
- leading and trailing ASCII spaces match the English value
- glossary terms that must not come back (活动流, 客户发票项, 问责人, 严重性)
- a Chinese character is not glued to a Latin word, except glossary acronyms
- two- and three-letter English captions such as Mo, Tu and th are translated

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
# A leading letter avoids treating comparisons such as "< 20%" as tags.
TAG = re.compile(r"</?[A-Za-z][^>]*>")
CJK = re.compile(r"[\u4e00-\u9fff]")
GLUE = re.compile(r"[\u4e00-\u9fff][A-Za-z]{2,}|[A-Za-z]{2,}[\u4e00-\u9fff]")
# Acronyms and product tokens from the glossary. They may sit next to Chinese.
ACRONYM = """
WBS BBS SBS RACI RIDA KPI SLA HR CRM LDAP SSO SAML IMAP SMTP SSL TLS PDF CSV
Excel SQL HTML JSON XML URL API UTF Dojo Scrum cron PHP CSS JS OK ID OS MB
AM PM FTE VAT DNS IP URI EOL CK OTP Word xlsx Email ProjeQtOr MSProject
Php HELLO DN Where CRON debug html csv Ldap IdP SAML2 PHPMail ProjectQr MS
""".split()
ACRONYM_RE = re.compile("|".join(re.escape(token) for token in sorted(set(ACRONYM), key=len, reverse=True)), re.I)
FORBIDDEN = ("活动流", "客户发票项", "问责人", "严重性", "上午问责", "上午负责")
ABBREV_VALUES_OK = {"MB", "HR", "OS", "RACI", "RIDA", "WBS", "BBS", "KPI", "OK", "ID"}


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
    edge_space = []
    forbidden = []
    glued = []
    untranslated_abbrev = []
    allowed_latin = {
        "applicationTitle", "buttonExcel", "Excel", "colBbs", "colSbs", "colWbs",
        "labelShowWbsShort", "langEn", "oAuth2", "planningMSProject", "raci",
        "reportCategoryKpi", "reportRida", "themeProjectom", "colScrumMaster",
        "passNum", "pwdErrorDijit",
    }
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
        if key not in allowed_latin and key != "currentLocaleOfFile" and not CJK.search(zh_value) and re.search(r"[A-Za-z]{3,}", value):
            # Proper nouns and tokens may legitimately stay in Latin letters,
            # but a value with no Chinese at all is treated as untranslated.
            still_english.append(key)
        en_lead = len(value) - len(value.lstrip(" "))
        en_trail = len(value) - len(value.rstrip(" "))
        zh_lead = len(zh_value) - len(zh_value.lstrip(" "))
        zh_trail = len(zh_value) - len(zh_value.rstrip(" "))
        if (en_lead, en_trail) != (zh_lead, zh_trail):
            edge_space.append(key)
        for word in FORBIDDEN:
            if word in zh_value:
                forbidden.append(f"{key}:{word}")
                break
        if GLUE.search(ACRONYM_RE.sub(" ", zh_value)):
            glued.append(key)
        if (
            key not in allowed_latin
            and key != "currentLocaleOfFile"
            and re.fullmatch(r"[A-Za-z]{2,3}", value.strip())
            and zh_value.strip() == value.strip()
            and value.strip() not in ABBREV_VALUES_OK
        ):
            untranslated_abbrev.append(key)

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
    if edge_space:
        errors.append(f"leading/trailing space mismatch ({len(edge_space)}): {', '.join(edge_space[:12])}")
    if forbidden:
        errors.append(f"glossary forbidden wording ({len(forbidden)}): {', '.join(forbidden[:12])}")
    if glued:
        errors.append(f"Chinese glued to a Latin word ({len(glued)}): {', '.join(glued[:12])}")
    if untranslated_abbrev:
        errors.append(f"untranslated short caption ({len(untranslated_abbrev)}): {', '.join(untranslated_abbrev[:12])}")

    print(f"en keys: {len(en)}")
    print(f"zh keys: {len(zh)}")
    print(f"placeholder mismatches: {len(placeholder_mismatch)}")
    print(f"HTML tag mismatches: {len(tag_mismatch)}")
    print(f"entity mismatches: {len(entity_mismatch)}")
    print(f"raw punctuation: {len(raw_punct)}")
    print(f"untranslated (no CJK): {len(still_english)}")
    print(f"edge-space mismatches: {len(edge_space)}")
    print(f"forbidden wording: {len(forbidden)}")
    print(f"glued Latin: {len(glued)}")
    print(f"untranslated short captions: {len(untranslated_abbrev)}")
    if errors:
        print("FAILED")
        for error in errors:
            print("-", error)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
