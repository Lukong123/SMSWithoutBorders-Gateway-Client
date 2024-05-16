import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine


class FailedMessageWindow(Gtk.Box):
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


        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        screen = Gdk.Screen.get_default()
        width_get = screen.get_width()
        container_main.set_size_request(int(width_get * 0.4), -1)
        # container_main.set_size_request(500, -1)
        
        container_main.set_margin_top(10)
        container_main.set_name("container_main_msg")
        container1.pack_start(container_main, False, False, 0)

        row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row1.set_homogeneous(False)
        row1.set_name("row1") 
        row1.set_margin_top(10)
        container_main.pack_start(row1, False, False, 0)

        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        row1.pack_start(left_box, False, False, 0)

        number_label = Gtk.Label()
        number_label.set_text("Phone Number")
        number_label.set_name("number-label")
        number_label.set_margin_start(0)
        left_box.pack_start(number_label, False, False, 20)

        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        row1.pack_end(right_box, False, False, 0)

        time_label = Gtk.Label()
        time_label.set_text("06:08 pm")
        time_label.set_name("time-label") 
        right_box.pack_end(time_label, False, False, 20)

        row2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row2.set_homogeneous(False)
        row2.set_name("row2") 
        container_main.pack_start(row2, False, False, 0)

        left_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box2.set_homogeneous(True)
        row2.pack_start(left_box2, False, False, 0)

        message_label = Gtk.Label()
        message_label.set_text("Message...")
        message_label.set_name("message-label")
        left_box2.pack_start(message_label, False, False, 20)

        row3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row3.set_homogeneous(False)
        row3.set_name("row3") 
        row3.set_margin_bottom(10)
        container_main.pack_start(row3, True, False, 0)

        left_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box3.set_homogeneous(True)
        row3.pack_start(left_box3, False, False, 0)

        delete_icon = Gtk.Image.new_from_icon_name("edit-delete", Gtk.IconSize.BUTTON)
        left_box3.pack_start(delete_icon, False, False, 20)

        right_box_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box_3.set_homogeneous(True)
        row3.pack_end(right_box_3, False, False, 0)
        tick_icon = Gtk.Image.new_from_icon_name("dialog-error", Gtk.IconSize.BUTTON)
        right_box_3.pack_start(tick_icon, False, False, 10)

        resend_label = Gtk.Label()
        resend_label.set_text("Resend")
        resend_label.set_name("resend-label")
        right_box_3.pack_end(resend_label, False, False, 20)


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