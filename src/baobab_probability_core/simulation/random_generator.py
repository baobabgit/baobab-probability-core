"""Encapsulation du générateur pseudo-aléatoire."""

import random
from typing import Optional


class RandomGenerator:
    """Isoler et fixer la graine pour des simulations reproductibles."""

    def __init__(self, seed: Optional[int] = None) -> None:
        """Construit un générateur.

        :param seed: Graine ; ``None`` pour un état non fixé.
        """
        # Usage statistique / reproductibilité, pas de besoin cryptographique.
        self._rng: random.Random = random.Random(seed)  # nosec B311

    @property
    def rng(self) -> random.Random:
        """Instance ``random.Random`` sous-jacente."""
        return self._rng
