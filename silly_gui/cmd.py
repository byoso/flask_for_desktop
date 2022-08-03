#! /usr/bin/env python3
# coding: utf-8

from flamewok.cli import cli

from silly_gui import __version__
from silly_gui.plop.ploppers import (
    plop_main_flask_1,
    plop_main_flask_2,
    plop_main_django_1,
    plop_main_django_2,
)


documentation = """
---   Build your app in a few steps   ---

STRUCTURE
You could have this structure:

root directory of the project/
    |
    |__An installer file for your final app
    |
    |__silly_gui_app/
        |
        |__silly_gui_main.py
        |
        |__flask or django app/


WORKFLOW
1. Make your app with django or flask as you are used to, keep it in a
    repository.

2. Add the required silly_gui_main file with 'plop' (read the help)

3. Create an installer if you want to distribute your application.
You can use 'geninstaller plop installer' or any installer you want,
don't forgot to provide your dependencies.

"""


def tip():
    print(documentation)


def todo():
    print("TODO")


if __name__ == "__main__":

    cli.route(
        "Program: Silly GUI",
        "Make a local applications with the web framework of your choice",
        f"Version: {__version__}",
        "",
        "_"*80,
        "   HELP",
        ("-h", cli.help, "display this help"),
        ("--help", cli.help, "idem"),
        ("", cli.help, "idem"),
        "_"*80,
        "   PLOP - provides a silly_gui_main file in the working directory",
        "* PLOP for FLASK",
        ("plop flask 1", plop_main_flask_1, "single window interface"),
        ("plop flask 2", plop_main_flask_2, "customizable interface"),
        "* PLOP for DJANGO (experimental, you should not trust it)",
        ("plop django 1", plop_main_django_1, "single window interface"),
        ("plop django 2", plop_main_django_2, "customizable interface"),
        "DOCUMENTATION",
        ("tip", tip, "a minute to read a tip, houres saved"),
    )
