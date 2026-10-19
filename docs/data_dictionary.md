# Data dictionary

The dataset contains one row per synthetic company observation. `Q0` is the current quarter, `Q1` is the immediately preceding quarter, and `Q10` is the most distant historical quarter.

## Targets

The nine `Q0_*` targets are total assets, total liabilities, total stockholders' equity, gross profit, cost of revenues, revenues, operating income, operating expenses, and EBITDA.

## Quarterly financial predictors

For each quarter `Q1` through `Q10`, the dataset includes 16 financial variables:

| Variable | Meaning |
|---|---|
| `TOTAL_ASSETS` | Current and noncurrent assets |
| `TOTAL_CURRENT_ASSETS` | Assets expected to be converted or used within one year |
| `TOTAL_NONCURRENT_ASSETS` | Longer-lived assets |
| `TOTAL_LIABILITIES` | Current and noncurrent obligations |
| `TOTAL_CURRENT_LIABILITIES` | Obligations expected within one year |
| `TOTAL_NONCURRENT_LIABILITIES` | Obligations extending beyond one year |
| `TOTAL_LIABILITIES_AND_EQUITY` | Total company funding from liabilities and equity |
| `TOTAL_STOCKHOLDERS_EQUITY` | Residual shareholder interest after liabilities |
| `NET_INCOME` | Earnings after expenses, interest, and taxes |
| `GROSS_PROFIT` | Revenues less cost of revenues |
| `COST_OF_REVENUES` | Direct cost of goods or services sold |
| `REVENUES` | Income from primary operations |
| `OPERATING_INCOME` | Core operating profit before interest and taxes |
| `OPERATING_EXPENSES` | Expenses associated with core operations |
| `EBITDA` | Earnings before interest, taxes, depreciation, and amortization |
| `DEPRECIATION_AND_AMORTIZATION` | Noncash depreciation and amortization expense |

Each quarter from `Q0` through `Q10` also has a fiscal-year-end flag.

## Current company metadata

The 31 metadata columns describe the company's current state:

- Workforce and governance risk: `fullTimeEmployees`, `auditRisk`, `boardRisk`, `compensationRisk`, `shareHolderRightsRisk`, `overallRisk`
- Share data: `floatShares`, `sharesOutstanding`
- Earnings and analyst estimates: `trailingEps`, `forwardEps`, `targetHighPrice`, `targetLowPrice`, `targetMeanPrice`, `targetMedianPrice`, `recommendationMean`, `recommendationKey`, `numberOfAnalystOpinions`
- Cash flow and capital structure: `totalCash`, `totalCashPerShare`, `ebitda`, `totalDebt`, `totalRevenue`, `revenuePerShare`, `freeCashflow`, `operatingCashflow`, `revenueGrowth`
- Earnings yields: `trailingEY`, `forwardEY`
- Categories: `industry`, `sector`, `financialCurrency`

The four categorical variables used by the modeling pipelines are `industry`, `sector`, `financialCurrency`, and `recommendationKey`.

