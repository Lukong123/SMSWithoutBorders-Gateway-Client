import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine


class HomeModemWindow(Gtk.Box):
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

        # container1 main
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box-modem")
        container1.pack_start(center_box, False, False, 0)

        # Horizontal line widget
        line = HorizontalLine()
        container1.pack_start(line, False, False, 0)


        # device label
        device_label = Gtk.Label()
        device_label.set_text("MTN 4.2")
        center_box.pack_start(device_label, False, False, 30)


        # Container 2
        container2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container2.set_vexpand(True)
        container2.set_homogeneous(False)
        container2.set_border_width(10)

        container2.set_valign(Gtk.Align.CENTER)
        container2.set_halign(Gtk.Align.CENTER)

        # grid for usb modem box information
        grid = Gtk.Grid()
        grid.set_column_spacing(80)
        grid.set_name("box-info")
        container2.pack_start(grid, True, True, 0)

        # dummy content
        labels = [
            "Manufacturer:",
            "Model:",
            "Serial Number:",
            "IMEI:",
            "ICCID:",
            "Firmware Version:",
            "Signal Strength:",
            "Connection Status:",
        ]
        values = [
            "Dummy Manufacturer",
            "Dummy Model",
            "Dummy Serial Number",
            "Dummy IMEI",
            "Dummy ICCID",
            "Dummy Firmware Version",
            "Dummy Signal Strength",
            "Dummy Connection Status",
        ]

        # Create column headers
        header_a = Gtk.Label()
        header_a.set_text("Box Info")
        header_a.set_name("box-info-header")
        grid.attach(header_a, 0, 0, 1, 1)

        header_b = Gtk.Label()
        header_b.set_text("Box Info")
        header_b.set_name("box-info-header")
        grid.attach(header_b, 1, 0, 1, 1)


        for i in range(len(labels)):
            label = Gtk.Label()
            label.set_text(labels[i])
            label.set_margin_top(10)
            value = Gtk.Label()

            value.set_text(values[i])

            grid.attach(label, 0, i+1, 1, 1)
            grid. attach(value, 1, i+1, 1, 1)

        container1.pack_start(container2, True, True, 0)

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
        css_path = "gui/utils/styles/styles.css"
        # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def initialize_views(self, stack):
        # send view
        send_view = SendMessageWindow()
        stack.add_named(send_view, "send")

        # incoming
        incoming_view = IncomingMessageWindow()
        stack.add_named(incoming_view, "incoming")

    def send_label_clicked(self, widget, event, stack):
        # print("send label click")
        # send_window = SendMessageWindow()
        # send_window.show_all()
        stack.set_visible_child_name("send")
        
    def outgoing_label_clicked(self, widget, event):
        print("outgoing label click")
        outgoing_window = OutgoingMessageWindow()
        outgoing_window.show_all()

    def message_forwarding_label_clicked(label):
        message_forwarding_window = MessageForwardingWindow()
        message_forwarding_window.show_all()

    def incoming_label_clicked(self, widget, event):
        # incoming_window = IncomingMessageWindow()
        # incoming_window.show_all()
        stack.set_visible_child_name("incoming")

    def failed_label_clicked(label):
        failed_window = FailedMessageWindow()
        failed_window.show_all()

    def export_label_clicked(label):
        export_window = ExportMessageWindow()
        export_window.show_all()

    def encrypted_label_clicked(label):
        encrypted_window = EncryptedMessageWindow()
        encrypted_window.show_all()

    def about_label_clicked(label):
        about_window = AboutWindow()
        about_window.show_all()

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ModemWindow()
    app.run()