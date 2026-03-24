"""Échantillon ou comptage invalide."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class InvalidSampleException(BaobabProbabilityCoreException):
    """Données observées vides ou incohérentes."""
