# creating class

# class User:
#   pass
#
# user1 = User()
# user1.id = "111"
# user1.name = "monu"
#
# print(user1.name)


class User:

  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username

    