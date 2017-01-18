"""
    2017.01.16
    Simple implement some custom exception
"""


class NotCompletelyConvertedException(Exception):
    pass


class NotFoundAccessKeyInfoInConf(Exception):
    pass


class NotFoundRemoteRepo(Exception):
    pass


class NotFoundTemplateConf(Exception):
    pass
