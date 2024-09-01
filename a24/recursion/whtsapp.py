import pywhatkit as kit
from datetime import datetime, timedelta

# Get the current time
now = datetime.now()

# Add one minute to the current time
send_time = now + timedelta(minutes=1)

# Extract the hours and minutes
hour = send_time.hour
minute = send_time.minute

# Define the phone number and message
phone_number = "+919899800837"
message = "Good Morning. How are you ?"

# Send the WhatsApp message
kit.sendwhatmsg(phone_number, message, hour, minute)
