#!/usr/bin/env python3

from subprocess import call, check_call, CalledProcessError, DEVNULL

from pathlib import Path
import sys


REPO_DIR = Path(__file__).parent


def main():
    args = " ".join(sys.argv[1:])

    try:
        check_call(["docker", "image", "inspect", "kibot"], stdout=DEVNULL)
    except CalledProcessError:
        check_call(["docker", "build", ".", "-t", "kibot"])

    retcode = call(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{REPO_DIR}:/usr/src/project",
            "kibot",
            "bash",
            "-c",
            f"cd /usr/src/project && ./kibot {args}",
        ]
    )
    sys.exit(retcode)


if __name__ == "__main__":
    main()
