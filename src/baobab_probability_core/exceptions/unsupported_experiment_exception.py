"""Configuration de simulation ou expérience non supportée."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class UnsupportedExperimentException(BaobabProbabilityCoreException):
    """Paramètres d'expérience aléatoire invalides ou non gérés."""
