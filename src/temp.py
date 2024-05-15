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