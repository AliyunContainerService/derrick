#! /usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

DOCKERFILE = "Dockerfile"


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
