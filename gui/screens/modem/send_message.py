import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Pango
from gui.utils.widgets.horizontal_line import HorizontalLine

from src.api_callbacks import ModemHandler


class SendMessageWindow(Gtk.Box):
    def __init__(self, modem_handler, modem_name):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        self.set_homogeneous(False)
        self.set_border_width(5)

        # self.handler = ModemHandler()
        self.modem_handler = modem_handler
        self.modem_name = modem_name

        # container main
        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_name("center-box-message")
        self.pack_start(container_main, True, True, 0)


        # Send button with label and logo
        send_button = Gtk.Button()
        send_button.set_margin_bottom(50)
        send_button.set_label("Send")
        send_button.set_name("send_btn")
        send_button.set_image(Gtk.Image.new_from_icon_name("mail-send", Gtk.IconSize.BUTTON))
        container_main.pack_start(send_button, False, False, 10)

        send_button.connect("clicked", self.on_send_button_clicked)


        # message label
        message_label = Gtk.Label()
        message_label.set_text("NEW MESSAGE")
        container_main.pack_start(message_label, False, False, 5)

        # Horizontal line widget
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        container_main.pack_start(line, False, False, 0)

        # Text entry for phone number
        self.number_entry = Gtk.Entry()
        self.number_entry.set_placeholder_text("Number:")
        container_main.pack_start(self.number_entry, False, False, 0)

        self.grid = Gtk.Grid()

        self.add(self.grid)


        # self.create_textview()

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_size_request(400, 200) 
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        scrolledwindow.set_margin_top(0)

        self.textview  = Gtk.TextView()
        textbuffer = self.textview.get_buffer()
        textbuffer.set_text(
            "Compose..."
        )

        scrolledwindow.add(self.textview)
        # self.grid.attach(scrolledwindow, 0, 0, 1, 1)


        container_main.pack_start(scrolledwindow, False, False, 0)
        

    

        # # Adjusting container size
        # screen = Gdk.Screen.get_default()
        # self.set_size_request(-1, int(screen.get_height() * 0.55))

    def on_send_button_clicked(self,widget):
        text_buffer = self.textview.get_buffer()
        text_start_iter = text_buffer.get_start_iter()
        text_end_iter = text_buffer.get_end_iter()
        text = text_buffer.get_text(text_start_iter, text_end_iter, True)
        number = self.number_entry.get_text()

        result = self.modem_handler.send_messages(text, number, self.modem_name)
        print(f"after the result {result}")
        print(f"text buffer context {text}")
        print(f"number buffer context {number}")
        print(f"  result type {type(result)}")



   