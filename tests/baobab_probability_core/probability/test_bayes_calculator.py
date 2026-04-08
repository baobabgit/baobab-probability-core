"""Tests pour :class:`BayesCalculator`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.bayes_calculator import BayesCalculator


class TestBayesCalculator:
    """Formule de Bayes."""

    def test_posterior_nominal_strictly_inside_unit_interval(self) -> None:
        """Cas nominal : résultat strictement dans ``[0, 1]``."""
        calc = BayesCalculator()
        post = calc.posterior(likelihood=0.5, prior=0.4, marginal=0.5)
        assert 0.0 < post < 1.0
        assert post == pytest.approx(0.4)

    def test_posterior_exactly_zero(self) -> None:
        """``P(B|A) = 0`` lorsque ``P(A|B) * P(B) = 0`` avec ``P(A) > 0``."""
        calc = BayesCalculator()
        post = calc.posterior(likelihood=0.0, prior=0.7, marginal=0.3)
        assert post == 0.0

    def test_posterior_exactly_one(self) -> None:
        """``P(B|A) = 1`` lorsque le numérateur égale ``P(A)``."""
        calc = BayesCalculator()
        post = calc.posterior(likelihood=1.0, prior=0.5, marginal=0.5)
        assert post == 1.0

    def test_posterior_boundary_one_from_standard_example(self) -> None:
        """Exemple classique ``0.8 * 0.5 / 0.4 = 1`` (produit égal à ``P(A)``)."""
        calc = BayesCalculator()
        post = calc.posterior(likelihood=0.8, prior=0.5, marginal=0.4)
        assert post == pytest.approx(1.0)

    def test_marginal_zero_rejected(self) -> None:
        """``P(A) = 0`` hors domaine ``]0, 1]``."""
        calc = BayesCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            calc.posterior(0.5, 0.5, 0.0)

    def test_marginal_above_one_rejected(self) -> None:
        """``P(A) > 1`` invalide pour une probabilité."""
        calc = BayesCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            calc.posterior(0.5, 0.5, 1.01)

    def test_joint_exceeds_marginal_rejected(self) -> None:
        """``P(A|B) * P(B) > P(A)`` : posterior théorique > 1, rejeté."""
        calc = BayesCalculator()
        with pytest.raises(InvalidProbabilityValueException) as exc_info:
            calc.posterior(likelihood=0.9, prior=0.9, marginal=0.5)
        assert "P(A)" in str(exc_info.value)

    def test_formerly_invalid_posterior_above_one_rejected(self) -> None:
        """Autre triple incohérent : ``0.95 * 0.95 / 0.5 > 1`` avant la validation."""
        calc = BayesCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            calc.posterior(likelihood=0.95, prior=0.95, marginal=0.5)
