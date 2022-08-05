#! /usr/bin/env python3
# -*- coding : utf-8 -*-

"""Customizable converter file, with or without:
- indicator in the system tray
- the main window
- opening the app in the default browser
"""


import os

import flask_fd.gui as fgui
import flask_fd.launchers as fgl

from flaskapp import main as flask_app  # use your own names here

# MUST be in your main executable, some paths will be relative to this.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PORT = fgl.free_port()
# =====================================================================


# set the server launcher (here for flask)
def launch_function():
    flask_app.app.run(debug=False, port=PORT)


# create the launcher object
server_launcher = fgl.ServerLauncher(
    port=PORT,
    home_page="/",
    launcher=launch_function)


# Here are some callbacks examples =====================================
# called from the indicator in the systray
def callback_function_1(*args):
    print("Some example function")


def callback_function_2(*args):
    print("Another example function")


def open_default(*args):
    """Open the application in the default browser of the system"""
    fgui.open_in_main_browser(port=PORT, home_page="/")


# Building the main interface =========================================

# Browser

def new_browser(*args):
    """Creates a browser"""
    browser = fgui.SillyBrowser(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        port=PORT,
        home_page="/",
        icon='FlaskFdIcon',
        is_main=False,  # closing a main widget closes the entire application
        )
    return browser


# Indicator

def new_indicator():
    indicator = fgui.Indicator(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='FlaskFdIcon',  # required
        label='label example',  # str or None
        menu_items=[
            # ("main window", main_window),
            ("open application", new_browser),
            ("open in browser", open_default),
            ("Function 1", callback_function_1),
            ("Function 2", callback_function_2),
            "_separator",
        ],
        # closing a main widget closes the entire application and server:
        is_main=True,
        # set the server launcher in a single main widget, only once:
        server_launcher=server_launcher
    )
    return indicator


open_default()  # uncomment to show the app in the default browser

# new_browser()  # uncomment to show the main window on launch

# create the indicator
# it will also launches the server as we defined the server_launcher
# in it, so, create this widget the last.
new_indicator()
