#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoints


class EngineManager(ExtensionPoints):
    """
    EngineManager will load all engine such as
    Swarm,Kubernetes and so on
    """

    def load(self):
        from derrick.engines.swarm_engine import SwarmEngine
        from derrick.engines.kubernetes_engine import KubernetesEngine

        self.register(SwarmEngine())
        self.register(KubernetesEngine())
