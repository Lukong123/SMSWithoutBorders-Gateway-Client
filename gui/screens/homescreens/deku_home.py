import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ModemWindow(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_border_width(10)
        self.set_homogeneous(False)

        # Add your content for the ModemWindow here


class DekuHomeWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Home Window")

        self.set_border_width(10)
        self.set_default_size(400, 300)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        deku_home_label = Gtk.Label("Deku Home")
        self.notebook.append_page(Gtk.Label("Content for Deku Home"), deku_home_label)

        modem_container_label = Gtk.Label("Modem Container")
        event_box = Gtk.EventBox()
        event_box.connect("button-press-event", self.on_modem_1_click)
        event_box.add(Gtk.Label("Modem MTN 4.2"))
        self.notebook.append_page(event_box, modem_container_label)

        modem_2_label = Gtk.Label("Modem Orange 33")
        self.notebook.append_page(Gtk.Label("Content for Modem Orange 33"), modem_2_label)

        self.modem_window = ModemWindow()

    def on_modem_1_click(self, widget, event):
        print("Modem 1 clicked!")
        current_page = self.notebook.get_current_page()
        if current_page == 1:
            self.notebook.set_current_page(-1)  # Switch to the last page
            self.notebook.remove_page(-1)  # Remove the last page if it exists

            self.notebook.append_page(self.modem_window, Gtk.Label("Modem MTN 4.2"))
            self.modem_window.show_all()


win = DekuHomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()