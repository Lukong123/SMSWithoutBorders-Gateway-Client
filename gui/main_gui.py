import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils.widgets.horizontal_line import HorizontalLine
from screens.modem.modem_window import ModemWindow
from screens.homescreens.deku_home import DekuHomeWindow

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
        nav_bar.set_name("nav-bar")  # Set the CSS class name

        main_box.pack_start(nav_bar, False, False, 0)
        
        # stack
        stack = Gtk.Stack()
        main_box.pack_start(stack, True, True, 0)
        
        # navbar content 
        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")
        title_label_event_box = Gtk.EventBox()
        title_label_event_box.add(title_label)
        title_label_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        title_label_event_box.connect("button-press-event", self.on_title_label_clicked, stack)
        left_box.pack_start(title_label_event_box, False, False, 20)


        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        # icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 20)

        self.initialize_views(stack)
       
        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

        screen = self.get_screen()
        max_width = screen.get_width()
        self.set_size_request(max_width, -1)
    def initialize_views(self,stack):
        # title label(home)
        title_label_view = DekuHomeWindow()
        stack.add_named(title_label_view, "deku_home")

    def on_title_label_clicked(self, widget, event, stack):
        stack.set_visible_child_name("deku_home")
   
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