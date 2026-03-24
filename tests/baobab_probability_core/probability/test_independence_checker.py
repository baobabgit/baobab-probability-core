"""Tests pour :class:`IndependenceChecker`."""

from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace
from baobab_probability_core.probability.independence_checker import IndependenceChecker


class TestIndependenceChecker:
    """Indépendance."""

    def test_independent_product_space(self) -> None:
        """Espace produit équiprobable 2x2."""
        space = FiniteProbabilitySpace({"00": 0.25, "01": 0.25, "10": 0.25, "11": 0.25})
        chk = IndependenceChecker()
        a = Event(["00", "01"])
        b = Event(["00", "10"])
        assert chk.are_independent(space, a, b)
