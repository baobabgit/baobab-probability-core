# Cahier des charges complet — `baobab-probability-core`

## 1. Contexte

Le projet `baobab-probability-core` est une librairie Python dédiée au calcul probabiliste et à l’analyse statistique élémentaire. Elle doit constituer un **noyau métier réutilisable** par d’autres projets de l’écosystème Baobab.

La librairie ne doit pas être pensée comme une application finale, mais comme une brique de base exploitable par :

- une CLI,
- une API,
- une librairie de reporting,
- un moteur de simulation,
- un projet de comparaison théorie / données observées.

Cette librairie a trois responsabilités majeures :

1. **calculer des probabilités théoriques**,
2. **simuler des expériences aléatoires**,
3. **comparer la théorie aux observations empiriques**.

---

## 2. Objectif produit

Développer une librairie Python installable, documentée et testée, permettant :

- le calcul exact de probabilités discrètes,
- la manipulation de distributions discrètes classiques,
- l’exécution de simulations statistiques reproductibles,
- l’analyse d’échantillons observés,
- la comparaison entre un modèle théorique et des observations.

Le projet doit être conçu pour une **v1 robuste, claire et maintenable**, avec un périmètre volontairement maîtrisé.

---

## 3. Objectifs fonctionnels

La librairie doit permettre de :

- représenter des événements et des espaces probabilistes finis,
- effectuer des calculs probabilistes standards,
- manipuler des lois discrètes usuelles,
- simuler des expériences aléatoires paramétrables,
- produire des résultats observés exploitables,
- calculer des métriques de comparaison entre théorie et observation,
- exposer une API Python claire, stable et typée.

---

## 4. Hors périmètre v1

Ne pas implémenter en v1 :

- interface CLI,
- interface web,
- génération de graphiques,
- génération de rapports PDF ou HTML,
- notebooks dédiés,
- statistiques inférentielles avancées,
- distributions continues complexes,
- moteur symbolique,
- dépendance obligatoire à `numpy`, `pandas` ou `scipy`.

Des extensions futures pourront exister, mais la v1 doit rester légère et maîtrisée.

---

## 5. Public cible

La librairie s’adresse à :

- des développeurs Python,
- des projets de simulation,
- des outils pédagogiques,
- des projets d’analyse statistique simple,
- des briques applicatives ayant besoin d’un noyau probabiliste réutilisable.

---

## 6. Contraintes générales de développement

Le développement doit respecter strictement les contraintes suivantes (référence détaillée : `docs/00_dev_constraints.md`) :

### 6.1 Structure du projet

- Le code source doit être placé sous `src/baobab_probability_core`.
- Les tests doivent être placés dans `tests/`.
- La documentation de développement doit être placée dans `docs/`.
- L’architecture doit être organisée par domaines fonctionnels.
- **Une classe par fichier**.
- Les tests doivent refléter l’arborescence du code source.

### 6.2 Style de programmation

- Le projet doit être développé en **programmation orientée objet**.
- Les noms doivent respecter PEP 8.
- Les classes doivent être en `PascalCase`.
- Les fonctions, méthodes, variables, modules et packages doivent être en `snake_case`.
- Les constantes doivent être en `UPPER_SNAKE_CASE`.
- Les noms doivent être explicites.

### 6.3 Typage

- Toutes les fonctions et méthodes doivent être typées.
- Tous les attributs de classe et d’instance doivent être annotés.
- Le projet doit passer `mypy` en mode strict ou quasi strict.

### 6.4 Documentation

- Toutes les classes, méthodes et fonctions publiques doivent avoir des docstrings.
- Le format attendu est **reStructuredText**.
- Le projet doit inclure :
  - `README.md`
  - `CHANGELOG.md`
  - `docs/dev_diary.md`

### 6.5 Qualité

Le code doit passer sans erreur :

- `black`
- `pylint`
- `mypy`
- `flake8`
- `bandit`

Longueur maximale des lignes : **100 caractères**.

### 6.6 Tests

- Un fichier de tests par classe.
- Les tests doivent être organisés en classes `TestNomClasse`.
- Couverture minimale : **90 %**.
- Les fichiers de couverture doivent être placés dans `docs/tests/coverage`.

### 6.7 Configuration

Tout ce qui peut être centralisé doit l’être dans `pyproject.toml`, notamment :

- métadonnées du projet,
- dépendances,
- configuration qualité,
- configuration pytest,
- configuration coverage.

### 6.8 Exceptions

- Le projet doit avoir une **exception racine spécifique**.
- Toutes les exceptions du projet doivent hériter de cette exception racine.
- Les erreurs spécifiques au projet doivent faire l’objet d’**exceptions spécifiques dédiées**.

### 6.9 Versioning

