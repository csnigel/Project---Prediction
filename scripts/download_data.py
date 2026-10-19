"""Download GitHub Release data assets and verify their checksums."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
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
    parser.add_argument("--base-url", required=True, help="Release URL ending in /download/data-v1")
    parser.add_argument("--dest", type=Path, default=ROOT / "data" / "raw")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    args.dest.mkdir(parents=True, exist_ok=True)
    base_url = args.base_url.rstrip("/")

    for record in manifest["files"]:
        target = args.dest / record["name"]
        if target.exists() and not args.force:
            if target.stat().st_size == record["bytes"] and sha256(target) == record["sha256"]:
                print(f"OK {record['name']} already present")
                continue
            raise SystemExit(f"Existing file failed verification: {target}")

        temporary = target.with_suffix(target.suffix + ".part")
        url = f"{base_url}/{record['name']}"
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, temporary)
        if temporary.stat().st_size != record["bytes"] or sha256(temporary) != record["sha256"]:
            temporary.unlink(missing_ok=True)
            raise SystemExit(f"Downloaded file failed verification: {record['name']}")
        temporary.replace(target)
        print(f"OK {record['name']}")


if __name__ == "__main__":
    main()

