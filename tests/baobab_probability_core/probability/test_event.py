"""Tests pour :class:`Event`."""

from baobab_probability_core.probability.event import Event


class TestEvent:
    """Événements."""

    def test_union_intersection(self) -> None:
        """Opérations ensemblistes."""
        a = Event(["1", "2"])
        b = Event(["2", "3"])
        assert a.union(b).outcomes == frozenset({"1", "2", "3"})
        assert a.intersection(b).outcomes == frozenset({"2"})

    def test_empty(self) -> None:
        """Événement vide."""
        assert Event([]).is_empty()
