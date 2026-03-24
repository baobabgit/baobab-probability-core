"""Résumé descriptif simple."""

from collections.abc import Sequence

from baobab_probability_core.validators.sample_validator import SampleValidator


class DescriptiveStatistics:
    """Agrégats de base sur une série numérique."""

    def __init__(
        self,
        count: int,
        mean: float,
        minimum: float,
        maximum: float,
    ) -> None:
        """Construit le résumé (usage interne ou tests)."""
        self.count: int = count
        self.mean: float = mean
        self.minimum: float = minimum
        self.maximum: float = maximum

    @classmethod
    def from_values(cls, values: Sequence[float]) -> "DescriptiveStatistics":
        """Calcule compte, moyenne, min et max.

        :raises InvalidSampleException: si la série est vide.
        """
        validator: SampleValidator = SampleValidator()
        validator.validate_non_empty_sequence(values, "values")
        seq: list[float] = list(values)
        n: int = len(seq)
        avg: float = sum(seq) / n
        return cls(count=n, mean=avg, minimum=min(seq), maximum=max(seq))
