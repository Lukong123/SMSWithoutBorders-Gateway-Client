import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
from gui.utils.widgets.horizontal_line import HorizontalLine

from src.api_callbacks import ModemHandler
from gui.screens.modem.outgoing_message import OutgoingMessageWindow


class SendMessageWindow(Gtk.Box):
    def __init__(self, modem_handler, modem_name, recepient_number=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)

        # self.handler = ModemHandler()
        self.modem_handler = modem_handler
        self.modem_name = modem_name
        self.outgoing_message = OutgoingMessageWindow( modem_name=modem_name, modem_handler=modem_handler)

        mainscrolledwindow = Gtk.ScrolledWindow()
        self.add(mainscrolledwindow) 

        self.container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.container1.set_vexpand(True)
        self.container1.set_homogeneous(False)
        self.container1.set_border_width(10)
        self.popover= Gtk.Popover.new(self)
        self.popover.set_position(Gtk.PositionType.TOP)
        popover_label = Gtk.Label(label="Message Sent")
        self.popover.add(popover_label)

        mainscrolledwindow.add(self.container1)
    
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
        secure = Gtk.MenuItem(label="Secure")
        search = Gtk.MenuItem(label="Search")
        block = Gtk.MenuItem(label="Block")
        delete = Gtk.MenuItem(label="Delete")

        menu.append(secure)
        menu.append(search)
        menu.append(block)
        menu.append(delete)

        menu.show_all()

        def on_menu_item_clicked(widget, label):
            print(f"{label} clicked")

        # Connect items to callback with a label
        secure.connect("activate", self.on_secure_clicked)
        search.connect("activate", on_menu_item_clicked, "Option 2")
        block.connect("activate", on_menu_item_clicked, "Option 3")
        delete.connect("activate", on_menu_item_clicked, "Option 3")


        # Connect the click event on the image to show the menu
        def on_image_clicked(widget, event):
            if event.button == 1:  # Left-click
                menu.popup(None, None, None, None, event.button, event.time)

        image_event_box.connect("button-press-event", on_image_clicked)



        # main_menu_bar = Gtk.MenuBar()

        # other_menu = Gtk.Menu()
        # other_menu_drop_down = Gtk.MenuItem("Others")

        # other_secure = Gtk.MenuItem("Secure")
        # other_search = Gtk.MenuItem("Search")
        # other_mute = Gtk.MenuItem("Mute")
        # other_block = Gtk.MenuItem("Block")
        # other_delete = Gtk.MenuItem("Delete")

        # other_secure.connect("activate", self.on_secure_clicked)


        # other_menu_drop_down.set_submenu(other_menu)
        # other_menu.append(other_secure)
        # other_menu.append(other_search)
        # other_menu.append(other_mute)
        # other_menu.append(other_block)
        # other_menu.append(other_delete)

        # main_menu_bar.append(other_menu_drop_down)



        # right_box.pack_end(main_menu_bar, False, False, 20)

        header = Gtk.Label()
        header.set_text("Send Message")
        header.set_name("header_label")
        self.container1.pack_start(header, False, False, 0)



        # container main
        self.send_ui()

    def send_ui(self):
        self.container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        self.container_main.set_halign(Gtk.Align.CENTER)
        self.container_main.set_name("center-box-send")
        self.container1.pack_start(self.container_main, False, False, 0)



        # message label
        message_label = Gtk.Label()
        message_label.set_text("NEW MESSAGE")
        self.container_main.pack_start(message_label, False, False, 5)

        # Horizontal line widget
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        self.container_main.pack_start(line, False, False, 0)

        number_label = Gtk.Label()
        number_label.set_text("Phone Number")
        number_label.set_name("number_label")
        self.container_main.pack_start(number_label, False, False, 0)

        # Text entry for phone number
        self.number_entry = Gtk.Entry()
        self.number_entry.set_placeholder_text("677777777")
        # if recepient_number:
        #     recepient_number.set_text(recepient_number)
        self.number_entry.set_name("number_entry")
        self.container_main.pack_start(self.number_entry, False, False, 0)


        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_size_request(400, 200) 
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        # scrolledwindow.set_margin_top(0)

        self.textview  = Gtk.TextView()
        textbuffer = self.textview.get_buffer()
        textbuffer.set_text("Compose...")
        self.textview.set_name('textbuffer')

        scrolledwindow.add(self.textview)

        self.container_main.pack_start(scrolledwindow, False, False, 0)

        # Send button with label and logo
        send_button = Gtk.Button()
        send_button.set_margin_bottom(15)
        send_button.set_margin_top(10)

        send_button.set_label("Send")
        send_button.set_name("send_btn")
        send_button.set_image(Gtk.Image.new_from_icon_name("mail-send", Gtk.IconSize.BUTTON))
        self.container_main.pack_start(send_button, False, False, 10)

        send_button.connect("clicked", self.on_send_button_clicked)


    def show_message_sent_popover(self):
        self.popover.show_all()
        GLib.timeout_add_seconds(3, self.hide_message_sent_popover)

    def hide_message_sent_popover(self):
        self.popover.hide()
        return False



    def reload_send_ui(self):
        text_buffer = self.textview.get_buffer()
        text_buffer.set_text("Compose...")

        self.number_entry.set_text("")  # Clear the entered number

        self.number_entry.set_placeholder_text("677777777")


    def on_send_button_clicked(self, widget):
        text_buffer = self.textview.get_buffer()
        text_start_iter = text_buffer.get_start_iter()
        text_end_iter = text_buffer.get_end_iter()
        text = text_buffer.get_text(text_start_iter, text_end_iter, True)
        number = self.number_entry.get_text()
        result = self.modem_handler.send_messages(text, number, self.modem_name)

        self.show_message_sent_popover()
        self.reload_send_ui()


        # OutgoingMessageWindow.reload_outgoing_messages()
        outgoing_message_window = OutgoingMessageWindow( self.modem_name, self.modem_handler)
        outgoing_message_window.reload_outgoing_messages()


        # GLib.idle_add(self.reload_send_ui())



        if result is not None:
            self.modem_handler.load_outgoing(self.modem_name)
            print("above the self.load way")
            self.outgoing_message.reload_outgoing_messages()
            print("after the reload")
            self.outgoing_message.message_ui()
            print("outgoing loaded done")
        else:
            print("outgoing loaded undone")

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "gui/utils/styles/styles.css"
        css_provider.load_from_path(css_path)
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    


    def get_resource_path(self, rel_path):
        dir_of_py_file = os.path.dirname(__file__)
        rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
        abs_path_to_resource = os.path.abspath(rel_path_to_resource)
        return abs_path_to_resource

    def on_secure_clicked(self, widget):
        dialog = SecurePopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("ok button clikc")
        elif response == Gtk.ResponseType.CANCEL:
            print("cancel button clikc")

        dialog.destroy()
   
class SecurePopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable Secure Connection", Gtk.DialogFlags.MODAL, parent=None)

        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

        self.set_default_size(200, 100)
        self.set_border_width(30)

        box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label("Are you sure you want to request secure connection?")
        box.pack_start(label, True, True, 10)
        area = self.get_content_area()
        area.add(box)

        area = self.get_content_area()
        action_area = self.get_action_area()
        action_area.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.show_all()