import os
import chalk as log


def exists(path):
    path_arr = path.split("/")
    last_path = path_arr[-1]
    file_arr = last_path.split(".")

    isFile, isPath = False, False
    if len(file_arr) > 0:
        isFile = True
    else:
        isPath = True

    if isFile == True:
        parent_dir = os.path.abspath(os.path.join(path, os.pardir))
        if os.path.exists(parent_dir) != True:
            try:
                os.system("mkdir -p %s" % path)
            except Exception, e:
                log.red("Failed to create parent dir in path")
                return False

        if os.path.exists(path):
            touch(path)

    if isPath == True:
        if os.path.exists(path) != True:
            try:
                os.system("mkdir -p %s" % path)
            except Exception, e:
                log.red("Failed to create file in path")
                return False
    return True

def touch(file_name):
    try:
        os.utime(file_name, None)
    except:
        open(file_name, 'a').close()
