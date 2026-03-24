"""Loi géométrique (nombre d'essais jusqu'au premier succès, inclus)."""

from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class GeometricDistribution(BaseDistribution):
    """Géométrique : ``P(X=k) = (1-p)^{k-1} p`` pour ``k >= 1``."""

    def __init__(self, probability: float) -> None:
        """Construit la loi.

        :param probability: ``p`` dans ``(0, 1]``.
        :raises InvalidDistributionParameterException: si ``p <= 0`` ou ``p > 1``.
        """
        if probability <= 0.0 or probability > 1.0:
            raise InvalidDistributionParameterException(
                "p doit être dans (0, 1] pour la géométrique (nombre d'essais jusqu'au succès)."
            )
        self._p: float = probability

    @property
    def probability(self) -> float:
        """Paramètre ``p``."""
        return self._p

    def probability_of(self, value: int) -> float:
        """Probabilité que le premier succès arrive à l'essai ``value``."""
        if value < 1:
            return 0.0
        return ((1.0 - self._p) ** (value - 1)) * self._p

    def expected_value(self) -> float:
        """Espérance ``1/p``."""
        return 1.0 / self._p

    def variance(self) -> float:
        """Variance ``(1-p)/p^2``."""
        return (1.0 - self._p) / (self._p**2)
