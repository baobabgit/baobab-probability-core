"""Tests pour :class:`HypergeometricDistribution`."""

import pytest

from baobab_probability_core.distributions.hypergeometric_distribution import (
    HypergeometricDistribution,
)
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class TestHypergeometricDistribution:
    """Hypergéométrique."""

    def test_mean(self) -> None:
        """Espérance connue."""
        d = HypergeometricDistribution(10, 4, 3)
        assert d.expected_value() == pytest.approx(1.2)

    def test_k_exceeds_n(self) -> None:
        """K > N."""
        with pytest.raises(InvalidDistributionParameterException):
            HypergeometricDistribution(5, 10, 2)

    def test_pmf_and_variance(self) -> None:
        """Masse et variance (N>1)."""
        d = HypergeometricDistribution(6, 3, 2)
        assert d.probability_of(1) > 0.0
        assert d.variance() >= 0.0

    def test_sample_exceeds_population(self) -> None:
        """n > N."""
        with pytest.raises(InvalidDistributionParameterException):
            HypergeometricDistribution(5, 2, 6)

    def test_variance_small_population(self) -> None:
        """Branche ``N <= 1`` pour la variance."""
        d = HypergeometricDistribution(1, 1, 1)
        assert d.variance() == pytest.approx(0.0)

    def test_negative_parameters(self) -> None:
        """Paramètres négatifs."""
        with pytest.raises(InvalidDistributionParameterException):
            HypergeometricDistribution(-1, 0, 0)

    def test_degenerate_population_zero(self) -> None:
        """Cas ``N = n = K = 0`` (dégénéré)."""
        d = HypergeometricDistribution(0, 0, 0)
        assert d.expected_value() == pytest.approx(0.0)
        assert d.probability_of(0) == pytest.approx(1.0)
        assert d.probability_of(1) == pytest.approx(0.0)
