"""


"""
import json
import logging
import os
import sys

from .config import RenderConfig
from .cli import MainCli


# from .exceptions import ()

log = logging.getLogger("resume-render")


def _main():

    config = RenderConfig()

    log.info("Starting Resume Renderer")
    log.debug(f"  PID: {os.getpid()}")
    log.debug(f"  Args: {sys.argv[1:]}")

    MainCli(config).handle_args(sys.argv[1:])


def main():

    try:
        _main()
    except (
        KeyboardInterrupt
    ) as e:
        log.error(f"Exiting due to {e.__class__}: {str(e)}")
