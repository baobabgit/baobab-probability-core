"""Tests pour :class:`InvalidCombinatorialParameterException`."""

from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)


class TestInvalidCombinatorialParameterException:
    """Exception combinatoire."""

    def test_raise(self) -> None:
        """Instanciation."""
        e = InvalidCombinatorialParameterException("bad")
        assert str(e) == "bad"
