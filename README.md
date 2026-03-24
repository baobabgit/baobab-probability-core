# baobab-probability-core

Bibliothèque Python pour **probabilités discrètes**, **simulations reproductibles** et **comparaison théorie / observations**. Elle constitue un noyau métier réutilisable (CLI, API, reporting, moteurs de simulation) sans dépendances scientifiques obligatoires en production.

## Objectifs

- Calcul exact de probabilités et combinatoire sur entiers.
- Manipulation de lois discrètes usuelles (Bernoulli, binomiale, géométrique, hypergéométrique, Poisson).
- Simulations déterministes à graine fixée.
- Analyse d’effectifs et fréquences empiriques.
- Métriques simples d’écart et d’adéquation (χ² de Pearson, variation totale).

## Prérequis

- Python **3.11+**

## Installation

```bash
pip install -e .
```

Dépendances de développement (tests, formatage, lint) :

```bash
pip install -e ".[dev]"
```

## Exemples

### Loi binomiale

```python
from baobab_probability_core.distributions.binomial_distribution import BinomialDistribution

distribution = BinomialDistribution(trials=10, probability=0.4)
probability = distribution.probability_of(3)
mean = distribution.expected_value()
variance = distribution.variance()
```

### Simulation Bernoulli

```python
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.bernoulli_simulator import BernoulliSimulator

config = SimulationConfig(iterations=1000, seed=42)
simulator = BernoulliSimulator(config=config)
result = simulator.run(success_probability=0.3)
# Contrat typé privilégié : result.trial_outcomes, result.bernoulli_success_total
# Compatibilité : result.data["values"], result.data["successes"]
```

### Comparaison probabilité / fréquence

```python
from baobab_probability_core.comparison.theoretical_observation_comparator import (
    TheoreticalObservationComparator,
)

comparator = TheoreticalObservationComparator()
comparison = comparator.compare_probability(
    theoretical_probability=0.3,
    observed_successes=297,
    observed_trials=1000,
)
```

## Structure du projet

```text
src/baobab_probability_core/
├── combinatorics/      # Factorielles, permutations, arrangements, combinaisons
├── comparison/         # Écarts théorie / observation, adéquation
├── constants/          # Constantes numériques partagées
├── distributions/      # Lois discrètes
├── exceptions/         # Hiérarchie d'exceptions métier
├── probability/        # Espaces finis, Bayes, conditionnelles
├── simulation/         # Générateur, config, simulateurs
├── statistics/         # Effectifs, moments, descriptifs
├── utils/              # Comparaisons flottantes
└── validators/         # Validation des entrées
tests/baobab_probability_core/   # Tests miroir (une classe → un module de tests)
docs/
├── 00_dev_constraints.md  # Contraintes de développement (Markdown)
├── dev_diary.md             # Journal de développement
└── tests/coverage/          # Rapports de couverture (générés)
```

## Qualité

```bash
black src tests
flake8 src tests
mypy src/baobab_probability_core
pylint src/baobab_probability_core
bandit -r src/baobab_probability_core
pytest
```

Couverture minimale attendue : **90 %** (voir `pyproject.toml`).

Les réglages **flake8** sont dans `pyproject.toml` (`[tool.flake8]`). Comme flake8 ne charge pas ce fichier nativement, la dépendance de développement **Flake8-pyproject** applique cette configuration lorsque vous exécutez `flake8` après `pip install -e ".[dev]"`.

## Intégration continue

Le workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) s’exécute uniquement lorsqu’un **tag Git** est poussé sur le dépôt (`git push origin <tag>`). Il lance : installation Python **3.11**, `pip install -e ".[dev]"`, puis `black --check`, `flake8`, `pylint`, `mypy`, `bandit` et `pytest`. La couverture est imposée par `pytest` (seuil **90 %** défini dans `pyproject.toml`) : le job échoue si le seuil n’est pas atteint.

## Contribution

- Respecter **PEP 8**, typage strict, **une classe par fichier** côté production.
- Docstrings publiques en **reStructuredText**.
- Suivre les contraintes de développement décrites dans [`docs/00_dev_constraints.md`](docs/00_dev_constraints.md).
- Ajouter ou mettre à jour les tests et une entrée dans `docs/dev_diary.md`.

## Version

Version actuelle : **1.0.0** (voir `pyproject.toml`), **statut stable** (classifier PyPI `Production/Stable`), versioning **SemVer**, tags de release `vMAJOR.MINOR.PATCH`.

Dépôt : [github.com/baobabgit/baobab-probability-core](https://github.com/baobabgit/baobab-probability-core).

## Licence

Voir le fichier `LICENSE` à la racine du dépôt.
