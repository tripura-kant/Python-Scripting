import smtplib

my_email = "tripurakanttest@gmail.com"
password = "dzpc djzm vkwn zdcq"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email , password=password)