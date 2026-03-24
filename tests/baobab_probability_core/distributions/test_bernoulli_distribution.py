"""Tests pour :class:`BernoulliDistribution`."""

import pytest

from baobab_probability_core.distributions.bernoulli_distribution import BernoulliDistribution
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)


class TestBernoulliDistribution:
    """Loi de Bernoulli."""

    def test_probability_mass(self) -> None:
        """Masse sur 0 et 1."""
        d = BernoulliDistribution(0.25)
        assert d.probability == pytest.approx(0.25)
        assert d.probability_of(0) == pytest.approx(0.75)
        assert d.probability_of(1) == pytest.approx(0.25)
        assert d.probability_of(2) == 0.0

    def test_mean_variance(self) -> None:
        """Moments."""
        d = BernoulliDistribution(0.4)
        assert d.expected_value() == pytest.approx(0.4)
        assert d.variance() == pytest.approx(0.24)

    def test_invalid_p(self) -> None:
        """p hors intervalle."""
        with pytest.raises(InvalidProbabilityValueException):
            BernoulliDistribution(1.1)

    def test_default_support_empty(self) -> None:
        """Support par défaut de :class:`BaseDistribution`."""
        d = BernoulliDistribution(0.5)
        assert list(d.support()) == []
