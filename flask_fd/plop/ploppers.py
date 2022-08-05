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


def plop_main_flask_1():
    cwd = os.getcwd()
    # file
    "plop's main_flask_1.py in your cwd"
    file = os.path.join(BASE_DIR, "flask/main_flask_fd_1.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_flask_fd_1.py'))
    print(f"main_flask_1.py plopped in {cwd}")
    # icon
    _plop_icon(cwd)


def plop_main_flask_2():
    cwd = os.getcwd()
    # file
    "plop's main_flask_2.py in your cwd"
    file = os.path.join(BASE_DIR, "flask/main_flask_fd_2.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_flask_fd_2.py'))
    print(f"main_flask_2.py plopped in {cwd}")
    # icon
    _plop_icon(cwd)


def plop_main_flask_3():
    cwd = os.getcwd()
    # file
    "plop's main_flask_3.py in your cwd"
    file = os.path.join(BASE_DIR, "flask/main_flask_fd_3.py")
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_flask_fd_3.py'))
    print(f"main_flask_3.py plopped in {cwd}")
    # icon
    _plop_icon(cwd)


def plop_installer():
    "plop's main_flask_2.py in your cwd"
    file = os.path.join(BASE_DIR, "installer/installer")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'installer'))
    print(f"installer plopped in {cwd}")
