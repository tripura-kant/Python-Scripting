# This is file 60.py

import datetime
import random
import time

import pywhatkit

# Read the messages from the text file
with open('/Users/tripurakant/Documents/Imp-folder/py/Python-Scripting/250questions/messages.txt', 'r') as file:
    messages = file.readlines()

while True:
    # Get the current time
    current_time = datetime.datetime.now()

    # Format the current time as a string
    formatted_time = current_time.strftime("%H:%M:%S")

    # Choose a random message from the list
    random_message = random.choice(messages).strip()

    # Send a WhatsApp message to the specified number with the random message and current time
    pywhatkit.sendwhatmsg("+917008460780",
                          f"{random_message} Current time: {formatted_time}",
                          current_time.hour, current_time.minute)

    # Wait for 1 minute (60 seconds) before sending the next message
    time.sleep(60.0)
