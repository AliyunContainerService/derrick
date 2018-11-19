#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
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

DERRICK_HOME = ".derrick"
DERRICK_APPLICATION_CONF = "derrick_conf"
RIGGING_HOME = "rigging"
DERRICK_COMMANDS = "commands"

WORKSPACE_ENV = "WORKSPACE"
DERRICK_HOME_ENV = "DERRICK_HOME"

DERRICK_VERSION = "0.0.23"
NEW_LINE = "\n"
FOUR_WHITESPACE = "    "
COMMANDS_DOC_SECTION = "[COMMANDS_DOC_SECTION]"
DEBUG_MODE = "--debug"


def singleton(cls):
    """
    singleton annotation to make derrick and ExtensionPoints single
    :param cls:
    :return:
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


def get_derrick_home():
    env_home = os.getenv(DERRICK_HOME_ENV)
    if env_home is not None:
        return env_home
    else:
        return os.path.join(os.path.expanduser("~"), DERRICK_HOME)


def get_rigging_home():
    derrick_home = get_derrick_home()
    return os.path.join(derrick_home, RIGGING_HOME)


def get_rigging_home():
    return os.path.join(get_derrick_home(), RIGGING_HOME)


def get_derrick_source_path():
    derrick_source_path = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    return derrick_source_path


def get_commands_home():
    return os.path.join(get_derrick_home(), DERRICK_COMMANDS)


def get_workspace():
    return os.getcwd()


# check if derrick is used for the first time.
def check_derrick_first_setup():
    derrick_home = get_derrick_home()
    if not os.path.exists(derrick_home):
        return True
    return False


def check_application_first_setup():
    application_conf = os.path.join(os.getcwd(), DERRICK_APPLICATION_CONF)
    if not os.path.exists(application_conf):
        return True
    return False


def check_dockerfile_exists():
    dockerfile_path = os.path.join(os.getcwd(), "Dockerfile")
    if os.path.exists(dockerfile_path):
        return True
    return False


def is_windows():
    version = platform.system()
    if version is "Windows":
        return True
    return False
