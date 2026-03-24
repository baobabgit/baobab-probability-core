"""Comparaison point par point entre loi théorique et empirique."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DistributionComparisonResult:
    """Écarts entre probabilités théoriques et fréquences observées."""

    modalities: tuple[str, ...]
    theoretical_probabilities: tuple[float, ...]
    observed_frequencies: tuple[float, ...]
    absolute_errors: tuple[float, ...]
    sum_absolute_errors: float
    max_absolute_error: float
