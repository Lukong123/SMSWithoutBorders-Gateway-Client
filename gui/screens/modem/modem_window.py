import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from screens.modem.send_message import SendMessageWindow
from screens.modem.incoming_message import IncomingMessageWindow
from screens.modem.home_modem import HomeModemWindow


class ModemWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")
        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)

        

        # Create the sidebar
        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.set_size_request(150, -1)
        sidebar.set_homogeneous(False)
        sidebar.set_border_width(0)
        sidebar.set_name("sidebar")
        main_box.pack_start(sidebar, False, False, 0)
        

        # Create the stack to switch between views
        stack = Gtk.Stack()
        main_box.pack_start(stack, True, True, 0)

        # Sidebar content
        sidebar_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.pack_start(sidebar_top, False, False, 0)

        home_modem_label = Gtk.Label()
        home_modem_label.set_text("Home Modem")
        home_modem_label.set_name("side_label")
        home_modem_label.set_name("active")
        home_modem_label.set_margin_bottom(8)
        home_modem_label.set_margin_top(60)
        home_modem_event_box = Gtk.EventBox()
        home_modem_event_box.add(home_modem_label)
        home_modem_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        home_modem_event_box.connect("button-press-event", self.on_home_modem_clicked, stack)
        sidebar_top.pack_start(home_modem_event_box, False, False, 0)

        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(line, False, False, 0)

        # send
        send_label = Gtk.Label()
        send_label.set_text("Send")
        send_label.set_name("side_label")
        send_label.set_margin_bottom(8)
        send_label.set_margin_top(8)
        send_event_box = Gtk.EventBox()
        send_event_box.add(send_label)
        send_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        send_event_box.connect("button-press-event", self.on_send_clicked, stack)
        sidebar_top.pack_start(send_event_box, False, False, 0)

        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(line, False, False, 0)

        # incoming
        incoming_label = Gtk.Label()
        incoming_label.set_text("Incoming")
        incoming_label.set_name("side_label")
        incoming_label.set_margin_bottom(8)
        incoming_label.set_margin_top(8)
        incoming_event_box = Gtk.EventBox()
        incoming_event_box.add(incoming_label)
        incoming_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        incoming_event_box.connect("button-press-event", self.on_incoming_clicked, stack)
        
        sidebar_top.pack_start(incoming_event_box, False, False, 0)

        self.initialize_views(stack)

    def initialize_views(self, stack):

        # home modem view
        home_modem_view = HomeModemWindow()
        stack.add_named(home_modem_view, "home_modem")
        
        # send view
        send_view = SendMessageWindow()
        stack.add_named(send_view, "send")

        # incoming view
        incoming_view = IncomingMessageWindow()
        stack.add_named(incoming_view, "incoming")
        
    def on_home_modem_clicked(self, widget, event, stack):
        stack.set_visible_child_name("home_modem")

    def on_send_clicked(self, widget, event, stack):
        stack.set_visible_child_name("send")

    def on_incoming_clicked(self, widget, event, stack):
        stack.set_visible_child_name("incoming")

    



# if __name__ == "__main__":
#     win = ModemWindow()
#     win.show_all()
#     Gtk.main()