"""Loi binomiale."""

from baobab_probability_core.combinatorics.combination_calculator import CombinationCalculator
from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.validators.distribution_parameter_validator import (
    DistributionParameterValidator,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BinomialDistribution(BaseDistribution):
    """Binomiale ``B(n, p)``."""

    def __init__(self, trials: int, probability: float) -> None:
        """Construit la loi.

        :param trials: Nombre d'essais ``n >= 0``.
        :param probability: Probabilité de succès ``p ∈ [0, 1]``.
        """
        self._int_val: DistributionParameterValidator = DistributionParameterValidator()
        self._prob_val: ProbabilityValidator = ProbabilityValidator()
        self._int_val.validate_non_negative_int(trials, "n")
        self._prob_val.validate_closed_unit_interval(probability)
        self._n: int = trials
        self._p: float = probability
        self._comb: CombinationCalculator = CombinationCalculator()

    @property
    def trials(self) -> int:
        """Nombre d'essais ``n``."""
        return self._n

    @property
    def probability(self) -> float:
        """Probabilité de succès ``p``."""
        return self._p

    def probability_of(self, value: int) -> float:
        """``P(X=k) = C(n,k) p^k (1-p)^{n-k}`` pour ``k`` dans ``[0, n]``."""
        if value < 0 or value > self._n:
            return 0.0
        coeff: int = self._comb.count(self._n, value)
        return coeff * (self._p**value) * ((1.0 - self._p) ** (self._n - value))

    def expected_value(self) -> float:
        """Espérance ``n p``."""
        return self._n * self._p

    def variance(self) -> float:
        """Variance ``n p (1-p)``."""
        return self._n * self._p * (1.0 - self._p)
