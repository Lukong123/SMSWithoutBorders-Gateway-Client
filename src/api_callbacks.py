from src.modem_manager import ModemManager
from src.modem import Modem

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


def callback_function(Modem):
    # pp = modem.enable
    props1 = Modem.get_modem_property('Manufacturer')
    props2 = Modem.get_modem_property('Model')

    modem_name = f"{props1} {props2}"


    print(modem_name)

mm = ModemManager()
mm.add_modem_connected_handler(callback_function)
modem_list = mm.list_modems()
print(modem_list)
modem_list_length= len(modem_list)
print(modem_list_length)


mm.daemon()