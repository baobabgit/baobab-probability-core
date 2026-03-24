"""Tests pour :class:`SimulationConfig`."""

import pytest

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)
from baobab_probability_core.simulation.simulation_config import SimulationConfig


class TestSimulationConfig:
    """Configuration."""

    def test_properties(self) -> None:
        """Accesseurs."""
        c = SimulationConfig(10, 42)
        assert c.iterations == 10
        assert c.seed == 42

    def test_iterations_invalid(self) -> None:
        """iterations < 1."""
        with pytest.raises(UnsupportedExperimentException):
            SimulationConfig(0, 1)
