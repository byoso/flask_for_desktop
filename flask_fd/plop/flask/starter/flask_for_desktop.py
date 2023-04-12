#! /usr/bin/env python3
# -*- coding : utf-8 -*-

"""
FOLLOW THE 3 STEPS BELLOW TO USE THIS SNIPPET
"""

import os

import flask_fd.gui as fgui
import flask_fd.launchers as fgl


# STEP 1: import your flask app object as 'flask_app'
from flaskapp.main import app as flask_app  # use your own names here


# STEP 2: customize the indicator
def new_indicator():
    indicator = fgui.Indicator(
        #################### ONLY FROM HERE ####################
        icon='FlaskFdIcon',  # required
        label='label example',  # str or None
        menu_items=[
            ("open in browser", open_default),
            # ("Function 1", callback_button, ["add any kind of data here"]),  # example
            # ("Function 2", callback_button, {"if you": "whant to"}),  # example
            "_separator",
            # the quit button is already included at the end of the menu
        ],
        ######################## TO THERE ########################
        base_dir=os.path.abspath(os.path.dirname(__file__)),
        # closing the indicator closes the entire application and server:
        is_main=True,
        # set the server launcher in a single main widget, only once:
        server_launcher=server_launcher
    )
    return indicator

# STEP 3: make some callback functions if you want:
def callback_button(*item):
    """Example of callback function"""
    text = f"{item[0].data}"
    print(text)
    os.system(f"notify-send {text}")


# You are done ! Congratulations !


########################################################################
### DO NOT MODIFY THE CODE BELOW (unless you know what you're doing) ###
########################################################################

PORT = fgl.free_port()

# set the server launcher (here for flask)
def launch_function():
    flask_app.run(debug=False, port=PORT)

# create the launcher object
server_launcher = fgl.ServerLauncher(
    port=PORT,
    home_page="/",
    launcher=launch_function)


def open_default(*item):
    """Open the application in the default browser of the system"""
    fgui.open_in_main_browser(port=PORT, home_page="/")


if __name__ == "__main__":
    open_default()
    new_indicator()
