"""Tests pour :class:`BinomialDistribution`."""

import pytest

from baobab_probability_core.distributions.binomial_distribution import BinomialDistribution
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)


class TestBinomialDistribution:
    """Binomiale."""

    def test_binomial_pmf(self) -> None:
        """Symétrie n=0."""
        d0 = BinomialDistribution(0, 0.5)
        assert d0.probability_of(0) == pytest.approx(1.0)

    def test_trials_negative(self) -> None:
        """n négatif."""
        with pytest.raises(InvalidDistributionParameterException):
            BinomialDistribution(-1, 0.5)

    def test_p_invalid(self) -> None:
        """p hors [0,1]."""
        with pytest.raises(InvalidProbabilityValueException):
            BinomialDistribution(5, 1.5)

    def test_pmf_outside_support(self) -> None:
        """k hors [0, n]."""
        d = BinomialDistribution(3, 0.5)
        assert d.probability_of(10) == 0.0

    def test_trials_property(self) -> None:
        """Accesseurs."""
        d = BinomialDistribution(7, 0.2)
        assert d.trials == 7
        assert d.probability == pytest.approx(0.2)
        assert d.expected_value() == pytest.approx(7 * 0.2)
        assert d.variance() == pytest.approx(7 * 0.2 * 0.8)
