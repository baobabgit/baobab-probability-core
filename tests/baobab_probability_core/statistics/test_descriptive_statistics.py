"""Tests pour :class:`DescriptiveStatistics`."""

from baobab_probability_core.statistics.descriptive_statistics import DescriptiveStatistics


class TestDescriptiveStatistics:
    """Résumé descriptif."""

    def test_from_values(self) -> None:
        """Agrégation."""
        ds = DescriptiveStatistics.from_values([2.0, 4.0, 6.0])
        assert ds.count == 3
        assert ds.mean == 4.0
        assert ds.minimum == 2.0
        assert ds.maximum == 6.0
