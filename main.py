#!/usr/bin/env python3
"""Lance la veille CVE et pousse le rapport sur Git."""

from __future__ import annotations

from scripts.veille import main as run_veille
from scripts.git_push import commit_and_push
from pathlib import Path


def main() -> None:
    result = run_veille()
    today = Path("rapports") / f"veille_CVE_{__import__('datetime').date.today().isoformat()}.md"
    commit_and_push(today, "Ajout rapport CVE")
    if result == 0:
        print("Veille terminee")
    else:
        print("Veille terminee avec erreurs")


if __name__ == "__main__":
    main()
