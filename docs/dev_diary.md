# Journal de développement — baobab-probability-core

Les entrées les plus récentes en premier.

---

## 2026-03-24 — CI déclenchée par tags uniquement

**Modifications :** `.github/workflows/ci.yml` : déclencheur `push` limité aux **tags** (plus de `pull_request`). Mise à jour de la section **Intégration continue** dans `README.md`.

**Buts :** Lancer les quality gates à la publication / étiquetage plutôt qu’à chaque push ou PR.

**Impacts :** Les développeurs doivent lancer les contrôles en local avant merge ; la CI ne signale plus automatiquement les régressions sur les branches sans tag.

---

## 2026-03-24 — CI GitHub Actions

**Modifications :** Ajout de `.github/workflows/ci.yml` déclenché sur `push` et `pull_request` : Python 3.11, `pip install -e ".[dev]"`, enchaînement `black --check`, `flake8`, `pylint`, `mypy`, `bandit`, `pytest` (seuil de couverture inchangé, via `pyproject.toml`). Section **Intégration continue** dans `README.md`.

**Buts :** Verrouiller les quality gates sur chaque changement ; alignement avec `docs/00_dev_constraints.md`.

**Impacts :** Les PR sans tests ou sans style conforme seront signalées par un workflow rouge ; pas de changement du code applicatif.

---

## 2026-03-24 — contraintes de développement en Markdown

**Modifications :** Renommage de `docs/00_dev_constraints.py` en `docs/00_dev_constraints.md` (contenu déjà rédigé en Markdown, sans perte d’information). Ajout d’un court rappel en tête de document ; section journal alignée sur `docs/dev_diary.md` pour ce dépôt. Suppression du fichier `.py` pour éviter toute confusion avec du code exécutable. Mises à jour de `README.md` (structure `docs/`, lien vers les contraintes) et de `docs/01_specifications.md` (référence explicite au fichier de contraintes).

**Buts :** Documentation cohérente avec les conventions du dépôt ; aucune dépendance d’outil sur un faux module Python.

**Impacts :** Les contributeurs lisent les contraintes dans un vrai fichier Markdown ; les ancres et le sommaire restent valides.

---

## 2026-03-24 — alignement métadonnées release stable

**Modifications :** `pyproject.toml` : classifier `Development Status :: 5 - Production/Stable` (remplace la bêta), `project.urls.Homepage` → `https://github.com/baobabgit/baobab-probability-core`. `README.md` (section Version : statut stable + lien dépôt), `CHANGELOG.md` (sous-section *Modifié* pour la version 1.0.0).

**Buts :** Cohérence entre la version SemVer 1.0.0 annoncée et les métadonnées présentées aux utilisateurs / PyPI ; URL du dépôt alignée sur l’organisation GitHub réelle.

**Impacts :** Aucun changement de code applicatif ; publication PyPI future reflétera un produit stable et le bon lien de projet.

---

## 2026-03-24 — ~23:20 (UTC+1)

**Modifications :** Implémentation complète de la v1 selon le cahier des charges : arborescence `src/baobab_probability_core` (exceptions, validateurs, combinatoire, probabilité sur espaces finis, distributions discrètes, simulation, statistiques empiriques, comparaison théorie/observation, utilitaires flottants), `pyproject.toml` (métadonnées SemVer 1.0.0, outillage black/mypy/pytest-cov/pylint/flake8/bandit), suite de tests miroir avec couverture ≥ 90 %, `README.md`, `CHANGELOG.md`, configuration `flake8`, exclusion bandit justifiée pour `random.Random` (usage statistique non cryptographique).

**Buts :** Livrer un noyau installable, typé, documenté (docstrings reStructuredText), sans dépendance de production obligatoire hors bibliothèque standard.

**Impacts :** Base réutilisable pour CLI/API/reporting futurs ; rapports de couverture générés sous `docs/tests/coverage/` (non versionnés via `.gitignore`).

---

## 2026-03-24 — ~22:00 (UTC+1)

**Modifications :** État initial du dépôt partiellement amorcé ; reconstruction alignée sur les tests existants et extension jusqu’aux critères d’acceptation (qualité, couverture, documentation).

**Buts :** Alignement strict sur l’architecture cible et les contraintes OOP / une classe par fichier.

**Impacts :** Stabilisation de l’API publique d’import (chemins de modules explicites).
