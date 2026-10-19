# Dataset setup

The project uses four synthetic CSV files supplied for the course. They are excluded from Git history and should be distributed as assets on a GitHub Release tagged `data-v1`.

| File | Rows | Columns | Size |
|---|---:|---:|---:|
| `train.csv` | 100,000 | 212 | 351.9 MB |
| `train2.csv` | 50,000 | 212 | 176.0 MB |
| `test_individual.csv` | 50,000 | 203 | 168.0 MB |
| `test_final.csv` | 50,000 | 203 | 168.0 MB |

## Manual GitHub Release upload

1. Publish this repository through GitHub Desktop or the GitHub website.
2. On the repository page, choose **Releases → Draft a new release**.
3. Create the tag `data-v1` and title the release `Synthetic financial prediction data v1`.
4. Drag the four files from `data/raw/` into the release-assets area.
5. Publish the release.
6. Verify a clean download into a temporary directory:

```bash
python scripts/download_data.py \
  --base-url https://github.com/OWNER/REPOSITORY/releases/download/data-v1 \
  --dest path/to/temporary/data
python scripts/verify_data.py --data-dir path/to/temporary/data
```

7. Delete the local `data/raw/*.csv` files only after all four remote downloads pass checksum verification.

The exact sizes, shapes, and SHA-256 checksums are recorded in `manifest.json`.

