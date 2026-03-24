"""Tests pour :class:`PoissonDistribution`."""

import pytest

from baobab_probability_core.distributions.poisson_distribution import PoissonDistribution
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class TestPoissonDistribution:
    """Poisson."""

    def test_mean_equals_lambda(self) -> None:
        """Espérance."""
        d = PoissonDistribution(2.5)
        assert d.expected_value() == pytest.approx(2.5)
        assert d.variance() == pytest.approx(2.5)

    def test_lambda_non_positive(self) -> None:
        """λ <= 0."""
        with pytest.raises(InvalidDistributionParameterException):
            PoissonDistribution(0.0)

    def test_negative_k_zero_mass(self) -> None:
        """Support entier négatif."""
        d = PoissonDistribution(3.0)
        assert d.probability_of(2) > 0.0
        d = PoissonDistribution(1.0)
        assert d.probability_of(-1) == 0.0

    def test_lambda_property_and_support(self) -> None:
        """Accesseur et plage bornée du support."""
        d = PoissonDistribution(2.0)
        assert d.lambda_rate == pytest.approx(2.0)
        assert max(d.support()) == 100
