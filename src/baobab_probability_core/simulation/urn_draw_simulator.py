"""Tirages dans une urne finie, avec ou sans remise."""

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)
from baobab_probability_core.simulation.random_generator import RandomGenerator
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.simulation_result import SimulationResult


class UrnDrawSimulator:
    """Simule des échantillons depuis une urne binaire (succès / échec)."""

    def __init__(self, config: SimulationConfig) -> None:
        """Construit le simulateur."""
        self._config: SimulationConfig = config

    def run_with_replacement(
        self,
        population_size: int,
        success_balls: int,
        sample_size: int,
    ) -> SimulationResult:
        """À chaque tirage, la boule est remise : ``n`` tirages indépendants.

        Le nombre de succès suit ``B(n, K/N)``.

        :returns: ``data['successes_per_trial']`` liste de longueur ``iterations``.
        """
        self._validate_population(population_size, success_balls)
        if sample_size < 0:
            raise UnsupportedExperimentException("sample_size doit être positif ou nul.")
        gen: RandomGenerator = RandomGenerator(self._config.seed)
        p: float = success_balls / population_size
        results: list[int] = []
        for _ in range(self._config.iterations):
            succ: int = 0
            for _d in range(sample_size):
                if gen.rng.random() < p:
                    succ += 1
            results.append(succ)
        return SimulationResult(data={"successes_per_trial": results})

    def run_without_replacement(
        self,
        population_size: int,
        success_balls: int,
        sample_size: int,
    ) -> SimulationResult:
        """Tirages sans remise : hypergéométrique par itération.

        :returns: ``data['successes_per_trial']``.
        """
        self._validate_population(population_size, success_balls)
        self._validate_sample_without_replacement(population_size, sample_size)
        gen: RandomGenerator = RandomGenerator(self._config.seed)
        results: list[int] = []
        for _ in range(self._config.iterations):
            # Urne comme liste 0/1 mélangée
            urn: list[int] = [1] * success_balls + [0] * (population_size - success_balls)
            gen.rng.shuffle(urn)
            drawn: int = sum(urn[:sample_size])
            results.append(drawn)
        return SimulationResult(data={"successes_per_trial": results})

    def _validate_population(self, population_size: int, success_balls: int) -> None:
        if population_size < 1:
            raise UnsupportedExperimentException("La population doit être au moins 1.")
        if not 0 <= success_balls <= population_size:
            raise UnsupportedExperimentException(
                "Le nombre de boules « succès » doit être entre 0 et la population."
            )

    def _validate_sample_without_replacement(self, population_size: int, sample_size: int) -> None:
        if sample_size < 0 or sample_size > population_size:
            raise UnsupportedExperimentException(
                "La taille d'échantillon doit être entre 0 et la population (tirage sans remise)."
            )
