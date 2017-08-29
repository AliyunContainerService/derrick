#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from chalk import log

_logger = logging.getLogger("derrick")
_handler = log.ChalkHandler()
_logger.addHandler(_handler)
_logger.setLevel(logging.INFO)


class Logger(object):
    @staticmethod
    def set_debug_mode():
        _logger.setLevel(logging.DEBUG)

    @staticmethod
    def warn(msg, *args, **kwargs):
        _logger.warn(msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        _logger.error(msg, *args, **kwargs)

    @staticmethod
    def info(msg, *args, **kwargs):
        _logger.info(msg, *args, **kwargs)

    @staticmethod
    def debug(msg, *args, **kwargs):
        _logger.debug(msg, *args, **kwargs)
