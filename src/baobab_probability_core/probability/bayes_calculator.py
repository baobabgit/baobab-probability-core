"""Théorème de Bayes sur probabilités scalaires."""

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BayesCalculator:
    """Posterior ``P(B|A) = P(A|B) P(B) / P(A)``."""

    def __init__(self) -> None:
        """Initialise les validateurs."""
        self._validator: ProbabilityValidator = ProbabilityValidator()

    def posterior(
        self,
        likelihood: float,
        prior: float,
        marginal: float,
    ) -> float:
        """Calcule la probabilité a posteriori.

        :param likelihood: ``P(A|B)``.
        :param prior: ``P(B)``.
        :param marginal: ``P(A)``.
        :returns: ``P(B|A)``.
        :raises InvalidProbabilityValueException: si marges nulles ou incohérentes.
        """
        self._validator.validate_closed_unit_interval(likelihood)
        self._validator.validate_closed_unit_interval(prior)
        if marginal <= 0.0:
            raise InvalidProbabilityValueException(
                "P(A) doit être strictement positif pour appliquer Bayes."
            )
        return likelihood * prior / marginal
