from src.modem_manager import ModemManager
from src.modem import Modem



def callback_function(Modem):
    # pp = modem.enable
    props1 = Modem.get_modem_property('Manufacturer')
    props2 = Modem.get_modem_property('Model')

    modem_name = f"{props1} {props2}"


    print(modem_name)


# mm = ModemManager()
# mm.add_modem_connected_handler(callback_function)
# modem_list = mm.list_modems()
# print(modem_list)
print("enabling....", Modem.enable)
# modem_list_length= len(modem_list)
# print(modem_list_length)


# mm.daemon()




