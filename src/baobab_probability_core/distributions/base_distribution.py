"""Classe abstraite pour les lois discrètes."""

from abc import ABC, abstractmethod
from collections.abc import Iterable


class BaseDistribution(ABC):
    """Interface commune aux distributions discrètes."""

    @abstractmethod
    def probability_of(self, value: int) -> float:
        """Probabilité ``P(X = value)``."""

    @abstractmethod
    def expected_value(self) -> float:
        """Espérance mathématique."""

    @abstractmethod
    def variance(self) -> float:
        """Variance."""

    def support(self) -> Iterable[int]:
        """Support borné pour itération (surcharge optionnelle)."""
        return range(0, 0)
