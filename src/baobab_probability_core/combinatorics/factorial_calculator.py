"""Factorielle exacte sur entiers."""

import math

from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class FactorialCalculator:
    """Calcule ``n!`` pour ``n >= 0``."""

    def factorial(self, n: int) -> int:
        """Retourne ``n!``.

        :param n: Entier naturel.
        :returns: Factorielle exacte.
        :raises InvalidCombinatorialParameterException: si ``n < 0``.
        """
        if n < 0:
            raise InvalidCombinatorialParameterException(
                f"n doit être positif ou nul pour la factorielle (reçu {n})."
            )
        return math.factorial(n)
