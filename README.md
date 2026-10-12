# Work team distribution — prototype

Prototype de sélection de work teams pour un chantier (Work Order + Work Order Line Items `49xxxxxx`).

Critères de pré-processing (tous activables) : zone d'intervention (code postal), spécialités, priorité P1, services opt-out, limite (20 par défaut).
Vue entonnoir, onglets Work teams et Services (consultation et modification en mémoire, non persistées).

## Structure
- `index.html` : application statique (HTML/CSS/JS, sans build)
- `data/*.json` : jeu de données fictif (100 work teams)
- `scripts/generate-data.py` : régénère `data/` (graine fixe)

## Exécuter en local
```bash
python3 -m http.server 8000   # puis http://localhost:8000
```

Déployé via GitHub Pages (branche `main`, racine).
