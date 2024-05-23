import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine
from src.api_callbacks import ModemHandler


class HomeModemWindow(Gtk.Box):
    def __init__(self, modem_properties, modem_name ):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)
        self.modem_handler = ModemHandler()
        self.modem_handler.handle_modem_connected() #work  on ensuring in handles only clicked modem
        self.modem_properties = self.modem_handler.get_modem_properties(modem_name)
       
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

        for properties in self.modem_properties:
            prop_list = []
            if "Manufacturer" in properties:
                # devi.set_text(f"Manufacturer: {properties['Manufacturer']}")
                manufac = properties['Manufacturer']
                prop_list.append(manufac)
            if "Model" in properties:
                model = properties['Model']
                prop_list.append(model)
            if "PrimaryPort" in properties:
                model = properties['PrimaryPort']
                prop_list.append(model)
            
        device_label = Gtk.Label()
        device_label.set_text(f"{prop_list[0]} {prop_list[1]} {prop_list[2]}")
        center_box.pack_start(device_label, False, False, 30)

        for properties in self.modem_properties:
            prop_list = []
            if "Manufacturer" in properties:
                # devi.set_text(f"Manufacturer: {properties['Manufacturer']}")
                manufac = properties['Manufacturer']
                prop_list.append(manufac)
            if "Model" in properties:
                # prop2_label.set_text(f"Model: {properties['Model']}")
                manufac = properties['Model']


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

        
        container_property = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container_property.set_vexpand(True)
        container_property.set_homogeneous(False)
        container_property.set_border_width(10)
        container_property.set_valign(Gtk.Align.CENTER)
        container_property.set_halign(Gtk.Align.CENTER)

        # property_mapping = {
        #     "Manufacturer": "Manufacturer",
        #     "Model": "Model",
        # }

        # property_labels = {
        #     property_name: Gtk.Label() for property_name in property_mapping
        # }

        # property_labels = {}
        # for property_name in property_mapping:
        #     label = Gtk.Label()
        #     property_labels[property_name] = label
        #     container_property.pack_start(label, False, False, 10)
        # print(f"property labels {property_labels}")
        # # print(f"property name {property_name}")


        # for properties in self.modem_properties:
        #     for property_name, label in property_labels.items():
        #         if property_mapping[property_name] in properties:
        #             value = properties[property_mapping[property_name]]
        #             label.set_text(f"{property_name}: {value}")
        #             break
        #     else:
        #         label.set_text(f"{property_name}: N/A")
        # for label in property_labels.values():
        #     container_property.pack_start(label, False, False, 12)

        # prop1_label = Gtk.Label()
        # prop2_label = Gtk.Label()



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


            # if "Imei" in properties
        # prop1_label.set_text(f"Manufacturer: {self.modem_properties['Manufacturer']}")
        # prop2_label.set_text(f"Model: {self.modem_properties['Model'] for properties in self.modem_properties}")

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
    
    def listing_properties(self):
        pass

    def update_modem_list(self):
        print("Updating modem labels...")
        # modem = ModemHandler()
        self.modem_handler.handle_modem_connected()
        modem_names = self.modem_handler.get_modem_names()
        print("Updating device labels after callback...")
        print("Modem list length:", len(modem_names))

        modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container2 = self.modem_label.get_parent().get_parent()
        # container2.remove(self.modem_label)
        container2.pack_start(modem_container, False, False, 0)

        for modem_name in modem_names:
            modem_label = Gtk.Label()
            modem_label.set_text(modem_name)
            modem_label.set_name("modem_label")
            print(f"-{modem_name}")

            event_box = Gtk.EventBox()
            # event_box.connect("button-press-event", self.on_modem_click(event, modem_name))
            event_box.connect("button-press-event", lambda widget, event, name=modem_name: self.on_modem_click(widget, event, name))
            event_box.add(modem_label)  # Add the modem label to the event box
            modem_container.pack_start(event_box, False, False, 0)

            modem_container.pack_start(modem_label, False, False, 0)

        # Call show_all on the container2 to ensure all labels are displayed
        container2.show_all()



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