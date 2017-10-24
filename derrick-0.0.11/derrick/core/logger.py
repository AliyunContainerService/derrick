#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys

import chalk


class ChalkHandler(logging.StreamHandler):
    def format(self, record):
        """
        Format the specified record.

        If a formatter is set, use it. Otherwise, use the default formatter
        for the module.
        """
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = ChalkFormatter()
        return fmt.format(record)


class ChalkFormatter(logging.Formatter):
    def formatMessage(self, record):
        message = super(ChalkFormatter, self).formatMessage(record)
        level = record.levelno
        _chalk = get_chalk_color(level)
        return _chalk(message)

    def format(self, record):
        if sys.version_info[0] < 3:
            level = record.levelno
            _chalk = get_chalk_color(level)
            self._fmt = _chalk(self._fmt)
        return super(ChalkFormatter, self).format(record)

    def formatException(self, ei):
        exception = super(ChalkFormatter, self).formatException(ei)
        return chalk.format_red(exception)


def get_chalk_color(level):
    """
    gets the appropriate piece of chalk for the logging level
    """
    if level >= logging.ERROR:
        _chalk = chalk.format_magenta
    elif level >= logging.WARNING:
        _chalk = chalk.format_yellow
    elif level >= logging.INFO:
        _chalk = chalk.format_cyan
    elif level >= logging.DEBUG:
        _chalk = chalk.format_green
    return _chalk


_logger = logging.getLogger("derrick")
_handler = ChalkHandler()
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
