"""Tests pour :class:`DistributionObservation`."""

import pytest

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.statistics.distribution_observation import DistributionObservation


class TestDistributionObservation:
    """Effectifs par modalité."""

    def test_total(self) -> None:
        """Somme des effectifs."""
        obs = DistributionObservation({"a": 3, "b": 7})
        assert obs.total_count() == 10

    def test_empty_mapping_rejected(self) -> None:
        """Mapping vide."""
        with pytest.raises(InvalidSampleException):
            DistributionObservation({})

    def test_zero_total_rejected(self) -> None:
        """Somme nulle interdite."""
        with pytest.raises(InvalidSampleException):
            DistributionObservation({"a": 0, "b": 0})

    def test_counts_property(self) -> None:
        """Copie des comptages."""
        obs = DistributionObservation({"a": 1})
        assert obs.counts == {"a": 1}
