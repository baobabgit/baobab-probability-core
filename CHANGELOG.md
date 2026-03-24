# Changelog

## [Non publié]

### Modifié

- **Probabilité** : `Event` et `FiniteProbabilitySpace` sont génériques sur des issues **hashables** (`OutcomeT` borné par `Hashable`) ; les usages existants avec des clés `str` restent valides. `ProbabilityCalculator`, `ConditionalProbabilityCalculator` et `IndependenceChecker` propagent le même paramètre de type.
- **Simulation** : `SimulationResult` est une `dataclass` typée (tuples entiers, effectifs de dé triés par face) ; la propriété `data` reprend les clés `values`, `successes`, `counts_by_face`, `successes_per_trial`. La construction `SimulationResult(data=...)` n’est plus prise en charge.

## [1.0.0] — 2026-03-24

### Modifié

- Métadonnées de packaging : classifier PyPI `Development Status :: 5 - Production/Stable`, URL `Homepage` pointant vers `baobabgit/baobab-probability-core`.

### Ajouté

- Première version publiable du noyau `baobab-probability-core`.
- Combinatoire : factorielle, permutations, arrangements, combinaisons avec validations strictes.
- Probabilité : événements, espaces finis, complément / union / intersection, conditionnement, Bayes, indépendance (tolérance flottante).
- Distributions discrètes : Bernoulli, binomiale, géométrique (succès au k-ième essai), hypergéométrique, Poisson.
- Simulation : `SimulationConfig`, `RandomGenerator`, `SimulationResult`, simulateurs Bernoulli, binomiale, dé, urne (avec / sans remise).
- Statistiques empiriques : `DistributionObservation`, fréquences, moments, descriptifs.
- Comparaison : `ProbabilityComparisonResult`, `DistributionComparisonResult`, `TheoreticalObservationComparator`, `GoodnessOfFitCalculator` (χ² de Pearson, distance en variation totale).
- Exceptions métier hiérarchisées sous `BaobabProbabilityCoreException`.
- Configuration centralisée dans `pyproject.toml`, tests avec couverture ≥ 90 %, rapports HTML/XML sous `docs/tests/coverage/`.
