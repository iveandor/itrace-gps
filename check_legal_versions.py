#!/usr/bin/env python3
"""법적 문서 버전 정합성 검사 — legal/versions.json 과 HTML 헤더·부칙이 같은 시행일을 가리키는지.

앱(iTrace·iLogMobile)이 legal/versions.json 의 version(= 시행일, YYYY-MM-DD)을 가입 시 동의 버전으로
기록하므로, HTML 을 개정할 때 헤더 시행일·약관 부칙·매니페스트 세 곳이 함께 움직여야 한다.
사용: python3 check_legal_versions.py   (exit 0 = 정합, 1 = 불일치)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "legal" / "versions.json"
DOCS = {
    "terms": ROOT / "terms_of_use.html",
    "privacy": ROOT / "privacy_policy.html",
}
HEADER_RE = re.compile(r"시행일\s*<strong>(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.</strong>")
REVISED_RE = re.compile(r"최종 수정일\s*<strong>(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.</strong>")
APPENDIX_RE = re.compile(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일부터 시행")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def iso(y, m, d):
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def main():
    errors = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != 1:
        errors.append(f"manifest schemaVersion must be 1 (got {manifest.get('schemaVersion')!r})")
    documents = manifest.get("documents", {})

    for key, path in DOCS.items():
        html = path.read_text(encoding="utf-8")
        doc = documents.get(key)
        if doc is None:
            errors.append(f"manifest missing documents.{key}")
            continue

        version = doc.get("version", "")
        notice_from = doc.get("noticeFrom", "")
        revised_at = doc.get("revisedAt", "")
        history = doc.get("history", [])
        for name, value in (("version", version), ("noticeFrom", notice_from), ("revisedAt", revised_at)):
            if not ISO_RE.match(str(value)):
                errors.append(f"{key}.{name} must be YYYY-MM-DD (got {value!r})")

        header = HEADER_RE.search(html)
        if not header:
            errors.append(f"{path.name}: 시행일 header not found")
        else:
            header_iso = iso(*header.groups())
            if header_iso != version:
                errors.append(f"{path.name}: header 시행일 {header_iso} != manifest {key}.version {version}")

        revised = REVISED_RE.search(html)
        if not revised:
            errors.append(f"{path.name}: 최종 수정일 header not found")
        else:
            revised_iso = iso(*revised.groups())
            if revised_iso != revised_at:
                errors.append(f"{path.name}: header 최종 수정일 {revised_iso} != manifest {key}.revisedAt {revised_at}")

        if key == "terms":
            dates = [iso(*m) for m in APPENDIX_RE.findall(html)]
            if not dates:
                errors.append(f"{path.name}: 부칙 시행일 not found")
            else:
                latest = max(dates)
                if latest != version:
                    errors.append(f"{path.name}: 부칙 latest 시행일 {latest} != manifest terms.version {version}")
                expected_history = sorted((d for d in dates if d != latest), reverse=True)
                if sorted(history, reverse=True) != expected_history:
                    errors.append(f"manifest terms.history {history} != 부칙 previous dates {expected_history}")

        if notice_from > version:
            errors.append(f"{key}: noticeFrom {notice_from} must be <= version {version}")
        if revised_at > version:
            errors.append(f"{key}: revisedAt {revised_at} must be <= version {version}")
        for h in history:
            if not ISO_RE.match(str(h)):
                errors.append(f"{key}.history entry must be YYYY-MM-DD (got {h!r})")
            elif h >= version:
                errors.append(f"{key}: history entry {h} must be older than version {version}")
        if "requiresExplicitConsent" not in doc or not isinstance(doc["requiresExplicitConsent"], bool):
            errors.append(f"{key}.requiresExplicitConsent must be a boolean")

        print(f"{key:8s} version={version} noticeFrom={notice_from} revisedAt={revised_at} "
              f"explicit={doc.get('requiresExplicitConsent')} history={history}")

    if errors:
        print("\nMISMATCH:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\nOK: legal/versions.json matches terms_of_use.html and privacy_policy.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
