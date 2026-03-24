# Validation technique avant release (quality gates)

Ce document enregistre **quels contrôles** doivent passer, **comment** ils sont exécutés dans le dépôt, une **preuve** (locale + CI), et la **conclusion** pour un GO release stable.

---

## Date de validation documentaire

**2026-03-24** — actualisation après exécution locale complète des six contrôles (voir § Preuve locale) et prise en compte du workflow **CI** sur `push` et `pull_request` ([`.github/workflows/ci.yml`](../.github/workflows/ci.yml)), aligné sur `docs/00_dev_constraints.md`.

---

## Liste des contrôles et critères de réussite

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
- **Vérification explicite :** en l’état du dépôt à la date ci-dessus, la couverture totale rapportée par `pytest` est **d’environ 99,75 %** (au-dessus du plancher).
- Les rapports HTML/XML sont générés sous `docs/tests/coverage/` (fichiers générés ; non versionnés de façon obligatoire selon `.gitignore` du projet).

---

## Preuve locale (référence)

Enchaînement **black → flake8 → pylint → mypy → bandit → pytest** après `pip install -e ".[dev]"` sur l’arbre à jour :

- **Python** : 3.13.12 (Windows) — la CI GitHub utilise **3.11** ; les commandes sont les mêmes.
- **Résultat** : **code retour 0** pour chaque étape ; **115** tests, tous verts ; couverture **≥ 90 %** (≈ **99,75 %**).

---

## Intégration continue (GitHub Actions)

- **Fichier workflow** : [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)
- **Nom du workflow** : **CI**
- **Déclencheurs** : **`push`** et **`pull_request`**.
- **Job** : `quality` sur `ubuntu-latest`, Python **3.11**, mêmes étapes que le tableau ci-dessus. Une couverture **strictement inférieure au seuil 90 %** ou un test en échec fait échouer le job (`pytest` + `pyproject.toml`).

**Référence de run CI (branche `main`, dernier succès vérifié au moment de la mise à jour)** :

- Run ID : **23508172802**
- URL : https://github.com/baobabgit/baobab-probability-core/actions/runs/23508172802

**Référence archivée (CI déclenchée uniquement par tags sur l’historique ; sans tag actif sur le dépôt aujourd’hui)** :

- Run ID : **23507200123**
- URL : https://github.com/baobabgit/baobab-probability-core/actions/runs/23507200123

Le dépôt expose un **badge CI** dans [`README.md`](../README.md) (lien vers la liste des exécutions du workflow).

---

## Conclusion de validation technique

Sous réserve que l’arborescence et les dépendances correspondent à cette documentation (notamment `pip install -e ".[dev]"` pour les outils) :

1. Les **quality gates** listés sont **exhaustifs** par rapport aux attentes usuelles du projet (formatage, lint, typage, sécurité, tests, couverture).
2. Le **seuil de couverture 90 %** est **atteint et dépassé** ; il est **appliqué en CI** comme en local.
3. Le workflow **CI** sur GitHub Actions **réexécute les mêmes contrôleurs** que ce tableau.

**Le projet est donc considéré comme techniquement prêt pour une release stable** au sens de ces critères automatisés. Tout GO fonctionnel ou produit reste distinct (p.ex. validation métier, publication PyPI, communication).

---

## Maintenir cette preuve

Avant une release ou un GO formel :

1. Synchroniser `main`, installer `".[dev]"`.
2. Enchaîner les commandes du tableau (ou s’appuyer sur le run CI après **push** ou sur la CI de la **pull_request**).
3. Mettre à jour **la date**, **la preuve locale** si les chiffres changent, et **l’URL du dernier run CI** sur `main` dans ce fichier via une PR dédiée.
