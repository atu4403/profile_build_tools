import os
from profile_build_tools import (
    get_pypi_stats,
    get_qiita_stats,
    get_github_stats,
    update_atcoder_images,
)
from pathlib import Path
from string import Template

PYPI_LIST = ["env-paths", "timeit2", "remind-task"]
QIITA_USER = "atu4403"
GITHUB_USER = "atu4403"
ATCODER_USER = "atu4403"
TEMPLATE = Path("test/README.tpl.md").read_text()
OUTPATH = Path("test/README.md")
# pypi
pypi_list = ""
for st in get_pypi_stats(PYPI_LIST):
    pypi_list += f"- {st}\n"

# qiita
qiita_list = ""
for st in get_qiita_stats(QIITA_USER):
    qiita_list += f"- {st}\n"

# github
github_list = ""
for st in get_github_stats(GITHUB_USER):
    github_list += f"- {st}\n"

out_text = Template(TEMPLATE).substitute(
    PYPI_CONTENTS=pypi_list, QIITA_CONTENTS=qiita_list, GITHUB_CONTENTS=github_list
)
OUTPATH.write_text(out_text)

# AtCoder images
host = "localhost" if os.environ.get("CI") else "192.168.0.143"
update_atcoder_images(ATCODER_USER, host=host)
