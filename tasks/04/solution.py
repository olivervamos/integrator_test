import pathlib

import aiviro

FILE_PATH = pathlib.Path("index.html").resolve()


def solution():
    """Implement your solution here"""
    aiviro.init_logging()

    FILE_PATH = "file:///C:/Users/ARTINUSER/Desktop/aiviro/aiviro-integrator-test%20(4)/integrator-test-main/tasks/04/index.html"
    r = aiviro.create_web_robot(headless=True)
    r.go_to_url(FILE_PATH)
    #r.go_to_url(f"file://{FILE_PATH}")
    



if __name__ == "__main__":
    solution()
