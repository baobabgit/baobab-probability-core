"""Conteneur de résultats de simulation."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SimulationResult:
    """Résultats agrégés d'une simulation (structure libre dans ``data``)."""

    data: dict[str, Any] = field(default_factory=dict)
