"""Probabilités conditionnelles."""

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.event import Event, OutcomeT
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace


class ConditionalProbabilityCalculator:
    """Calcule ``P(A|B) = P(A ∩ B) / P(B)``."""

    def conditional(
        self,
        space: FiniteProbabilitySpace[OutcomeT],
        event_a: Event[OutcomeT],
        event_b: Event[OutcomeT],
    ) -> float:
        """Probabilité conditionnelle de ``A`` sachant ``B``.

        :raises InvalidProbabilityValueException: si ``P(B) = 0``.
        """
        intersection: Event[OutcomeT] = event_a.intersection(event_b)
        p_b: float = space.probability_of_event(event_b)
        if p_b == 0.0:
            raise InvalidProbabilityValueException(
                "P(B) doit être strictement positif pour P(A|B)."
            )
        p_ab: float = space.probability_of_event(intersection)
        return p_ab / p_b
