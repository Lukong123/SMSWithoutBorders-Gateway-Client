from src.modem_manager import ModemManager
from src.modem import Modem


class ModemHandler:
    def __init__(self):
        self.modem_names = []
        self.modems = {}

    def handle_modem_connected(self):
        mm = ModemManager()
        modem_list = mm.list_modems()
        if modem_list:
            for modem in modem_list.values():
                props1 = modem.get_modem_property('Manufacturer')
                props2 = modem.get_modem_property('Model')
                modem_name = f"{props1} {props2}"
                self.modem_names.append(modem_name)
                self.modems[modem_name] = modem
        else:
            print("No modems found.")

    def get_modem_names(self):
        return self.modem_names
    def get_modem_list_length(self):
        mm = ModemManager()
        modem_list = mm.list_modems()
        return len(modem_list)
    
    def enable_modem(self, modem_name):
        # modem_name = modem_name
        if modem_name in self.modems:
            print(f"testing just after if {self.modems}")
            modem = self.modems[modem_name]
            print(f"after after {modem}")
            modem.enable()
            print(f"Enabled modem: {modem_name}")
            print(f"modem to be returned {modem}")
            return modem
        else:
            print(f"Modem {modem_name} not found")
    
    def get_modem_properties(self, modem_name):
        # modem_name = modem_name
        properties_list = []
        if self.enable_modem(modem_name):
            properties = {}
            modem = self.modems[modem_name]
            properties['Manufacturer'] = modem.get_modem_property('Manufacturer')
            properties['Model'] = modem.get_modem_property('Model')
            properties['DeviceIdentifier'] = modem.get_modem_property('DeviceIdentifier')
            properties['EquipmentIdentifier'] = modem.get_modem_property('EquipmentIdentifier')
            properties['PrimaryPort'] = modem.get_modem_property('PrimaryPort')
            properties['Imei'] = modem.get_3gpp_property('Imei')
            properties['OperatorCode'] = modem.get_3gpp_property('OperatorCode')
            properties['OperatorName'] = modem.get_3gpp_property('OperatorName')

            properties_list.append(properties)
        else:
            return[f"{modem_name} is not enabled"]
        return properties_list
        

    def get_properties(self):
        mm = ModemManager()
        modem_list = mm.list_modems()
        property_list = []
        if modem_list:
            for modem in modem_list.values():
                properties = {}
                properties['Manufacturer'] = modem.get_modem_property('Manufacturer')
                properties['Model'] = modem.get_modem_property('Model')
                properties['DeviceIdentifier'] = modem.get_modem_property('DeviceIdentifier')
                properties['EquipmentIdentifier'] = modem.get_modem_property('EquipmentIdentifier')
                properties['PrimaryPort'] = modem.get_modem_property('PrimaryPort')
                # properties['Imei'] = modem.get_3gpp_property('Imei')
                # properties['OperatorCode'] = modem.get_3gpp_property('OperatorCode')
                # properties['OperatorName'] = modem.get_3gpp_property('OperatorName')

                

                self.modem_names.append(properties['Manufacturer'])
                self.modems[properties['Manufacturer']] = modem

                property_list.append(properties)
        else:
            print("No modems found.")

        return property_list

    def get_test(self):
        mm = ModemManager()
        modem_list = mm.list_modems()
        property_list = []
        if modem_list:
            for modem in modem_list.values():
                properties = {}
                properties['Manufacturer'] = modem.get_modem_properties()
                self.modem_names.append(properties['Manufacturer'])
                self.modems[properties['Manufacturer']] = modem

                property_list.append(properties)
        else:
            print("No modems found.")

        return property_list
        


handler = ModemHandler()
handler.handle_modem_connected()

modem_names = handler.get_modem_names()
# modem_list = handler.get_modem_list_length()
# print("Available Modems:")
# for modem_name in modem_names:
#     print("- ", modem_name)
    

# print("Modem List:", modem_list)
# if modem_names:
#     first_modem = modem_names[0]
#     print("Enabling modem:", first_modem)
#     handler.enable_modem(first_modem)
# else:
#     print("No modems found.")


# first_modem = modem_names[0]
# handler.enable_modem(first_modem)
# print("Properties for first modem:", first_modem)
# properties_list = handler.get_modem_properties(first_modem)
# for properties in properties_list:
#     print("Manufac:", properties['Imei'],first_modem)
#     print("Manufac:", properties['OperatorCode'],first_modem)
#     print("Manufac:", properties['OperatorName'],first_modem)


# handler = ModemHandler()
# properties_list = handler.get_properties()
# print("listing", properties_list)

# for properties in properties_list:
#     print("Operator Name:", properties['Manufacturer'])
