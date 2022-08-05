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


# =====================================================================
# MUST be in your main executable, some paths will be relative to this.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PORT = fgl.free_port()

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
def callback_button(*item):
    text = f"{item[0].data}"
    print(text)
    os.system(f"notify-send {text}")


def open_default(*item):
    """Open the application in the default browser of the system"""
    fgui.open_in_main_browser(port=PORT, home_page="/")


# Building the main interface =========================================

# Main Window
def new_window(*item):
    params = {
        # Minimum settings
        'title': "My new app",
        'base_dir': BASE_DIR,  # do not change this
        'port': PORT,  # do not change this
        'server_launcher': None,  # None or server_launcher
        'home_page': "/",
        'icon': 'FlaskFdIcon',
        'is_main': False,  # closing the window closes the entire application
        # If the window has a header bar:
        'header_bar': True,
        'subtitle': "Your flask app's window",
        'buttons_left': [
            # comment those you don't want, change the order as you like
            'hb_home',
            'hb_refresh',
        ],
        'buttons_right': [
            'hb_next',
            'hb_previous',
        ]
    }

    return fgui.window_builder(**params)


# Indicator

def new_indicator():
    indicator = fgui.Indicator(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='FlaskFdIcon',  # required
        label='label example',  # str or None
        menu_items=[
            ("open application", new_window),
            ("open in browser", open_default),
            ("Function 1", callback_button, ["add any kind of data here"]),
            ("Function 2", callback_button, {"if you": "whant to"}),
            "_separator",
        ],
        # closing the indicator closes the entire application and server:
        is_main=True,
        # set the server launcher in a single main widget, only once:
        server_launcher=server_launcher
    )
    return indicator


new_window()

# create the indicator
# it will also launches the server as we defined the server_launcher
# in it, so, create this widget the last.
new_indicator()
