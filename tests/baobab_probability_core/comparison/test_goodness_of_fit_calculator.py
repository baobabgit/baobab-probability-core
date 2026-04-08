"""Tests pour :class:`GoodnessOfFitCalculator`."""

import pytest

from baobab_probability_core.comparison.goodness_of_fit_calculator import GoodnessOfFitCalculator
from baobab_probability_core.exceptions.incompatible_observation_exception import (
    IncompatibleObservationException,
)
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)


class TestGoodnessOfFitCalculator:
    """Chi-deux et distance en variation."""

    def test_pearson_chi_square_perfect(self) -> None:
        """Modèle identique aux données."""
        g = GoodnessOfFitCalculator()
        obs = {"a": 10, "b": 10}
        theo = {"a": 0.5, "b": 0.5}
        assert g.pearson_chi_square_statistic(obs, theo) == pytest.approx(0.0)

    def test_keys_mismatch(self) -> None:
        """Clés différentes."""
        g = GoodnessOfFitCalculator()
        with pytest.raises(IncompatibleObservationException):
            g.pearson_chi_square_statistic({"a": 1}, {"b": 1})

    def test_total_variation(self) -> None:
        """Distance TV."""
        g = GoodnessOfFitCalculator()
        d = g.total_variation_distance({"a": 0.5, "b": 0.5}, {"a": 0.5, "b": 0.5})
        assert d == pytest.approx(0.0)

    def test_pearson_expected_zero_observed_zero(self) -> None:
        """E_k=0 et O_k=0 : terme ignoré."""
        g = GoodnessOfFitCalculator()
        chi2 = g.pearson_chi_square_statistic({"a": 0, "b": 10}, {"a": 0.0, "b": 1.0})
        assert chi2 == pytest.approx(0.0)

    def test_pearson_expected_zero_observed_positive(self) -> None:
        """Incohérence théorie / données."""
        g = GoodnessOfFitCalculator()
        with pytest.raises(IncompatibleObservationException):
            g.pearson_chi_square_statistic({"a": 5, "b": 5}, {"a": 0.0, "b": 1.0})

    def test_tv_keys_mismatch(self) -> None:
        """TV : clés différentes."""
        g = GoodnessOfFitCalculator()
        with pytest.raises(IncompatibleObservationException):
            g.total_variation_distance({"a": 1.0}, {"b": 1.0})

    def test_pearson_rejects_invalid_theoretical(self) -> None:
        """Chi-deux : ``p`` invalide avec modalités alignées."""
        g = GoodnessOfFitCalculator()
        obs = {"a": 10, "b": 10}
        theo = {"a": 0.6, "b": 0.6}
        with pytest.raises(InvalidProbabilityValueException):
            g.pearson_chi_square_statistic(obs, theo)

    def test_total_variation_rejects_invalid_distribution_despite_matching_keys(self) -> None:
        """TV : deuxième distribution invalide, supports identiques."""
        g = GoodnessOfFitCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            g.total_variation_distance({"a": 0.5, "b": 0.5}, {"a": 0.6, "b": 0.6})

    def test_total_variation_rejects_invalid_first_distribution(self) -> None:
        """TV : première distribution invalide."""
        g = GoodnessOfFitCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            g.total_variation_distance({"a": 0.7, "b": 0.7}, {"a": 0.5, "b": 0.5})
