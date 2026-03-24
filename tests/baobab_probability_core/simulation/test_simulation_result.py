"""Tests pour :class:`SimulationResult`."""

from dataclasses import FrozenInstanceError

import pytest

from baobab_probability_core.simulation.simulation_result import SimulationResult


class TestSimulationResult:
    """Résultat typé et vue ``data`` compatible."""

    def test_frozen_dataclass(self) -> None:
        """Instance immuable (:func:`dataclasses.dataclass` ``frozen=True``)."""
        r = SimulationResult(trial_outcomes=(1, 0))
        assert r.trial_outcomes == (1, 0)
        with pytest.raises(FrozenInstanceError):
            r.trial_outcomes = (0, 1)  # type: ignore[misc]

    def test_data_bernoulli_shape(self) -> None:
        """Clés legacy pour Bernoulli."""
        r = SimulationResult(
            trial_outcomes=(1, 0, 1),
            bernoulli_success_total=2,
        )
        assert r.data["values"] == [1, 0, 1]
        assert r.data["successes"] == 2

    def test_data_binomial_only_values(self) -> None:
        """Binomiale : uniquement ``values`` dans la vue dict."""
        r = SimulationResult(trial_outcomes=(3, 5, 4))
        assert r.data == {"values": [3, 5, 4]}
        assert r.bernoulli_success_total is None

    def test_face_counts_and_data_dice(self) -> None:
        """Dé : tuples triés et dictionnaire dérivé."""
        r = SimulationResult(face_counts_sorted=((1, 10), (2, 20), (6, 5)))
        assert r.face_counts == {1: 10, 2: 20, 6: 5}
        assert r.data["counts_by_face"] == {1: 10, 2: 20, 6: 5}

    def test_urn_legacy_key(self) -> None:
        """Urne : ``successes_per_trial`` dans ``data``."""
        r = SimulationResult(urn_successes_per_iteration=(1, 2, 0))
        assert r.data["successes_per_trial"] == [1, 2, 0]

    def test_empty_data_when_no_payload(self) -> None:
        """Aucun champ renseigné → ``data`` vide."""
        assert SimulationResult().data == {}
