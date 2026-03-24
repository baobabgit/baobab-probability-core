"""Exceptions métier du package."""

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)
from baobab_probability_core.exceptions.incompatible_observation_exception import (
    IncompatibleObservationException,
)
from baobab_probability_core.exceptions.invalid_combinatorial_parameter_exception import (
    InvalidCombinatorialParameterException,
)
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.exceptions.unsupported_experiment_exception import (
    UnsupportedExperimentException,
)

__all__ = [
    "BaobabProbabilityCoreException",
    "IncompatibleObservationException",
    "InvalidCombinatorialParameterException",
    "InvalidDistributionParameterException",
    "InvalidProbabilityValueException",
    "InvalidSampleException",
    "UnsupportedExperimentException",
]
