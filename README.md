# CyberPote

Petit projet contenant un assistant cyber permettant de verifier rapidement quelques points de securite systeme et d'automatiser la veille des vulnérabilités.

## Lancer l'assistant en ligne de commande

```bash
./assistant_cyber.py
```

L'assistant affiche un menu interactif proposant plusieurs outils :

- visualiser les ports ouverts
- consulter des conseils de securite
- verifier le statut du pare-feu
- lister les mises a jour disponibles via APT
- afficher les dernieres connexions

## Lancer la veille CVE manuellement

```bash
python3 main.py
```

Cela récupère les dix dernières CVE critiques (CVSS >= 8), génère un rapport Markdown dans `rapports/` et pousse le fichier sur le dépôt Git.

## Interface Web

Une interface Streamlit permet de lancer la veille d'un clic :

```bash
streamlit run interface.py
```

## Installation des dépendances

Un script `setup.sh` installe toutes les bibliothèques requises (requests, GitPython, streamlit).
