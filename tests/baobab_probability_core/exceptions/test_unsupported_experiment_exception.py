"""Tests pour :class:`UnsupportedExperimentException`."""

from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)


class TestUnsupportedExperimentException:
    """Exception expérience."""

    def test_message(self) -> None:
        """Message."""
        e = UnsupportedExperimentException("non supporté")
        assert str(e) == "non supporté"
