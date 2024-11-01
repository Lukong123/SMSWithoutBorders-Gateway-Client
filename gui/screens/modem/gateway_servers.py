import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

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

        # Create a MenuButton with an icon
        nav_icon_button = Gtk.Button()
        nav_icon_button.set_name("nav-icon-button")
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        nav_icon_button.set_image(nav_icon)

        
        right_box.pack_end(nav_icon, False, False, 20)

        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        icon_evnet_box = Gtk.EventBox()
        icon_evnet_box.add(nav_icon)
        right_box.pack_end(icon_evnet_box, False, False, 20)

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
        https.connect("activate", on_menu_item_clicked, "opt 1")
        smtp.connect("activate", self.on_settings_clicked)
        ftp.connect("activate", self.on_settings_clicked)



        # Connect the click event on the image to show the menu
        def on_icon_clicked(widget, event):
            if event.button == 1:  # Left-click
                menu.popup(None, None, None, None, event.button, event.time)

        icon_evnet_box.connect("button-press-event", on_icon_clicked)
        

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
        message_label.set_text("No routed gateways!")
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



    def on_settings_clicked(self, widget):
        dialog = SettingsPopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("ok button clikc")
        elif response == Gtk.ResponseType.CANCEL:
            print("cancel button clikc")

        dialog.destroy()
   
class SettingsPopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Gateway Server Settings", Gtk.DialogFlags.MODAL, parent=None)

        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

        self.set_default_size(200, 100)
        self.set_border_width(30)

        box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label_heading = Gtk.Label("Enable Automatic Protocol Routing")
        label_heading.set_name("label_heading")
        box.pack_start(label_heading, True, True, 10)
        label_body = Gtk.Label()
        label_body.set_text("Turn this on by clicking OK to route only to 1 protocol at a time."
                            " This begins with HTTP and performs a round-robin lookup for the other protocls.\n"
                            " \n Use this to avoid receiving the same message to multiple protocols.")
        box.pack_start(label_body, True, True, 20)
        area = self.get_content_area()
        area.add(box)

        area = self.get_content_area()
        action_area = self.get_action_area()
        action_area.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.show_all()

# if __name__ == "__main__":
#     app = ModemWindow()
#     app.run()