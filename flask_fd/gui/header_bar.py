
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as wk


class SillyHeaderBar(gtk.HeaderBar):
    def __init__(
        self,
        title="title",
        subtitle=None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.set_show_close_button(True)
        self.set_title(title)
        if subtitle is not None:
            self.set_subtitle(subtitle)
