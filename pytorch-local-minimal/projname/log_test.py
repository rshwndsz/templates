import os
import logging
import pytest
from projname.log import Logger


def test_logger(caplog):
    logger = Logger()
    logger.debug("Testing logger with DEBUG")
    assert "Testing logger with DEBUG" in open('.logs/LOG.log').read()
