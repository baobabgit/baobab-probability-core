"""Tests pour :class:`InvalidProbabilityValueException`."""

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)


class TestInvalidProbabilityValueException:
    """Messages par défaut et personnalisés."""

    def test_default_message(self) -> None:
        """Message par défaut."""
        exc = InvalidProbabilityValueException()
        assert str(exc) == InvalidProbabilityValueException.DEFAULT_MESSAGE

    def test_custom_message(self) -> None:
        """Message personnalisé."""
        exc = InvalidProbabilityValueException("détail")
        assert str(exc) == "détail"
