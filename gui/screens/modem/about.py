import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine
from src.api_callbacks import ModemHandler


class AboutWindow(Gtk.Box):
    def __init__(self, modem_properties, modem_name, modem_handler):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)
        # self.modem_handler = ModemHandler()
        self.modem_handler = modem_handler
        self.modem_handler.handle_modem_connected() #work  on ensuring in handles only clicked modem
        self.modem_properties = self.modem_handler.get_modem_properties(modem_name)
        
        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)
        self.pack_start(container1, True, True, 0)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")
        container1.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label") 
        left_box.pack_start(title_label, False, False, 20)

        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 20)


        
        container_property = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        container_property.set_vexpand(True)
        container_property.set_homogeneous(False)
        container_property.set_border_width(10)
        container_property.set_halign(Gtk.Align.CENTER)

        prop1_label = Gtk.Label()
        prop2_label = Gtk.Label()
        prop3_label = Gtk.Label()
        prop4_label = Gtk.Label()
        prop5_label = Gtk.Label()
        prop6_label = Gtk.Label()
        prop7_label = Gtk.Label()
        prop8_label = Gtk.Label()


        for properties in self.modem_properties:
            if "Manufacturer" in properties:
                prop1_label.set_text(f"Manufacturer: {properties['Manufacturer']}")
            if "Model" in properties:
                prop2_label.set_text(f"Model: {properties['Model']}")
            if "Imei" in properties:
                prop3_label.set_text(f"Imei: {properties['Imei']}")
            else:
                prop3_label.set_text(f"Imei: N/A")
            if "OperatorCode" in properties:
                prop4_label.set_text(f"Operator Code: {properties['OperatorCode']}")
            if "OperatorName" in properties:
                prop5_label.set_text(f"Operator Name: {properties['OperatorName']}")
            if "DeviceIdentifier" in properties:
                prop6_label.set_text(f"Device Identifier: {properties['DeviceIdentifier']}")
            if "EquipmentIdentifier" in properties:
                prop7_label.set_text(f"Equipment Identifier: {properties['EquipmentIdentifier']}")
            if "PrimaryPort" in properties:
                prop8_label.set_text(f"Primary Port: {properties['PrimaryPort']}")
            if "OperatorCode" in properties:
                prop8_label.set_text(f"Operator Code: {properties['OperatorCode']}")
            if "OperatorCode" in properties:
                prop8_label.set_text(f"Operator Code: {properties['OperatorCode']}")

        container_property.pack_start(prop1_label, False, False, 10)
        container_property.pack_start(prop2_label, False, False, 10)
        container_property.pack_start(prop3_label, False, False, 10)
        container_property.pack_start(prop4_label, False, False, 10)
        container_property.pack_start(prop5_label, False, False, 10)
        container_property.pack_start(prop6_label, False, False, 10)
        container_property.pack_start(prop7_label, False, False, 10)
        container_property.pack_start(prop8_label, False, False, 10)




        container1.pack_start(container_property, True, True, 0)

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

    def send_label_clicked(self, widget, event):
        print("send label click")
        send_window = SendMessageWindow()
        send_window.show_all()
        
    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ModemWindow()
    app.run()