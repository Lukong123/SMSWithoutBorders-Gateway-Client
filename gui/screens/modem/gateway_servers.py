import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

import subprocess
import os

from gui.utils.widgets.horizontal_line import HorizontalLine
from gui.screens.modem.send_message import SendMessageWindow


class GateWayServersWindow(Gtk.Box):
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


        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
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

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)


        image_file = "../../utils/icons/elipsis-vertical.svg"
        image_path = self.get_resource_path(image_file)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=image_path,
            width=15,
            height=15,
            preserve_aspect_ratio=True
        )
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        image_event_box = Gtk.EventBox()
        image_event_box.add(image)
        right_box.pack_end(image_event_box, False, False, 20)



        menu = Gtk.Menu()
        https = Gtk.MenuItem(label="Add HTTPS Gateway server")
        smtp = Gtk.MenuItem(label="Add SMTP Gateway server")
        ftp = Gtk.MenuItem(label="Add FTP Gateway server")

        menu.append(https)
        menu.append(smtp)
        menu.append(ftp)

        menu.show_all()

        def on_menu_item_clicked(widget, label):
            print(f"{label} clicked")

        # Connect items to callback with a label
        https.connect("activate", self.on_https_clicked)
        smtp.connect("activate", self.on_smtp_clicked)
        ftp.connect("activate", self.on_ftp_clicked)



        # Connect the click event on the image to show the menu
        def on_image_clicked(widget, event):
            if event.button == 1:  # Left-click
                menu.popup(None, None, None, None, event.button, event.time)

        image_event_box.connect("button-press-event", on_image_clicked)
        

        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        screen = Gdk.Screen.get_default()
        width_get = screen.get_width()
        container_main.set_size_request(int(width_get * 0.4), -1)
        # container_main.set_size_request(500, -1)
        
        container_main.set_margin_top(300)
        container1.pack_start(container_main, False, False, 0)

        center_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 60)
        center_container.set_halign(Gtk.Align.CENTER)
        container_main.pack_start(center_container, False, False, 0)

        message_label = Gtk.Label()
        message_label.set_text("No Gateway Server Added!")
        message_label.set_name("message-label-fwd")
        center_container.pack_start(message_label, False, False, 20)


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

        fab_button.connect("clicked", self.on_fab_button_clicked)


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


    def get_resource_path(self, rel_path):
        dir_of_py_file = os.path.dirname(__file__)
        rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
        abs_path_to_resource = os.path.abspath(rel_path_to_resource)
        return abs_path_to_resource

    def send_label_clicked(self, widget, event):
        print("send label click")
        send_window = SendMessageWindow()
        send_window.show_all()

    def on_fab_button_clicked(self, button):
        # Switch to the "send" view in the stack
        print("recognize click on fab button")
       
        modem_window = self.get_toplevel()
        stack = modem_window.get_children()[0].get_children()[1] 
        stack.set_visible_child_name("send")


        
    def run(self):
        Gtk.main()



    def on_https_clicked(self, widget):
        http_dialog = HttpsPopUp(self)

        response = http_dialog.run()

        # Check the response from the dialog
        if response == Gtk.ResponseType.OK:
            url = http_dialog.url_entry.get_text()
            identifier_entry = http_dialog.optional_identifier_entry.get_text()
            # save_data = login_dialog.save_data_checkbox.get_active()

            # Handle login logic here, for example, print the information
            print(f"urle: {url}")
            print(f"identifer : {identifier_entry}")

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        # Destroy the dialog after use
        http_dialog.destroy()


          
    def on_smtp_clicked(self, widget):
        dialog = SmtpPopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("ok button clikc")
        elif response == Gtk.ResponseType.CANCEL:
            print("cancel button clikc")

        dialog.destroy()
    
    def on_ftp_clicked(self, widget):
        dialog = FtpPopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("ok button clikc")
        elif response == Gtk.ResponseType.CANCEL:
            print("cancel button clikc")

        dialog.destroy()
      
    
