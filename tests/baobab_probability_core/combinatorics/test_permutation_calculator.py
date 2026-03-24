"""Tests pour :class:`PermutationCalculator`."""

from baobab_probability_core.combinatorics.permutation_calculator import PermutationCalculator


class TestPermutationCalculator:
    """Permutations = factorielle."""

    def test_count_matches_factorial(self) -> None:
        """Cohérence avec n!."""
        calc = PermutationCalculator()
        assert calc.count(4) == 24
