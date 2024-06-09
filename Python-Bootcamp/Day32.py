import smtplib

my_email = "tripurakanttest@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user= , password=)