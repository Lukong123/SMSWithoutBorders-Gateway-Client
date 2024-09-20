import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import subprocess

from gui.utils.widgets.horizontal_line import HorizontalLine
from gui.screens.modem.send_message import SendMessageWindow
from src.api_callbacks import ModemHandler


class IncomingMessageWindow(Gtk.Box):
    def __init__(self, incoming_messages, modem_name, modem_path, modem_handler):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)
        # self.modem_handler= ModemHandler()
        self.modem_handler = modem_handler
        self.modem_path = modem_path
        self.modem_name = modem_name
        
        self.modem_handler.handle_modem_connected()
        self.incoming_messages = self.modem_handler.get_get_incoming_message(modem_path)

        # self.reply_label = reply_label
        # reply_label = self.reply_
        
        # scrolled window
        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow) 

        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)
        scrolledwindow.add(container1)
        
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
        container_main.set_margin_top(10)
        screen = Gdk.Screen.get_default()
        width_get = screen.get_width()
        container_main.set_size_request(int(width_get * 0.4), -1)

        container_main.set_name("container_main_msg")
        container1.pack_start(container_main, False, False, 0)
        
        for message in self.incoming_messages:
            message_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=10)
            message_box.set_margin_top(10)
            message_box.set_margin_right(20)
            message_box.set_margin_left(20)
            message_box.set_name("container_main_msg")
            container_main.pack_start(message_box, False, False, 0)

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
            message_label.set_text(text_value)
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
            reply_label.set_has_window(True)
            reply_label.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
            reply_label.connect("button-press-event", self.on_reply_label_clicked)
            right_box_3.pack_end(reply_label, False, False, 20)

                    
        

        # floating action button
        fab_button = Gtk.Button()
        fab_button.set_tooltip_text("Compose")
        fab_button.get_style_context().add_class("fab-button")

        message_icon = Gtk.Image.new_from_icon_name("mail-send-symbolic", Gtk.IconSize.BUTTON)
        fab_button.add(message_icon)
        fab_button.set_size_request(50, 50)
        alignment = Gtk.Alignment.new(1, 0.8, 0, 0)
        alignment.set_padding(0, 0, 10, 10) 
        alignment.add(fab_button)
        container1.pack_end(alignment, False, False, 0)

        fab_button.connect("clicked", self.on_fab_button_clicked)

# Add the aligned floating action button to the main container
        # self.pack_end(alignment, False, False, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()
    

    def on_delete_button_clicked(self,widget,message_id):
        print("After the delete button clicked")
        print(f"Message ID: {message_id}")
        row_count = self.modem_handler.delete_message(message_id), 
        print(f"Rows deleted: {row_count}")
    

    def on_reply_label_clicked(self, event_box, event, recepient_number = None):
        # Switch to the "send" view in the stack
        print("recognize click on fab button")
       
        modem_window = self.get_toplevel()
        stack = modem_window.get_children()[0].get_children()[1] 
        stack.set_visible_child_name("send")
        send_message_window = SendMessageWindow(modem_handler=self.modem_handler, modem_name=self.modem_name, recepient_number=recepient_number)
        send_message_window.show_all()

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


        
    # def run(self):
    #     Gtk.main()

# if __name__ == "__main__":
#     app = ModemWindow()
#     app.run()