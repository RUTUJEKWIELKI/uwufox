#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import re
from pathlib import Path


VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:\.(\d+))?$")


def parse_version(value):
    match = VERSION.fullmatch(value)
    if not match:
        return None
    return tuple(int(part or 0) for part in match.groups())


def main():
    parser = argparse.ArgumentParser(
        description="Choose the next numeric Uwufox release version."
    )
    parser.add_argument("--base-version", required=True)
    parser.add_argument("--run-number", type=int, required=True)
    parser.add_argument("--tags-file", type=Path, required=True)
    args = parser.parse_args()

    base = parse_version(args.base_version)
    if base is None:
        parser.error("base version must contain three or four numeric components")
    if args.run_number < 1:
        parser.error("workflow run number must be positive")

    versions = [base]
    versions.extend(
        version
        for tag in args.tags_file.read_text(encoding="utf-8").splitlines()
        if (version := parse_version(tag)) is not None
    )
    major, minor, patch, _build = max(versions)

    # The patch increases for each release; the fourth component keeps
    # simultaneous workflow runs on the same patch uniquely ordered.
    print(f"{major}.{minor}.{patch + 1}.{args.run_number}")


if __name__ == "__main__":
    main()
