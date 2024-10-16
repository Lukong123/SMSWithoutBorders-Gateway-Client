import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Pango
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
        self.outgoing_message = OutgoingMessageWindow(outgoing_messages=[], modem_name=modem_name, modem_handler=modem_handler)

        mainscrolledwindow = Gtk.ScrolledWindow()
        self.add(mainscrolledwindow) 

        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)
        mainscrolledwindow.add(container1)

        header = Gtk.Label()
        header.set_text("Send Message")
        header.set_name("header_label")
        container1.pack_start(header, False, False, 0)



        # container main
        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_name("center-box-send")
        container1.pack_start(container_main, False, False, 0)



        # message label
        message_label = Gtk.Label()
        message_label.set_text("NEW MESSAGE")
        container_main.pack_start(message_label, False, False, 5)

        # Horizontal line widget
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        container_main.pack_start(line, False, False, 0)

        number_label = Gtk.Label()
        number_label.set_text("Phone Number")
        number_label.set_name("number_label")
        container_main.pack_start(number_label, False, False, 0)

        # Text entry for phone number
        self.number_entry = Gtk.Entry()
        self.number_entry.set_placeholder_text("677777777")
        if recepient_number:
            recepient_number.set_text(recepient_number)
        self.number_entry.set_name("number_entry")
        container_main.pack_start(self.number_entry, False, False, 0)

        # self.grid = Gtk.Grid()

        # self.add(self.grid)


        # self.create_textview()

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
        # self.grid.attach(scrolledwindow, 0, 0, 1, 1)


        container_main.pack_start(scrolledwindow, False, False, 0)

        # Send button with label and logo
        send_button = Gtk.Button()
        send_button.set_margin_bottom(15)
        send_button.set_margin_top(10)

        send_button.set_label("Send")
        send_button.set_name("send_btn")
        send_button.set_image(Gtk.Image.new_from_icon_name("mail-send", Gtk.IconSize.BUTTON))
        container_main.pack_start(send_button, False, False, 10)

        send_button.connect("clicked", self.on_send_button_clicked)

        

    

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
        print(f"  result  {result}")
        self.modem_handler.load_outgoing(self.modem_name)
        print("above the self.load way")
        self.outgoing_message.reload_outgoing_messages()
        print("after the reload")
        if result:
            # self.modem_handler.load_outgoing(self.modem_name)
            self.outgoing_message.message_ui()
            # OutgoingMessageWindow.reload_outgoing_messages()
            # self.outgoing_message_window.
            print("outgoing loaded done")
        else:
            print("outgoing loaded undone")

    def on_send_button_clicked(self, widget):
        text_buffer = self.textview.get_buffer()
        text_start_iter = text_buffer.get_start_iter()
        text_end_iter = text_buffer.get_end_iter()
        text = text_buffer.get_text(text_start_iter, text_end_iter, True)
        number = self.number_entry.get_text()
        result = self.modem_handler.send_messages(text, number, self.modem_name)
        print(f"after the result {result}")
        print(f"text buffer context {text}")
        print(f"number buffer context {number}")
        print(f"result type {type(result)}")
        print(f"result {result}")
        if result is not None:
            self.modem_handler.load_outgoing(self.modem_name)
            print("above the self.load way")
            self.outgoing_message.reload_outgoing_messages()
            print("after the reload")
            # You may need to adjust this part based on your OutgoingMessageWindow class
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

    # def onFocusIn(self, event):
    #     if (textbuf.get_text(textbuf.get_start_iter(), textbuf.get_end_iter(), True) == placeholderStr):
    #         textbuf.set_text("")
    #     return False


    # def onFocusOut(self, event):
    #     if (textbuf.get_text(textbuf.get_start_iter(), textbuf.get_end_iter(), True) == ""):
    #         textbuf.set_text(placeholderStr)
    #     return False

   