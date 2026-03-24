"""Tests pour :class:`BinomialSimulator`."""

from baobab_probability_core.simulation.binomial_simulator import BinomialSimulator
from baobab_probability_core.simulation.simulation_config import SimulationConfig


class TestBinomialSimulator:
    """Binomiale simulée."""

    def test_reproducible(self) -> None:
        """Même graine → même suite."""
        a = BinomialSimulator(SimulationConfig(50, 7))
        b = BinomialSimulator(SimulationConfig(50, 7))
        ra, rb = a.run(10, 0.4), b.run(10, 0.4)
        assert ra.trial_outcomes == rb.trial_outcomes
        assert list(ra.trial_outcomes or ()) == ra.data["values"]
