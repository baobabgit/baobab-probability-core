"""Tests pour :class:`GeometricDistribution`."""

import pytest

from baobab_probability_core.distributions.geometric_distribution import GeometricDistribution
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class TestGeometricDistribution:
    """Géométrique."""

    def test_pmf(self) -> None:
        """k=1 donne p."""
        d = GeometricDistribution(0.25)
        assert d.probability_of(1) == pytest.approx(0.25)
        assert d.probability_of(0) == 0.0

    def test_mean_variance(self) -> None:
        """Moments."""
        d = GeometricDistribution(0.5)
        assert d.probability == pytest.approx(0.5)
        assert d.expected_value() == pytest.approx(2.0)
        assert d.variance() == pytest.approx(2.0)

    def test_p_zero(self) -> None:
        """p = 0 interdit."""
        with pytest.raises(InvalidDistributionParameterException):
            GeometricDistribution(0.0)

    def test_p_above_one(self) -> None:
        """p > 1 interdit."""
        with pytest.raises(InvalidDistributionParameterException):
            GeometricDistribution(1.1)
