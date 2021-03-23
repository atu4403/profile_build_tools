import os
import pathlib
from selenium import webdriver
import base64


def update_atcoder_images(
    username: str,
    status_path: str = "images/ratingStatus.png",
    graph_path: str = "images/ratingGraph.png",
    host: str = "localhost",
):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor=f"http://{host}:4444/wd/hub",
        desired_capabilities=options.to_capabilities(),
        options=options,
    )
    driver.get(f"https://atcoder.jp/users/{username}")
    driver.implicitly_wait(30)

    def to_bytes(elid):
        sc = "return arguments[0].toDataURL('image/png').substring(21);"
        el = driver.find_element_by_id(elid)
        b64 = driver.execute_script(sc, el)
        return base64.b64decode(b64)

    STATUS_PATH = pathlib.Path(status_path)
    GRAPH_PATH = pathlib.Path(graph_path)
    os.makedirs(STATUS_PATH.parent, exist_ok=True)
    os.makedirs(GRAPH_PATH.parent, exist_ok=True)
    STATUS_PATH.write_bytes(to_bytes("ratingStatus"))
    GRAPH_PATH.write_bytes(to_bytes("ratingGraph"))
    driver.quit()
