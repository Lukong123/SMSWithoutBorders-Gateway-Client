# from src.modem_manager import ModemManager
from src.modem_manager import ModemManager



def modem_connected_callback(modem):
    print("modem connected")

mm = ModemManager()
mm.add_modem_connected_handler(print_hello)
mm.daemon()
