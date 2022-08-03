#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import os

import silly_gui.gui as sgui
import silly_gui.launchers as sgl

from flaskapp import main as flask  # use your own names here

# MUST be in your main executable, some paths will be relative to this.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PORT = sgl.free_port()  # gives the first free port starting from default 5001
# =====================================================================


# set the server launcher (here for flask)
def launch_function():
    flask.app.run(debug=False, port=PORT)


# create the launcher object
server_launcher = sgl.ServerLauncher(
    port=PORT,
    home_page="/",
    launcher=launch_function)


# Building the main interface =========================================

# Browser

def new_browser(*args):
    """Creates a browser"""
    browser = sgui.SillyBrowser(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='sgIcon',
        is_main=True,  # closing a main widget closes the entire application
        server_launcher=server_launcher
        )
    return browser


new_browser()  # comment to hide the main window on launch
