"""Paramètres combinatoires invalides."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class InvalidCombinatorialParameterException(BaobabProbabilityCoreException):
    """Entiers négatifs ou incohérence (n, k) pour les formules combinatoires."""
