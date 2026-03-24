"""Tests pour :class:`SimulationResult`."""

from baobab_probability_core.simulation.simulation_result import SimulationResult


class TestSimulationResult:
    """Résultat."""

    def test_data(self) -> None:
        """Champ data."""
        r = SimulationResult(data={"x": 1})
        assert r.data["x"] == 1
