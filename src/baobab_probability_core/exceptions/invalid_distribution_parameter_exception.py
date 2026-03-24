"""Paramètre de loi invalide."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class InvalidDistributionParameterException(BaobabProbabilityCoreException):
    """Paramètre de distribution incompatible avec la définition."""
