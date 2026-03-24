"""Distributions discrètes classiques."""

from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.distributions.bernoulli_distribution import BernoulliDistribution
from baobab_probability_core.distributions.binomial_distribution import BinomialDistribution
from baobab_probability_core.distributions.geometric_distribution import GeometricDistribution
from baobab_probability_core.distributions.hypergeometric_distribution import (
    HypergeometricDistribution,
)
from baobab_probability_core.distributions.poisson_distribution import PoissonDistribution

__all__ = [
    "BaseDistribution",
    "BernoulliDistribution",
    "BinomialDistribution",
    "GeometricDistribution",
    "HypergeometricDistribution",
    "PoissonDistribution",
]
