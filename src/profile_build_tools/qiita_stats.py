# pypiから指定のmoduleを取得して情報を得る
import json
from os import name
import time
import arrow
import urllib.request


def _get_qiita_json(username):
    url = f"https://qiita.com/api/v2/users/{username}/items?per_page=100"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
    return body


def _to_list(json_list: list) -> list:
    li = []
    for json_dict in json_list:
        created_at = arrow.get(json_dict["created_at"])
        j = {
            "title": json_dict["title"],
            "url": json_dict["url"],
            "likes_count": json_dict["likes_count"],
            "reactions_count": json_dict["reactions_count"],
            "page_views_count": json_dict["page_views_count"],
            "updated_at": created_at.format("YYYY-MM-DD"),
        }
        li.append(j)
    return li


def get_qiita_stats(username: str):
    res = []
    j = _get_qiita_json(username)
    l = _to_list(j)
    for d in l:
        s = f'[{d["title"]}]({d["url"]}): {d["updated_at"]}'
        res.append(s)
    return res


# [remind\-task · PyPI](https://pypi.org/project/remind-task/): 通知を繰り返すCLIアプリケーション。macOS専用
