#!/usr/bin/env python3
"""
PQC Quickstart Tutor — Database Integrity Checker

Validates that all files referenced in database/index.json exist,
checks for broken markdown links, and verifies no absolute paths
leaked into the repo.

Usage:
    python tools/check_database.py          # check everything
    python tools/check_database.py --json   # JSON output for CI
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # type: ignore

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = REPO_ROOT / "database" / "index.json"

# ── helpers ──────────────────────────────────────────────────────────

def find_markdown_files(base: Path) -> list[Path]:
    """Return all .md files under base, sorted."""
    return sorted(base.rglob("*.md"))

def find_all_files(base: Path) -> list[Path]:
    """Return all files under base (not dirs, not dot-ignored)."""
    return sorted(
        p for p in base.rglob("*")
        if p.is_file()
        and not any(part.startswith(".") for part in p.parts if part != ".")
    )

def count_files(base: Path) -> int:
    return len([p for p in base.rglob("*") if p.is_file()])

# ── checks ───────────────────────────────────────────────────────────

def check_index_consistency() -> list[str]:
    """Verify index.json entries match actual files on disk."""
    errors = []
    if not INDEX_PATH.exists():
        errors.append(f"MISSING: {INDEX_PATH}")
        return errors

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = json.load(f)

    # Check each file listed in index exists on disk
    for category, info in index.get("categories", {}).items():
        base = REPO_ROOT / info["path"]
        for filename in info.get("files", []):
            fpath = base / filename
            if not fpath.exists():
                errors.append(f"INDEX references missing file: {fpath.relative_to(REPO_ROOT)}")

    # Check actual files are all listed in index
    actual_md_files = set()
    for f in find_markdown_files(REPO_ROOT / "database"):
        actual_md_files.add(str(f.relative_to(REPO_ROOT).as_posix()))

    indexed_files = set()
    for category, info in index.get("categories", {}).items():
        for filename in info.get("files", []):
            indexed_files.add(f"{info['path']}/{filename}")

    missing_from_index = actual_md_files - indexed_files
    if missing_from_index:
        for mf in sorted(missing_from_index):
            errors.append(f"FILE not in index.json but exists on disk: {mf}")

    return errors


def check_absolute_paths() -> list[str]:
    """Scan all text files for absolute Windows/Unix paths that leaked."""
    errors = []
    abs_patterns = [
        (re.compile(r'[A-Z]:\\\\[^\s"\'<>]+'), "Windows backslash path"),
        (re.compile(r'[A-Z]:/[^\s"\'<>]+'), "Windows forward-slash path"),
        (re.compile(r'/home/\w+/[^\s"\'<>]+'), "Unix /home/ path"),
    ]
    scan_dirs = [
        REPO_ROOT / ".claude",
        REPO_ROOT / ".cursor",
        REPO_ROOT / ".github",
    ]
    scan_files = [
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "CLAUDE.md",
        REPO_ROOT / "PLATFORMS.md",
        REPO_ROOT / "README.md",
        REPO_ROOT / "install.bat",
        REPO_ROOT / "pqc-tutor.bat",
    ]

    for fpath in scan_files:
        if not fpath.exists():
            continue
        try:
            content = fpath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_no, line in enumerate(content.splitlines(), 1):
            for pattern, desc in abs_patterns:
                if pattern.search(line):
                    errors.append(f"ABSOLUTE_PATH ({desc}) in {fpath.name}:{line_no}: {line.strip()[:100]}")

    for sdir in scan_dirs:
        if not sdir.exists():
            continue
        for fpath in find_all_files(sdir):
            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for line_no, line in enumerate(content.splitlines(), 1):
                for pattern, desc in abs_patterns:
                    if pattern.search(line):
                        rel = fpath.relative_to(REPO_ROOT)
                        errors.append(f"ABSOLUTE_PATH ({desc}) in {rel}:{line_no}: {line.strip()[:100]}")

    return errors


def check_essential_files() -> list[str]:
    """Verify all essential repo files exist."""
    errors = []
    essential = [
        "AGENTS.md",
        "CLAUDE.md",
        "PLATFORMS.md",
        "README.md",
        "LICENSE",
        "NOTICE.md",
        "install.bat",
        "pqc-tutor.bat",
        ".cursor/rules/pqc-tutor.mdc",
        ".github/copilot-instructions.md",
        ".claude/commands/pqc.md",
        ".claude/skills/pqc-tutor/SKILL.md",
        ".claude/skills/pqc-tutor/resources/database_index.md",
        ".claude/skills/pqc-tutor/resources/prompt_templates.md",
        "database/index.json",
        "tools/check_database.py",
    ]
    for path in essential:
        if not (REPO_ROOT / path).exists():
            errors.append(f"MISSING essential file: {path}")
    return errors


def check_no_settings_local() -> list[str]:
    """settings.local.json must not exist in the repo."""
    errors = []
    local = REPO_ROOT / ".claude" / "settings.local.json"
    if local.exists():
        errors.append(f"LEAKED: {local.relative_to(REPO_ROOT)} — contains local paths/secrets, must be deleted")
    return errors


def check_offical_renamed() -> list[str]:
    """offical/ must not exist; official/ must."""
    errors = []
    old = REPO_ROOT / "offical"
    new = REPO_ROOT / "official"
    if old.exists():
        errors.append("TYPO: 'offical/' directory still exists — must be 'official/'")
    if not new.exists():
        errors.append("MISSING: 'official/' directory not found")
    return errors


def check_markdown_links() -> list[str]:
    """Check for broken internal markdown links."""
    errors = []
    link_re = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    db_dir = REPO_ROOT / "database"

    all_md = find_markdown_files(db_dir)

    for fpath in all_md:
        try:
            content = fpath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_no, line in enumerate(content.splitlines(), 1):
            for match in link_re.finditer(line):
                target = match.group(2)
                # Skip external URLs
                if target.startswith(("http://", "https://", "#")):
                    continue
                # Resolve relative links
                target_path = (fpath.parent / target).resolve()
                if not target_path.exists():
                    rel_src = fpath.relative_to(REPO_ROOT)
                    # Only report if target is within repo
                    try:
                        target_path.relative_to(REPO_ROOT)
                        errors.append(f"BROKEN_LINK in {rel_src}:{line_no}: {target}")
                    except ValueError:
                        pass  # target outside repo

    return errors


def check_gitignore_consistency() -> list[str]:
    """Verify .gitignore covers essential patterns."""
    errors = []
    gi = REPO_ROOT / ".gitignore"
    if not gi.exists():
        errors.append("MISSING: .gitignore")
        return errors

    content = gi.read_text(encoding="utf-8")
    required = [
        "settings.local.json",
        "*.pdf",
        "official/**",
    ]
    for pattern in required:
        if pattern not in content:
            errors.append(f"GITIGNORE missing pattern: {pattern}")
    return errors


# ── main ─────────────────────────────────────────────────────────────

def run_all_checks() -> dict[str, list[str]]:
    return {
        "index_consistency": check_index_consistency(),
        "absolute_paths": check_absolute_paths(),
        "essential_files": check_essential_files(),
        "no_settings_local": check_no_settings_local(),
        "offical_renamed": check_offical_renamed(),
        "markdown_links": check_markdown_links(),
        "gitignore_consistency": check_gitignore_consistency(),
    }


def main():
    parser = argparse.ArgumentParser(description="PQC Database Integrity Checker")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    results = run_all_checks()
    total_errors = sum(len(v) for v in results.values())

    if args.json:
        output = {
            "status": "pass" if total_errors == 0 else "fail",
            "total_errors": total_errors,
            "checks": {k: {"errors": v} for k, v in results.items()},
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print("=" * 60)
        print("PQC Quickstart Tutor — Database Integrity Check")
        print("=" * 60)
        for check_name, errors in results.items():
            status = "✅" if not errors else "❌"
            label = check_name.replace("_", " ").title()
            print(f"\n{status} {label}: {len(errors)} issue(s)")
            for err in errors:
                print(f"   → {err}")

        print("\n" + "=" * 60)
        if total_errors == 0:
            print("✅ ALL CHECKS PASSED")
        else:
            print(f"❌ {total_errors} ISSUE(S) FOUND")
        print("=" * 60)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
