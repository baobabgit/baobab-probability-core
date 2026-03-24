"""Tests pour :class:`EmpiricalMomentCalculator`."""

import pytest

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.statistics.empirical_moment_calculator import (
    EmpiricalMomentCalculator,
)


class TestEmpiricalMomentCalculator:
    """Moyenne et variance."""

    def test_mean_variance(self) -> None:
        """Série simple."""
        em = EmpiricalMomentCalculator()
        vals = [1.0, 2.0, 3.0, 4.0]
        assert em.mean(vals) == pytest.approx(2.5)
        assert em.variance(vals, unbiased=True) == pytest.approx(5 / 3)

    def test_variance_unbiased_too_short(self) -> None:
        """n < 2 pour variance non biaisée."""
        em = EmpiricalMomentCalculator()
        with pytest.raises(InvalidSampleException):
            em.variance([1.0], unbiased=True)
