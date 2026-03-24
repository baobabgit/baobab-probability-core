"""Validation d'échantillons et de comptages."""

from collections.abc import Mapping, Sequence

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException


class SampleValidator:
    """Contrôles sur listes d'observations et dictionnaires de comptes."""

    def validate_non_empty_sequence(
        self, values: Sequence[object], name: str = "échantillon"
    ) -> None:
        """Vérifie qu'une séquence n'est pas vide.

        :param values: Données observées.
        :param name: Libellé pour les messages.
        :raises InvalidSampleException: si ``values`` est vide.
        """
        if len(values) == 0:
            raise InvalidSampleException(f"{name} ne doit pas être vide.")

    def validate_non_empty_mapping(
        self, counts: Mapping[str, int], name: str = "comptages"
    ) -> None:
        """Vérifie qu'un mapping de comptages n'est pas vide.

        :param counts: Modalité → effectif.
        :param name: Libellé pour les messages.
        :raises InvalidSampleException: si ``counts`` est vide.
        """
        if len(counts) == 0:
            raise InvalidSampleException(f"{name} ne doit pas être vide.")

    def validate_non_negative_counts(self, counts: Mapping[str, int]) -> None:
        """Vérifie que tous les effectifs sont positifs ou nuls.

        :param counts: Modalité → effectif.
        :raises InvalidSampleException: si un effectif est négatif.
        """
        for modality, count in counts.items():
            if count < 0:
                raise InvalidSampleException(
                    f"Effectif négatif pour la modalité {modality!r}: {count}."
                )
