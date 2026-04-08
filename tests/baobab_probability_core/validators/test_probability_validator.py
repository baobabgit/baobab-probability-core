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

    def test_open_zero_closed_one_accepts_interior_and_one(self) -> None:
        """Accepte ``]0, 1]``."""
        v = ProbabilityValidator()
        v.validate_open_zero_closed_one(1.0)
        v.validate_open_zero_closed_one(0.5)

    def test_open_zero_closed_one_rejects_zero(self) -> None:
        """Rejette la borne 0."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_open_zero_closed_one(0.0)

    def test_open_zero_closed_one_rejects_above_one(self) -> None:
        """Rejette ``> 1``."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_open_zero_closed_one(1.01)