- Le projet doit suivre **SemVer**.
- La version doit être portée dans `pyproject.toml`.
- Les releases doivent pouvoir être taguées sous la forme `vMAJOR.MINOR.PATCH`.

### 6.10 Journal de développement

Le fichier `docs/dev_diary.md` doit être tenu à jour avec :

- date et heure,
- modifications,
- buts,
- impacts.

Ordre décroissant : les entrées les plus récentes en premier.

---

## 7. Architecture cible

Arborescence cible recommandée :

```text
src/baobab_probability_core/
├── __init__.py
├── exceptions/
│   ├── __init__.py
│   ├── baobab_probability_core_exception.py
│   ├── invalid_probability_value_exception.py
│   ├── invalid_distribution_parameter_exception.py
│   ├── invalid_sample_exception.py
│   ├── incompatible_observation_exception.py
│   └── unsupported_experiment_exception.py
├── constants/
│   ├── __init__.py
│   └── mathematical_constants.py
├── validators/
│   ├── __init__.py
│   ├── probability_validator.py
│   ├── distribution_parameter_validator.py
│   └── sample_validator.py
├── combinatorics/
│   ├── __init__.py
│   ├── factorial_calculator.py
│   ├── permutation_calculator.py
│   ├── arrangement_calculator.py
│   └── combination_calculator.py
├── probability/
│   ├── __init__.py
│   ├── event.py
│   ├── finite_probability_space.py
│   ├── probability_calculator.py
│   ├── conditional_probability_calculator.py
│   ├── bayes_calculator.py
│   └── independence_checker.py
├── distributions/
│   ├── __init__.py
│   ├── base_distribution.py
│   ├── bernoulli_distribution.py
│   ├── binomial_distribution.py
│   ├── geometric_distribution.py
│   ├── hypergeometric_distribution.py
│   └── poisson_distribution.py
├── simulation/
│   ├── __init__.py
│   ├── random_generator.py
│   ├── simulation_config.py
│   ├── simulation_result.py
│   ├── bernoulli_simulator.py
│   ├── binomial_simulator.py
│   ├── dice_roll_simulator.py
│   └── urn_draw_simulator.py
├── statistics/
│   ├── __init__.py
│   ├── frequency_analyzer.py
│   ├── empirical_moment_calculator.py
│   ├── descriptive_statistics.py
│   └── distribution_observation.py
├── comparison/
│   ├── __init__.py
│   ├── probability_comparison_result.py
│   ├── distribution_comparison_result.py
│   ├── goodness_of_fit_calculator.py
│   └── theoretical_observation_comparator.py
└── utils/
    ├── __init__.py
    └── floating_point_comparator.py
```

---

## 8. Exigences fonctionnelles détaillées

## 8.1 Combinatoire

Implémenter les calculateurs suivants :

- factorielle,
- permutation,
- arrangement,
- combinaison.

### Exigences

- validation stricte des entrées,
- refus des valeurs invalides,
- résultats exacts sur entiers,
- docstrings complètes,
- exceptions métier dédiées.

### Cas à supporter

- zéro,
- un,
- grands entiers raisonnables,
- cas invalides : négatifs, incohérences de paramètres.

---

## 8.2 Calculs de probabilité

Implémenter des services permettant de calculer :

- probabilité simple,
- complémentaire,
- intersection,
- union,
- probabilité conditionnelle,
- indépendance,
- théorème de Bayes.

### Exigences

- tous les calculs doivent être documentés,
- les validations doivent être strictes,
- les incohérences doivent lever des exceptions dédiées,
- les calculs doivent gérer les problèmes classiques de flottants via une tolérance centrale.

### Cas à gérer

- probabilité hors intervalle `[0, 1]`,
- division par zéro en conditionnelle,
- événements incompatibles,
- contrôles de cohérence.

---

## 8.3 Modélisation d’espace probabiliste fini

Implémenter une représentation d’un espace probabiliste discret fini.

### Objets attendus

#### `Event`

Doit représenter un événement discret identifiable ; les issues sont des valeurs **hashables** (souvent ``str``, entiers, tuples, énumérations), pas uniquement des chaînes.

#### `FiniteProbabilitySpace`

Doit permettre de :

- définir un univers fini,
- enregistrer des issues,
- associer des probabilités,
- valider que la somme des probabilités vaut 1, à tolérance près,
- récupérer des probabilités associées à des événements simples.

### Exigences

- API explicite,
- validations robustes,
- gestion des incohérences par exceptions spécifiques.

---

## 8.4 Distributions discrètes

Implémenter une hiérarchie pour les lois discrètes suivantes :

- Bernoulli,
- Binomiale,
- Géométrique,
- Hypergéométrique,
- Poisson.

### Classe abstraite

Créer une classe abstraite `BaseDistribution` définissant au minimum :

- `probability_of(value: int) -> float`
- `expected_value() -> float`
- `variance() -> float`

