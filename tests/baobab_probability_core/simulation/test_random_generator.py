"""Tests pour :class:`RandomGenerator`."""

from baobab_probability_core.simulation.random_generator import RandomGenerator


class TestRandomGenerator:
    """Générateur."""

    def test_deterministic_seed(self) -> None:
        """Même graine → même tirage."""
        a = RandomGenerator(123)
        b = RandomGenerator(123)
        assert a.rng.random() == b.rng.random()
