import datetime
import random

import pywhatkit

# Initialize current minute
current_minute = datetime.datetime.now().minute

with open('/Users/tripurakant/Documents/Imp-folder/py/Python-Scripting/250questions/messages.txt', 'r') as file:
    messages = file.readlines()

while True:
    # Increment the current minute by 1
    current_time = datetime.datetime.now()
    current_minute += 1
    formatted_time = current_time.strftime("%H:%M:%S")
    random_message = random.choice(messages).strip()
    # Wait for 1 minute (60 seconds) before sending the next message
    # time.sleep(.10)

    # Send a WhatsApp message to the specified number
    # pywhatkit.sendwhatmsg("+917008460780",
    #                       "Geeks For Geeks!",
    #                       datetime.datetime.now().hour, current_minute)
    pywhatkit.sendwhatmsg("+918544425434",

                          f"{random_message} Current time: {datetime.datetime.now()}",
                          datetime.datetime.now().hour, current_minute)
