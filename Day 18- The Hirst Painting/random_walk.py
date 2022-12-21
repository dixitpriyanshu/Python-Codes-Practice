from turtle import Turtle, Screen
import random

timmy = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270, 360]
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))












Screen = Screen()
Screen.exitonclick()