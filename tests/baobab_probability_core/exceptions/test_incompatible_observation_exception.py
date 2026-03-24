"""Tests pour :class:`IncompatibleObservationException`."""

from baobab_probability_core.exceptions.incompatible_observation_exception import (
    IncompatibleObservationException,
)


class TestIncompatibleObservationException:
    """Instanciation."""

    def test_default_message(self) -> None:
        """Message par défaut."""
        exc = IncompatibleObservationException()
        assert str(exc) == IncompatibleObservationException.DEFAULT_MESSAGE
