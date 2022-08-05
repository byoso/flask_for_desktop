import os
from threading import Thread


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
gi.require_version('WebKit2', '4.0')

from flask_fd.gui.web import SillyWebView
from flask_fd.gui.header_bar import SillyHeaderBar


main = gtk.main
main_quit = gtk.main_quit


class SillyBrowser(gtk.Window):
    """gtk.Window doc:
    http://lazka.github.io/pgi-docs/index.html#gtk-3.0/classes/Window.html#gtk.Window
    """
    def __init__(
            self,
            port=5051,
            home_page="",
            title="Flask for desktop",
            header_bar=None,
            subtitle="Your app's window",
            icon='FlaskFdIcon',  # png without ".png" extention
            is_main=False,
            server_launcher=None,
            base_dir=None,
            *args, **kwargs
            ):
        super().__init__(*args, **kwargs)
        self.is_main = is_main
        self.set_size_request(80, 60)
        self.set_default_size(800, 600)
        self.scroll = gtk.ScrolledWindow()
        self.viewport = gtk.Viewport()
        self.viewport.add(self.scroll)
        self.add(self.viewport)
        # Header Bar
        if header_bar is not None:
            self.header_bar = header_bar
            for button in [
                    *self.header_bar.buttons_left,
                    *self.header_bar.buttons_right,
                    ]:
                if button.name == "hb_home":
                    button.connect("clicked", self._home)
                if button.name == "hb_refresh":
                    button.connect("clicked", self._refresh)
                if button.name == "hb_previous":
                    button.connect("clicked", self._previous)
                if button.name == "hb_next":
                    button.connect("clicked", self._next)
                if button.name == "hb_find":
                    button.connect("clicked", self._find)
            self.set_titlebar(self.header_bar)
        else:
            self.set_title(title)
        self.connect("button-press-event", self._on_button_press_event)
        self.show_all()
        self.home_page = home_page
        self.server_launcher = server_launcher
        if self.server_launcher is not None:
            self.port = self.server_launcher.port
        else:
            self.port = port
        # Icon
        if base_dir:
            self.base_dir = base_dir
            if icon:
                icon_path = os.path.join(self.base_dir, icon)
                self.set_icon_from_file(icon_path)
        # Webkit2 settings
        self.web_view = SillyWebView()
        self._home()
        self.web_view.load_uri(
            f"http://localhost:{self.port}{self.home_page}"
            )
        self.scroll.add(self.web_view)
        self.web_view.connect("close", self._close)  # if closed from JS
        self.web_view.connect("button-press-event", self._on_button_press_event)
        self.web_view.show()
        if is_main:
            self.connect("delete-event", gtk.main_quit)

        if self.server_launcher is not None:
            self._run()

    def _run(self):
        Thread(
            target=self.server_launcher.launch,
            daemon=True, name="silly_gui").start()
        gtk.main()

    def _home(self, *args):
        self.web_view.load_uri(
            f"http://localhost:{self.port}{self.home_page}"
            )

    def _refresh(self, *args):
        uri = self.web_view.get_uri()
        self.web_view.load_uri(uri)

    def _previous(self, *args):
        self.web_view.go_back()

    def _next(self, *args):
        self.web_view.go_forward()

    def _find(self, *args):
        print("find")
        self.web_view.get_inspector()

    def _on_button_press_event(self, widget, event):
        if event.button == 8:
            self._previous()
            return True
        if event.button == 9:
            self._next()
            return True

    def _close(self):
        self.destroy()