class HttpsPopUp(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add HTTPS Gateway Server", parent=None, flags=Gtk.DialogFlags.MODAL)

        self.add_button("Add", Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

        self.set_default_size(500, 400)
        self.set_border_width(30)

        # Create the main box for the dialog
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        url_label = Gtk.Label("URL")
        url_label.set_xalign(0)
        box.pack_start(url_label, True, True, 5)

        self.url_entry = Gtk.Entry()
        self.url_entry.set_placeholder_text("Enter URL - e.g. https://example.com")
        box.pack_start(self.url_entry, True, True, 0)

        optional_identifier_label = Gtk.Label("Identifier Tag")
        optional_identifier_label.set_xalign(0)
        box.pack_start(optional_identifier_label, True, True, 5)

        self.optional_identifier_entry = Gtk.Entry()
        self.optional_identifier_entry.set_placeholder_text("(Optional) Identifier Tag")
        box.pack_start(self.optional_identifier_entry, True, True, 0)

        # Message about saving data
        label_body = Gtk.Label("Route incoming messages of format")
        box.pack_start(label_body, True, True, 10)

        # Checkboxes for saving data
        self.save_data_checkbox = Gtk.CheckButton(label="All (default)")
        self.save_data_checkbox.set_active(True)  # Ticked by default
        self.dont_save_data_checkbox = Gtk.CheckButton(label="Base64")
        self.dont_save_data_checkbox.set_active(False)  # Unticked by default

        # Create a box for checkboxes
        checkbox_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        checkbox_box.pack_start(self.save_data_checkbox, True, True, 0)
        checkbox_box.pack_start(self.dont_save_data_checkbox, True, True, 0)

        # Add checkboxes box to the main box
        box.pack_start(checkbox_box, True, True, 10)

        # Add the main box to the content area
        area = self.get_content_area()
        action_area = self.get_action_area()
        action_area.set_layout(Gtk.ButtonBoxStyle.CENTER)
        area.add(box)

        # Show all widgets
        self.show_all()


class SmtpPopUp(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add SMTP Gateway Server", parent=None, flags=Gtk.DialogFlags.MODAL)

        self.add_button("Add", Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

        self.set_default_size(500, 400)
        self.set_border_width(30)

        # Create the main box for the dialog
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        host_label = Gtk.Label("Host")
        host_label.set_xalign(0)
        box.pack_start(host_label, True, True, 5)

        self.host_entry = Gtk.Entry()
        self.host_entry.set_placeholder_text("Host")
        box.pack_start(self.host_entry, True, True, 0)

        username_label = Gtk.Label("Username")
        username_label.set_xalign(0)
        box.pack_start(username_label, True, True, 5)

        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Username")
        box.pack_start(self.username_entry, True, True, 0)

        password_label = Gtk.Label("Password")
        password_label.set_xalign(0)
        box.pack_start(password_label, True, True, 5)

        self.password_entry = Gtk.Entry()
        self.password_entry.set_placeholder_text("Enter your password")
        self.password_entry.set_visibility(False)  # Password hidden by default
        box.pack_start(self.password_entry, True, True, 0)

        port_label = Gtk.Label("Port")
        port_label.set_xalign(0)
        box.pack_start(port_label, True, True, 5)

        self.port_entry = Gtk.Entry()
        self.port_entry.set_placeholder_text("587")
        box.pack_start(self.port_entry, True, True, 0)

        from_label = Gtk.Label("From...")
        from_label.set_xalign(0)
        box.pack_start(from_label, True, True, 5)

        self.from_entry = Gtk.Entry()
        self.from_entry.set_placeholder_text("From")
        box.pack_start(self.from_entry, True, True, 0)

        recepient_label = Gtk.Label("Receipient")
        recepient_label.set_xalign(0)
        box.pack_start(recepient_label, True, True, 5)

        self.recepient_entry = Gtk.Entry()
        self.recepient_entry.set_placeholder_text("Recepient")
        box.pack_start(self.recepient_entry, True, True, 0)

        label_info = Gtk.Label("Use commas for multiple recipients e.g\n"
                               "example@email.com, example1@email.com")
        box.pack_start(label_info, True, True, 10)
    

        subject_label = Gtk.Label("Subject")
        subject_label.set_xalign(0)
        box.pack_start(subject_label, True, True, 5)

        self.subject_entry = Gtk.Entry()
        self.subject_entry.set_placeholder_text("(Optional) Subject")
        box.pack_start(self.subject_entry, True, True, 0)

        label_body = Gtk.Label("Route incoming messages of format")
        box.pack_start(label_body, True, True, 10)
    

        # Checkboxes for saving data
        self.save_data_checkbox = Gtk.CheckButton(label="All (default)")
        self.save_data_checkbox.set_active(True)  # Ticked by default
        self.dont_save_data_checkbox = Gtk.CheckButton(label="Base64")
        self.dont_save_data_checkbox.set_active(False)  # Unticked by default

        # Create a box for checkboxes
        checkbox_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        checkbox_box.pack_start(self.save_data_checkbox, True, True, 0)
        checkbox_box.pack_start(self.dont_save_data_checkbox, True, True, 0)

        # Add checkboxes box to the main box
        box.pack_start(checkbox_box, True, True, 10)
        space_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.pack_start(space_box, True, True, 10)


        # Add the main box to the content area
        area = self.get_content_area()
        action_area = self.get_action_area()
        action_area.set_layout(Gtk.ButtonBoxStyle.CENTER)
        area.add(box)

        # Show all widgets
        self.show_all()


class FtpPopUp(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add FTP Gateway Server", parent=None, flags=Gtk.DialogFlags.MODAL)

        self.add_button("Add", Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

        self.set_default_size(500, 400)
        self.set_border_width(30)

        # Create the main box for the dialog
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        host_label = Gtk.Label("Host")
        host_label.set_xalign(0)
        box.pack_start(host_label, True, True, 5)

        self.host_entry = Gtk.Entry()
        self.host_entry.set_placeholder_text("Host")
        box.pack_start(self.host_entry, True, True, 0)

        username_label = Gtk.Label("Username")
        username_label.set_xalign(0)
        box.pack_start(username_label, True, True, 5)

        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Username")
        box.pack_start(self.username_entry, True, True, 0)

        password_label = Gtk.Label("Password")
        password_label.set_xalign(0)
        box.pack_start(password_label, True, True, 5)

        self.password_entry = Gtk.Entry()
        self.password_entry.set_placeholder_text("Enter your password")
        self.password_entry.set_visibility(False)  # Password hidden by default
        box.pack_start(self.password_entry, True, True, 0)

        # Message about saving data
        label_body = Gtk.Label("Route incoming messages of format")
        box.pack_start(label_body, True, True, 10)

        # Checkboxes for saving data
        self.save_data_checkbox = Gtk.CheckButton(label="All (default)")
        self.save_data_checkbox.set_active(True)  # Ticked by default
        self.dont_save_data_checkbox = Gtk.CheckButton(label="Base64")
        self.dont_save_data_checkbox.set_active(False)  # Unticked by default

        # Create a box for checkboxes
        checkbox_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        checkbox_box.pack_start(self.save_data_checkbox, True, True, 0)
        checkbox_box.pack_start(self.dont_save_data_checkbox, True, True, 0)

        # Add checkboxes box to the main box
        box.pack_start(checkbox_box, True, True, 10)
        space_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.pack_start(space_box, True, True, 10)
        # Add the main box to the content area
        area = self.get_content_area()
        action_area = self.get_action_area()
        action_area.set_layout(Gtk.ButtonBoxStyle.CENTER)
        area.add(box)

        # Show all widgets
        self.show_all()

# if __name__ == "__main__":
#     app = ModemWindow()
#     app.run()