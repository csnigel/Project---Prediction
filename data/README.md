# Dataset

The project uses four synthetic CSV files supplied for the course. They are excluded from Git history because of their size and are available as assets in the [`data-v1` GitHub Release](https://github.com/csnigel/Project---Prediction/releases/tag/data-v1).

| File | Rows | Columns | Size |
|---|---:|---:|---:|
| `train.csv` | 100,000 | 212 | 351.9 MB |
| `train2.csv` | 50,000 | 212 | 176.0 MB |
| `test_individual.csv` | 50,000 | 203 | 168.0 MB |
| `test_final.csv` | 50,000 | 203 | 168.0 MB |

## Download and verify

Download all four release assets and verify their SHA-256 checksums:

```bash
python scripts/download_data.py \
  --base-url https://github.com/csnigel/Project---Prediction/releases/download/data-v1
python scripts/verify_data.py
```

By default, the download script places the files in the ignored `data/raw/` directory. The exact sizes, shapes, and SHA-256 checksums are recorded in [`manifest.json`](manifest.json).

