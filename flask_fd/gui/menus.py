import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def create_menu_item(arg):
    """
    arg can be str (anything or '_separator'),
    or a tuple (label, callback_function)
    """
    if isinstance(arg, tuple):
        # tuple expected to be (label, callback)
        item = Gtk.MenuItem(arg[0])
        item.connect('activate', arg[1])
    else:
        if arg == '_separator':
            item = Gtk.SeparatorMenuItem()
        else:
            item = Gtk.MenuItem(arg)

    return item
