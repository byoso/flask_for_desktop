"""
This module handles the 'plop' command when used to copy an already
existing file (in the package) to the user's cwd.
"""
import os
import shutil

from geninstaller.helpers import set_executable

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def plop_main_flask_1():
    "plop's main_flask_1.py in your cwd"
    file = os.path.join(BASE_DIR, "flask/main_flask_1.py")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_flask_1.py'))
    print(f"main_flask_1.py plopped in {cwd}")


def plop_main_flask_2():
    "plop's main_flask_2.py in your cwd"
    file = os.path.join(BASE_DIR, "flask/main_flask_2.py")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_flask_2.py'))
    print(f"main_flask_2.py plopped in {cwd}")


def plop_main_django_1():
    "plop's main_django_1.py in your cwd"
    file = os.path.join(BASE_DIR, "django/main_django_1.py")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_django_1.py'))
    print(f"main_django_1.py plopped in {cwd}")


def plop_main_django_2():
    "plop's main_django_2.py in your cwd"
    file = os.path.join(BASE_DIR, "django/main_django_2.py")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    set_executable(os.path.join(cwd, 'main_django_2.py'))
    print(f"main_django_2.py plopped in {cwd}")
