import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()

def random_color():
    r =  random.randint(0, 255)
    g =  random.randint(0, 255)
    b =  random.randint(0, 255)
    return (r, g, b)

def draw_circles(size_of_gap):
    angle = int(360/size_of_gap)
    for _ in range(angle):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()  + size_of_gap)

timmy.speed("fastest")

draw_circles(10)


Screen = t.Screen()
Screen.exitonclick()