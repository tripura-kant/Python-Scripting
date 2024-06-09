import smtplib

my_email = "tripurakanttest@gmail.com"
password = "dzpc djzm vkwn zdcq"
print("email start")
connection = smtplib.SMTP("smtp.gmail.com") 
connection.starttls()
print("email progress")
connection.login(user=my_email , password=password)
connection.sendmail(from_addr=my_email, to_addrs="tripurakant@yahoo.com", msg="hello tripura 9 jun ")
connection.close()
print("email sent")