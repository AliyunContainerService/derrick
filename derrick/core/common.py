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
DERRICK_VERSION = "0.0.1"
DOCKERFILE = "Dockerfile"
DERRICK_HOME = "DERRICK_HOME"
DERRICK_APPLICATION_CONF = ".derrick_application_conf"
RIGGING_HOME = "rigging"
DEBUG_MODE = "--debug"
WORKSPACE = "WORKSPACE"
DERRICK_BUILT_IN = "builtIn"
DERRICK_COMMANDS = "commands"
NEW_LINE = "\n"
FOUR_WHITESPACE = "    "

COMMANDS_DOC_SECTION = "[COMMANDS_DOC_SECTION]"


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
    dockerfile_path = os.path.join(os.getcwd(), DOCKERFILE)
    if os.path.exists(dockerfile_path) == True:
        return True
    return False


def which(name, flags=os.X_OK):
    """
    Search PATH for executable files with the given name.
    On newer versions of MS-Windows, the PATHEXT environment variable will be
    set to the list of file extensions for files considered executable. This
    will normally include things like ".EXE". This function will also find files
    with the given name ending with any of these extensions.
    On MS-Windows the only flag that has any meaning is os.F_OK. Any other
    flags will be ignored.
    @type name: C{str}
    @param name: The name for which to search.
    @type flags: C{int}
    @param flags: Arguments to L{os.access}.
    @rtype: C{list}
    @param: A list of the full paths to files found, in the order in which they
    were found.
    """
    result = []
    exts = list(filter(None, os.environ.get('PATHEXT', '').split(os.pathsep)))
    path = os.environ.get('PATH', None)

    if path is None:
        return []

    for p in os.environ.get('PATH', '').split(os.pathsep):
        p = os.path.join(p, name)
        if os.access(p, flags):
            result.append(p)
        for e in exts:
            pext = p + e
            if os.access(pext, flags):
                result.append(pext)

    return result
