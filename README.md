# CyberPote

Petit projet contenant un assistant cyber permettant de verifier
rapidement quelques points de securite systeme.

## Lancer l'assistant

```bash
./assistant_cyber.py
```

L'assistant affiche un menu interactif proposant plusieurs outils :

- visualiser les ports ouverts
- consulter des conseils de securite
- verifier le statut du pare-feu
- lister les mises a jour disponibles via APT
- afficher les dernieres connexions

## Surveillance des CVE critiques

Un script automatise permet de recuperer les dix dernieres CVE ayant un
score CVSS superieur ou egal a 8. Il genere quotidiennement un rapport
Markdown dans le dossier `rapports/`.

```bash
python3 scripts/fetch_latest_cves.py
```
