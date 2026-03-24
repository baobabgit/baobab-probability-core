"""Tests pour :class:`ProbabilityCalculator`."""

import pytest

from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace
from baobab_probability_core.probability.probability_calculator import ProbabilityCalculator


class TestProbabilityCalculator:
    """Calculs sur espace fini."""

    def test_complement(self) -> None:
        """Complément."""
        calc = ProbabilityCalculator()
        assert calc.complement(0.2) == pytest.approx(0.8)

    def test_union_independent(self) -> None:
        """Deux issues disjointes."""
        space = FiniteProbabilitySpace({"a": 0.4, "b": 0.3, "c": 0.3})
        calc = ProbabilityCalculator()
        ea = Event(["a"])
        eb = Event(["b"])
        assert calc.union(space, ea, eb) == pytest.approx(0.7)

    def test_intersection(self) -> None:
        """P(A ∩ B)."""
        space = FiniteProbabilitySpace({"a": 0.2, "b": 0.3, "c": 0.5})
        calc = ProbabilityCalculator()
        assert calc.intersection(space, Event(["a", "b"]), Event(["b", "c"])) == pytest.approx(0.3)

    def test_simple(self) -> None:
        """Alias simple."""
        space = FiniteProbabilitySpace({"x": 1.0})
        calc = ProbabilityCalculator()
        assert calc.simple(space, Event(["x"])) == pytest.approx(1.0)

    def test_union_int_space(self) -> None:
        """Espace à issues entières : même équation d'union."""
        space = FiniteProbabilitySpace({10: 0.5, 20: 0.3, 30: 0.2})
        calc = ProbabilityCalculator()
        assert calc.union(space, Event([10]), Event([20])) == pytest.approx(0.8)
