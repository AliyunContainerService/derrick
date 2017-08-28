#! /usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

DERRICK_LOGO = """
    8888888b.                       d8b        888
    888  "Y88b                      Y8P        888
    888    888                                 888
    888    888 .d88b. 888d888888d888888 .d8888b888  888
    888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
    888    88888888888888    888    888888     888888K
    888  .d88PY8b.    888    888    888Y88b.   888 "88b
    8888888P"  "Y8888 888    888    888 "Y8888P888  888

    ===================================================
    Derrick is a scaffold tool to migrate applications
    You can use Derrick to migrate your project simply.
    ===================================================
"""
DOCKERFILE = "Dockerfile"
DERRICK_HOME = "DERRICK_HOME"
RIGGING_HOME = "rigging"
DEBUG_MODE = "debug"
WORKSPACE = "WORKSPACE"
DERRICK_BUILT_IN = "builtIn"


def singleton(cls):
    """
    singleton annotation to make derrick and ExtensionPoints single
    :param cls:
    :return:
    """
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance
