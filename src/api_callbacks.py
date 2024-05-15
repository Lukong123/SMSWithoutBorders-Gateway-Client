
from modem_manager import ModemManager
import modem

def modem_connected_callback(modem):
    print("modem connected")


def callback_function(modem: modem.Modem):
    # pp = modem.enable
    props1 = modem.get_modem_property('Manufacturer')
    props2 = modem.get_modem_property('Model')

    modem_name = f"{props1} {props2}"


    print(modem_name)

mm = ModemManager()
mm.add_modem_connected_handler(callback_function)
modem_list = mm.list_modems()
print(modem_list)
modem_list_length= len(modem_list)
print(modem_list_length)


mm.daemon()
