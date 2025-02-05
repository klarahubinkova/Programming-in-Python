# POZOR! Program se želvou se nesmí jmenovat "turtle.py", jinak dochází ke konfliktům jmen.
from turtle import forward, right, left, shape, penup, pendown, exitonclick

# Změní tvar
shape('turtle')

# Posune se dopředu
forward(50)
# Otočí se o 90° doprava
right(90)

# Zvedne pero (přestane psát)
penup()
forward(50)
# Položí pero (začne psát)
pendown()

# Otočí se doleva o 90°
left(90)
forward(50)

# Okno s želvou se nezavře automaticky hned po doběhnutí programu, čeká na manuální zavření
exitonclick()
