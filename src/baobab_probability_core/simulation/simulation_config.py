"""Configuration de simulation."""

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)


class SimulationConfig:
    """Paramètres communs : nombre d'itérations et graine."""

    def __init__(self, iterations: int, seed: int | None) -> None:
        """Construit la configuration.

        :param iterations: Nombre de répétitions (strictement positif).
        :param seed: Graine ; ``None`` pour un comportement non déterministe.
        :raises UnsupportedExperimentException: si ``iterations < 1``.
        """
        if iterations < 1:
            raise UnsupportedExperimentException(f"iterations doit être >= 1 (reçu {iterations}).")
        self._iterations: int = iterations
        self._seed: int | None = seed

    @property
    def iterations(self) -> int:
        """Nombre d'itérations."""
        return self._iterations

    @property
    def seed(self) -> int | None:
        """Graine de reproductibilité."""
        return self._seed
