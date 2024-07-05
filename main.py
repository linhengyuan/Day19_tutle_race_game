from turtle import Turtle, Screen
import random

jimmi = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red", "blue", "purple", "orange", "yellow"]

y_axis = -100
turtle_list = []
is_race_on = True

for turtle_index in range(5):
    turtle_object = Turtle(shape="turtle")
    turtle_object.penup()
    turtle_object.color(color_list[turtle_index])
    turtle_object.goto(x=-230, y=y_axis)
    y_axis += 50
    turtle_list.append(turtle_object)

while is_race_on:

    for turtle in turtle_list:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"you win! the winner is {turtle.pencolor()}")
            else:
                print(f"you lost! the winner is {turtle.pencolor()}")

screen.exitonclick()
