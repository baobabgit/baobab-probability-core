"""Tests pour :class:`FrequencyAnalyzer`."""

import pytest

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.statistics.frequency_analyzer import FrequencyAnalyzer


class TestFrequencyAnalyzer:
    """Fréquences relatives."""

    def test_relative_frequencies(self) -> None:
        """Somme = 1."""
        fa = FrequencyAnalyzer()
        rel = fa.relative_frequencies({"a": 1, "b": 3})
        assert rel["a"] == pytest.approx(0.25)
        assert sum(rel.values()) == pytest.approx(1.0)

    def test_zero_total(self) -> None:
        """Effectifs tous nuls."""
        fa = FrequencyAnalyzer()
        with pytest.raises(InvalidSampleException):
            fa.relative_frequencies({"a": 0})
