#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
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
DERRICK_COMMANDS = "commands"


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


def get_derrick_home():
    env_home = os.getenv(DERRICK_HOME)
    if env_home != None:
        return env_home
    else:
        return os.path.join(os.path.expanduser("~"), ".derrick")


def get_rigging_home():
    derrick_home = get_derrick_home()
    return os.path.join(derrick_home, "rigging")


def get_rigging_home():
    return os.path.join(get_derrick_home(), RIGGING_HOME)


def get_derrick_source_path():
    derrick_source_path = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    return derrick_source_path


def get_built_in_rigging_path():
    derrick_source_path = get_derrick_source_path()
    return os.path.join(derrick_source_path, DERRICK_BUILT_IN)


def get_commands_home():
    derrick_source_path = get_derrick_source_path()
    return os.path.join(derrick_source_path, DERRICK_COMMANDS)
