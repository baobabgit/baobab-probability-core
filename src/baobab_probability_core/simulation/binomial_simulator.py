"""Simulation de lois binomiales (somme de Bernoulli)."""

from baobab_probability_core.simulation.random_generator import RandomGenerator
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.simulation_result import SimulationResult
from baobab_probability_core.validators.distribution_parameter_validator import (
    DistributionParameterValidator,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BinomialSimulator:
    """Pour chaque itération, compte les succès sur ``n`` essais."""

    def __init__(self, config: SimulationConfig) -> None:
        """Construit le simulateur."""
        self._config: SimulationConfig = config
        self._int_val: DistributionParameterValidator = DistributionParameterValidator()
        self._prob_val: ProbabilityValidator = ProbabilityValidator()

    def run(self, trials: int, success_probability: float) -> SimulationResult:
        """Simule ``iterations`` réalisations de ``B(n, p)``.

        :param trials: Nombre d'essais ``n`` par itération.
        :param success_probability: Probabilité de succès ``p``.
        :returns: ``trial_outcomes`` (succès par itération) ; clé legacy ``data['values']``.
        """
        self._int_val.validate_non_negative_int(trials, "n")
        self._prob_val.validate_closed_unit_interval(success_probability)
        gen: RandomGenerator = RandomGenerator(self._config.seed)
        values: list[int] = []
        for _ in range(self._config.iterations):
            s: int = 0
            for _t in range(trials):
                if gen.rng.random() < success_probability:
                    s += 1
            values.append(s)
        return SimulationResult(trial_outcomes=tuple(values))
