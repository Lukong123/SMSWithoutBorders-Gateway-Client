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


# def callback_function(Modem):
#     # pp = modem.enable
#     props1 = Modem.get_modem_property('Manufacturer')
#     props2 = Modem.get_modem_property('Model')

#     modem_name = f"{props1} {props2}"


#     print(modem_name)


# mm = ModemManager()
# mm.add_modem_connected_handler(callback_function)
# # modem_list = mm.list_modems()
# # print(modem_list)
# # print("enabling....", Modem.enable)
# # modem_list_length= len(modem_list)
# # print(modem_list_length)


# mm.daemon()


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
        if modem_name in self.modems:
            modem = self.modems[modem_name]
            modem.enable = True
            print(f"Enabled modem: {modem_name}")
        else:
            print(f"Modem '{modem_name}' not found")
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
                # properties['Imei'] = modem.get_modem_property('Imei')
                # properties['OperatorCode'] = modem.get_modem_property('OperatorCode')
                # properties['OperatorName'] = modem.get_modem_property('OperatorName')
                # properties['EquipmentIdentifier'] = modem.get_3gpp_property('NetworkNotification')

                

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
        


# handler = ModemHandler()
# handler.handle_modem_connected()

# modem_names = handler.get_modem_names()
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

handler = ModemHandler()
properties_list = handler.get_properties()
print("listing", properties_list)

for properties in properties_list:
    print("IMEI:", properties['DeviceIdentifier'])