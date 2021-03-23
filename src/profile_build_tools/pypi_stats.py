# pypiから指定のmoduleを取得して情報を得る
import json
from os import name
import time
import arrow
import urllib.request


def _get_pypi_json(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
    return body


def _to_dict(json_dict) -> dict:
    version = json_dict["info"]["version"]
    update_utc = arrow.get(json_dict["releases"][version][0]["upload_time_iso_8601"])
    j = {
        "name": json_dict["info"]["name"],
        "summary": json_dict["info"]["summary"],
        "package_url": json_dict["info"]["package_url"],
        "version": version,
        "update_utc": update_utc.format(),
        "update_jst": update_utc.to("asia/tokyo").format(),
    }
    return j


def get_pypi_stats(li: list, sleep: int = 1):
    res = []
    for package_name in li:
        j = _get_pypi_json(package_name)
        d = _to_dict(j)
        s = f'[{d["name"]}]({d["package_url"]}): {d["summary"]}'
        res.append(s)
        time.sleep(sleep)
    return res


# [remind\-task · PyPI](https://pypi.org/project/remind-task/): 通知を繰り返すCLIアプリケーション。macOS専用
