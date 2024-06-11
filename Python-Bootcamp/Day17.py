# creating class

# class User:
#   pass
#
# user1 = User()
# user1.id = "111"
# user1.name = "monu"
#
# print(user1.name)

# class User:
#   def __init__(self, user_id, username, roll_no):
#     self.id = user_id
#     self.username = username
#     self.roll_no = roll_no

# User1 = User("001", "tripura", "13")
#
# print(User1.username)
# print(User1.id)
# print(User1.roll_no)


class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer

Question1 = Question("2+3=5", True)


print(Question1)