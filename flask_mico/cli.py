import os
import re
import sys

BASE_DIR = os.path.abspath((os.path.dirname(__file__)))
TEMLLATE_DIR = os.path.join(BASE_DIR, "project_template")
PORJECT_NAME = "project_name"
TEM_ARG = "{{project_name}}"


def create_project():
    if len(sys.argv) < 2:
        print("Missing project name!")
        return
    name = sys.argv[1]
    if not re.match(r"^[a-zA-Z]+[a-zA-Z_]*$", name):
        print("Project name unqualified!")
        return

    pro_path = "./"
    if len(sys.argv) >= 3:
        if not sys.argv[2].startswith("/"):
            pro_path = os.path.join(pro_path, sys.argv[2])
        else:
            pro_path = sys.argv[2]
    # make project templates
    for (root, dirs, files) in os.walk(TEMLLATE_DIR):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        mid_path = root.replace(TEMLLATE_DIR, "")
        mid_path = mid_path.replace(PORJECT_NAME, name).lstrip("/")
        if mid_path:
            path_ = os.path.join(pro_path, mid_path)
        else:
            path_ = pro_path

        for file in files:
            if not file.endswith("-tpl"):
                continue
            if not os.path.exists(path_):
                os.mkdir(path_)
            with open(os.path.join(root, file), "r") as f:
                content = f.read().replace(TEM_ARG, name)
                wirte2file(os.path.join(
                    path_, file.replace("-tpl", "")), content)


def wirte2file(path, content):
    with open(path, "w") as f:
        f.write(content)
