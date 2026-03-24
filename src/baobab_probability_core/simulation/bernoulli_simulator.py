"""Simulation de tirages de Bernoulli."""

from baobab_probability_core.simulation.random_generator import RandomGenerator
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.simulation_result import SimulationResult
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BernoulliSimulator:
    """Répète des essais de Bernoulli indépendants."""

    def __init__(self, config: SimulationConfig) -> None:
        """Construit le simulateur.

        :param config: Nombre d'itérations et graine.
        """
        self._config: SimulationConfig = config
        self._validator: ProbabilityValidator = ProbabilityValidator()

    def run(self, success_probability: float) -> SimulationResult:
        """Simule ``iterations`` tirages de Bernoulli.

        :param success_probability: Probabilité de succès ``p``.
        :returns: ``data['values']`` liste de 0/1, ``data['successes']`` total.
        """
        self._validator.validate_closed_unit_interval(success_probability)
        gen: RandomGenerator = RandomGenerator(self._config.seed)
        values: list[int] = []
        for _ in range(self._config.iterations):
            u: float = gen.rng.random()
            values.append(1 if u < success_probability else 0)
        successes: int = sum(values)
        return SimulationResult(
            data={
                "values": values,
                "successes": successes,
            }
        )
