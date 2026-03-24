"""Représentation d'un événement comme ensemble d'issues."""

from collections.abc import Iterable


class Event:
    """Événement discret : ensemble fini d'issues (labels)."""

    def __init__(self, outcomes: Iterable[str]) -> None:
        """Construit l'événement.

        :param outcomes: Issues constituant l'événement (unicité conservée).
        """
        self._outcomes: frozenset[str] = frozenset(outcomes)

    @property
    def outcomes(self) -> frozenset[str]:
        """Issues de l'événement."""
        return self._outcomes

    def union(self, other: "Event") -> "Event":
        """Union ensembliste."""
        return Event(self.outcomes | other.outcomes)

    def intersection(self, other: "Event") -> "Event":
        """Intersection ensembliste."""
        return Event(self.outcomes & other.outcomes)

    def is_empty(self) -> bool:
        """Indique si l'événement est vide."""
        return len(self._outcomes) == 0
