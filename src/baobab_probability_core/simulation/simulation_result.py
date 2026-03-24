"""Conteneur de résultats de simulation."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SimulationResult:
    """Résultat typé d'une simulation.

    Seuls les attributs pertinents pour l'expérience exécutée sont renseignés ; les
    autres valent ``None``.

    :ivar trial_outcomes: Pour Bernoulli ou binomiale : une valeur entière par itération
        (0/1 pour Bernoulli, nombre de succès pour la binomiale simulée).
    :ivar bernoulli_success_total: Pour Bernoulli uniquement : total des succès,
        identique à ``sum(trial_outcomes)`` lorsque ``trial_outcomes`` est renseigné.
    :ivar face_counts_sorted: Pour le dé : paires ``(face, effectif)`` triées par face
        croissante (effectifs de simulation agrégés).
    :ivar urn_successes_per_iteration: Pour l'urne : nombre de succès par itération
        (longueur = nombre d'itérations de la configuration).

    La propriété :attr:`data` reproduit l'ancien dictionnaire ``dict[str, Any]`` pour
    compatibilité ; les champs ci-dessus constituent le contrat public privilégié.
    """

    trial_outcomes: tuple[int, ...] | None = None
    bernoulli_success_total: int | None = None
    face_counts_sorted: tuple[tuple[int, int], ...] | None = None
    urn_successes_per_iteration: tuple[int, ...] | None = None

    @property
    def face_counts(self) -> dict[int, int]:
        """Effectifs par face de dé ; dictionnaire vide si non applicable."""
        if self.face_counts_sorted is None:
            return {}
        return dict(self.face_counts_sorted)

    @property
    def data(self) -> dict[str, Any]:
        """Vue historique type ``dict`` (mêmes clés que les versions précédentes).

        Préférer les attributs typés pour le code nouveau.
        """
        legacy: dict[str, Any] = {}
        if self.trial_outcomes is not None:
            legacy["values"] = list(self.trial_outcomes)
        if self.bernoulli_success_total is not None:
            legacy["successes"] = self.bernoulli_success_total
        if self.face_counts_sorted is not None:
            legacy["counts_by_face"] = dict(self.face_counts_sorted)
        if self.urn_successes_per_iteration is not None:
            legacy["successes_per_trial"] = list(self.urn_successes_per_iteration)
        return legacy
