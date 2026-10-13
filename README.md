# Work team distribution — prototype

Prototype de sélection de work teams pour un chantier (Work Order + Work Order Line Items `49xxxxxx`).

Critères de pré-processing (tous activables) : zone d'intervention (code postal), spécialités, priorité P1, services opt-out, limite (20 par défaut).
Vue entonnoir, onglets Work teams et Services (consultation et modification en mémoire, non persistées).

## Variantes
- `index.html` : **Services / Spécialités** (services 49xxxxxx liés à des spécialités, opt-out de services).
- `quote.html` : **Quote Framework** : le devis est composé d'ouvrages (work items) ; plus de spécialités, de lien service-spécialité ni d'opt-out. Critères : zone, ouvrages (la work team réalise tous les ouvrages du devis), priorité P1 (au moins un ouvrage du devis en P1), limite.

## Structure
- `index.html` : application statique (HTML/CSS/JS, sans build)
- `data/*.json` : jeu de données fictif (100 work teams)
- `scripts/generate-data.py` : régénère les données de la variante Services / Spécialités
- `scripts/generate-quote-data.py` : régénère `data/q-*.json` (variante Quote)

## Exécuter en local
```bash
python3 -m http.server 8000   # puis http://localhost:8000
```

Déployé via GitHub Pages (branche `main`, racine).
