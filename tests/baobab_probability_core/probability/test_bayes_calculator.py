"""Tests pour :class:`BayesCalculator`."""

import pytest

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.probability.bayes_calculator import BayesCalculator


class TestBayesCalculator:
    """Formule de Bayes."""

    def test_posterior(self) -> None:
        """Vérification numérique simple."""
        calc = BayesCalculator()
        # P(B|A) = P(A|B)P(B)/P(A)
        post = calc.posterior(likelihood=0.8, prior=0.5, marginal=0.4)
        assert post == pytest.approx(1.0)

    def test_marginal_zero(self) -> None:
        """P(A) nul."""
        calc = BayesCalculator()
        with pytest.raises(InvalidProbabilityValueException):
            calc.posterior(0.5, 0.5, 0.0)
