"""Tests pour :class:`ArrangementCalculator`."""

import pytest

from baobab_probability_core.combinatorics.arrangement_calculator import ArrangementCalculator
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class TestArrangementCalculator:
    """Arrangements A(n, k)."""

    def test_arrangement_values(self) -> None:
        """Exemples manuels."""
        calc = ArrangementCalculator()
        assert calc.count(5, 2) == 20
        assert calc.count(5, 0) == 1

    def test_k_greater_than_n(self) -> None:
        """Incohérence détectée."""
        calc = ArrangementCalculator()
        with pytest.raises(InvalidCombinatorialParameterException):
            calc.count(2, 5)

    def test_negative_n(self) -> None:
        """n négatif."""
        calc = ArrangementCalculator()
        with pytest.raises(InvalidCombinatorialParameterException):
            calc.count(-1, 0)
