import requests
import simplejson as json
import re

MAX_RETRY_TIMES = 3
LATEST = "latest"


def procfile_to_commands(procfile_data):
    commands_arr = procfile_data.split(":")
    run_command = commands_arr[-1].lstrip().rstrip()
    commands = run_command.split(" ")
    return commands


def convert_to_commands_arr(command_str):
    return command_str.split(" ")


def calculate_version(version_origin, remote_repo, filter_keys):
    version = version_origin.strip("[^>=~<]")
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
