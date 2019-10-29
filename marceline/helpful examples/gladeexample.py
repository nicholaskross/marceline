import gtk
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("example.glade")

window = builder.get_object("window1")
window.show_all()
