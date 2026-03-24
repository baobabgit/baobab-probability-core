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
        assert ra.trial_outcomes == rb.trial_outcomes
        assert list(ra.trial_outcomes or ()) == ra.data["values"]
        assert ra.bernoulli_success_total == rb.bernoulli_success_total
        assert ra.bernoulli_success_total == sum(ra.trial_outcomes or ())
