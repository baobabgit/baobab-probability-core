"""Tests pour :class:`TheoreticalObservationComparator`."""

import pytest

from baobab_probability_core.comparison.theoretical_observation_comparator import (
    TheoreticalObservationComparator,
)
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.statistics.distribution_observation import DistributionObservation


class TestTheoreticalObservationComparator:
    """Comparateur théorie / données."""

    def test_compare_probability(self) -> None:
        """Exemple cahier des charges."""
        c = TheoreticalObservationComparator()
        r = c.compare_probability(0.3, 297, 1000)
        assert r.theoretical_probability == 0.3
        assert r.observed_frequency == pytest.approx(0.297)

    def test_compare_probability_theoretical_zero(self) -> None:
        """Erreur relative absente si p théorique nul."""
        c = TheoreticalObservationComparator()
        r = c.compare_probability(0.0, 0, 100)
        assert r.relative_error is None

    def test_trials_zero(self) -> None:
        """Essais nuls."""
        c = TheoreticalObservationComparator()
        with pytest.raises(InvalidSampleException):
            c.compare_probability(0.5, 0, 0)

    def test_compare_distributions(self) -> None:
        """Par modalité."""
        c = TheoreticalObservationComparator()
        obs = DistributionObservation({"a": 50, "b": 50})
        r = c.compare_distributions({"a": 0.5, "b": 0.5}, obs)
        assert r.sum_absolute_errors == pytest.approx(0.0)

    def test_invalid_successes(self) -> None:
        """Succès incohérents avec les essais."""
        c = TheoreticalObservationComparator()
        with pytest.raises(InvalidProbabilityValueException):
            c.compare_probability(0.5, 10, 5)

    def test_compare_distributions_key_mismatch(self) -> None:
        """Modalités différentes."""
        c = TheoreticalObservationComparator()
        obs = DistributionObservation({"a": 10})
        with pytest.raises(InvalidSampleException):
            c.compare_distributions({"a": 0.5, "b": 0.5}, obs)

    def test_compare_distributions_rejects_invalid_theoretical(self) -> None:
        """Distribution théorique invalide (somme > 1) malgré clés cohérentes."""
        c = TheoreticalObservationComparator()
        obs = DistributionObservation({"a": 50, "b": 50})
        with pytest.raises(InvalidProbabilityValueException):
            c.compare_distributions({"a": 0.6, "b": 0.6}, obs)
