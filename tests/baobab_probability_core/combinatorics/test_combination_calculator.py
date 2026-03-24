"""Tests pour :class:`CombinationCalculator`."""

import pytest

from baobab_probability_core.combinatorics.combination_calculator import CombinationCalculator
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class TestCombinationCalculator:
    """Coefficients binomiaux."""

    def test_binomial_coefficients(self) -> None:
        """Valeurs usuelles."""
        calc = CombinationCalculator()
        assert calc.count(5, 2) == 10
        assert calc.count(5, 0) == 1
        assert calc.count(6, 4) == calc.count(6, 2)

    def test_k_greater_than_n(self) -> None:
        """Incohérence."""
        calc = CombinationCalculator()
        with pytest.raises(InvalidCombinatorialParameterException):
            calc.count(2, 5)

    def test_negative_n(self) -> None:
        """n négatif."""
        calc = CombinationCalculator()
        with pytest.raises(InvalidCombinatorialParameterException):
            calc.count(-1, 0)
