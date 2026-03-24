"""Constantes numériques partagées."""

# Tolérance par défaut pour comparaisons flottantes (sommes de probabilités, etc.).
DEFAULT_FLOAT_TOLERANCE: float = 1e-9

# Seuil minimal pour éviter une division par zéro dans les erreurs relatives.
MIN_POSITIVE_FOR_RELATIVE_ERROR: float = 1e-15
