#! /usr/bin/env python
# -*- coding: utf-8 -*-

class BadUsageException(Exception):
    pass


class RiggingCompileException(Exception):
    pass


class RiggingDetectException(Exception):
    pass


class ParamsShortageException(Exception):
    pass


class UnmarshalFailedException(Exception):
    pass


class DerrickConfigIsNotValidException(Exception):
    pass
