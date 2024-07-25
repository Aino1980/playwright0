import os


def get_path(path: str = None):
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if path:
        if "/" in path:
            path = path.split("/")
        elif "\\" in path:
            path = path.split("\\")
        else:
            path = [path]
        return os.path.join(root_path, *path)
    else:
        return root_path
