"""Tests pour :class:`DiceRollSimulator`."""

import pytest

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)
from baobab_probability_core.simulation.dice_roll_simulator import DiceRollSimulator
from baobab_probability_core.simulation.simulation_config import SimulationConfig


class TestDiceRollSimulator:
    """Dé équilibré."""

    def test_counts_sum(self) -> None:
        """Somme des comptages = itérations."""
        sim = DiceRollSimulator(SimulationConfig(600, 1))
        r = sim.run(6)
        assert sum(r.face_counts.values()) == 600
        assert r.face_counts_sorted == tuple(sorted(r.data["counts_by_face"].items()))

    def test_invalid_sides(self) -> None:
        """Moins de 2 faces."""
        sim = DiceRollSimulator(SimulationConfig(10, 1))
        with pytest.raises(UnsupportedExperimentException):
            sim.run(1)
