
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as wk

from flask_fd.gui.header_bar import SillyHeaderBar
from flask_fd.gui.containers import SillyBrowser, SillyWebView


def get_params(value, params):
    if value in params and params[value]:
        return True
    return False


def _build_buttons(header_bar, params):
    header_bar.buttons_left = []
    for name in params['buttons_left']:
        button = gtk.Button()
        button.name = name
        if name == 'hb_home':
            btn_home_image = gtk.Image.new_from_icon_name("go-home", gtk.IconSize(5))

        if name == 'hb_refresh':
            btn_home_image = gtk.Image.new_from_icon_name("view-refresh", gtk.IconSize(5))

        if name == 'hb_previous':
            btn_home_image = gtk.Image.new_from_icon_name("go-previous", gtk.IconSize(5))

        if name == 'hb_next':
            btn_home_image = gtk.Image.new_from_icon_name("go-next", gtk.IconSize(5))

        if name == 'hb_find':
            btn_home_image = gtk.Image.new_from_icon_name("edit-find", gtk.IconSize(5))
        button.add(btn_home_image)
        header_bar.pack_start(button)
        header_bar.buttons_left.append(button)
    header_bar.buttons_right = []
    for name in params['buttons_right']:
        button = gtk.Button()
        button.name = name
        if name == 'hb_home':
            btn_home_image = gtk.Image.new_from_icon_name("go-home", gtk.IconSize(5))

        if name == 'hb_refresh':
            btn_home_image = gtk.Image.new_from_icon_name("view-refresh", gtk.IconSize(5))

        if name == 'hb_previous':
            btn_home_image = gtk.Image.new_from_icon_name("go-previous", gtk.IconSize(5))

        if name == 'hb_next':
            btn_home_image = gtk.Image.new_from_icon_name("go-next", gtk.IconSize(5))

        if name == 'hb_find':
            btn_home_image = gtk.Image.new_from_icon_name("edit-find", gtk.IconSize(5))
        button.add(btn_home_image)
        header_bar.pack_end(button)
        header_bar.buttons_right.append(button)


def window_builder(*args, **params):
    if not get_params('header_bar', params):
        header_bar = None
    else:
        header_bar = SillyHeaderBar(
            title=params['title'],
            subtitle=params['subtitle'],
        )
        _build_buttons(header_bar, params)

    window = SillyBrowser(
        port=params["port"],
        home_page=params["home_page"],
        title=params["title"],
        header_bar=header_bar,
        subtitle=params["subtitle"],
        icon=params["icon"],  # png without ".png" extention
        is_main=params["is_main"],
        server_launcher=params["server_launcher"],
        base_dir=params["base_dir"],
    )

    return window
