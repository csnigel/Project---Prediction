"""Dataset path and schema helpers."""

from __future__ import annotations

from pathlib import Path


DATASET_NAMES = (
    "train.csv",
    "train2.csv",
    "test_individual.csv",
    "test_final.csv",
)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_data_dir() -> Path:
    return repository_root() / "data" / "raw"


def require_datasets(data_dir: Path | None = None) -> dict[str, Path]:
    directory = Path(data_dir) if data_dir is not None else default_data_dir()
    paths = {name: directory / name for name in DATASET_NAMES}
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            "Missing dataset files. Follow data/README.md: " + ", ".join(missing)
        )
    return paths

