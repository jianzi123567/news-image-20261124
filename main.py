#!/usr/bin/env python3
"""news-image-20261124: publish the bundled 24 November 2026 news image.

The repository ships entry.png, a 1024x1024 picture summing up the
day's world news. This program copies those exact bytes to the output
directory. It performs no network access, reads no clock and uses no
randomness, so repeated runs always produce the same output.
"""

import os
import sys
import zlib
from pathlib import Path

BUNDLED_NAME = "entry.png"
LIMIT_BYTES = 1_048_576

# File signatures we accept, as (magic bytes, label) pairs.
KNOWN_KINDS = (
    (b"\x89PNG\r\n\x1a\n", "PNG"),
    (b"\xff\xd8\xff", "JPEG"),
)


def load_image_bytes():
    """Read and validate the bundled image; return (bytes, kind)."""
    here = Path(__file__).resolve().parent
    image_path = here / BUNDLED_NAME
    if not image_path.is_file():
        sys.exit(f"bundled image {BUNDLED_NAME} is missing")
    payload = image_path.read_bytes()
    if not payload:
        sys.exit(f"bundled image {BUNDLED_NAME} is empty")
    if len(payload) > LIMIT_BYTES:
        sys.exit(f"bundled image {BUNDLED_NAME} exceeds 1 MiB")
    kind = None
    for magic, label in KNOWN_KINDS:
        if payload.startswith(magic):
            kind = label
            break
    if kind is None:
        sys.exit(f"bundled image {BUNDLED_NAME} is not PNG or JPEG")
    print(f"bundled image is {kind}, {len(payload)} bytes, "
          f"crc32 {zlib.crc32(payload) & 0xFFFFFFFF:08x}")
    return payload, kind


def publish(payload):
    """Write the image to the output directory and confirm the copy."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {out_dir}: {exc}")
    target = out_dir / BUNDLED_NAME
    try:
        target.write_bytes(payload)
    except OSError as exc:
        sys.exit(f"cannot write {target}: {exc}")
    written = target.read_bytes()
    if not target.is_file():
        sys.exit("output image was not created")
    if len(written) != len(payload):
        sys.exit("output image has the wrong size")
    if zlib.crc32(written) != zlib.crc32(payload):
        sys.exit("output image differs from the bundled image")
    print(f"wrote {target} ({len(written)} bytes, "
          f"crc32 {zlib.crc32(written) & 0xFFFFFFFF:08x})")


def run():
    payload, _kind = load_image_bytes()
    publish(payload)


if __name__ == "__main__":
    run()
