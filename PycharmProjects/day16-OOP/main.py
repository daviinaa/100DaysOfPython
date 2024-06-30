import turtle

# import another_module
# print(another_module.variable)

# from turtle import Turtle, Screen
#
# # Name your object
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("HotPink1")
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
# object from class

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["electric", "water", "fire"])
table.align = "l"
print(table)
