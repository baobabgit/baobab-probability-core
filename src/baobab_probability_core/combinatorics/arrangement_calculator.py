"""Arrangements (k-uplets ordonnés sans répétition)."""

from baobab_probability_core.combinatorics.factorial_calculator import FactorialCalculator
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class ArrangementCalculator:
    """Calcule ``A(n, k) = n! / (n - k)!``."""

    def __init__(self) -> None:
        """Initialise le calculateur."""
        self._factorial: FactorialCalculator = FactorialCalculator()

    def count(self, n: int, k: int) -> int:
        """Retourne le nombre d'arrangements de ``k`` objets parmi ``n``.

        :param n: Taille de l'ensemble.
        :param k: Nombre de tirages ordonnés sans remise.
        :raises InvalidCombinatorialParameterException: si ``k > n`` ou entrées invalides.
        """
        if k < 0 or n < 0:
            raise InvalidCombinatorialParameterException(
                "n et k doivent être positifs ou nuls pour les arrangements."
            )
        if k > n:
            raise InvalidCombinatorialParameterException(
                f"k ne peut pas dépasser n pour A(n,k) (reçu n={n}, k={k})."
            )
        if k == 0:
            return 1
        return self._factorial.factorial(n) // self._factorial.factorial(n - k)
