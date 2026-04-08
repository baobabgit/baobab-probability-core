"""Tests pour :class:`ProbabilityValidator`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class TestProbabilityValidator:
    """Intervalle unité et distribution discrète."""

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

    def test_discrete_valid_accepted(self) -> None:
        """Distribution valide acceptée."""
        v = ProbabilityValidator()
        v.validate_discrete_probability_distribution({"a": 0.5, "b": 0.5})

    def test_discrete_empty_rejected(self) -> None:
        """Mapping vide rejeté."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({})

    def test_discrete_negative_rejected(self) -> None:
        """Probabilité négative rejetée."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": -0.1, "b": 1.1})

    def test_discrete_above_one_rejected(self) -> None:
        """Probabilité > 1 rejetée (somme = 1 mais masse invalide)."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": 1.5, "b": -0.5})

    def test_discrete_sum_below_one_rejected(self) -> None:
        """Somme < 1 rejetée."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": 0.2, "b": 0.3})

    def test_discrete_sum_above_one_rejected(self) -> None:
        """Somme > 1 rejetée."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": 0.6, "b": 0.6})

    def test_discrete_non_finite_rejected(self) -> None:
        """Valeur non finie rejetée."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": float("nan"), "b": 1.0})

    def test_discrete_inf_rejected(self) -> None:
        """Infini rejeté."""
        v = ProbabilityValidator()
        with pytest.raises(InvalidProbabilityValueException):
            v.validate_discrete_probability_distribution({"a": float("inf"), "b": 0.0})
