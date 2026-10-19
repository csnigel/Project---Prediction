"""Accounting identities used for prediction post-processing."""

from __future__ import annotations

import numpy as np


def derive_stockholders_equity(
    total_assets: np.ndarray, total_liabilities: np.ndarray
) -> np.ndarray:
    """Compute stockholders' equity as assets less liabilities."""
    return np.asarray(total_assets) - np.asarray(total_liabilities)


def derive_operating_income(
    gross_profit: np.ndarray, operating_expenses: np.ndarray
) -> np.ndarray:
    """Compute operating income as gross profit less operating expenses."""
    return np.asarray(gross_profit) - np.asarray(operating_expenses)

