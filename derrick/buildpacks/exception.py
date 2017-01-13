import chalk as log


class NotCompletelyConvertedException(Exception):
    log.red("Not completely converted.But something works well.")
