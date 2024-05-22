import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gui.utils.widgets.horizontal_line import HorizontalLine

from gui.screens.modem.modem_window import ModemWindow

# from src.api_callbacks import callback_function, ModemPass, callback_function_name
from src.api_callbacks import ModemHandler


class DekuLinux(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")

        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")  # Set the CSS class name

        main_box.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")  # Set a custom CSS name for the label
        left_box.pack_start(title_label, False, False, 20)

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        # icon
        nav_icon = Gtk.Image.new_from_icon_name("symbolic-grid", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 20)

        # Horizontal line widget
        line = HorizontalLine()
        main_box.pack_end(line, False, False, 0)

        # Container 2
        container2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container2.set_vexpand(True)
        container2.set_homogeneous(False)
        container2.set_border_width(10)

        # Event box
        event_box = Gtk.EventBox()
        event_box.connect("button-press-event", self.on_modem_1_click)
        container2.pack_start(event_box, False, False, 0)

        # text box
        modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container2.pack_start(modem_container, False, False, 0)

        # modem text
        self.modem_label = Gtk.Label()
        event_box.add(self.modem_label)
        modem_container.pack_start(self.modem_label, False, False, 0)
        self.update_modem_list()


        modem_2 = Gtk.Label()
        modem_2.set_text("Modem Orange 33")
        modem_2.set_name("modem_label")
        modem_container.pack_end(modem_2, False, False, 0)

        main_box.pack_end(container2, True, True, 0)

        # # Horizontal line widget
        line = HorizontalLine()
        main_box.pack_end(line, False, False, 0)
        

        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)

        # text box
        text_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container1.pack_start(text_box, False, False, 0)

        # Welcome text
        welcome_label = Gtk.Label()
        welcome_label.set_text("Welcome to Deku Linux\nLorem ipsum dolor set eid adoi adihl eiha diuhad.\n Diahe, ihad a akldiv i dau ekdhuc.")
        welcome_label.set_line_wrap(True)
        text_box.pack_start(welcome_label, False, False, 0)

        # center box
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box")
        container1.pack_start(center_box, False, False, 0)

        # device label
        self.device_label = Gtk.Label()
        # self.modem_label = Gtk.Label()
        center_box.pack_start(self.device_label, False, False, 30)
        # center_box.pack_start(self.modem_label, False, False, 30)

        self.update_device_label()
        # self.update_modem_list()

    
        main_box.pack_end(container1, True, True, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()
        self.modem_window = ModemWindow()


    def update_device_label(self):
        print("Updating device label ...")
        modem = ModemHandler()
        modem.handle_modem_connected()
        modem_list_length = modem.get_modem_list_length()
        print("Updating device label after call back...")
        print("Modem list length:", modem_list_length)
        self.device_label.set_text(f"{modem_list_length} device(s)")
    

    def update_modem_list(self):
        print("Updating modem labels...")
        modem = ModemHandler()
        modem.handle_modem_connected()
        modem_names = modem.get_modem_names()
        print("Updating device labels after callback...")
        print("Modem list length:", len(modem_names))

        modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container2 = self.modem_label.get_parent().get_parent()
        # container2.remove(self.modem_label)
        container2.pack_start(modem_container, False, False, 0)

        for modem_name in modem_names:
            modem_label = Gtk.Label()
            modem_label.set_text(modem_name)
            modem_label.set_name("modem_label")
            print(f"-{modem_name}")
            modem_container.pack_start(modem_label, False, False, 0)

        # Call show_all on the container2 to ensure all labels are displayed
        container2.show_all()
    def on_modem_1_click(self, widget, event):
        print("Modem 1 clicked!")
        main_box = self.get_child()
        main_box.remove(self.modem_window)
        self.modem_window.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "gui/utils/styles/styles.css"

       # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


    def run(self):
        Gtk.main()


if __name__ == "__main__":
    app = DekuLinux()
    app.run()