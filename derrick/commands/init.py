#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command
from derrick.core.derrick import Derrick
from derrick.core.logger import Logger


class Init(Command):
    # implement the interface
    def execute(self, context):
        rigging_manager = Derrick().get_rigging_manager()
        all_rigging = rigging_manager.all()

        detected = False
        handled_rigging = []
        for rigging_name in all_rigging:
            rigging = all_rigging.get(rigging_name)
            try:
                handled, platform = rigging.detect(context)
                if handled == True:
                    detected = True
                    handled_rigging.append({"rigging_name": rigging_name, "rigging": rigging, "platform": platform})
            except Exception as e:
                Logger.debug("Failed to detect your application's platform with rigging(%s),because of %s"
                             % (rigging_name, e.message))
        if detected != False:
            if len(handled_rigging) > 1:
                pass
            else:
                rigging_dict = handled_rigging[0]
                rigging = rigging_dict.get("rigging")
                try:
                    results = rigging.compile(context)
                    Logger.debug("The platform is %s,the rigging used is %s"
                                 % (rigging_dict.get("platform"), rigging_dict.get("rigging_name")))
                    Logger.debug("The results is %s" % results)
                except Exception as e:
                    Logger.error("Failed to compile your application.because of %s" % e.message)
        else:
            Logger.warn(
                "Failed to detect your application's platform."
                "Maybe you can upgrade Derrick to get more platforms supported.")

    def get_help_desc(self):
        return "derrick init (-d | --debug)"
