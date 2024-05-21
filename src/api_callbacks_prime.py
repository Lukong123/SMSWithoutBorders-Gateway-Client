from src.modem_manager import ModemManager
from src.modem import Modem



def pass_func():
    print("hello")

def callback_function_name(Modem):
    props1 = Modem.get_modem_property('Manufacturer')
    props2 = Modem.get_modem_property('Model')
    modem_name = f"{props1} {props2}"
    mm = ModemManager()
    mm.add_modem_connected_handler(modem_connected_handler=pass_func)
    print(modem_name)
    return modem_name




