import base64
import logging
import time
import datetime

from src.modem_manager import ModemManager
from src.modem import Modem
from src.messaging import Messaging
from src.sms import SMS
from src.api import get_messages, send_sms
from src.inbound import new_message_handler
from src.message_store import MessageStore
from src.ratchet import Ratchets

from smswithoutborders_libsig.protocols import (
    States,
    HEADERS,
    GENERATE_DH,
    DH,
    KDF_CK,
    KDF_RK,
    ENCRYPT,
    DECRYPT,
    CONCAT,
    DHRatchet,
)

from smswithoutborders_libsig.keypairs import Keypairs, x25519





class ModemHandler:
    def __init__(self):
        self.modem_names = []
        self.modems = {}
        self.modem_paths = []
        self.messaging = None
        self.modem_manager = ModemManager()
        self.messagestore = MessageStore()
        self.modem_imsi = ""


    def handle_modem_connected(self):
        mm = ModemManager()
        modem_list = self.modem_manager.list_modems()
        print(f"modem list:{modem_list}")
        if modem_list:
            modem_paths = list(modem_list.keys())
            for modem_path in modem_paths:
                print(f" some where up {modem_path}")
                # self.get_get_incoming_message(modem_path) 
                self.modem_paths.append(modem_path)
                
            print(f"modem pathsss {modem_paths}")
            for modem in modem_list.values():
                props1 = modem.get_modem_property('Manufacturer')
                props2 = modem.get_modem_property('Model')
                modem_name = f"{props1} {props2}"
                self.modem_names.append(modem_name)
                self.modems[modem_name] = modem
                self.messaging = Messaging(modem)
                self.modem_imsi = modem.get_sim().get_property("Imsi")
        else:
            print("No modems found.")

    def get_modem_names(self):
        return self.modem_names

    def get_modem_path(self):
        path = []
        for i in self.modem_paths:
            path.append(str(i))
            # print(f"modem path {i}")
        return path

    def get_modem_list_length(self):
        mm = ModemManager()
        modem_list = mm.list_modems()
        return len(modem_list)
    
    def enable_modem(self, modem_name):
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


    def load_incoming(self, modem_imsi=None, fetch_type='incoming') -> list:
        messages = []
        try:
            stored_messages = MessageStore().load(
                    sim_imsi=self.modem_imsi,

                    _type=fetch_type)
        except Exception as error:
            raise error

        else:
            stored_messages = sorted(stored_messages, key=lambda x: x[4], reverse=True)
            for message in stored_messages:
                ret_message = {}
                ret_message['id'] = message[0]
                ret_message['text'] = message[2]
                ret_message['number'] = message[3]
                ret_message['timestamp'] = message[4]
                ret_message['date_stored'] = message[5]
                ret_message['type'] = message[6]
                # ret_message['status'] = message[7]



                messages.append(ret_message)
        
        # print(f"incoming messages here from new function: {messages}")

        return messages
    

    def send_messages(self,  text: str, number: str, modem_imsi ):
        try:

            # # modem = modem_manager.get_modem(modem_path)
            # alice = x25519("alice_keys.db")
            # alice_public_key_original = alice.init()

            # bob = x25519("bob_keys.db")
            # bob_public_key_original = bob.init()

            # SK = alice.agree(bob_public_key_original)
            # SK1 = bob.agree(alice_public_key_original)
            # # original_plaintext = b"Sending double ratchet messsage"

            # alice_state = States()
            # text_base64 = base64.b64encode(text.encode('utf-8'))

            # Ratchets.alice_init(
            #     alice_state, SK, bob_public_key_original, "alice_keys"
            # )
            # header, alice_ciphertext = Ratchets.encrypt(
            #     state=alice_state,
            #      data=text_base64, AD=bob_public_key_original
            # )

            # print(f"alice cipher text: {alice_ciphertext}")


            # s_header = header.serialize()
            # a_header1 = HEADERS.deserialize(s_header)

            timestamp = time.time()

            message_id = MessageStore().store(
                modem_imsi, text, number,
                timestamp, 'outgoing', 'sending')

            msg = self.messaging.send_sms( text, number)
            logging.debug("Modem IMSI: %s", modem_imsi)
            logging.debug("message success text:%s, and number: %s ", text,number)
            logging.info("sent sms successfully! info")
            logging.info("Message Id: %s", message_id)
        
        except Exception as error:
            logging.exception(f"exception as an error for sent message: {error}")


    def load_outgoing(self, modem_imsi, fetch_type='outgoing') -> list:
        messages = []
        try:
            stored_messages = MessageStore().load(
                    sim_imsi=modem_imsi,

                    _type=fetch_type)
        except Exception as error:
            raise error

        else:
            for message in stored_messages:
                ret_message = {}
                ret_message['id'] = message[0]
                ret_message['text'] = message[2]
                ret_message['number'] = message[3]
                # ret_message['timestamp'] = message[4]
                timestamp_unix = float(message[4])
                timestamp_seconds = timestamp_unix // 1000  # Convert milliseconds to seconds
                timestamp_ms = timestamp_unix % 1000  # Extract milliseconds
                # timestamp_dt = datetime.datetime.fromtimestamp(timestamp_seconds) + datetime.timedelta(milliseconds=timestamp_ms)
                timestamp_dt = datetime.datetime.utcfromtimestamp(timestamp_seconds) + datetime.timedelta(milliseconds=timestamp_ms)
                ret_message['timestamp'] = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
    
                ret_message['date_stored'] = message[5]
                ret_message['type'] = message[6]
                # ret_message['status'] = message[7]



                messages.append(ret_message)
        
        # print(f"messages here outgoing: {messages}")

        return messages
    
    def delete_message(self, message_id) -> int:
        try:
            row_count = MessageStore().delete(message_id)
            logging.info("Message with id %s deleted successfully!!", message_id)
        except Exception as error:
            raise error
    
        return row_count
    
    def clearing_stack(self):
        # Put in an exception and print the exceptions
        if self.messaging.clear_stack():

            print("stack cleared")
            print("stack cleared")
        else:
            print("not cleared")
            print("not cleared")
            print("not cleared")

        


        
    # def get_messages(self, )

    # def sending_api(self, modem_path, text, number ):
    #     try:
    #         print("api sending try")
    #         modem_handler = ModemHandler() 
    #         api_send = send_sms(modem_path, text, number, modem_manager=modem_handler)
    #         print(f"api send return type of a thing {api_send}")
    #     except Exception as error:
    #         print(error)
    #         print("api's own error")




handler = ModemHandler()
handler.handle_modem_connected()

modem_names = handler.get_modem_names()

first_modem = modem_names[0]
# handler.enable_modem(first_modem)
# # print("Properties for first modem:", handler.get_modem_properties(first_modem))
# properties_list = handler.get_modem_properties(first_modem)
# test_apisend = handler.sending_api(first_modem,"Testing that sending api send", "687022472" )
# test_getget = handler.get_get_incoming_message(  '/org/freedesktop/ModemManager1/Modem/1')

# test_send = handler.send_messages(  "should delete","687022472", first_modem)
# test_delete = handler.delete_message('13')
# test_load_incoming = handler.load_incoming(  first_modem)
handler.clearing_stack()
# test_load_incoming = handler.load_incoming(  first_modem)

# test_load_outgoing = handler.load_outgoing(  first_modem)



# for properties in properties_list:
#     print("Manufac:", properties['Imei'],first_modem)
   