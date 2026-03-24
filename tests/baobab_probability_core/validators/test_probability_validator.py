"""Tests pour :class:`ProbabilityValidator`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class TestProbabilityValidator:
    """Intervalle unité."""

    def test_valid(self) -> None:
        """Accepte [0,1]."""
        v = ProbabilityValidator()
        v.validate_closed_unit_interval(0.0)
        v.validate_closed_unit_interval(1.0)

    def test_invalid(self) -> None:
        """Rejette hors plage."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_closed_unit_interval(1.5)
