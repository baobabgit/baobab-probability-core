"""Loi de Bernoulli."""

from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BernoulliDistribution(BaseDistribution):
    """Bernoulli de paramètre ``p``."""

    def __init__(self, probability: float) -> None:
        """Construit la loi.

        :param probability: Probabilité de succès ``p ∈ [0, 1]``.
        """
        self._validator: ProbabilityValidator = ProbabilityValidator()
        self._validator.validate_closed_unit_interval(probability)
        self._p: float = probability

    @property
    def probability(self) -> float:
        """Paramètre ``p``."""
        return self._p

    def probability_of(self, value: int) -> float:
        """``P(X=1)=p``, ``P(X=0)=1-p``."""
        if value == 1:
            return self._p
        if value == 0:
            return 1.0 - self._p
        return 0.0

    def expected_value(self) -> float:
        """Espérance ``p``."""
        return self._p

    def variance(self) -> float:
        """Variance ``p(1-p)``."""
        return self._p * (1.0 - self._p)
