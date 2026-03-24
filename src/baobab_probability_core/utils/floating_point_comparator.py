"""Comparaisons flottantes robustes."""

from baobab_probability_core.constants.mathematical_constants import DEFAULT_FLOAT_TOLERANCE


class FloatingPointComparator:
    """Utilitaires de cohérence sur les nombres flottants."""

    def __init__(self, tolerance: float = DEFAULT_FLOAT_TOLERANCE) -> None:
        """Initialise le comparateur.

        :param tolerance: Écart maximal accepté pour considérer deux valeurs égales.
        """
        self._tolerance: float = tolerance

    @property
    def tolerance(self) -> float:
        """Tolérance de comparaison."""
        return self._tolerance

    def is_close(self, a: float, b: float) -> bool:
        """Indique si ``a`` et ``b`` sont proches à tolérance près."""
        return abs(a - b) <= self._tolerance

    def sum_is_one(self, values: list[float]) -> bool:
        """Vérifie si ``sum(values)`` vaut 1 à tolérance près."""
        return self.is_close(sum(values), 1.0)
