"""Tests pour :class:`ProbabilityComparisonResult`."""

from baobab_probability_core.comparison.probability_comparison_result import (
    ProbabilityComparisonResult,
)


class TestProbabilityComparisonResult:
    """Dataclass de comparaison."""

    def test_fields(self) -> None:
        """Champs accessibles."""
        r = ProbabilityComparisonResult(
            theoretical_probability=0.3,
            observed_frequency=0.31,
            absolute_error=0.01,
            relative_error=1 / 30,
        )
        assert r.theoretical_probability == 0.3
        assert r.relative_error is not None
