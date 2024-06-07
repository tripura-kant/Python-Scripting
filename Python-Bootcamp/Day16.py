# import another_module
#
# print(another_module.tripura_kant)

# from turtle import Turtle
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
#
# myscreen =  Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable(["Pokemon Name", "Type"])
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtlle", "Water"])
table.add_row(["Charmender", "Fire"])
print(table)