import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine
from src.api_callbacks import ModemHandler


class OutgoingMessageWindow(Gtk.Box):
    def __init__(self, outgoing_messages, modem_name, modem_handler):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)
        self.modem_handler = modem_handler
        self.modem_name = modem_name
        
        self.modem_handler.handle_modem_connected()
        self.outgoing_messages = self.modem_handler.load_outgoing(modem_name)   
        self.container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.popover= Gtk.Popover.new(self)
        self.popover.set_position(Gtk.PositionType.TOP)
        popover_label = Gtk.Label(label="Delete Successful")
        self.popover.add(popover_label)

        # scrolled window
        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow) 

        # Container 1
        self.container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.container1.set_vexpand(True)
        self.container1.set_homogeneous(False)
        self.container1.set_border_width(10)
        scrolledwindow.add(self.container1)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")
        self.container1.pack_start(nav_bar, False, False, 0)

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
        header = Gtk.Label()
        header.set_text("Outgoing Messages")
        header.set_name("header_label")
        self.container1.pack_start(header, False, False, 5)

        self.message_ui()

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
        self.container1.pack_end(alignment, False, False, 0)

        fab_button.connect("clicked", self.on_fab_button_clicked)


        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

    def message_ui(self):
        self.container_main.set_halign(Gtk.Align.CENTER)
        self.container_main.set_margin_top(10)
        screen = Gdk.Screen.get_default()
        width_get = screen.get_width()
        self.container_main.set_size_request(int(width_get * 0.4), -1)

        self.container_main.set_name("container_main_msg")
        self.container1.pack_start(self.container_main, False, False, 0)

        for message in self.outgoing_messages:
            message_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=10)
            message_box.set_margin_top(10)
            message_box.set_margin_right(20)
            message_box.set_margin_left(20)


            message_box.set_name("container_main_msg")
            self.container_main.pack_start(message_box, False, False, 0)

            row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            row1.set_homogeneous(False)
            row1.set_name("row1") 
            row1.set_margin_top(10)
            message_box.pack_start(row1, False, False, 0)

            left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            left_box.set_homogeneous(True)
            row1.pack_start(left_box, False, False, 0)

            # values
            number_value = str(message.get("number", ""))
            text_value = message.get("text", "")
            timestamp_value = str(message.get("timestamp", ""))

            number_label = Gtk.Label()
            number_label.set_text(number_value)
            number_label.set_name("number-label")
            number_label.set_margin_start(0)
            left_box.pack_start(number_label, False, False, 20)

            right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            right_box.set_homogeneous(True)
            row1.pack_end(right_box, False, False, 0)
                
            time_label = Gtk.Label()
            time_label.set_text(timestamp_value)
            time_label.set_name("time-label") 
            right_box.pack_end(time_label, False, False, 20)

            row2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            row2.set_homogeneous(False)
            row2.set_name("row2") 
            message_box.pack_start(row2, False, False, 0)

            left_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            left_box2.set_homogeneous(True)
            row2.pack_start(left_box2, False, False, 0)

            message_label = Gtk.Label()
            message_label.set_text(str(text_value))
            message_label.set_name("message-label")
            left_box2.pack_start(message_label, False, False, 20)

            row3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            row3.set_homogeneous(False)
            row3.set_name("row3") 
            row3.set_margin_bottom(10)
            message_box.pack_start(row3, True, False, 0)

            left_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            left_box3.set_homogeneous(True)
            row3.pack_start(left_box3, False, False, 0)

            delete_button = Gtk.Button()
            # delete_button.set_margin_bottom(50)
            delete_button.set_label("Delete")
            delete_button.set_name("delete_btn")

            delete_button.connect("clicked", self.on_delete_button_clicked, message['id'])
            left_box3.pack_start(delete_button, False, False, 20)

            right_box_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            right_box_3.set_homogeneous(True)
            row3.pack_end(right_box_3, False, False, 0)

            reply_label = Gtk.Label()
            reply_label.set_text("Reply")
            reply_label.set_name("time-label") 
            right_box_3.pack_end(reply_label, False, False, 20)
        self.container_main.show_all()

    def show_delete_successful_popover(self):
        self.popover.show_all()
        GLib.timeout_add_seconds(2, self.hide_delete_successful_popover)

    def hide_delete_successful_popover(self):
        self.popover.hide()
        # self.reload_outgoing_messages()
        return False

        
    def on_delete_button_clicked(self, widget, message_id):
        print("After the delete button clicked")
        print(f"Message ID: {message_id}")
        
        row_count_tuple = self.modem_handler.delete_message(message_id)
        row_count = row_count_tuple[0] if isinstance(row_count_tuple, tuple) else row_count_tuple
        
        print(f"Rows deleted: {row_count}")
        
        # Check if the message was successfully deleted
        if row_count > 0:
            self.show_delete_successful_popover()
            self.reload_outgoing_messages()

    def reload_outgoing_messages(self):
        self.outgoing_messages = self.modem_handler.load_outgoing(self.modem_name)
        self.container_main.foreach(Gtk.Widget.destroy) 
        self.message_ui()

       
    def on_fab_button_clicked(self, button):
        # Switch to the "send" view in the stack
        print("recognize click on fab button")
       
        modem_window = self.get_toplevel()
        stack = modem_window.get_children()[0].get_children()[1] 
        stack.set_visible_child_name("send")


    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "gui/utils/styles/styles.css"
        # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

#     def send_label_clicked(self, widget, event):
#         print("send label click")
#         send_window = SendMessageWindow()
#         send_window.show_all()
        
#     def run(self):
#         Gtk.main()

# if __name__ == "__main__":
#     app = ModemWindow()
#     app.run()