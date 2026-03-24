"""Test d'indépendance sur un espace fini."""

from baobab_probability_core.constants.mathematical_constants import DEFAULT_FLOAT_TOLERANCE
from baobab_probability_core.probability.event import Event, OutcomeT
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace
from baobab_probability_core.utils.floating_point_comparator import FloatingPointComparator


class IndependenceChecker:
    """Vérifie ``P(A ∩ B) ≈ P(A) P(B)``."""

    def __init__(self, tolerance: float = DEFAULT_FLOAT_TOLERANCE) -> None:
        """Initialise le comparateur."""
        self._comparator: FloatingPointComparator = FloatingPointComparator(tolerance)

    def are_independent(
        self,
        space: FiniteProbabilitySpace[OutcomeT],
        event_a: Event[OutcomeT],
        event_b: Event[OutcomeT],
    ) -> bool:
        """Indique si ``A`` et ``B`` sont indépendants (approximation flottante)."""
        p_a: float = space.probability_of_event(event_a)
        p_b: float = space.probability_of_event(event_b)
        inter: Event[OutcomeT] = event_a.intersection(event_b)
        p_ab: float = space.probability_of_event(inter)
        expected: float = p_a * p_b
        return self._comparator.is_close(p_ab, expected)
