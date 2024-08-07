import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from src.api_callbacks import ModemHandler


from gui.screens.modem.send_message import SendMessageWindow
from gui.screens.modem.incoming_message import IncomingMessageWindow
from gui.screens.modem.home_modem import HomeModemWindow
from gui.screens.modem.outgoing_message import OutgoingMessageWindow
from gui.screens.modem.failed_message import FailedMessageWindow
from gui.screens.modem.encrypted_message import EncryptedMessageWindow
from gui.screens.modem.message_forwarding import MessageForwardingWindow
from gui.screens.modem.export_message import ExportMessageWindow
from gui.screens.modem.about import AboutWindow

from gui.utils.widgets.horizontal_line import HorizontalLine

class ModemWindow(Gtk.Window):
    def __init__(self, modem_properties, modem_name):
        super().__init__(title="Deku Linux App")
        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)
        self.modem_handler = ModemHandler()
        self.modem_handler.handle_modem_connected()
        
        self.modem_properties = self.modem_handler.get_modem_properties(modem_name)
        self.modem_name = modem_name
        self.incoming_messages = self.modem_handler.get_get_incoming_message()
        

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
        
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(incoming_event_box, False, False, 0)

        # outgoing
        outgoing_label = Gtk.Label()
        outgoing_label.set_text("Outgoing")
        outgoing_label.set_name("side_label")
        outgoing_label.set_margin_bottom(8)
        outgoing_label.set_margin_top(8)
        outgoing_event_box = Gtk.EventBox()
        outgoing_event_box.add(outgoing_label)
        outgoing_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        outgoing_event_box.connect("button-press-event", self.on_outgoing_clicked, stack)

        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(outgoing_event_box, False, False, 0)

        # failed
        failed_label = Gtk.Label()
        failed_label.set_text("Failed")
        failed_label.set_name("side_label")
        failed_label.set_margin_bottom(8)
        failed_label.set_margin_top(8)
        failed_event_box = Gtk.EventBox()
        failed_event_box.add(failed_label)
        failed_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        failed_event_box.connect("button-press-event", self.on_failed_clicked, stack)

        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(failed_event_box, False, False, 0)

        # encrypted
        encrypted_label = Gtk.Label()
        encrypted_label.set_text("Encrypted")
        encrypted_label.set_name("side_label")
        encrypted_label.set_margin_bottom(38)
        encrypted_label.set_margin_top(8)
        encrypted_event_box = Gtk.EventBox()
        encrypted_event_box.add(encrypted_label)
        encrypted_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        encrypted_event_box.connect("button-press-event", self.on_encrypted_clicked, stack)
        
        sidebar_top.pack_start(encrypted_event_box, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)


        # message forwarding
        message_forwarding_label = Gtk.Label()
        message_forwarding_label.set_text("Message Forwarding")
        message_forwarding_label.set_name("side_label")
        message_forwarding_label.set_margin_bottom(8)
        message_forwarding_label.set_margin_top(38)
        message_forwarding_event_box = Gtk.EventBox()
        message_forwarding_event_box.add(message_forwarding_label)
        message_forwarding_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        message_forwarding_event_box.connect("button-press-event", self.on_message_forwarding_clicked, stack)
        
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(message_forwarding_event_box, False, False, 0)

        # export
        export_label = Gtk.Label()
        export_label.set_text("Export")
        export_label.set_name("side_label")
        export_label.set_margin_bottom(8)
        export_label.set_margin_top(8)
        export_event_box = Gtk.EventBox()
        export_event_box.add(export_label)
        export_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        export_event_box.connect("button-press-event", self.on_export_clicked, stack)
        
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(export_event_box, False, False, 0)

        # about
        about_label = Gtk.Label()
        about_label.set_text("About")
        about_label.set_name("side_label")
        about_label.set_margin_bottom(8)
        about_label.set_margin_top(8)
        about_event_box = Gtk.EventBox()
        about_event_box.add(about_label)
        about_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        about_event_box.connect("button-press-event", self.on_about_clicked, stack)
        
        line = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        sidebar_top.pack_start(about_event_box, False, False, 0)

        self.initialize_views(stack)

    def initialize_views(self, stack):

        # home modem view
        home_modem_view = HomeModemWindow(self.modem_properties, self.modem_name)
        stack.add_named(home_modem_view, "home_modem")
        
        # send view
        send_view = SendMessageWindow()
        stack.add_named(send_view, "send")

        # incoming view
        incoming_view = IncomingMessageWindow(self.incoming_messages, self.modem_name)
        stack.add_named(incoming_view, "incoming")

        # outgoing view
        outgoing_view = OutgoingMessageWindow()
        stack.add_named(outgoing_view, "outgoing")

        # failed view
        failed_view = FailedMessageWindow()
        stack.add_named(failed_view, "failed")

        # encrypted view
        encrypted_view = EncryptedMessageWindow()
        stack.add_named(encrypted_view, "encrypted")

        # message forwarding view
        message_forwarding_view = MessageForwardingWindow()
        stack.add_named(message_forwarding_view, "message_forwarding")

        # export view
        export_view = ExportMessageWindow()
        stack.add_named(export_view, "export")

        # about view
        about_view = AboutWindow(self.modem_properties, self.modem_name)
        stack.add_named(about_view, "about")



    def on_home_modem_clicked(self, widget, event, stack):
        stack.set_visible_child_name("home_modem")

    def on_send_clicked(self, widget, event, stack):
        stack.set_visible_child_name("send")
        self.set_active_label("send_label")

    def on_incoming_clicked(self, widget, event, stack):
        stack.set_visible_child_name("incoming")
        self.set_active_label("incoming_label")

    def on_outgoing_clicked(self, widget, event, stack):
        stack.set_visible_child_name("outgoing")
        self.set_active_label("outgoing_label")

    def on_failed_clicked(self, widget, event, stack):
        stack.set_visible_child_name("failed")
        self.set_active_label("failed_label")
   
    def on_encrypted_clicked(self, widget, event, stack):
        stack.set_visible_child_name("encrypted")
        self.set_active_label("encrypted_label")

    def on_message_forwarding_clicked(self, widget, event, stack):
        stack.set_visible_child_name("message_forwarding")
        self.set_active_label("message_forwarding_label")

    def on_export_clicked(self, widget, event, stack):
        stack.set_visible_child_name("export")
        self.set_active_label("export_label")

    def on_about_clicked(self, widget, event, stack):
        stack.set_visible_child_name("about")
        self.set_active_label("about_label")

    def on_test_clicked(self, widget, event, stack):
        popover = Gtk.Popover.new_from_widget(widget)
        popover.set_position(Gtk.PositionType.BOTTOM)
        
        item1 = Gtk.Label()
        item1.set_text("item 1")

        item2 = Gtk.Label()
        item2.set_text("Item 2")

        # dropdownbox = Gtk.

    def set_active_label(self, label_name):
        sidebar = self.get_child().get_children()[0]
        sidebar_top = sidebar.get_children()[0]

        for child in sidebar_top.get_children():
            if isinstance(child, Gtk.EventBox):
                if child.get_children()[0].get_name() == "active":
                    child.get_children()[0].set_name("side_label")
                    child.get_children()[0].get_style_context().remove_class("active")

                for child in sidebar_top.get_children():
                    if isinstance(child, Gtk.EventBox):
                        if child.get_children()[0].get_name() == label_name:
                            child.get_children()[0].set_name("active")
                            child.get_children()[0].get_style_context().add_class("active")


