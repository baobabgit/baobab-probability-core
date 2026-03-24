"""Tests pour :class:`DistributionParameterValidator`."""

import pytest

from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)
from baobab_probability_core.validators.distribution_parameter_validator import (
    DistributionParameterValidator,
)


class TestDistributionParameterValidator:
    """Contrôles sur entiers et taux."""

    def test_non_negative_int(self) -> None:
        """n >= 0."""
        v = DistributionParameterValidator()
        v.validate_non_negative_int(0)
        with pytest.raises(InvalidDistributionParameterException):
            v.validate_non_negative_int(-1)

    def test_positive_int(self) -> None:
        """n > 0."""
        v = DistributionParameterValidator()
        v.validate_positive_int(1)
        with pytest.raises(InvalidDistributionParameterException):
            v.validate_positive_int(0)

    def test_positive_rate(self) -> None:
        """λ > 0."""
        v = DistributionParameterValidator()
        v.validate_positive_rate(0.1)
        with pytest.raises(InvalidDistributionParameterException):
            v.validate_positive_rate(0.0)
