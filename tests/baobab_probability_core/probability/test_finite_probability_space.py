"""Tests pour :class:`FiniteProbabilitySpace`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace


class TestFiniteProbabilitySpace:
    """Espaces finis valides et invalides."""

    def test_uniform_two_outcomes(self) -> None:
        """Espace équiprobable."""
        space = FiniteProbabilitySpace({"a": 0.5, "b": 0.5})
        assert space.probability_of_outcome("a") == 0.5
        ev = Event(["a"])
        assert space.probability_of_event(ev) == 0.5

    def test_sum_not_one(self) -> None:
        """Somme ≠ 1 rejetée."""
        with pytest.raises(InvalidProbabilityValueException):
            FiniteProbabilitySpace({"a": 0.3, "b": 0.3})

    def test_unknown_outcome(self) -> None:
        """Issue absente."""
        space = FiniteProbabilitySpace({"a": 1.0})
        with pytest.raises(InvalidProbabilityValueException):
            space.probability_of_outcome("z")

    def test_empty_universe(self) -> None:
        """Univers vide."""
        with pytest.raises(InvalidProbabilityValueException):
            FiniteProbabilitySpace({})

    def test_negative_probability(self) -> None:
        """Probabilité négative."""
        with pytest.raises(InvalidProbabilityValueException):
            FiniteProbabilitySpace({"a": -0.1, "b": 1.1})
