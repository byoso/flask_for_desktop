#! /usr/bin/env python3
# coding: utf-8


import os


def open_in_main_browser(port=5000, home_page="", *args):
    os.system(f"xdg-open http://localhost:{port}/{home_page}")
