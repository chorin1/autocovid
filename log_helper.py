import os
import logging
import sys

PARENT_PATH = os.path.dirname(os.path.realpath(__file__))
LOGGING_FILE_PATH = os.path.join("__logger", "{}.log")


def set_logger(name):
    """A logging helper.
    Keeps the logged experiments in the __logger path.
    Both prints out on the Terminal and writes on the
    .log file."""
    os.makedirs("__log", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(f"__log/{name}.log"),
            logging.StreamHandler(sys.stdout)
        ])
    return logging
