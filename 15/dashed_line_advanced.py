from turtle import forward, penup, pendown, exitonclick

# Vykreslí přerušovanou čáru s narůstající délkou čárek
for index in range(10):
    pendown()
    forward(10 + index)
    penup()
    forward(10)

exitonclick()