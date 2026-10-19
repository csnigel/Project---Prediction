from __future__ import annotations

import unittest

import numpy as np

from financial_prediction.accounting import (
    derive_operating_income,
    derive_stockholders_equity,
)
from financial_prediction.metrics import mean_target_smape, smape


class MetricTests(unittest.TestCase):
    def test_perfect_predictions_score_zero(self) -> None:
        values = np.array([0.0, 1.0, -2.0])
        self.assertEqual(smape(values, values), 0.0)

    def test_opposite_signs_score_two_hundred(self) -> None:
        self.assertEqual(smape(np.array([1.0]), np.array([-1.0])), 200.0)

    def test_targets_receive_equal_weight(self) -> None:
        truth = np.array([[1.0, 1.0], [1.0, 1.0]])
        prediction = np.array([[1.0, -1.0], [1.0, -1.0]])
        self.assertEqual(mean_target_smape(truth, prediction), 100.0)


class AccountingTests(unittest.TestCase):
    def test_accounting_identities(self) -> None:
        np.testing.assert_array_equal(
            derive_stockholders_equity(np.array([10.0]), np.array([4.0])),
            np.array([6.0]),
        )
        np.testing.assert_array_equal(
            derive_operating_income(np.array([8.0]), np.array([3.0])),
            np.array([5.0]),
        )


if __name__ == "__main__":
    unittest.main()
