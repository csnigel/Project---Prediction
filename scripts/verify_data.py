"""Verify local dataset sizes and SHA-256 checksums against the manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data" / "raw")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    failures = []
    for record in manifest["files"]:
        path = args.data_dir / record["name"]
        if not path.is_file():
            failures.append(f"missing: {path}")
            continue
        actual_size = path.stat().st_size
        actual_hash = sha256(path)
        ok = actual_size == record["bytes"] and actual_hash == record["sha256"]
        print(f"{'OK' if ok else 'FAIL'} {record['name']} ({actual_size:,} bytes)")
        if not ok:
            failures.append(record["name"])
    if failures:
        raise SystemExit("Dataset verification failed: " + ", ".join(failures))
    print("All dataset files match the release manifest.")


if __name__ == "__main__":
    main()

