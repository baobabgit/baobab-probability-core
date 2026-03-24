# Validation technique avant release (quality gates)

Ce document enregistre **quels contrôles** doivent passer, **comment** ils sont exécutés dans le dépôt, et une **preuve de réussite** (locale + CI) pour le GO release.

---

## Date de validation documentaire

**2026-03-24** — contenu aligné sur l’exécution locale des commandes ci-dessous et sur le dernier run CI du workflow associé au tag `v1.0.0`.

---

## Liste des contrôles et conditions de réussite

| Contrôle | Commande | Réussite attendue |
|----------|----------|-------------------|
| Formatage | `black --check src tests` | Code conforme ; sortie « All done » ; code retour 0 |
| Style PEP 8 | `flake8 src tests` | Aucun signalement ; code retour 0 (config `[tool.flake8]` via **Flake8-pyproject** après `pip install -e ".[dev]"`) |
| Analyse statique | `pylint src/baobab_probability_core` | Score attendu **10.00/10** (réglages dans `pyproject.toml`) ; code retour 0 |
| Typage | `mypy src/baobab_probability_core` | `Success: no issues found` ; code retour 0 |
| Sécurité | `bandit -r src/baobab_probability_core` | Aucun finding bloquant du projet ; code retour 0 |
| Tests + couverture | `pytest` | Tous les tests passent ; message **`Required test coverage of 90% reached`** (option `--cov-fail-under=90` dans `pyproject.toml`) |

Référence normative : [`docs/00_dev_constraints.md`](00_dev_constraints.md).

---

## Seuil de couverture

- **Minimum imposé : 90 %** (`[tool.pytest.ini_options] addopts` → `--cov-fail-under=90`).
- Les rapports HTML/XML sont générés sous `docs/tests/coverage/` (fichiers générés, non versionnés de façon obligatoire selon `.gitignore` du projet).

---

## Preuve locale (référence)

Exécution unique sur l’arbre de sources à jour, environnement de développement avec `pip install -e ".[dev]"` :

- **Python** : 3.13.12 (Windows).
- **Résultat** : les six commandes ci-dessus se terminent avec **code retour 0** ; **115** tests collectés, tous verts ; couverture totale rapportée **≈ 99,75 %** (≥ 90 %).

> Pour une preuve strictement alignée sur la CI, ré-exécuter les mêmes commandes sous **Python 3.11** (version du workflow GitHub Actions).

---

## Intégration continue (GitHub Actions)

- **Fichier workflow** : [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)
- **Nom du workflow** : **CI**
- **Déclencheurs** : **`push`** (toutes branches) et **`pull_request`**.
- **Job** : `quality` sur `ubuntu-latest`, Python **3.11**, mêmes étapes que le tableau ci-dessus (black, flake8, pylint, mypy, bandit, pytest). Une couverture **strictement inférieure au seuil 90 %** fait échouer le job : `pytest` applique `--cov-fail-under=90` depuis `pyproject.toml`.

**Référence de run historique (tag `v1.0.0`, succès, ancien déclencheur tags uniquement)** :

- Run ID : **23507200123**
- URL : https://github.com/baobabgit/baobab-probability-core/actions/runs/23507200123

---

## Maintenir cette preuve

Avant une release ou un GO formel :

1. Synchroniser `main`, installer `".[dev]"`.
2. Enchaîner les commandes du tableau (ou s’appuyer sur le run CI après push ou sur la CI de la **pull_request**).
3. Mettre à jour **la date** et, si nécessaire, **l’URL du dernier run CI** dans ce fichier via une PR dédiée.
