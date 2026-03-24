"""Opérations probabilistes de base sur des scalaires."""

from baobab_probability_core.probability.event import Event
from baobab_probability_core.probability.finite_probability_space import FiniteProbabilitySpace
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class ProbabilityCalculator:
    """Complément, union, intersection sur un espace fini."""

    def __init__(self) -> None:
        """Initialise le validateur."""
        self._validator: ProbabilityValidator = ProbabilityValidator()

    def complement(self, probability: float) -> float:
        """Retourne ``1 - p`` avec validation de ``p``."""
        self._validator.validate_closed_unit_interval(probability)
        return 1.0 - probability

    def union(
        self,
        space: FiniteProbabilitySpace,
        event_a: Event,
        event_b: Event,
    ) -> float:
        """``P(A ∪ B) = P(A) + P(B) - P(A ∩ B)``."""
        pa: float = space.probability_of_event(event_a)
        pb: float = space.probability_of_event(event_b)
        inter: Event = event_a.intersection(event_b)
        pab: float = space.probability_of_event(inter)
        return pa + pb - pab

    def intersection(
        self,
        space: FiniteProbabilitySpace,
        event_a: Event,
        event_b: Event,
    ) -> float:
        """``P(A ∩ B)``."""
        inter: Event = event_a.intersection(event_b)
        return space.probability_of_event(inter)

    def simple(self, space: FiniteProbabilitySpace, event: Event) -> float:
        """Probabilité d'un événement (alias explicite)."""
        return space.probability_of_event(event)
