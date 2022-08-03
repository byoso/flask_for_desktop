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


# Here are some callbacks examples =====================================
def callback_function_1(*args):
    print("Some example function")


def callback_function_2(*args):
    print("Another example function")


def open_default(*args):
    """Open the application in the default browser of the system"""
    sgui.open_in_main_browser(port=PORT, home_page=server_launcher.home_page)


# Building the main interface =========================================

# Browser

def new_browser(*args):
    """Creates a browser"""
    browser = sgui.SillyBrowser(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        port=PORT,
        home_page=server_launcher.home_page,
        icon='sgIcon',
        is_main=False,  # closing a main widget closes the entire application
        )
    return browser


# Indicator

def new_indicator():
    indicator = sgui.Indicator(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        icon='sgIcon',  # required
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
