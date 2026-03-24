"""Probabilité invalide ou incohérence probabiliste."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class InvalidProbabilityValueException(BaobabProbabilityCoreException):
    """Probabilité hors ``[0, 1]`` ou somme incorrecte."""

    DEFAULT_MESSAGE: str = "Valeur de probabilité invalide ou incohérente."

    def __init__(self, message: str | None = None) -> None:
        """Construit l'exception.

        :param message: Détail ; si absent, :attr:`DEFAULT_MESSAGE` est utilisé.
        """
        super().__init__(message if message is not None else self.DEFAULT_MESSAGE)
