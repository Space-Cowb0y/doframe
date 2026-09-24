import os
import sys


def resource_path(relative_path: str) -> str:
    base_dir = getattr(sys, "_MEIPASS", None)
    if base_dir:
        return os.path.join(base_dir, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
