#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import os

import silly_gui.gui as sgui
import silly_gui.launchers as sgl


# MUST be in your main executable, some paths will be relative to this.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# PORT = sgl.free_port(5050)  # bug: doesn't work with django, why ?
PORT = 5051
# =====================================================================
# !!!! SET YOUR OWN PATH HERE !!!!
# setting a virtual environment is prudent, but could work without
env_path = os.path.join(BASE_DIR, "env/bin/activate")
launch_command = f"""
source {env_path}
./djangoapp/manage.py runserver {PORT}
"""


# set the server launcher (here for django)
def launch_function():
    os.system(launch_command)


# create the launcher object
server_launcher = sgl.ServerLauncher(
    port=PORT,
    home_page="",
    launcher=launch_function)


# Building the main interface =========================================

# Browser

def new_browser(*args):
    """Creates a browser"""
    browser = sgui.SillyBrowser(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='sgIcon',
        is_main=True,  # closing a main widget closes the entire application
        server_launcher=server_launcher,
        )
    return browser


new_browser()  # comment to hide the main window on launch
