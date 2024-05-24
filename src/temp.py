#!/bin/python3


from modem_manager import ModemManager
import modem

def callback_function(modem: modem.Modem):
    props = modem.get_modem_property('EquipmentIdentifier')

    print(props)

if __name__ == '__main__':

    mm = ModemManager()

    mm.add_modem_connected_handler(callback_function)

    mm.daemon()


    # def update_modem_list(self):
    #     print("Updating modem labels...")
    #     modem = ModemHandler()
    #     modem.handle_modem_connected()
    #     modem_names = modem.get_modem_names()
    #     print("Updating device labels after callback...")
    #     print("Modem list length:", len(modem_names))

    #     modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #     container2 = self.modem_label.get_parent().get_parent()
    #     # container2.remove(self.modem_label)
    #     container2.pack_start(modem_container, False, False, 0)

    #     for modem_name in modem_names:
    #         modem_label = Gtk.Label()
    #         modem_label.set_text(modem_name)
    #         modem_label.set_name("modem_label")
    #         print(f"-{modem_name}")

    #         event_box = Gtk.EventBox()
    #         # event_box.connect("button-press-event", self.on_modem_click)
    #         event_box.connect("button-press-event", lambda widget, event, name=modem_name: self.on_modem_click(widget, event, name))
    #         event_box.add(modem_label)  # Add the modem label to the event box
    #         modem_container.pack_start(event_box, False, False, 0)

    #         modem_container.pack_start(modem_label, False, False, 0)

    #     # Call show_all on the container2 to ensure all labels are displayed
    #     container2.show_all()

    # def on_modem_click(self, widget, event, modem_name):
    #     modem_name = self.modem_label.get_text()

    #     print(f"Modem {modem_name} clicked!")
    #     modem_handler = ModemHandler()
    #     modem_handler.enable_modem(modem_name)
    #     modem_properties = modem_handler.get_properties()
    #     modem_window = ModemWindow(modem_properties)
    #     modem_window.show_all()



# code that works for enable
# def on_modem_1_click(self, widget, event):
#     modem_name = self.modem_label.get_text()  # Retrieve the modem name associated with the clicked label
#     print(f"Modem '{modem_name}' clicked!")

#     # Enable the clicked modem
#     handler = ModemHandler()
#     handler.handle_modem_connected()
#     handler.enable_modem(modem_name)

#     main_box = self.get_child()
#     main_box.remove(self.modem_window)
#     self.modem_window.show_all()




    # def update_modem_list(self):
    #     print("Updating modem labels...")
    #     modem = ModemHandler()
    #     modem.handle_modem_connected()
    #     modem_names = modem.get_modem_names()
    #     print("Updating device labels after callback...")
    #     print("Modem list length:", len(modem_names))

    #     modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #     container2 = self.modem_label.get_parent().get_parent()
    #     # container2.remove(self.modem_label)
    #     container2.pack_start(modem_container, False, False, 0)

    #     for modem_name in modem_names:
    #         modem_label = Gtk.Label()
    #         modem_label.set_text(modem_name)
    #         modem_label.set_name("modem_label")
    #         print(f"-{modem_name}")

    #         event_box = Gtk.EventBox()
    #         # event_box.connect("button-press-event", self.on_modem_click)
    #         event_box.connect("button-press-event", lambda widget, event, name=modem_name: self.on_modem_click(widget, event, name))
    #         event_box.add(modem_label)  # Add the modem label to the event box
    #         modem_container.pack_start(event_box, False, False, 0)

    #         modem_container.pack_start(modem_label, False, False, 0)

    #     # Call show_all on the container2 to ensure all labels are displayed
    #     container2.show_all()



################################################################################################333
##################################################################################################33333
############################################################################################333333
#################################################################################################333
# def modem_connected_callback(modem):
#     print("modem connected")

# def pass_func():
#     print("hello")

# def callback_function(Modem):
#     # pp = modem.enable
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')

#     modem_name = f"{props1} {props2}"
#     print("before modem manager")
#     mm = ModemManager()
#     print("before add manager")

#     mm.add_modem_connected_handler(modem_connected_handler=pass_func)
#     print("after add modem manager")

#     print(modem_name)
#     return modem_name


# mm = ModemManager()
# mm.add_modem_connected_handler(callback_function)

# mm.daemon()

# def callback_function(Modem):
#     mm = ModemManager()
#     modem_list = mm.list_modems()
#     modem_list_length = len(modem_list)
#     return modem_list_length

# def callback_modemlist(Modem):
#     mm = ModemManager()
#     modem_list = mm.list_modems()
#     return modem_list


# def callback_modem_name(Modem):
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')
#     modem_name = f"{props1} {props2}"
#     return modem_name

# class ModemPass:
#     pass

# def callback_function_name(Modem):
#     # pp = modem.enable
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')

#     modem_name = f"{props1} {props2}"
#     print("before modem manager")
#     mm = ModemManager()
#     print("before add manager")

#     mm.add_modem_connected_handler(modem_connected_handler=pass_func)
#     print("after add modem manager")

#     print(modem_name)
#     return modem_name


# def callback_function_test(Modem):
#     # pp = modem.enable
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')

#     modem_name = f"{props1} {props2}"

#     print(modem_name)
#     # return modem_name


# mm = ModemManager()
# mm.add_modem_connected_handler(callback_function_test)

# mm.daemon()


# def callback_function(Modem):
#     # pp = modem.enable
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')

#     modem_name = f"{props1} {props2}"


#     print(modem_name)



#======================================================================================
#===================================================================================
#==============================================================================
    # def update_modem_list(self):
    #     print("Updating modem labels...")
    #     modem = ModemHandler()
    #     modem.handle_modem_connected()
    #     modem_names = modem.get_modem_names()
    #     print("Updating device labels after callback...")
    #     print("Modem list length:", len(modem_names))

    #     modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #     container2 = self.modem_label.get_parent().get_parent()
    #     container2.pack_start(modem_container, False, False, 0)

    #     def on_modem_closure(modem_name):
    #         def on_modem_click(widget, event):
    #             print(f"Modem {modem_name} clicked!")

    #             modem_handler = ModemHandler()
    #             modem_handler.enable_modem(modem_name)
    #             modem_properties = modem_handler.get_properties()
    #             modem_window = ModemWindow(modem_properties)
    #             modem_window.show_all()

    #         return on_modem_click

    #     for modem_name in modem_names:
    #         modem_label = Gtk.Label()
    #         modem_label.set_text(modem_name)
    #         modem_label.set_name("modem_label")

    #         event_box = Gtk.EventBox()
    #         event_box.connect("button-press-event", on_modem_closure(modem_name))
    #         event_box.add(modem_label)
    #         modem_container.pack_start(event_box, False, False, 0)

    #     container2.show_all()

