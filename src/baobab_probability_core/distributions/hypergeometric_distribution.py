"""Loi hypergéométrique."""

from baobab_probability_core.combinatorics.combination_calculator import CombinationCalculator
from baobab_probability_core.distributions.base_distribution import BaseDistribution
from baobab_probability_core.exceptions.invalid_distribution_parameter_exception import (
    InvalidDistributionParameterException,
)


class HypergeometricDistribution(BaseDistribution):
    """Tirages sans remise : ``N`` boules dont ``K`` succès, échantillon ``n``."""

    def __init__(self, population: int, success_population: int, sample_size: int) -> None:
        """Construit la loi.

        :param population: Taille ``N``.
        :param success_population: Nombre de succès ``K`` dans la population.
        :param sample_size: Taille d'échantillon ``n``.
        """
        self._validate(population, success_population, sample_size)
        self._n_pop: int = population
        self._k_succ: int = success_population
        self._n_samp: int = sample_size
        self._comb: CombinationCalculator = CombinationCalculator()

    def _validate(self, population: int, success_population: int, sample_size: int) -> None:
        if population < 0 or success_population < 0 or sample_size < 0:
            raise InvalidDistributionParameterException(
                "N, K et n doivent être des entiers positifs ou nuls."
            )
        if success_population > population:
            raise InvalidDistributionParameterException(
                "Le nombre de succès K ne peut pas dépasser la population N."
            )
        if sample_size > population:
            raise InvalidDistributionParameterException(
                "La taille d'échantillon n ne peut pas dépasser la population N."
            )

    def probability_of(self, value: int) -> float:
        """``P(X=k) = C(K,k) C(N-K, n-k) / C(N,n)``."""
        low: int = max(0, self._n_samp - (self._n_pop - self._k_succ))
        high: int = min(self._n_samp, self._k_succ)
        if value < low or value > high:
            return 0.0
        num: int = self._comb.count(self._k_succ, value) * self._comb.count(
            self._n_pop - self._k_succ, self._n_samp - value
        )
        den: int = self._comb.count(self._n_pop, self._n_samp)
        return num / den

    def expected_value(self) -> float:
        """Espérance ``n K / N``."""
        if self._n_pop == 0:
            return 0.0
        return self._n_samp * self._k_succ / self._n_pop

    def variance(self) -> float:
        """Variance de l'hypergéométrique."""
        if self._n_pop <= 1:
            return 0.0
        n: int = self._n_samp
        k: int = self._k_succ
        big_n: int = self._n_pop
        return n * (k / big_n) * ((big_n - k) / big_n) * ((big_n - n) / (big_n - 1))
