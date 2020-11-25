#!/usr/bin/env python3
"""Executed during setup to compile .proto files"""

from pathlib import Path
import subprocess
try:
    from protoc import PROTOC_EXE
except ImportError:
    PROTOC_EXE = "protoc"


def build(*_setup_kwargs):
    """Run the protocol buffer compiler"""

    root = Path("tensorflow_models") / "research"
    subprocess.run(
        "{} --python_out=. object_detection/protos/*.proto".format(PROTOC_EXE),
        cwd=root,
        shell=True,
        check=False,
    )


if __name__ == "__main__":
    build()
