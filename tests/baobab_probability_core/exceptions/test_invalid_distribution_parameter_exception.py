"""Tests pour :class:`InvalidDistributionParameterException`."""

from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class TestInvalidDistributionParameterException:
    """Exception paramètre."""

    def test_is_base_subclass(self) -> None:
        """Hiérarchie."""
        e = InvalidDistributionParameterException("x")
        assert str(e) == "x"
