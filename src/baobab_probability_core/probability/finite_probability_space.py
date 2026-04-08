"""Espace probabiliste fini sur un univers dénombrable."""

from collections.abc import Mapping
from typing import Generic

from baobab_probability_core.constants.mathematical_constants import DEFAULT_FLOAT_TOLERANCE
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.event import Event, OutcomeT
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class FiniteProbabilitySpace(Generic[OutcomeT]):
    """Univers fini avec probabilités sur chaque issue (issues : type hashable)."""

    def __init__(
        self,
        outcome_probabilities: Mapping[OutcomeT, float],
        tolerance: float | None = None,
    ) -> None:
        """Construit l'espace.

        :param outcome_probabilities: Issue → probabilité. Clés hashables
            (ex. ``str``, ``int``, ``tuple``, :class:`enum.Enum`).
        :param tolerance: Tolérance sur la somme ; défaut : constante globale.
        :raises InvalidProbabilityValueException: si l'univers est vide, si une
            probabilité est non finie ou hors ``[0, 1]``, ou si la somme ≠ 1 à
            tolérance près.
        """
        tol: float = DEFAULT_FLOAT_TOLERANCE if tolerance is None else tolerance
        ProbabilityValidator(tol).validate_discrete_probability_distribution(
            outcome_probabilities,
            name="L'univers probabiliste",
        )
        self._outcomes: dict[OutcomeT, float] = dict(outcome_probabilities)

    def probability_of_outcome(self, outcome: OutcomeT) -> float:
        """Probabilité d'une issue élémentaire.

        :raises InvalidProbabilityValueException: si l'issue est absente.
        """
        if outcome not in self._outcomes:
            raise InvalidProbabilityValueException(f"Issue inconnue : {outcome!r}.")
        return self._outcomes[outcome]

    def probability_of_event(self, event: Event[OutcomeT]) -> float:
        """Probabilité d'un événement (somme des issues)."""
        total: float = 0.0
        for o in event.outcomes:
            total += self.probability_of_outcome(o)
        return total
