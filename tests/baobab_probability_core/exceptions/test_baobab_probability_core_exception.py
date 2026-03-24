"""Tests pour :class:`BaobabProbabilityCoreException`."""

import pytest

from baobab_probability_core.exceptions.baobab_probability_core_exception import (
    BaobabProbabilityCoreException,
)


class TestBaobabProbabilityCoreException:
    """Couverture de l'exception racine."""

    def test_can_raise_and_catch(self) -> None:
        """L'exception racine est levable et interceptable."""
        with pytest.raises(BaobabProbabilityCoreException):
            raise BaobabProbabilityCoreException("erreur")