Une méthode `support()` peut être ajoutée si jugé pertinent.

### Exigences communes

Chaque distribution doit :

- valider ses paramètres à la construction,
- calculer la probabilité d’une valeur,
- calculer son espérance,
- calculer sa variance,
- être documentée,
- être testée indépendamment.

### Paramètres à valider

#### Bernoulli

- `p` dans `[0, 1]`

#### Binomiale

- `n >= 0`
- `p` dans `[0, 1]`

#### Géométrique

- `p` strictement positif et inférieur ou égal à 1

#### Hypergéométrique

- cohérence entre population totale, succès dans population, tirages

#### Poisson

- `lambda > 0`

---

## 8.5 Simulation statistique

Implémenter des simulateurs reproductibles.

### Composants attendus

#### `SimulationConfig`

Contient au minimum :

- `iterations`
- `seed`

#### `RandomGenerator`

Encapsule le générateur aléatoire standard Python afin de garantir :

- reproductibilité,
- isolation du comportement aléatoire,
- testabilité.

#### `SimulationResult`

Doit encapsuler les résultats d’une simulation sous forme typée (champs explicites selon l’expérience), avec une vue dictionnaire optionnelle compatible avec les versions précédentes pour les mêmes clés métier.

### Simulations à implémenter

- Bernoulli,
- binomiale,
- lancer de dé équilibré,
- tirage dans une urne,
- tirage avec remise,
- tirage sans remise.

### Exigences

- résultats déterministes avec la même graine,
- API simple,
- séparation claire entre configuration, moteur et résultat,
- pas d’utilisation directe dispersée du module `random` dans tout le projet.

---

## 8.6 Analyse statistique des observations

Implémenter des services permettant de calculer :

- effectifs observés,
- fréquences observées,
- fréquences relatives,
- moyenne empirique,
- variance empirique,
- statistiques descriptives de base.

### Objets attendus

#### `DistributionObservation`

Représente des observations discrètes ou un comptage de modalités.

#### `FrequencyAnalyzer`

Produit les comptages et fréquences.

#### `EmpiricalMomentCalculator`

Calcule les moments empiriques simples.

#### `DescriptiveStatistics`

Expose un résumé statistique réutilisable.

### Exigences

- validation de la non-vacuité lorsque nécessaire,
- gestion des entrées invalides,
- cohérence des sorties,
- documentation claire.

---

## 8.7 Comparaison théorie / observation

Implémenter des services de comparaison entre :

- une probabilité théorique et une fréquence observée,
- une distribution théorique et une distribution empirique.

### Composants attendus

#### `ProbabilityComparisonResult`

Doit contenir au minimum :

- probabilité théorique,
- fréquence observée,
- écart absolu,
- écart relatif.

#### `DistributionComparisonResult`

Doit contenir au minimum :

- modalités comparées,
- probabilités théoriques,
- fréquences observées,
- écarts par modalité,
- métriques agrégées.

#### `TheoreticalObservationComparator`

Service principal de comparaison.

### Métriques minimales

- erreur absolue,
- erreur relative,
- somme des écarts absolus,
- écart maximal.

---

## 8.8 Score d’adéquation simple

Implémenter un premier composant de type `GoodnessOfFitCalculator`.

### Objectif

Fournir une base de comparaison d’adéquation entre théorie et observations discrètes.

### Contraintes

- ne pas imposer `scipy` en production pour la v1,
- documenter clairement la formule retenue,
- nommer précisément les métriques,
- rester conservateur sur les prétentions statistiques.

Ce composant peut rester simple, mais il doit être proprement encapsulé.

---

## 9. Exigences non fonctionnelles

### 9.1 Robustesse

- validation systématique des entrées,
- exceptions métier spécifiques,
- comportements déterministes,
- absence de logique implicite cachée.

### 9.2 Lisibilité

- architecture claire,
- classes courtes et ciblées,
- responsabilités bien séparées,
- méthodes nommées explicitement.

### 9.3 Réutilisabilité

- ne pas coupler la librairie à un front, une CLI ou une API,
- conserver un noyau métier pur,
- éviter les dépendances inutiles.

### 9.4 Maintenabilité

- code typé,
- documentation structurée,
- tests explicites,
- journal de développement à jour.

### 9.5 Performance

La performance n’est pas l’objectif principal de la v1, mais :

- les algorithmes doivent être raisonnables,
- aucune complexité inutile ne doit être introduite,
- les simulations courantes doivent rester fluides pour des volumes usuels.

---

## 10. Exceptions du projet

Créer une hiérarchie d’exceptions dédiée.

### Exception racine

- `BaobabProbabilityCoreException`

### Exceptions minimales attendues

