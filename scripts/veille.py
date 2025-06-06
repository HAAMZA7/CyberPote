#!/usr/bin/env python3
"""Récupère les dix dernières CVE critiques et génère un rapport markdown."""

from __future__ import annotations

import datetime
from pathlib import Path
import requests

MIXTRAL_URL = "http://localhost:11434/api/generate"
NVD_URL = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?resultsPerPage=10&cvssScoreMin=8&sortBy=pubDate&noRejected"
)

def fetch_cves() -> list[dict]:
    """Retourne la liste des CVE récupérées sur le NVD."""
    resp = requests.get(NVD_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("vulnerabilities", [])


def summarize(text: str) -> str:
    """Résume le texte via le modèle local Mixtral."""
    payload = {
        "model": "mixtral",
        "prompt": text,
        "stream": False,
    }
    try:
        r = requests.post(MIXTRAL_URL, json=payload, timeout=60)
        r.raise_for_status()
        res = r.json()
        return res.get("response", text)
    except Exception:
        return text


def generate_report(vulns: list[dict]) -> Path:
    today = datetime.date.today().isoformat()
    report = Path("rapports") / f"veille_CVE_{today}.md"
    lines = [f"# Rapport CVE critique - {today}", ""]
    for item in vulns:
        cve = item.get("cve", {})
        cve_id = cve.get("id", "")
        desc = next(
            (d.get("value") for d in cve.get("descriptions", []) if d.get("lang") == "en"),
            "",
        )
        summary = summarize(desc) if desc else ""
        score = None
        metrics = cve.get("metrics", {})
        if metrics.get("cvssMetricV31"):
            score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
        elif metrics.get("cvssMetricV30"):
            score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]
        elif metrics.get("cvssMetricV2"):
            score = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]
        url = f"https://nvd.nist.gov/vuln/detail/{cve_id}" if cve_id else ""
        lines.extend([
            f"## {cve_id}",
            f"Score: {score}",
            f"[Lien]({url})",
            "",
            summary,
            "",
        ])
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def main() -> int:
    try:
        vulns = fetch_cves()
    except Exception as e:
        today = datetime.date.today().isoformat()
        report = Path("rapports") / f"veille_CVE_{today}.md"
        report.write_text(
            f"# Rapport CVE critique - {today}\n\nErreur de récupération des CVE : {e}\n",
            encoding="utf-8",
        )
        print(f"Rapport créé : {report} (avec erreur)")
        return 1

    path = generate_report(vulns)
    print(f"Rapport créé : {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
