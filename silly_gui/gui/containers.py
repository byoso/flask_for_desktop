import os
from threading import Thread


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as wk


main = gtk.main
main_quit = gtk.main_quit


class Window(gtk.Window):
    """gtk.Window doc:
    http://lazka.github.io/pgi-docs/index.html#gtk-3.0/classes/Window.html#gtk.Window
    """
    def __init__(
            self, title="title",
            subtitle="",
            icon='sgIcon',  # png without ".png" extention
            header_bar=True,
            is_main=True,
            show=True,
            base_dir=None,
            *args,
            **kwargs,
            ):

        gtk.Window.__init__(self)
        self.set_size_request(800, 600)
        self.scroll = gtk.ScrolledWindow()
        self.add(self.scroll)
        self.viewport = gtk.Viewport()
        self.scroll.add(self.viewport)
        self.main_box = gtk.VBox()
        self.viewport.add(self.main_box)
        # Header Bar
        if header_bar:
            self.header_bar = gtk.HeaderBar()
            self.header_bar.set_show_close_button(True)
            self.header_bar.set_title(title)
            self.header_bar.set_subtitle(subtitle)
            self.set_titlebar(self.header_bar)
        else:
            self.set_title(title)
        # Icon
        if base_dir:
            self.base_dir = base_dir
            if icon:
                icon_path = os.path.join(self.base_dir, icon)
                self.set_icon_from_file(icon_path)

        # window itself
        if is_main:
            self.connect("delete-event", gtk.main_quit)
        if show:
            self.show_all()


class SillyBrowser(gtk.Window):
    def __init__(
            self,
            port=5000,
            home_page="",
            title="Silly Browser",
            icon='sgIcon',  # png without ".png" extention
            is_main=False,
            server_launcher=None,
            base_dir=None,
            *args, **kwargs
            ):
        super().__init__(*args, **kwargs)
        self.set_size_request(80, 60)
        self.set_default_size(800, 600)
        self.set_title(title)
        scroll = gtk.ScrolledWindow()
        self.add(scroll)
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
        # # Jinja2 settings
        # self.environment = create_environment()
        # Webkit2 settings
        browserholder = wk.WebView()
        browserholder.set_editable(False)
        browserholder.load_uri(
            f"http://localhost:{self.port}{self.home_page}"
            )
        scroll.add(browserholder)
        browserholder.show()
        if is_main:
            self.connect("delete-event", gtk.main_quit)

        if self.server_launcher is not None:
            self.run()

    def run(self):
        Thread(
            target=self.server_launcher.launch,
            daemon=True, name="silly_gui").start()
        gtk.main()
