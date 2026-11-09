#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import configparser
import hashlib
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--application-ini", type=Path, required=True)
    parser.add_argument("--mar", type=Path, required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--release-tag", required=True)
    parser.add_argument("--display-version", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not re.fullmatch(r"[^/\s]+/[^/\s]+", args.repository):
        parser.error("repository must be in owner/repository form")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", args.release_tag):
        parser.error("release tag contains unsupported characters")

    application = configparser.ConfigParser(interpolation=None)
    if not application.read(args.application_ini) or "App" not in application:
        parser.error(f"cannot read application metadata from {args.application_ini}")

    app = application["App"]
    mar_hash = hashlib.sha512(args.mar.read_bytes()).hexdigest()
    mar_url = (
        f"https://github.com/{args.repository}/releases/download/"
        f"{quote(args.release_tag, safe='')}/{quote(args.mar.name)}"
    )

    updates = ET.Element("updates")
    update = ET.SubElement(
        updates,
        "update",
        {
            "type": "minor",
            "displayVersion": args.display_version,
            "appVersion": app["Version"],
            "platformVersion": app.get("PlatformVersion", app["Version"]),
            "buildID": app["BuildID"],
            "detailsURL": f"https://github.com/{args.repository}/releases/tag/{quote(args.release_tag, safe='')}",
        },
    )
    ET.SubElement(
        update,
        "patch",
        {
            "type": "complete",
            "URL": mar_url,
            "hashFunction": "sha512",
            "hashValue": mar_hash,
            "size": str(args.mar.stat().st_size),
        },
    )
    ET.indent(updates, space="  ")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(updates).write(args.output, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
