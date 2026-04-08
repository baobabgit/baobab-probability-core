"""Comparaison probabilité théorique / fréquence observée."""

from baobab_probability_core.comparison.distribution_comparison_result import (
    DistributionComparisonResult,
)
from baobab_probability_core.comparison.probability_comparison_result import (
    ProbabilityComparisonResult,
)
from baobab_probability_core.constants.mathematical_constants import (
    MIN_POSITIVE_FOR_RELATIVE_ERROR,
)
from baobab_probability_core.exceptions.invalid_probability_value_exception import (
    InvalidProbabilityValueException,
)
from baobab_probability_core.exceptions.invalid_sample_exception import InvalidSampleException
from baobab_probability_core.statistics.distribution_observation import DistributionObservation
from baobab_probability_core.statistics.frequency_analyzer import FrequencyAnalyzer
from baobab_probability_core.validators.probability_validator import ProbabilityValidator


class TheoreticalObservationComparator:
    """Écarts entre modèle et données de comptage."""

    def __init__(self) -> None:
        """Initialise analyseurs et validateurs."""
        self._prob_val: ProbabilityValidator = ProbabilityValidator()
        self._frequency: FrequencyAnalyzer = FrequencyAnalyzer()

    def compare_probability(
        self,
        theoretical_probability: float,
        observed_successes: int,
        observed_trials: int,
    ) -> ProbabilityComparisonResult:
        """Compare ``p`` à la fréquence ``succès / essais``.

        :raises InvalidSampleException: si ``observed_trials <= 0``.
        :raises InvalidProbabilityValueException: si ``p`` hors ``[0,1]``.
        """
        self._prob_val.validate_closed_unit_interval(theoretical_probability)
        if observed_trials <= 0:
            raise InvalidSampleException(
                "Le nombre d'essais observés doit être strictement positif."
            )
        if observed_successes < 0 or observed_successes > observed_trials:
            raise InvalidProbabilityValueException(
                "Les succès observés doivent être entre 0 et le nombre d'essais."
            )
        freq: float = observed_successes / observed_trials
        abs_err: float = abs(theoretical_probability - freq)
        rel: float | None
        if theoretical_probability > MIN_POSITIVE_FOR_RELATIVE_ERROR:
            rel = abs_err / theoretical_probability
        else:
            rel = None
        return ProbabilityComparisonResult(
            theoretical_probability=theoretical_probability,
            observed_frequency=freq,
            absolute_error=abs_err,
            relative_error=rel,
        )

    def compare_distributions(
        self,
        theoretical_probabilities: dict[str, float],
        observation: DistributionObservation,
    ) -> DistributionComparisonResult:
        """Écarts par modalité entre ``p_k`` théoriques et ``f_k`` empiriques.

        **Préconditions** : ``theoretical_probabilities`` doit être une distribution
        de probabilité valide (non vide, masses finies dans ``[0, 1]``, somme 1 à
        tolérance près). Les clés doivent coïncider exactement avec celles de
        ``observation``.

        **Cas rejetés** : distribution théorique invalide ; discordance de modalités.

        :param theoretical_probabilities: ``p_k`` par modalité.
        :param observation: Effectifs observés par modalité.
        :returns: Écarts absolus et agrégats.
        :raises InvalidProbabilityValueException: si la distribution théorique est
            invalide.
        :raises InvalidSampleException: si les ensembles de modalités diffèrent.
        """
        self._prob_val.validate_discrete_probability_distribution(
            theoretical_probabilities,
            name="La distribution théorique",
        )
        obs_freq: dict[str, float] = self._frequency.relative_frequencies(observation.counts)
        keys_obs: set[str] = set(observation.counts.keys())
        keys_theo: set[str] = set(theoretical_probabilities.keys())
        if keys_obs != keys_theo:
            raise InvalidSampleException("Les modalités théoriques et observées doivent coïncider.")
        keys: tuple[str, ...] = tuple(sorted(keys_obs))
        theo_list: list[float] = [theoretical_probabilities[k] for k in keys]
        obs_list: list[float] = [obs_freq[k] for k in keys]
        abs_errs: list[float] = [abs(t - o) for t, o in zip(theo_list, obs_list, strict=True)]
        return DistributionComparisonResult(
            modalities=keys,
            theoretical_probabilities=tuple(theo_list),
            observed_frequencies=tuple(obs_list),
            absolute_errors=tuple(abs_errs),
            sum_absolute_errors=sum(abs_errs),
            max_absolute_error=max(abs_errs) if abs_errs else 0.0,
        )
