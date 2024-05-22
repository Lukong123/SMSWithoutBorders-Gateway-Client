# from src.api_callbacks import callback_function, callback_modemlist, callback_modem_name
from src.api_callbacks_prime import callback_function_name
from src.modem import Modem


class MockModem:
    pass

# Create a MockModem object
# modem = MockModem()
modemd = Modem()

# Call the callback_function with the MockModem object
# result = callback_function(modem)
# modemlist= callback_modemlist(modem)
modemname = callback_function_name(modemd)

# Print the result
# print("Modem list length:", result)
# print("Modem list :", modemlist)
print("Modem Name :", modemname)

