from os import environ
import json
from profile_build_tools import (
    update_atcoder_images,
    get_pypi_stats,
    get_qiita_stats,
    get_github_stats,
    _to_list,
)
from pprint import pprint


# def test_update_atcoder_images():
#     environ["ATCODER_USERNAME"] = "atu4403"
#     host = "localhost" if environ.get("CI") else "192.168.0.143"
#     update_atcoder_images(host)


def test_to_markdown():
    with open("github_sample.json") as f:
        j = json.load(f)
    res = _to_list(j)
    pprint(res)
    assert 1 == 0


# def test_get_pypi_stats():
#     li = ["env-paths", "timeit2", "remind-task"]
#     res = get_pypi_stats(li)
#     pprint(res)
#     assert 1 == 0


# def test_get_qiita_stats():
#     res = get_qiita_stats("atu4403")
#     pprint(res)
#     assert 1 == 0


# def test_get_github_stats():
#     res = get_github_stats("atu4403")
#     pprint(res)
#     assert 1 == 0
