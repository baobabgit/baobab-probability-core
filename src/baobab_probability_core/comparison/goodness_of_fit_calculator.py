"""Métriques simples d'adéquation (sans dépendance à scipy)."""

from collections.abc import Mapping

from baobab_probability_core.exceptions.incompatible_observation_exception import (
    IncompatibleObservationException,
)
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class GoodnessOfFitCalculator:
    """Chi-deux de Pearson et distance en variation totale sur distributions discrètes."""

    def __init__(self) -> None:
        """Initialise le validateur de distributions."""
        self._prob_val: ProbabilityValidator = ProbabilityValidator()

    def pearson_chi_square_statistic(
        self,
        observed_counts: Mapping[str, int],
        theoretical_probabilities: Mapping[str, float],
    ) -> float:
        """Calcule ``χ² = Σ (O_k - E_k)² / E_k`` avec ``E_k = N p_k``.

        **Préconditions** : mêmes modalités pour ``observed_counts`` et
        ``theoretical_probabilities`` ; ce dernier doit être une distribution de
        probabilité valide (non vide, masses finies dans ``[0, 1]``, somme 1 à
        tolérance près).

        :param observed_counts: Effectifs observés par modalité.
        :param theoretical_probabilities: Probabilités théoriques ``p_k``.
        :raises IncompatibleObservationException: si les ensembles de clés diffèrent ou
            si un effectif théorique nul contredit une observation positive.
        :raises InvalidProbabilityValueException: si ``theoretical_probabilities`` n'est
            pas une distribution de probabilité valide.
        """
        keys_o: set[str] = set(observed_counts.keys())
        keys_t: set[str] = set(theoretical_probabilities.keys())
        if keys_o != keys_t:
            raise IncompatibleObservationException(
                "Les modalités observées et théoriques doivent coïncider."
            )
        self._prob_val.validate_discrete_probability_distribution(
            theoretical_probabilities,
            name="La distribution théorique",
        )
        total: int = sum(observed_counts.values())
        chi2: float = 0.0
        for k in keys_o:
            o_k: float = float(observed_counts[k])
            p_k: float = theoretical_probabilities[k]
            e_k: float = total * p_k
            if e_k <= 0.0:
                if o_k > 0.0:
                    raise IncompatibleObservationException(
                        f"Effectif théorique nul pour la modalité {k!r} mais observation > 0."
                    )
                continue
            chi2 += (o_k - e_k) ** 2 / e_k
        return chi2

    def total_variation_distance(
        self,
        probabilities_p: Mapping[str, float],
        probabilities_q: Mapping[str, float],
    ) -> float:
        """Distance en variation totale ``(1/2) Σ_k |p_k - q_k|`` sur le même support.

        **Préconditions** : ``probabilities_p`` et ``probabilities_q`` ont les mêmes
        clés ; chacune est une distribution de probabilité valide (non vide, masses
        finies dans ``[0, 1]``, somme 1 à tolérance près).

        **Cas rejetés** : supports différents ; l'une ou l'autre distribution invalide.

        :param probabilities_p: Première distribution ``p``.
        :param probabilities_q: Deuxième distribution ``q``.
        :raises IncompatibleObservationException: si les ensembles de modalités diffèrent.
        :raises InvalidProbabilityValueException: si ``p`` ou ``q`` n'est pas une
            distribution de probabilité valide.
        """
        keys_p: set[str] = set(probabilities_p.keys())
        keys_q: set[str] = set(probabilities_q.keys())
        if keys_p != keys_q:
            raise IncompatibleObservationException(
                "Les deux distributions doivent être définies sur les mêmes modalités."
            )
        self._prob_val.validate_discrete_probability_distribution(
            probabilities_p,
            name="La distribution p",
        )
        self._prob_val.validate_discrete_probability_distribution(
            probabilities_q,
            name="La distribution q",
        )
        return 0.5 * sum(abs(probabilities_p[k] - probabilities_q[k]) for k in keys_p)
