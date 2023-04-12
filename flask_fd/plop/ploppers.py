"""
This module handles the 'plop' command when used to copy an already
existing file (in the package) to the user's cwd.
"""
import os
import shutil

from flask_fd.helpers import set_executable

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def _plop_icon(cwd):
    file2 = os.path.join(BASE_DIR, "icon/FlaskFdIcon")
    shutil.copy(file2, cwd)
    print("Generic icon provided too")


def plop_converter():
    cwd = os.getcwd()
    # file
    file = os.path.join(BASE_DIR, "flask/flask_for_desktop.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'flask_for_desktop.py'))
    print(f"flask_for_desktop.py and an icon just plopped in {cwd} :)")
    # icon
    _plop_icon(cwd)


def plop_starter():
    cwd = os.getcwd()
    # file
    file = os.path.join(BASE_DIR, "flask/flask_for_desktop.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'flask_for_desktop.py'))
    # icon
    _plop_icon(cwd)
    # flask project
