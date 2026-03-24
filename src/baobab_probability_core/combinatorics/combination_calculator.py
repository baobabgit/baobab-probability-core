"""Combinaisons (sous-ensembles non ordonnés)."""

from baobab_probability_core.combinatorics.factorial_calculator import FactorialCalculator
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class CombinationCalculator:
    """Calcule ``C(n, k) = n! / (k! (n - k)!)``."""

    def __init__(self) -> None:
        """Initialise le calculateur."""
        self._factorial: FactorialCalculator = FactorialCalculator()

    def count(self, n: int, k: int) -> int:
        """Retourne le nombre de combinaisons de ``k`` objets parmi ``n``.

        :param n: Taille de l'ensemble.
        :param k: Taille du sous-ensemble.
        :raises InvalidCombinatorialParameterException: si ``k > n`` ou entrées invalides.
        """
        if k < 0 or n < 0:
            raise InvalidCombinatorialParameterException(
                "n et k doivent être positifs ou nuls pour les combinaisons."
            )
        if k > n:
            raise InvalidCombinatorialParameterException(
                f"k ne peut pas dépasser n pour C(n,k) (reçu n={n}, k={k})."
            )
        k = min(k, n - k)
        result: int = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result
