from turtle import Turtle, Screen
import random
timmy = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(side):
    angle = 360/side
    for _ in  range(side):
        timmy.forward(100)
        timmy.right(angle)

for side in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(side)
    


Screen = Screen()
Screen.exitonclick()