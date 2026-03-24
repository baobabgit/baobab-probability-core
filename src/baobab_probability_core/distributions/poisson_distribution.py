"""Loi de Poisson."""

import math
from collections.abc import Iterable

from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.validators.distribution_parameter_validator import (
    DistributionParameterValidator,
)


class PoissonDistribution(BaseDistribution):
    """Poisson de taux ``lambda_rate`` (notation ``λ``)."""

    def __init__(self, lambda_rate: float) -> None:
        """Construit la loi.

        :param lambda_rate: Intensité ``λ > 0``.
        :raises InvalidDistributionParameterException: si ``λ <= 0``.
        """
        self._validator: DistributionParameterValidator = DistributionParameterValidator()
        self._validator.validate_positive_rate(lambda_rate, "lambda")
        self._lambda_rate: float = lambda_rate

    @property
    def lambda_rate(self) -> float:
        """Paramètre ``λ``."""
        return self._lambda_rate

    def probability_of(self, value: int) -> float:
        """``P(X = k) = e^{-λ} λ^k / k!`` pour ``k >= 0``."""
        if value < 0:
            return 0.0
        return math.exp(-self._lambda_rate) * (self._lambda_rate**value) / math.factorial(value)

    def expected_value(self) -> float:
        """Espérance ``λ``."""
        return self._lambda_rate

    def variance(self) -> float:
        """Variance ``λ``."""
        return self._lambda_rate

    def support(self) -> Iterable[int]:
        """Support théorique infini : ici entiers ``0..100`` pour itération bornée."""
        return range(0, 101)
