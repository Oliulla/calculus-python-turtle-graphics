import time
import turtle as t

# set timing for turtle & hide turtle
time = time.time()
t.speed(1)
t.hideturtle()

# pen position start
t.penup()
t.goto(-200, -100)
t.pendown()

# X axis start
t.pen(pencolor='red', pensize=2)
t.setx(x=60)
t.pen(pencolor='black', pensize=5)
t.write('x')

# pen position start again
t.penup()
t.goto(-200, -100)
t.pendown()

# Y axis start
t.pen(pencolor='red', pensize=2)
t.sety(y=120)
t.pen(pencolor='black')
t.write('y')

# pen position start again
t.penup()
t.goto(-120, -60)
t.pendown()
t.pen(pencolor='green', pensize=2)
t.circle(110, 100)
t.pen(pencolor='red')
t.write('y = f(x)')

# pen position start again
t.penup()
t.goto(-110, -100)
t.pendown()
t.pen(pencolor='black')
t.right(45)
t.forward(200)

# pen position start here again
t.penup()
t.goto(-10, -100)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.left(35)
t.forward(143)
t.left(90)
t.forward(190)

# pen position start here again
t.penup()
t.goto(-75, -100)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.right(90)
t.forward(52)

# pen position start here again
t.penup()
t.goto(-10, -50)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.left(90)
t.forward(190)

# pen position start here again
t.penup()
t.goto(-6, 35)
t.pendown()
t.pen(pencolor='black', pensize=5)
t.write('B')

# pen position start here again
t.penup()
t.goto(-80, -50)
t.pendown()
t.pen(pencolor='black', pensize=5)
t.write('A')

# pen position start here again
t.penup()
t.goto(-62, -30)
t.pendown()
t.pen(pencolor='blue', pensize=2)
t.circle(10, -180)

# pen position start here again
t.penup()
t.goto(-50, -45)
t.pendown()
t.pen(pencolor='black', pensize=5)
t.write('A')

# pen position start here again
t.penup()
t.goto(-100, -100)
t.pendown()
t.pen(pencolor='blue', pensize=2)
t.circle(8, 180)

# pen position start here again
t.penup()
t.goto(-90, -95)
t.pendown()
t.pen(pencolor='black', pensize=4)
t.write('A')

# pen position start here again
t.penup()
t.goto(-210, 45)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.left(90)
t.forward(35)

# pen position start here again
t.penup()
t.goto(-210, -15)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.forward(35)

# pen position start here again
t.penup()
t.goto(-215, -8)
t.pendown()
t.pen(pencolor='green', pensize=2)
t.write('dy')

# pen position start here again
t.penup()
t.goto(5, 45)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.forward(35)

# pen position start here again
t.penup()
t.goto(5, -15)
t.pendown()
t.pen(pencolor='black', pensize=2)
t.forward(35)

# pen position start here again
t.penup()
t.goto(0, -8)
t.pendown()
t.pen(pencolor='green', pensize=2)
t.write('dy')

# pen position start here again
t.penup()
t.goto(-10, -110)
t.pendown()
t.right(90)
t.forward(25)

# pen position start here again
t.penup()
t.goto(-50, -110)
t.pendown()
t.forward(25)

# pen position start here again
t.penup()
t.goto(-47, -115)
t.pendown()
t.write('dx')

# pen position start here again
t.penup()
t.goto(-13, -58)
t.pendown()
t.forward(22)

# pen position start here again
t.penup()
t.goto(-51, -58)
t.pendown()
t.forward(22)

# pen position start here again
t.penup()
t.goto(-48, -64)
t.pendown()
t.write('dx')

t.done()
