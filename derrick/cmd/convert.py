import imp
import os
import chalk as log
from derrick.conf.derrick_conf import ScaffoldConf
import derrick.utils.file as fileUtil
from derrick.buildpacks.exception import NotCompletelyConvertedException


def convert(platform=None):
    path = os.getcwd()
    platform = verify_platform(platform=platform, path=path)

    if platform == None:
        log.red("Failed to detect your application platform")
        exit(-1)

    module = load_buildpacks(platform=platform)
    try:
        module.compile()
    except NotCompletelyConvertedException:
        exit(-1)
    except Exception, e:
        log.red("Unknown Exception occured,because of %s" % e.message)


"""
    load buildpacks one by one and check
"""


def verify_platform(platform=None, path=None):
    if platform == None:
        # check platform
        pass
    else:
        return platform


def detect(path=None):
    buildpack_modules = load_buildpacks()


def load_buildpacks(platform=None):
    sf = ScaffoldConf()
    buildpack_path = sf.get_buildpack_path()
    buildpack_modules = []

    if platform != None:
        buildpack_module_name = os.path.join("buildpack", "-", platform)
        module_path = os.path.join(buildpack_path, buildpack_module_name)
        module = {
            "name": buildpack_module_name,
            "module": imp.load_module(buildpack_module_name, module_path),
        }
        return module
    else:
        ok = fileUtil.exists(buildpack_path)
        if ok == True:
            dir_list = os.listdir(buildpack_path)
            for module_name in dir_list:
                module_path = os.path.join(buildpack_path, module_name)
                module = {
                    "name": module_name,
                    "module": imp.load_module(module_name, module_path),
                }
                buildpack_modules.append(module)

    return buildpack_modules
