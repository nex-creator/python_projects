# from turtle import Turtle, Screen
# import another_module
# print(another_module.another_variable)
# timmy = Turtle()
# print(timmy)
# print(timmy.shape("turtle"))
# print(timmy.color("red","black"))
# print(timmy.forward(100))
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)
table.align = "r"
print(table)