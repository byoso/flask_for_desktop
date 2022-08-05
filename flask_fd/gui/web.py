
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as wk


class SillyWebView(wk.WebView):
    """wk.WebView doc:
    http://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes/WebView.html"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_editable(False)
