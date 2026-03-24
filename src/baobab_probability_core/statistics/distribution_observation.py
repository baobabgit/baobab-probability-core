"""Observations discrètes sous forme d'effectifs par modalité."""

from collections.abc import Mapping

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.validators.sample_validator import SampleValidator


class DistributionObservation:
    """Comptage empirique par modalité (chaîne → entier)."""

    def __init__(self, counts: Mapping[str, int]) -> None:
        """Construit l'observation.

        :param counts: Modalité → effectif observé.
        :raises InvalidSampleException: si vide ou somme nulle.
        """
        self._validator: SampleValidator = SampleValidator()
        self._validator.validate_non_empty_mapping(dict(counts), "counts")
        self._validator.validate_non_negative_counts(dict(counts))
        total: int = sum(counts.values())
        if total == 0:
            raise InvalidSampleException("La somme des effectifs doit être strictement positive.")
        self._counts: dict[str, int] = dict(counts)

    @property
    def counts(self) -> dict[str, int]:
        """Effectifs par modalité."""
        return dict(self._counts)

    def total_count(self) -> int:
        """Effectif total ``N``."""
        return sum(self._counts.values())
