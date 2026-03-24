"""Permutations de ``n`` objets distincts."""

from baobab_probability_core.combinatorics.factorial_calculator import FactorialCalculator


class PermutationCalculator:
    """Nombre de permutations : ``n!``."""

    def __init__(self) -> None:
        """Initialise le calculateur de factorielles."""
        self._factorial: FactorialCalculator = FactorialCalculator()

    def count(self, n: int) -> int:
        """Retourne le nombre de permutations de ``n`` éléments.

        :param n: Taille de l'ensemble.
        :returns: ``n!``.
        """
        return self._factorial.factorial(n)
