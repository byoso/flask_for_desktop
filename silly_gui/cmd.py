#! /usr/bin/env python3
# coding: utf-8

from flamewok.cli import cli
from silly_gui import __version__

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
        "HELP",
        ("-h", cli.help, "display this help"),
        ("--help", cli.help, "idem"),
        ("", cli.help, "idem"),
        "PLOP (provides a local silly_gui_main file)",
        ("plop flask", todo, "get the file for flask"),
        ("plop flask mini", todo, "get the minimal file for flask"),
        ("plop django", todo, "get the file for django"),
        ("plop django mini", todo, "get the minimal file for django"),
        "DOCUMENTATION",
        ("tip", tip, "a minute to read a tip, houres saved"),

    )
