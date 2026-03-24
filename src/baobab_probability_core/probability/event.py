"""Représentation d'un événement comme ensemble d'issues."""

from __future__ import annotations

from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

OutcomeT = TypeVar("OutcomeT", bound=Hashable)


class Event(Generic[OutcomeT]):
    """Événement discret : ensemble fini d'issues (:class:`collections.abc.Hashable`)."""

    def __init__(self, outcomes: Iterable[OutcomeT]) -> None:
        """Construit l'événement.

        :param outcomes: Issues constituant l'événement (unicité conservée).
        """
        self._outcomes: frozenset[OutcomeT] = frozenset(outcomes)

    @property
    def outcomes(self) -> frozenset[OutcomeT]:
        """Issues de l'événement."""
        return self._outcomes

    def union(self, other: Event[OutcomeT]) -> Event[OutcomeT]:
        """Union ensembliste."""
        return Event(self.outcomes | other.outcomes)

    def intersection(self, other: Event[OutcomeT]) -> Event[OutcomeT]:
        """Intersection ensembliste."""
        return Event(self.outcomes & other.outcomes)

    def is_empty(self) -> bool:
        """Indique si l'événement est vide."""
        return len(self._outcomes) == 0
