from turtle import forward, penup, pendown, exitonclick

# Vykreslí přerušovanou čáru
for _ in range(10):
    pendown()
    forward(10)
    penup()
    forward(10)

exitonclick()