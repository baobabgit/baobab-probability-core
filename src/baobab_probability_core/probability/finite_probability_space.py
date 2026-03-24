"""Espace probabiliste fini sur un univers dénombrable."""

from collections.abc import Mapping

from baobab_probability_core.constants.mathematical_constants import DEFAULT_FLOAT_TOLERANCE
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.event import Event
from baobab_probability_core.utils.floating_point_comparator import FloatingPointComparator


class FiniteProbabilitySpace:
    """Univers fini avec probabilités sur chaque issue."""

    def __init__(
        self,
        outcome_probabilities: Mapping[str, float],
        tolerance: float | None = None,
    ) -> None:
        """Construit l'espace.

        :param outcome_probabilities: Issue → probabilité.
        :param tolerance: Tolérance sur la somme ; défaut : constante globale.
        :raises InvalidProbabilityValueException: si somme ≠ 1 ou probabilités invalides.
        """
        if len(outcome_probabilities) == 0:
            raise InvalidProbabilityValueException("L'univers ne doit pas être vide.")
        probs: list[float] = []
        for outcome, p in outcome_probabilities.items():
            if p < 0.0 or p > 1.0:
                raise InvalidProbabilityValueException(
                    f"Probabilité hors [0,1] pour l'issue {outcome!r}: {p}."
                )
            probs.append(p)
        self._comparator: FloatingPointComparator = FloatingPointComparator(
            tolerance if tolerance is not None else DEFAULT_FLOAT_TOLERANCE
        )
        if not self._comparator.sum_is_one(probs):
            raise InvalidProbabilityValueException(
                f"La somme des probabilités doit valoir 1 (somme = {sum(probs)})."
            )
        self._outcomes: dict[str, float] = dict(outcome_probabilities)

    def probability_of_outcome(self, outcome: str) -> float:
        """Probabilité d'une issue élémentaire.

        :raises InvalidProbabilityValueException: si l'issue est absente.
        """
        if outcome not in self._outcomes:
            raise InvalidProbabilityValueException(f"Issue inconnue : {outcome!r}.")
        return self._outcomes[outcome]

    def probability_of_event(self, event: Event) -> float:
        """Probabilité d'un événement (somme des issues)."""
        total: float = 0.0
        for o in event.outcomes:
            total += self.probability_of_outcome(o)
        return total
