#!/usr/bin/env python3
"""Fonctions utilitaires pour commit et push Git."""

from __future__ import annotations

from pathlib import Path
import subprocess


def commit_and_push(file: Path, message: str = "Mise a jour du rapport") -> None:
    subprocess.run(["git", "add", str(file)], check=False)
    subprocess.run(["git", "commit", "-m", message], check=False)
    subprocess.run(["git", "push", "origin", "work"], check=False)
