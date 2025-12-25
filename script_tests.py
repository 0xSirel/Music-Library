#!/usr/bin/env python3
import subprocess
import sys
import json
import tomllib

TOML_FILE = "pyproject.toml"
MODULE = "src/musiclibrary"


def run(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command)
    if result.returncode != 0:
        sys.exit(result.returncode)


def get_threshold():
    with open(TOML_FILE, "rb") as f:
        data = tomllib.load(f)
    return data["tool"]["coverage"]["report"]["fail_under"]


def main():
    COVERAGE_THRESHOLD = get_threshold()
    run(["pytest", f"--cov={MODULE}", "--cov-report=term"])
    run(["coverage", "json", "-o", "coverage.json"])

    with open("coverage.json") as f:
        data = json.load(f)
        total = data["totals"]["percent_covered"]
        print(f"Total coverage: {total:.2f}%")
        if total < COVERAGE_THRESHOLD:
            print(f"Coverage {total:.2f}% < {COVERAGE_THRESHOLD}%! FAIL")
            sys.exit(1)


if __name__ == "__main__":
    main()
