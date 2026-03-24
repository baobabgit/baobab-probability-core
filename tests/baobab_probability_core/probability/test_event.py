"""Tests pour :class:`Event`."""

from baobab_probability_core.probability.event import Event


class TestEvent:
    """Événements."""

    def test_union_intersection(self) -> None:
        """Opérations ensemblistes (issues ``str``)."""
        a = Event(["1", "2"])
        b = Event(["2", "3"])
        assert a.union(b).outcomes == frozenset({"1", "2", "3"})
        assert a.intersection(b).outcomes == frozenset({"2"})

    def test_union_intersection_int(self) -> None:
        """Issues entières hashables."""
        a = Event([1, 2])
        b = Event([2, 3])
        assert a.union(b).outcomes == frozenset({1, 2, 3})
        assert a.intersection(b).outcomes == frozenset({2})

    def test_union_intersection_tuple(self) -> None:
        """Issues tuple (ex. couples pour un produit fini)."""
        a = Event([(0, 0), (0, 1)])
        b = Event([(0, 1), (1, 0)])
        assert a.union(b).outcomes == frozenset({(0, 0), (0, 1), (1, 0)})
        assert a.intersection(b).outcomes == frozenset({(0, 1)})

    def test_empty(self) -> None:
        """Événement vide."""
        assert Event([]).is_empty()
