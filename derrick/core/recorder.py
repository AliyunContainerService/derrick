#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import simplejson as json

from derrick.core.common import *
from derrick.core.exceptions import UnmarshalFailedException
from derrick.core.logger import Logger
import traceback

ENGINE = "engine"


class Recorder(object):
    def load(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()


class FileRecorder(Recorder):
    def __init__(self):
        super(FileRecorder, self).__init__()
        try:
            self.load()
        except Exception as e:
            Logger.debug("File may not exists and will create after config creation.")

    def load(self):
        if self.config_file is None:
            raise Exception("You should supply at least one config file.")

        with open(self.config_file, "r") as f:
            content = f.read()
            if content is None or content is "" or len(content) is 0:
                pass
            else:
                try:
                    json_dict = json.loads(content)
                    self.unmarshal(json_dict)
                except Exception as e:
                    Logger.debug("Failed to load derrick_conf,because of %s" % e)

    def record(self, dict_data):
        self.unmarshal(dict_data)
        self.save()

    def get_record(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return None

    def save(self):
        with open(self.config_file, "w") as f:
            f.write(json.dumps(self, default=self.marshal))

    def marshal(self, item):
        return item.__dict__

    def unmarshal(self, dict_content):
        if dict_content is not None and issubclass(dict_content.__class__, dict):
            self.__dict__.update(dict_content)
        else:
            raise UnmarshalFailedException()


class ApplicationRecorder(FileRecorder):
    """
    ApplicationRecorder will record every useful information in whole lifecycle
    You can also get latest application status from ApplicationRecord
    """
    config_file = os.path.join(get_workspace(), DERRICK_APPLICATION_CONF)

    def __init__(self):
        super(ApplicationRecorder, self).__init__()


class DerrickRecorder(FileRecorder):
    """
    DerrickRecorder will record the conf all over the Derrick projects.
    """
    config_file = os.path.join(get_derrick_home(), DERRICK_APPLICATION_CONF)

    def __init__(self):
        super(DerrickRecorder, self).__init__()

    def is_valid(self):
        if self.get_record(ENGINE):
            return True
        else:
            return False
