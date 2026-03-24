"""Analyse des fréquences à partir d'effectifs."""

from collections.abc import Mapping

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.validators.sample_validator import SampleValidator


class FrequencyAnalyzer:
    """Calcule fréquences absolues et relatives à partir de comptages."""

    def __init__(self) -> None:
        """Initialise le validateur d'échantillons."""
        self._validator: SampleValidator = SampleValidator()

    def relative_frequencies(self, counts: Mapping[str, int]) -> dict[str, float]:
        """Retourne les fréquences relatives ``n_k / N``.

        :param counts: Effectifs par modalité.
        :returns: Modalité → fréquence dans ``[0, 1]``.
        :raises InvalidSampleException: si total nul ou entrées invalides.
        """
        self._validator.validate_non_empty_mapping(dict(counts), "counts")
        self._validator.validate_non_negative_counts(dict(counts))
        total: int = sum(counts.values())
        if total == 0:
            raise InvalidSampleException("La somme des effectifs doit être strictement positive.")
        return {k: counts[k] / total for k in counts}
