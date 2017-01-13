import chalk as log


class NotCompletelyConvertedException(Exception):
    log.red("Not completely converted.But something works well.")


class NotFoundAccessKeyInfoInConf(Exception):
    log.red("Not Found AccessKeyId or AccessKeySecret in derrick config path")
