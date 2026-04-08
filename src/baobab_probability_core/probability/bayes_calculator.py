"""Théorème de Bayes sur probabilités scalaires."""

from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class BayesCalculator:
    """Posterior ``P(B|A) = P(A|B) P(B) / P(A)``."""

    def __init__(self) -> None:
        """Initialise les validateurs."""
        self._validator: ProbabilityValidator = ProbabilityValidator()

    def posterior(
        self,
        likelihood: float,
        prior: float,
        marginal: float,
    ) -> float:
        """Calcule la probabilité a posteriori ``P(B|A) = P(A|B) P(B) / P(A)``.

        **Préconditions probabilistes** : les entrées doivent être cohérentes avec
        des probabilités sur ``[0, 1]`` : ``likelihood`` et ``prior`` dans ``[0, 1]``,
        ``marginal`` dans ``]0, 1]``, et ``likelihood * prior <= marginal`` (sinon
        ``P(B|A)`` dépasserait 1).

        **Cas rejetés** : ``marginal`` nul ou strictement supérieur à 1 ;
        ``likelihood`` ou ``prior`` hors ``[0, 1]`` ; produit
        ``likelihood * prior`` strictement supérieur à ``marginal``.

        :param likelihood: ``P(A|B)``, dans ``[0, 1]``.
        :type likelihood: float
        :param prior: ``P(B)``, dans ``[0, 1]``.
        :type prior: float
        :param marginal: ``P(A)``, dans ``]0, 1]``.
        :type marginal: float
        :returns: ``P(B|A)``, toujours dans ``[0, 1]`` lorsque les préconditions tiennent.
        :rtype: float
        :raises InvalidProbabilityValueException: si une précondition est violée.
        """
        self._validator.validate_closed_unit_interval(likelihood, name="P(A|B)")
        self._validator.validate_closed_unit_interval(prior, name="P(B)")
        self._validator.validate_open_zero_closed_one(marginal, name="P(A)")
        joint = likelihood * prior
        if joint > marginal:
            raise InvalidProbabilityValueException(
                "Cohérence probabiliste requise : P(A|B) * P(B) ne doit pas dépasser P(A) "
                f"(reçu produit {joint}, P(A)={marginal})."
            )
        return joint / marginal
