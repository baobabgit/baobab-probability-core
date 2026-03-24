"""Lancers de dé équilibré."""

from collections import Counter

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)
from baobab_probability_core.simulation.random_generator import RandomGenerator
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.simulation_result import SimulationResult


class DiceRollSimulator:
    """Compte les occurrences de chaque face sur des lancers i.i.d."""

    def __init__(self, config: SimulationConfig) -> None:
        """Construit le simulateur."""
        self._config: SimulationConfig = config

    def run(self, sides: int) -> SimulationResult:
        """Lance un dé à ``sides`` faces ``iterations`` fois.

        :param sides: Nombre de faces (au moins 2).
        :returns: ``face_counts`` et ``face_counts_sorted`` ; clé legacy
            ``data['counts_by_face']``.
        """
        if sides < 2:
            raise UnsupportedExperimentException(
                f"Un dé doit avoir au moins 2 faces (reçu {sides})."
            )
        gen: RandomGenerator = RandomGenerator(self._config.seed)
        counter: Counter[int] = Counter()
        for _ in range(self._config.iterations):
            face: int = gen.rng.randint(1, sides)
            counter[face] += 1
        return SimulationResult(
            face_counts_sorted=tuple(sorted(counter.items())),
        )
