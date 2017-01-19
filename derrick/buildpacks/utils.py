import os
import re

import requests
import simplejson as json

MAX_RETRY_TIMES = 3
LATEST = "latest"
SPLIT_COLON = ":"
SPLIT_ENTER = "\\\n&&  "


def parse_addons_in_package_management(data):
    data = data.lower()
    commands = []
    commands += install_package_by_search_module(data, "libffi-dev",
                                                 ["argon2-cffi", "bcrypt", "cffi", "cryptography", "django[argon2]",
                                                  "Django[argon2]",
                                                  "django[bcrypt]", "Django[bcrypt]", "PyNaCl", "pyOpenSSL",
                                                  "PyOpenSSL", "requests[security]",
                                                  "misaka"])
    commands += install_package_by_search_module(data, "libmemcache-dev", ["pylibmc"])
    commands += install_package_by_search_module(data, ["mysql-client", "libmysqlclient-dev"], ["mysql"])
    # commands += install_package_by_search_module(data, "redis-cli", ["redis"])
    commands += install_package_by_search_module(data, "postgresql-client", ["postgre"])
    # commands += install_package_by_search_module(data, "mongodb-clients", ["mongo"])
    return commands


def construct_system_dependencies(commands):
    SYSTEM_INSTALL_COMMANDS = ["apt-get update -y", "[INSTALL_COMMAND]",
                               "rm -rf /var/lib/apt/lists/*"]
    SPLIT_ENTER_WITHOUT_AND = "\\\n "
    if len(commands) > 0:
        commands_str = "apt-get install -y " + SPLIT_ENTER_WITHOUT_AND.join(commands)
        for i in range(0, len(SYSTEM_INSTALL_COMMANDS)):
            if SYSTEM_INSTALL_COMMANDS[i] == "[INSTALL_COMMAND]":
                SYSTEM_INSTALL_COMMANDS[i] = commands_str
        return SYSTEM_INSTALL_COMMANDS
    else:
        return []


def install_package_by_search_module(data, package_name, search_keys):
    for name in search_keys:
        if data.find(name) > -1:
            if isinstance(package_name, str) == True:
                return [package_name]
            else:
                return package_name
        else:
            return []


def procfile_to_commands(procfile_data):
    pos = procfile_data.index(":")
    command = procfile_data[pos + 1:-1]
    run_command = command.lstrip().rstrip()
    commands = run_command.split(" ")
    return commands


def convert_to_commands_arr(command_str):
    return command_str.split(" ")


def calculate_version(version_origin, remote_repo, filter_keys):
    version = version_origin.strip("[^>=~<v]")
    tags_list = get_remote_available_tags(remote_repo)
    version = choose_similar_tag(version, tags_list, filter_keys)
    return version


def get_remote_available_tags(remote_repo):
    tags_list = []
    for i in range(MAX_RETRY_TIMES):
        response = requests.get(remote_repo)
        status = response.status_code
        if status == 200:
            body = json.loads(response.text)
            results = body.get("results")
            for i in range(len(results)):
                repo = results[i]
                tags_list.append(repo.get("name"))
            break
    return tags_list


def choose_similar_tag(version, versions_list, filter_words):
    pattern = re.compile('[0-9]')
    max_fix_tag_number = 0
    best_fit_tag_number = 0
    for tag_version in versions_list:

        matched = False
        for word in filter_words:
            if tag_version.find(word) > 0:
                matched = True

        if matched:
            continue

        if max_fix_tag_number == 0 or best_fit_tag_number == 0:
            max_fix_tag_number = tag_version
            best_fit_tag_number = tag_version

        if pattern.match(tag_version[0]):
            max_fix_tag_number = max(tag_version, version) == tag_version and tag_version or version
        else:
            continue

        if best_fit_tag_number == version or max_fix_tag_number == version:
            best_fit_tag_number = max(best_fit_tag_number, max_fix_tag_number)
        else:
            best_fit_tag_number = min(best_fit_tag_number, max_fix_tag_number)

    if best_fit_tag_number == version:
        best_fit_tag_number = LATEST

    return best_fit_tag_number


def path_exists(*paths):
    path_exists_or_not = False
    for path in paths:
        path_exists_or_not = path_exists_or_not or os.path.exists(path)
    return path_exists_or_not


def copy_file_to_dest(dest_dir, src_dir, *paths):
    for path in paths:
        absolute_path = os.path.join(src_dir, path)
        with open(absolute_path) as file:
            data = file.read()
            f = open(os.path.join(dest_dir, path), "wa")
            f.write(data)
            f.close()


def replace_str_in_file(path, old, new):
    if os.path.exists(path) == True:
        with open(path, "r") as f:
            content = f.read()
            replace_content = content.replace(old, new)
            with open(path, "w") as f:
                f.write(replace_content)
        return True
    else:
        return False
