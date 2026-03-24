"""Résultat de comparaison d'une probabilité à une fréquence observée."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ProbabilityComparisonResult:
    """Écart entre une probabilité théorique et une fréquence empirique."""

    theoretical_probability: float
    observed_frequency: float
    absolute_error: float
    relative_error: float | None
