import json
from os import name
import time
import arrow
import urllib.request


def _get_github_json(username):
    url = f"https://api.github.com/users/{username}/repos"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
    return body


def _to_list(json_list: list) -> list:
    li = []
    for json_dict in json_list:
        created_at = arrow.get(json_dict["created_at"])
        pushed_at = arrow.get(json_dict["pushed_at"])
        j = {
            "name": json_dict["name"],
            "html_url": json_dict["html_url"],
            "description": json_dict["description"],
            "fork": json_dict["fork"],
            "language": json_dict["language"],
            "license": json_dict["license"],
            "size": json_dict["size"],
            "stargazers_count": json_dict["stargazers_count"],
            "watchers_count": json_dict["watchers_count"],
            "forks_count": json_dict["forks_count"],
            "created_at_utc": created_at.format(),
            "created_at_jst": created_at.to("Asia/Tokyo").format(),
            "update_at_utc": pushed_at.format(),
            "update_at_jst": pushed_at.to("Asia/Tokyo").format(),
        }
        li.append(j)
    return li


def get_github_stats(username: str):
    res = []
    j = _get_github_json(username)
    l = _to_list(j)
    for d in l:
        if not (d["fork"]) and d["description"]:
            s = f'[{d["name"]}]({d["html_url"]}): {d["description"]}'
            res.append(s)
    return res


# [remind\-task · PyPI](https://pypi.org/project/remind-task/): 通知を繰り返すCLIアプリケーション。macOS専用
