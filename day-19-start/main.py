from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title= "Make your bet",prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []
print(user_bet)
for turtle_index in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y =y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is wining.")
            else:
                print(f"You have lost! The {winning_color} turtle is wining.")
        rand_distance =  random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()