#! /usr/bin/env python3
# coding: utf-8

from flamewok.cli import cli

from flask_fd import __version__
from flask_fd.plop.ploppers import (
    plop_converter,
    plop_starter
)


documentation = """
---   Build your app in a few steps   ---

STRUCTURE
You could have this structure:

root directory of the project/
    |
    |__installer (file for your final app, optionnal)
    |
    |__flask_fd_app/
        |
        |__flask_for_desktop.py
        |
        |__flaskapp/
                |
                |__main.py



WORKFLOW
1. Make your app with flask as you are used to, keep it in a
    repository.

2. Add the required flask_main file with 'plop' (read the help)

3. Create an installer (for any linux distro)
    if you want your application to be installable
    The provided installer file uses geninstaller

"""


def tip():
    print(documentation)


def todo():
    print("TODO")


def cmd():
    cli.route(
        "Program: Flask for desktop",
        "Make a local gui with the web framework flask",
        f"Version: {__version__}",
        "",
        "_"*80,
        "   HELP",
        ("-h", cli.help, "display this help"),
        ("--help", cli.help, "idem"),
        ("", cli.help, "idem"),
        "_"*80,
        "   PLOP - provides a file in the working directory",
        ("plop converter", plop_converter, "get the files to convert an existing app"),
        ("plop starter", plop_starter, "Start an app from scratch"),
        "DOCUMENTATION",
        ("tip", tip, "a minute to read a tip, houres saved"),
    )


if __name__ == "__main__":
    cmd()
