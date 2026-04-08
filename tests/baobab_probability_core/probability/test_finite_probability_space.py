"""Tests pour :class:`FiniteProbabilitySpace`."""

from enum import Enum

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace


class CoinFace(Enum):
    """Issue d'exemple pour univers fini typé."""

    H = 1
    T = 2


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

    def test_non_finite_probability(self) -> None:
        """Probabilité non finie rejetée (validation centralisée)."""
        with pytest.raises(InvalidProbabilityValueException):
            FiniteProbabilitySpace({"a": float("nan"), "b": 1.0})

    def test_int_outcomes(self) -> None:
        """Univers dont les issues sont des entiers."""
        space = FiniteProbabilitySpace({1: 0.25, 2: 0.25, 3: 0.5})
        assert space.probability_of_outcome(3) == 0.5
        assert space.probability_of_event(Event([1, 2])) == 0.5

    def test_tuple_joint_outcomes(self) -> None:
        """Univers produit fini (couples hashables)."""
        space = FiniteProbabilitySpace(
            {
                (0, 0): 0.25,
                (0, 1): 0.25,
                (1, 0): 0.25,
                (1, 1): 0.25,
            }
        )
        assert space.probability_of_outcome((1, 1)) == 0.25
        assert space.probability_of_event(Event([(0, 0), (1, 1)])) == 0.5

    def test_enum_outcomes(self) -> None:
        """Issues : membres d'énumération (hashables)."""
        space = FiniteProbabilitySpace({CoinFace.H: 0.4, CoinFace.T: 0.6})
        assert space.probability_of_event(Event([CoinFace.H])) == pytest.approx(0.4)
