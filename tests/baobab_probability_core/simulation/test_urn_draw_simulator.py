"""Tests pour :class:`UrnDrawSimulator`."""

import pytest

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)
from baobab_probability_core.simulation.simulation_config import SimulationConfig
from baobab_probability_core.simulation.urn_draw_simulator import UrnDrawSimulator


class TestUrnDrawSimulator:
    """Urne avec / sans remise."""

    def test_with_replacement_reproducible(self) -> None:
        """Reproductibilité."""
        cfg = SimulationConfig(20, 5)
        a = UrnDrawSimulator(cfg)
        b = UrnDrawSimulator(cfg)
        ra, rb = a.run_with_replacement(10, 3, 4), b.run_with_replacement(10, 3, 4)
        assert ra.urn_successes_per_iteration == rb.urn_successes_per_iteration
        assert ra.data == rb.data

    def test_without_replacement(self) -> None:
        """Tirage sans remise borné."""
        r = UrnDrawSimulator(SimulationConfig(5, 1)).run_without_replacement(10, 4, 3)
        per = r.urn_successes_per_iteration or ()
        assert len(per) == 5
        assert all(0 <= x <= 3 for x in per)
        assert list(per) == r.data["successes_per_trial"]

    def test_invalid_population(self) -> None:
        """Population nulle."""
        with pytest.raises(UnsupportedExperimentException):
            UrnDrawSimulator(SimulationConfig(1, 1)).run_without_replacement(0, 0, 0)

    def test_negative_sample_with_replacement(self) -> None:
        """sample_size négatif avec remise."""
        with pytest.raises(UnsupportedExperimentException):
            UrnDrawSimulator(SimulationConfig(1, 1)).run_with_replacement(5, 2, -1)

    def test_success_balls_invalid(self) -> None:
        """K hors population."""
        with pytest.raises(UnsupportedExperimentException):
            UrnDrawSimulator(SimulationConfig(1, 1)).run_without_replacement(5, 6, 2)

    def test_sample_too_large_without_replacement(self) -> None:
        """n > N sans remise."""
        with pytest.raises(UnsupportedExperimentException):
            UrnDrawSimulator(SimulationConfig(1, 1)).run_without_replacement(4, 2, 5)
