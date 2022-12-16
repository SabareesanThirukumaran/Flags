from turtle import *

t = Turtle()

# setting the turtle graphics
pensize(3)
bgcolor('black')
speed(10)
goto(-130, 0)

# white color
color('white')
begin_fill()

# white background
left(90)
forward(280)
right(90)
forward(400)
right(90)
forward(280)
right(90)
forward(400)
end_fill()

# red color
color('red')

# red section
up()
goto(-130, 120)
down()
begin_fill()
left(180)
forward(180)
right(90)
forward(120)
left(90)
forward(40)
left(90)
forward(120)
right(90)
forward(180)
left(90)
forward(40)
left(90)
forward(180)
right(90)
forward(120)
left(90)
forward(40)
left(90)
forward(120)
right(90)
forward(180)
left(90)
forward(40)
end_fill()
