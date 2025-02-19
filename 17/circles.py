import turtle
t = turtle.Turtle()

t.pensize(3)
t.speed(0)
colors = ["SpringGreen", "Cyan", "DarkViolet", "DeepPink", "LightSalmon", "gold"]

for index in range(36):
    t.pencolor(colors[index % len(colors)])
    t.circle(100)
    t.right(10)

turtle.exitonclick()
