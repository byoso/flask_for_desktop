#! /usr/bin/env python3
# coding: utf-8


import socket


class ServerLauncher:
    def __init__(
            self,
            port=None,
            home_page="",
            launcher=None  # or function
            ):

        self.port = port
        self.home_page = home_page
        self.launcher = launcher

    def launch(self, *args, **kwargs):
        if self.launcher is None:
            self.generic_launcher()
        else:
            self.launch_function = self.launcher
        self.launch_function()

    def generic_launcher(self):
        # TODO: generic server
        pass


def free_port(port=5051):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
    except OSError:
        return free_port(port+1)
    s.close()
    return port
