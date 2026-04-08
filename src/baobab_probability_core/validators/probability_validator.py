"""Validation des probabilités dans ``[0, 1]``."""

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)


class ProbabilityValidator:
    """Contrôles sur des probabilités scalaires."""

    def validate_closed_unit_interval(self, value: float, name: str = "p") -> None:
        """Vérifie ``0 <= value <= 1``.

        :param value: Probabilité candidate.
        :param name: Nom du paramètre pour les messages.
        :raises InvalidProbabilityValueException: si hors intervalle.
        """
        if not 0.0 <= value <= 1.0:
            raise InvalidProbabilityValueException(f"{name} doit être dans [0, 1] (reçu {value}).")

    def validate_open_zero_closed_one(self, value: float, name: str = "p") -> None:
        """Vérifie ``0 < value <= 1`` (intervalle ouvert à 0, fermé à 1 ; ``]0, 1]``).

        :param value: Probabilité candidate (ex. masse marginale ``P(A)``).
        :param name: Nom du paramètre pour les messages.
        :raises InvalidProbabilityValueException: si hors ``]0, 1]``.
        """
        if not 0.0 < value <= 1.0:
            raise InvalidProbabilityValueException(f"{name} doit être dans ]0, 1] (reçu {value}).")
