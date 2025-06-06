#!/usr/bin/env python3
"""Fetch the latest CVEs with CVSS >= 8 from NVD and write a daily report."""

import json
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request

API_URL = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?resultsPerPage=10&cvssScoreMin=8&sortBy=pubDate&noRejected"
)


def fetch_cves():
    """Return a list of CVE items fetched from NVD."""
    req = Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as resp:
        data = json.load(resp)
    return data.get("vulnerabilities", [])


def generate_report(vulns):
    """Generate a markdown report of the CVEs and return the file path."""
    today = datetime.utcnow().date().isoformat()
    report_path = Path("rapports") / f"veille_CVE_{today}.md"
    lines = [f"# Rapport CVE critique - {today}", ""]
    for item in vulns:
        cve = item.get("cve", {})
        cve_id = cve.get("id")
        desc = ""
        for d in cve.get("descriptions", []):
            if d.get("lang") == "en":
                desc = d.get("value")
                break
        metrics = cve.get("metrics", {})
        score = None
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
            desc,
            "",
        ])
    report_path.write_text("\n".join(lines))
    return report_path


def main():
    try:
        vulns = fetch_cves()
    except Exception as e:
        print(f"Erreur lors de la recuperation des CVE : {e}")
        return 1
    path = generate_report(vulns)
    print(f"Rapport cree : {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
