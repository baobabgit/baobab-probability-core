"""Tests pour :class:`BernoulliSimulator`."""

from baobab_probability_core.simulation.bernoulli_simulator import BernoulliSimulator
from baobab_probability_core.simulation.simulation_config import SimulationConfig


class TestBernoulliSimulator:
    """Reproductibilité des tirages."""

    def test_reproducible(self) -> None:
        """Même graine → même suite."""
        a = BernoulliSimulator(SimulationConfig(100, 99))
        b = BernoulliSimulator(SimulationConfig(100, 99))
        ra = a.run(0.5)
        rb = b.run(0.5)
        assert ra.data["values"] == rb.data["values"]
        assert ra.data["successes"] == sum(ra.data["values"])
