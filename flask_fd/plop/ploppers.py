"""
This module handles the 'plop' command when used to copy an already
existing file (in the package) to the user's cwd.
"""
import os
import shutil

from flask_fd.helpers import set_executable

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def _plop_icon(cwd):
    file = os.path.join(BASE_DIR, "flask/starter/flaskapp/app/static/img/FlaskFdIcon")
    shutil.copy(file, cwd)
    print("Generic icon provided too")


def plop_converter():
    print("Flask-fd converter file ploped !")
    cwd = os.getcwd()
    # file
    file = os.path.join(BASE_DIR, "flask/starter/flask_for_desktop.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'flask_for_desktop.py'))
    print(f"flask_for_desktop.py and an icon just plopped in {cwd} :)")
    # icon
    _plop_icon(cwd)


def plop_starter():
    cwd = os.getcwd()
    # copy starter folders
    folder = os.path.join(BASE_DIR, "flask/starter")
    if os.path.exists(os.path.join(cwd, "flask_fd_app")):
        print("Aborted: flask_fd_app already exists in the current directory")
    else:
        shutil.copytree(folder, os.path.join(cwd, "flask_fd_app"))
        set_executable(os.path.join(cwd, 'flask_fd_app/flask_for_desktop.py'))
        print("Flask-fd starter kit ploped !")
