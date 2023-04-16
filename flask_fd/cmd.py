#! /usr/bin/env python3
# coding: utf-8

from flamewok.cli import cli

from flask_fd import __version__
from flask_fd.plop.ploppers import (
    plop_converter,
    plop_starter
)



def cmd():
    cli.route(
        "Program: Flask for desktop",
        "Build a local desktop gui with the web framework flask",
        f"Version: {__version__}",
        "",
        "_"*80,
        "   HELP",
        (["", "-h", "--help"], cli.help, "display this help"),
        "_"*80,
        "   PLOP - provides a file in the working directory",
        ("plop converter", plop_converter, "get the files to convert an existing app"),
        ("plop starter", plop_starter, "Start an app from scratch"),
    )


if __name__ == "__main__":
    cmd()
