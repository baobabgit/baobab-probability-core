"""Validation des probabilités scalaires et distributions discrètes."""

import math
from collections.abc import Mapping
from typing import Any

from baobab_probability_core.constants.mathematical_constants import DEFAULT_FLOAT_TOLERANCE
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.utils.floating_point_comparator import FloatingPointComparator


class ProbabilityValidator:
    """Contrôles sur des probabilités scalaires et des masses discrètes."""

    def __init__(self, float_tolerance: float = DEFAULT_FLOAT_TOLERANCE) -> None:
        """Initialise le validateur.

        :param float_tolerance: Tolérance pour vérifier ``sum(p_k) ≈ 1``.
        """
        self._float_cmp: FloatingPointComparator = FloatingPointComparator(float_tolerance)

    def validate_closed_unit_interval(self, value: float, name: str = "p") -> None:
        """Vérifie ``0 <= value <= 1``.

        :param value: Probabilité candidate.
        :param name: Nom du paramètre pour les messages.
        :raises InvalidProbabilityValueException: si hors intervalle.
        """
        if not 0.0 <= value <= 1.0:
            raise InvalidProbabilityValueException(f"{name} doit être dans [0, 1] (reçu {value}).")

    def validate_open_zero_closed_one(self, value: float, name: str = "p") -> None:
        """Vérifie ``0 < value <= 1`` (intervalle ouvert à 0, fermé à 1 ; ``]0, 1]``).

        :param value: Probabilité candidate (ex. masse marginale ``P(A)``).
        :param name: Nom du paramètre pour les messages.
        :raises InvalidProbabilityValueException: si hors ``]0, 1]``.
        """
        if not 0.0 < value <= 1.0:
            raise InvalidProbabilityValueException(f"{name} doit être dans ]0, 1] (reçu {value}).")

    def validate_discrete_probability_distribution(
        self,
        probabilities: Mapping[Any, float],
        *,
        name: str = "distribution théorique",
    ) -> None:
        """Vérifie une distribution de probabilité discrète (masses par modalité).

        **Préconditions** : au moins une modalité ; chaque masse est un réel fini dans
        ``[0, 1]`` ; ``sum_k p_k = 1`` à la tolérance d'instance (voir
        :class:`FloatingPointComparator` et :data:`DEFAULT_FLOAT_TOLERANCE`).

        **Cas rejetés** : mapping vide ; valeur non finie (``nan``, ``inf``) ; masse
        hors ``[0, 1]`` ; somme des masses différente de ``1`` hors tolérance.

        :param probabilities: Modalité → probabilité ``p_k`` (clés hashables).
        :type probabilities: Mapping[Any, float]
        :param name: Libellé pour contextualiser les messages d'erreur.
        :raises InvalidProbabilityValueException: si une précondition est violée.
        """
        if len(probabilities) == 0:
            raise InvalidProbabilityValueException(f"{name} ne doit pas être vide.")
        masses: list[float] = []
        for modality, p in probabilities.items():
            if not math.isfinite(p):
                raise InvalidProbabilityValueException(
                    f"{name} : probabilité non finie pour la modalité {modality!r} (reçu {p})."
                )
            if not 0.0 <= p <= 1.0:
                raise InvalidProbabilityValueException(
                    f"{name} : probabilité hors [0, 1] pour la modalité {modality!r} (reçu {p})."
                )
            masses.append(p)
        if not self._float_cmp.sum_is_one(masses):
            total: float = sum(masses)
            raise InvalidProbabilityValueException(
                f"{name} : la somme des probabilités doit valoir 1 à tolérance près "
                f"(somme = {total})."
            )
