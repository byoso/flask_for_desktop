import sys


HELP = (
    """
========================= Silly GUI ==================================
silly_gui is based on PyGobject.
It is basically a collection of pre-set and pre-built Gtk objects.

The purpose is to build interfaces faster and easyer. You can still
adjust precisely your settings and mix silly_gui with PyGobject.
Most silly_gui objects are heriting from the Gtk object of the same name.
ex: silly_gui.Window is heriting from Gtk.Window

usefull PyGobject api documentation here:
http://lazka.github.io/pgi-docs/index.html#Gtk-3.0

OPTIONS:
python3 -m silly_gui [option]

options are:
    '', '-h', '--help' : displays this help
    'plop' : provides the plop starter kit in your working directory (see help(silly_gui.plop))


    """
)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(HELP)
    if len(sys.argv) > 1:
        if sys.argv[1] in ('--help', '-h'):
            print(HELP)
        if sys.argv[1] == 'plop':
            print('TODO')
