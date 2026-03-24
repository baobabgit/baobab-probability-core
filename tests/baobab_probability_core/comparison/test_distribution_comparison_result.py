"""Tests pour :class:`DistributionComparisonResult`."""

from baobab_probability_core.comparison.distribution_comparison_result import (
    DistributionComparisonResult,
)


class TestDistributionComparisonResult:
    """Dataclass."""

    def test_fields(self) -> None:
        """Instanciation."""
        r = DistributionComparisonResult(
            modalities=("a",),
            theoretical_probabilities=(1.0,),
            observed_frequencies=(1.0,),
            absolute_errors=(0.0,),
            sum_absolute_errors=0.0,
            max_absolute_error=0.0,
        )
        assert r.max_absolute_error == 0.0
