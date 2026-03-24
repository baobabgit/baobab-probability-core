"""Tests pour :class:`InvalidSampleException`."""

from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException


class TestInvalidSampleException:
    """Exception échantillon."""

    def test_message(self) -> None:
        """Message."""
        e = InvalidSampleException("vide")
        assert str(e) == "vide"
