import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils.widgets.horizontal_line import HorizontalLine


class SendMessageWindow(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)

        # container main
        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_name("center-box-message")
        self.pack_start(container_main, True, True, 0)

        # message label
        message_label = Gtk.Label()
        message_label.set_text("NEW MESSAGE")
        container_main.pack_start(message_label, False, False, 5)

        # Horizontal line widget
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        container_main.pack_start(line, False, False, 0)

        # Text entry for phone number
        number_entry = Gtk.Entry()
        number_entry.set_placeholder_text("Number:")
        container_main.pack_start(number_entry, False, False, 0)

        # compose message
        text_area = Gtk.Entry()
        text_area.set_placeholder_text("Compose message...")
        text_area.set_size_request(600, 400)
        container_main.pack_start(text_area, False, False, 0)

        # Send button with label and logo
        send_button = Gtk.Button()
        send_button.set_margin_top(10)
        send_button.set_label("Send")
        send_button.set_name("send_btn")
        send_button.set_image(Gtk.Image.new_from_icon_name("mail-send", Gtk.IconSize.BUTTON))
        container_main.pack_start(send_button, False, False, 10)

        # Adjusting container size
        screen = Gdk.Screen.get_default()
        self.set_size_request(-1, int(screen.get_height() * 0.55))