- `InvalidProbabilityValueException`
- `InvalidDistributionParameterException`
- `InvalidSampleException`
- `IncompatibleObservationException`
- `UnsupportedExperimentException`

D’autres exceptions peuvent être ajoutées si utiles, mais elles doivent toutes hériter de l’exception racine.

---

## 11. API publique attendue

L’API doit permettre un usage de ce type :

```python
from baobab_probability_core.distributions.binomial_distribution import BinomialDistribution

distribution = BinomialDistribution(trials=10, probability=0.4)
probability = distribution.probability_of(3)
mean = distribution.expected_value()
variance = distribution.variance()
```

```python
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.bernoulli_simulator import BernoulliSimulator

config = SimulationConfig(iterations=1000, seed=42)
simulator = BernoulliSimulator(config=config)
result = simulator.run(success_probability=0.3)
```

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

L’API exacte peut être ajustée, mais elle doit rester cohérente, stable et explicite.

---

## 12. Dépendances

### 12.1 Production

Objectif prioritaire : **aucune dépendance externe obligatoire**.

La v1 doit s’appuyer au maximum sur la bibliothèque standard Python.

### 12.2 Développement

Prévoir dans les dépendances de développement :

- `pytest`
- `pytest-cov`
- `black`
- `pylint`
- `mypy`
- `flake8`
- `bandit`

Des outils complémentaires peuvent être ajoutés si justifiés, mais sans complexifier inutilement le projet.

---

## 13. Livrables attendus

Le développement doit produire au minimum :

- le package Python installable,
- l’arborescence `src/`,
- l’arborescence `tests/`,
- l’arborescence `docs/`,
- `pyproject.toml`,
- `README.md`,
- `CHANGELOG.md`,
- `docs/dev_diary.md`,
- les implémentations métier,
- les tests unitaires,
- la configuration qualité,
- une API publique cohérente.

---

## 14. README attendu

Le `README.md` doit inclure :

- description du projet,
- objectifs,
- installation,
- prérequis Python,
- exemples d’utilisation,
- structure du projet,
- règles de contribution,
- statut de version,
- licence.

---

## 15. Tests attendus

Chaque classe doit avoir son fichier de tests dédié.

### Les tests doivent couvrir au minimum

- cas nominaux,
- cas limites,
- cas invalides,
- exceptions levées,
- cohérence des calculs,
- reproductibilité des simulations,
- comparaison théorie / observation.

### Cas importants à couvrir

- `p = 0`
- `p = 1`
- `n = 0`
- probabilités invalides
- échantillons vides
- paramètres incohérents
- effets de la graine aléatoire
- tolérance flottante
- comparaison sur petits et grands volumes

---

## 16. Critères d’acceptation

Le projet sera considéré conforme si :

- la librairie s’installe correctement,
- l’arborescence respecte les contraintes,
- le code est typé,
- le code passe `black`, `pylint`, `mypy`, `flake8` et `bandit`,
- les tests passent,
- la couverture est au moins de 90 %,
- les exceptions spécifiques sont bien en place,
- la documentation minimale existe,
- le journal de développement est à jour,
- les fonctionnalités du périmètre v1 sont opérationnelles.

---

## 17. Plan de réalisation recommandé

Ordre recommandé de développement :

1. bootstrap du projet,
2. exceptions et validateurs,
3. combinatoire,
4. espace probabiliste et événements,
5. calculateurs de probabilité,
6. base des distributions,
7. distributions Bernoulli et Binomiale,
8. autres distributions discrètes,
9. socle de simulation,
10. simulateurs,
11. statistiques empiriques,
12. comparaison théorie / observation,
13. score d’adéquation,
14. documentation et durcissement qualité.

---

## 18. Consignes directes à l’IA de développement

Tu dois :

- respecter strictement l’architecture proposée,
- respecter les contraintes de développement énoncées,
- créer une classe par fichier,
- créer un fichier de tests par classe,
- centraliser la configuration dans `pyproject.toml`,
- créer des exceptions spécifiques au projet,
- documenter toutes les API publiques,
- tenir à jour `docs/dev_diary.md`,
- viser une couverture minimale de 90 %,
- éviter les dépendances de production inutiles,
- produire un code clair, maintenable et prêt pour une release v1.

Tu ne dois pas :

- introduire une CLI dans ce dépôt,
- mélanger plusieurs responsabilités dans une même classe,
- contourner le typage,
- utiliser des dépendances scientifiques lourdes sans justification,
- laisser des comportements implicites non documentés,
- produire du code non testé.

---

## 19. Résultat attendu en fin de v1

À la fin du développement, `baobab-probability-core` doit être une librairie Python fiable, propre et réutilisable, capable de servir de socle à tout projet Baobab nécessitant :

- des calculs probabilistes discrets,
- des simulations simples,
- une analyse statistique empirique,
- une comparaison entre modèle théorique et données observées.
