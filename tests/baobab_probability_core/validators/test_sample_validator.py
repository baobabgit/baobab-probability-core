"""Tests pour :class:`SampleValidator`."""

import pytest

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.validators.sample_validator import SampleValidator


class TestSampleValidator:
    """Validateur d'échantillons."""

    def test_empty_sequence(self) -> None:
        """Séquence vide."""
        v = SampleValidator()
        with pytest.raises(InvalidSampleException):
            v.validate_non_empty_sequence([])

    def test_negative_count(self) -> None:
        """Comptage négatif."""
        v = SampleValidator()
        with pytest.raises(InvalidSampleException):
            v.validate_non_negative_counts({"a": -1})
