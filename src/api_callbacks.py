from src.modem_manager import ModemManager
from src.modem import Modem
from src.messaging import Messaging
from src.sms import SMS
from src.api import get_messages 


class ModemHandler:
    def __init__(self):
        self.modem_names = []
        self.modems = {}
        # self.modem = 
        self.messaging = None
        self.modem_manager = ModemManager()

    def handle_modem_connected(self):
        mm = ModemManager()
        modem_list = self.modem_manager.list_modems()
        print(f"modem list:{modem_list}")
        if modem_list:
            modem_paths = list(modem_list.keys())
            for modem_path in modem_paths:
                self.get_gm(modem_path)
            print(f"modem path {modem_paths}")
            for modem in modem_list.values():
                props1 = modem.get_modem_property('Manufacturer')
                props2 = modem.get_modem_property('Model')
                modem_name = f"{props1} {props2}"
                self.modem_names.append(modem_name)
                self.modems[modem_name] = modem
                self.messaging = Messaging(modem)

                # message_paths = self.messaging.check_available_messages_test()

                # for message_path in message_paths:
                #     sms = SMS(message_path=message_path, messaging=self.messaging)
                #     self.incoming_messages_test(sms)
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
                self.modem_names.append(properties['Manufacturer'])
                self.modems[properties['Manufacturer']] = modem

                property_list.append(properties)
        else:
            print("No modems found.")

        return property_list
    
    def get_incoming_messages(self, modem):
        messages = self.messaging.check_available_messages()
        # messages.
        print(f"this {messages}")
    
    def incoming_messages_test(self, sms ):
        text, number, timestamp = sms.new_received_message()
        print(f"Text: {text}")
        print(f"Number: {number}")
        print(f"Timestamp: {timestamp}")

        # message_path = self.messaging.mess

        msg = SMS.new_received_message(self)
        print(f"msg {msg}")
    
    def get_gm(self, modem_path):
        gm_msg = get_messages(modem_path, self.modem_manager)
        print(f"gm msg {gm_msg}")


handler = ModemHandler()
handler.handle_modem_connected()

modem_names = handler.get_modem_names()

first_modem = modem_names[0]
handler.enable_modem(first_modem)
print("Properties for first modem:", first_modem)
properties_list = handler.get_modem_properties(first_modem)
for properties in properties_list:
    print("Manufac:", properties['Imei'],first_modem)
    print("Manufac:", properties['OperatorCode'],first_modem)
    print("Manufac:", properties['OperatorName'],first_modem)
    
msg = handler.get_incoming_messages(first_modem)
print(f"message check {msg}")
# handler.incoming_messages_test(first_modem)
print(f"antoerh {handler.get_gm(first_modem)}")