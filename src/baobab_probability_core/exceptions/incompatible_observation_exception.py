"""Observation incompatible avec le modèle théorique."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class IncompatibleObservationException(BaobabProbabilityCoreException):
    """Modalités ou dimensions différentes entre théorie et observation."""

    DEFAULT_MESSAGE: str = "Observation incompatible avec le modèle théorique."

    def __init__(self, message: str | None = None) -> None:
        """Construit l'exception.

        :param message: Détail ; si absent, :attr:`DEFAULT_MESSAGE` est utilisé.
        """
        super().__init__(message if message is not None else self.DEFAULT_MESSAGE)
