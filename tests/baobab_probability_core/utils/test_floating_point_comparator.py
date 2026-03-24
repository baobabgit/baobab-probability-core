"""Tests pour :class:`FloatingPointComparator`."""

from baobab_probability_core.utils.floating_point_comparator import FloatingPointComparator


class TestFloatingPointComparator:
    """Comparaisons flottantes."""

    def test_sum_is_one(self) -> None:
        """Somme normalisée."""
        c = FloatingPointComparator(1e-6)
        assert c.sum_is_one([0.1, 0.2, 0.3, 0.4])

    def test_tolerance_property(self) -> None:
        """Accesseur."""
        c = FloatingPointComparator(0.01)
        assert c.tolerance == 0.01
