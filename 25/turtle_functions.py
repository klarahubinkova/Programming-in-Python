from turtle import forward, backward, right, left, penup, pendown, exitonclick

def M():
    pendown()

    left(90)
    forward(60)
    right(90)
    
    for i in range(2):
        forward(10)
        right(90)
        forward(10)
        left(90)
    
    forward(10)

    for i in range(2):
        left(90)
        forward(10)
        right(90)
        forward(10)
    
    right(90)
    forward(60)
    left(90)

    penup()
    forward(10)


def O():
    forward(10)
    pendown()

    left(90)

    for i in range(2):
        forward(10)
        left(90)
        forward(10)
        right(90)
        forward(40)
        right(90)
        forward(10)
        left(90)
        forward(10)
        right(90)
        forward(30)
        right(90)
    
    right(90)

    penup()
    forward(50)


def D():
    pendown()

    left(90)
    forward(60)
    right(90)
    forward(30)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(40)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)  
    forward(30)
    right(180)

    penup()
    forward(50)

def R():
    pendown()

    left(90)
    forward(60)

    for i in range(2):
        right(90)
        forward(30)
    
    right(90)
    forward(20)
    left(90)

    for i in range(2):
        forward(10)
        left(90)
        forward(10)
        right(90)
    
    forward(10)
    left(90)
    
    penup()
    forward(10)

def A():
    pendown()

    left(90)
    forward(40)

    for i in range(2):
        right(90)
        forward(10)
        left(90)
        forward(10)
    
    right(90)
    forward(10)

    for i in range(2):
        right(90)
        forward(10)
        left(90)
        forward(10)
    
    right(90)
    forward(20)
    right(90)
    forward(50)
    left(180)
    forward(50)
    right(90)
    forward(20)
    left(90)

    penup()
    forward(10)

def N():
    pendown()

    left(90)
    forward(60)
    right(90)

    for i in range(3):
        forward(10)
        right(90)
        forward(20)
        left(90)
    
    forward(10)
    left(90)
    forward(60)
    right(90)
    
    penup()
    right(90)
    forward(60)
    left(90)
    forward(10)

def Y():
    left(90)
    forward(60)
    right(180)
    pendown()

    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    left(180)
    forward(30)
    right(90)
    forward(20)
    left(90)
    forward(30)
    
    penup()

def modrany():
    penup()
    forward(-200)
    M()
    O()
    D()
    R()
    A()
    N()
    Y()

def ddmm():
    penup()
    forward(-100)
    D()
    D()
    M()
    M()

modrany()

exitonclick()
