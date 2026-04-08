# Changelog

## [1.0.1] — 2026-04-09

### Corrigé

- **Bayes** : `BayesCalculator.posterior` impose des entrées cohérentes (`P(A)` dans `]0, 1]`, `P(A|B)·P(B) ≤ P(A)`) pour garantir un posterior dans `[0, 1]`.
- **Comparaison** : validation centralisée des distributions discrètes (`ProbabilityValidator.validate_discrete_probability_distribution`) appliquée aux comparateurs théorie / observation et à `FiniteProbabilitySpace` (masses finies, `[0, 1]`, somme 1 à tolérance près).

## [1.0.0] — 2026-03-24

### Modifié

- Métadonnées de packaging : classifier PyPI `Development Status :: 5 - Production/Stable`, URLs `Homepage`, `Repository` et `Changelog` dans `pyproject.toml`.
- **Intégration continue** : workflow GitHub Actions **CI** sur `push` et `pull_request` (black, flake8, pylint, mypy, bandit, pytest ; seuil de couverture **90 %**).
- **Documentation** : `docs/release_validation.md` (preuve des quality gates), badge CI dans le `README.md`.
- **Simulation** : `SimulationResult` est une `dataclass` typée (champs explicites, propriété `face_counts`) ; la propriété `data` reprend en lecture seule les clés `values`, `successes`, `counts_by_face`, `successes_per_trial`. La construction `SimulationResult(data=...)` n’est plus prise en charge.
- **Probabilité** : `Event` et `FiniteProbabilitySpace` sont génériques sur des issues **hashables** (`OutcomeT` borné par `Hashable`) ; `ProbabilityCalculator`, `ConditionalProbabilityCalculator` et `IndependenceChecker` propagent le même paramètre de type. Export public de `OutcomeT`.

### Ajouté

- Première version publiable du noyau `baobab-probability-core`.
- Combinatoire : factorielle, permutations, arrangements, combinaisons avec validations strictes.
- Probabilité : événements, espaces finis, complément / union / intersection, conditionnement, Bayes, indépendance (tolérance flottante).
- Distributions discrètes : Bernoulli, binomiale, géométrique (succès au k-ième essai), hypergéométrique, Poisson.
- Simulation : `SimulationConfig`, `RandomGenerator`, `SimulationResult`, simulateurs Bernoulli, binomiale, dé, urne (avec / sans remise).
- Statistiques empiriques : `DistributionObservation`, fréquences, moments, descriptifs.
- Comparaison : `ProbabilityComparisonResult`, `DistributionComparisonResult`, `TheoreticalObservationComparator`, `GoodnessOfFitCalculator` (χ² de Pearson, distance en variation totale).
- Exceptions métier hiérarchisées sous `BaobabProbabilityCoreException`.
- Configuration centralisée dans `pyproject.toml` (dont **flake8** via **Flake8-pyproject**), tests avec couverture ≥ 90 %, rapports HTML/XML sous `docs/tests/coverage/`.
