#! /usr/bin/env python3
# -*- coding : utf-8 -*-

"""Simpliest converter file, open the app in a simple GTK window."""


import os

import flask_fd.gui as fgui
import flask_fd.launchers as fgl

from flaskapp import main as flask_app  # use your own names here

# MUST be in your main executable, some paths will be relative to this.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PORT = fgl.free_port()  # gives the first free port starting from default 5001
# =====================================================================


# set the server launcher (here for flask)
def launch_function():
    # Here the Flask.app object is called 'app', change it if needed
    flask_app.app.run(debug=False, port=PORT)


# create the launcher object
server_launcher = fgl.ServerLauncher(
    port=PORT,
    home_page="/",
    launcher=launch_function)


# Building the main interface =========================================

# Browser

def new_browser(*args):
    """Creates a browser"""
    browser = fgui.SillyBrowser(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='FlaskFdIcon',
        is_main=True,  # closing a main widget closes the entire application
        server_launcher=server_launcher
        )
    return browser


new_browser()  # comment to hide the main window on launch
