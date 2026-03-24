"""Moments empiriques sur séries numériques."""

from collections.abc import Sequence

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.validators.sample_validator import SampleValidator


class EmpiricalMomentCalculator:
    """Moyenne et variance d'une série réelle."""

    def __init__(self) -> None:
        """Initialise le validateur."""
        self._validator: SampleValidator = SampleValidator()

    def mean(self, values: Sequence[float]) -> float:
        """Moyenne arithmétique."""
        self._validator.validate_non_empty_sequence(values, "values")
        seq: list[float] = list(values)
        return sum(seq) / len(seq)

    def variance(self, values: Sequence[float], unbiased: bool = True) -> float:
        """Variance empirique.

        :param unbiased: Si vrai, divise par ``n-1`` (estimateur sans biais).
        :raises InvalidSampleException: si ``unbiased`` et ``n < 2``.
        """
        self._validator.validate_non_empty_sequence(values, "values")
        seq: list[float] = list(values)
        n: int = len(seq)
        if unbiased and n < 2:
            raise InvalidSampleException(
                "Au moins deux observations sont requises pour une variance non biaisée."
            )
        m: float = sum(seq) / n
        ss: float = sum((x - m) ** 2 for x in seq)
        denom: int = n - 1 if unbiased else n
        return ss / denom
