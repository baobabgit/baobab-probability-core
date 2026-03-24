"""Validation des paramètres entiers et de taux pour les lois discrètes."""

from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class DistributionParameterValidator:
    """Contrôles communs aux distributions."""

    def validate_non_negative_int(self, value: int, name: str = "n") -> None:
        """Vérifie ``value >= 0``.

        :raises InvalidDistributionParameterException: si négatif.
        """
        if value < 0:
            raise InvalidDistributionParameterException(
                f"{name} doit être un entier positif ou nul (reçu {value})."
            )

    def validate_positive_int(self, value: int, name: str = "n") -> None:
        """Vérifie ``value > 0``.

        :raises InvalidDistributionParameterException: sinon.
        """
        if value < 1:
            raise InvalidDistributionParameterException(
                f"{name} doit être un entier strictement positif (reçu {value})."
            )

    def validate_positive_rate(self, value: float, name: str = "lambda") -> None:
        """Vérifie ``value > 0`` (taux type Poisson).

        :raises InvalidDistributionParameterException: sinon.
        """
        if value <= 0.0:
            raise InvalidDistributionParameterException(
                f"{name} doit être strictement positif (reçu {value})."
            )
