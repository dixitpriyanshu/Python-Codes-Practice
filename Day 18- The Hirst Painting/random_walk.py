import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()

def random_color():
    r =  random.randint(0, 255)
    g =  random.randint(0, 255)
    b =  random.randint(0, 255)
    return (r, g, b)


direction = [0, 90, 180, 270, 360]
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(300):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))












Screen = Screen()
Screen.exitonclick()