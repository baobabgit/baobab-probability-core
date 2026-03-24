"""Tests pour :class:`FactorialCalculator`."""

import pytest

from baobab_probability_core.combinatorics.factorial_calculator import FactorialCalculator
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class TestFactorialCalculator:
    """Factorielles exactes."""

    def test_zero_and_one(self) -> None:
        """Cas limites."""
        calc = FactorialCalculator()
        assert calc.factorial(0) == 1
        assert calc.factorial(1) == 1

    def test_small_values(self) -> None:
        """Valeurs usuelles."""
        calc = FactorialCalculator()
        assert calc.factorial(5) == 120

    def test_negative_rejected(self) -> None:
        """Entrées négatives interdites."""
        calc = FactorialCalculator()
        with pytest.raises(InvalidCombinatorialParameterException):
            calc.factorial(-1)
