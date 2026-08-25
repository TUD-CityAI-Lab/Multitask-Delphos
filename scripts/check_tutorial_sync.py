"""Verify published notebooks and their pinned-component provenance."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(__file__).with_name("tutorial_manifest.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gitlink_commit(component: str) -> str | None:
    process = subprocess.run(
        ["git", "ls-files", "--stage", "--", component],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    fields = process.stdout.split()
    return fields[1] if len(fields) >= 2 and fields[0] == "160000" else None


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures: list[str] = []
    compared_sources = 0

    for component, details in manifest.items():
        expected_commit = details["commit"]
        actual_commit = gitlink_commit(component)
        if actual_commit != expected_commit:
            failures.append(
                f"component pin: {component} is {actual_commit}, expected {expected_commit}"
            )

        source_dir = ROOT / component / details["source"]
        published_dir = ROOT / details["published"]
        expected_files = set(details["notebooks"])
        actual_files = {path.name for path in published_dir.glob("*.ipynb")}
        if actual_files != expected_files:
            failures.append(
                f"published notebook set: {published_dir.relative_to(ROOT)} "
                f"has {sorted(actual_files)}, expected {sorted(expected_files)}"
            )

        for filename, expected_hash in details["notebooks"].items():
            published = published_dir / filename
            if not published.exists():
                continue
            try:
                notebook = json.loads(published.read_text(encoding="utf-8"))
                if not isinstance(notebook.get("cells"), list):
                    raise ValueError("missing cells list")
            except (json.JSONDecodeError, ValueError) as exc:
                failures.append(f"invalid notebook: {published.relative_to(ROOT)} ({exc})")
                continue

            actual_hash = sha256(published)
            if actual_hash != expected_hash:
                failures.append(
                    f"notebook hash: {published.relative_to(ROOT)} is {actual_hash}, "
                    f"expected {expected_hash}"
                )

            source = source_dir / filename
            if source.exists():
                compared_sources += 1
                if source.read_bytes() != published.read_bytes():
                    failures.append(
                        f"source drift: {published.relative_to(ROOT)} != "
                        f"{source.relative_to(ROOT)}"
                    )

    if failures:
        print("Tutorial provenance check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    source_note = (
        f"; compared {compared_sources} initialised component sources"
        if compared_sources
        else "; private component sources not checked out"
    )
    print(f"Tutorial hashes and component pins are valid{source_note}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
