#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import simplejson as json

from derrick.core.common import *
from derrick.core.exceptions import UnmarshalFailedException
from derrick.core.logger import Logger


class Recorder(object):
    def load(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()


class ApplicationRecorder(Recorder):
    """
    ApplicationRecorder will record every useful information in whole lifecycle
    You can also get latest application status from ApplicationRecord
    """

    def __init__(self):
        super(ApplicationRecorder, self).__init__()
        self.config_file = os.path.join(get_workspace(), DERRICK_APPLICATION_CONF)
        self.load()

    def load(self):
        with open(self.config_file, "a+") as f:
            content = f.read()
            if content == None or content == "":
                pass
            else:
                try:
                    json_dict = json.loads(content)[0]['datapoints']
                    self.unmarshal(json_dict)
                except Exception as e:
                    Logger.error("Failed to loads .derrick_application_conf,because of %s" % e.message)

    def record(self, dict_data):
        self.unmarshal(dict_data)
        self.save()

    def save(self):
        with open(self.config_file, "a+") as f:
            f.write(json.dumps(self, default=self.marshal))

    def marshal(self, item):
        return item.__dict__

    def unmarshal(self, dict_content):
        if dict_content != None and type(dict_content) is dict:
            self.__dict__.update(dict_content)
        else:
            raise UnmarshalFailedException()
