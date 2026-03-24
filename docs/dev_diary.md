# Journal de développement — baobab-probability-core

Les entrées les plus récentes en premier.

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
