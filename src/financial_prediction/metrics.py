"""Evaluation metrics used throughout the project."""

from __future__ import annotations

import numpy as np


def smape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Return symmetric mean absolute percentage error on a 0-200 scale."""
    truth = np.asarray(y_true, dtype=float)
    prediction = np.asarray(y_pred, dtype=float)
    denominator = (np.abs(truth) + np.abs(prediction)) / 2.0
    ratio = np.divide(
        np.abs(truth - prediction),
        denominator,
        out=np.zeros_like(denominator, dtype=float),
        where=denominator != 0,
    )
    return float(100.0 * ratio.mean())


def mean_target_smape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Average target-level sMAPE, giving every output equal weight."""
    truth = np.asarray(y_true, dtype=float)
    prediction = np.asarray(y_pred, dtype=float)
    if truth.shape != prediction.shape or truth.ndim != 2:
        raise ValueError("Expected two equally shaped matrices: rows by targets")
    return float(np.mean([smape(truth[:, i], prediction[:, i]) for i in range(truth.shape[1])]))

