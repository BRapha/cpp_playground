#!/usr/bin/env python3

import argparse
import os
import subprocess
import shutil

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR
BUILD_DIR = BASE_DIR / "build"


def parse_args():
    parser = argparse.ArgumentParser(description="Build project")
    parser.add_argument("-c", "--clean", action="store_true", help="Make a clean build")
    parser.add_argument("-t", "--enable_testing", action="store_true", help="Enable testing")
    return parser.parse_args()


def configure(args):
    if args.clean and BUILD_DIR.is_dir():
        shutil.rmtree(BUILD_DIR)

    os.makedirs(BUILD_DIR, exist_ok=True)

    config_cmd = ["cmake", ".."]
    if (args.enable_testing):
        config_cmd.append("-DBUILD_TESTING=ON")
    else:
        config_cmd.append("-DBUILD_TESTING=OFF")

    subprocess.check_call(config_cmd, cwd=BUILD_DIR)


def build():
    build_cmd = ["cmake", "--build", "."]
    subprocess.check_call(build_cmd, cwd=BUILD_DIR)


def main():
    args = parse_args()
    configure(args)
    build()


if __name__ == "__main__":
    main()
