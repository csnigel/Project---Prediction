# Prediction problem

The task is to predict nine current-quarter (`Q0`) financial statement values for each company:

1. Total assets
2. Total liabilities
3. Total stockholders' equity
4. Gross profit
5. Cost of revenues
6. Revenues
7. Operating income
8. Operating expenses
9. EBITDA

Predictors include the same financial quantities and related statement values over quarters `Q1` through `Q10`, fiscal-year-end indicators, and current company metadata. `Id` is a row identifier and is never used as a predictor.

Performance is the unweighted mean of target-level symmetric mean absolute percentage error:

```text
sMAPE(y, p) = 100% × mean(|y - p| / ((|y| + |p|) / 2))
```

Each target contributes equally to the final score regardless of its monetary scale.

The data are synthetic. Results therefore describe performance on the supplied generator and should not be interpreted as a production forecast of real company fundamentals.

