import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from utils.widgets.horizontal_line import HorizontalLine


class IncomingMessageWindow(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)


        
        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)
        self.pack_start(container1, True, True, 0)

        # message content

        row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row1.set_size_request(-1, 50)
        row1.set_homogeneous(False)
        # row1.set_border_width(10)
        row1.set_name("nav-bar")
        container1.pack_start(row1, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box_row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box_row1.set_homogeneous(True)
        row1.pack_start(left_box_row1, False, False, 0)


        # Create a box for the right side of the navigation bar
        right_box_row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box_row1.set_homogeneous(True)
        row1.pack_end(right_box_row1, False, False, 20)

        # Icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box_row1.pack_end(nav_icon, False, False, 0)


        # container1 main
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box-sms")
        container1.pack_start(center_box, False, False, 0)


        # device label
        device_label = Gtk.Label()
        device_label.set_text("MTN 4.2")
        center_box.pack_start(device_label, False, False, 30)

        # floating action button
        fab_button = Gtk.Button()
        fab_button.set_tooltip_text("Compose")
        fab_button.get_style_context().add_class("fab-button")

        message_icon = Gtk.Image.new_from_icon_name("mail-send-symbolic", Gtk.IconSize.BUTTON)
        fab_button.add(message_icon)
        fab_button.set_size_request(50, 50)
        alignment = Gtk.Alignment.new(1, 0.8, 0, 0)
        alignment.set_padding(0, 50, 0, 50) 
        alignment.add(fab_button)
        container1.pack_end(alignment, False, False, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "utils/styles/styles.css"
        # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def send_label_clicked(self, widget, event):
        print("send label click")
        send_window = SendMessageWindow()
        send_window.show_all()
        
    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ModemWindow()
    app.run()