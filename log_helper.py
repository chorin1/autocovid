import os
import logging
import sys


def set_logger(name):
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
