"""Tests pour :class:`ConditionalProbabilityCalculator`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.conditional_probability_calculator import (
    ConditionalProbabilityCalculator,
)
from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace


class TestConditionalProbabilityCalculator:
    """Conditionnement."""

    def test_conditional(self) -> None:
        """P(A|B) simple."""
        space = FiniteProbabilitySpace({"a": 0.2, "b": 0.3, "c": 0.5})
        calc = ConditionalProbabilityCalculator()
        a = Event(["a"])
        b = Event(["a", "b"])
        assert calc.conditional(space, a, b) == pytest.approx(0.2 / 0.5)

    def test_b_zero(self) -> None:
        """P(B)=0."""
        space = FiniteProbabilitySpace({"a": 0.5, "b": 0.5})
        calc = ConditionalProbabilityCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            calc.conditional(space, Event(["a"]), Event([]))
