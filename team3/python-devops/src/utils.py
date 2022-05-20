import os
import sys
import logging

from loguru import logger


def get_output():
    return 'v1'


def setup_logger():
    logger.remove(handler_id=None)
    logger.add(
        sys.stdout, level=logging.INFO, format="{time:%Y-%m-%d %H:%M:%S} - {message}",
        serialize=True,
    )
    # logger.add(
    #     os.path.join('../log/', 'info.log'), level=logging.INFO,
    #     serialize=True,
    #     format="{time:%Y-%m-%d %H:%M:%S} - {message}",
    #     filter=lambda record: record['level'].name == 'INFO', rotation="00:00"
    # )
    # logger.add(
    #     os.path.join('../log/', 'error.log'),
    #     serialize=True,
    #     level=logging.ERROR, format="{time:%Y-%m-%d %H:%M:%S} - {message}", rotation="00:00"
    # )


