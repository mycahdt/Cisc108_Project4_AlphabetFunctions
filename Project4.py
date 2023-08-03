# Project 4- Turtle Functions
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

# Setup turtles; don't need to change these
import turtle
turtle.reset()
turtle.speed(10)
turtle.penup()
turtle.goto(-385, 240)
turtle.pendown()
turtle.speed(3)
#hi iwas here
###############################################################
# Part 1) Turtle Functions
# Define all of your turtle functions here.

#CONFIDENCE - CONFIDE
#LEADERSHIP - LARSHP

def draw_C(x_pos: int, y_pos: int) -> int:
    turtle.goto(x_pos,y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_O(x_pos: int, y_pos: int) -> int:
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_N(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(45)
    turtle.goto((x_pos+50),(y_pos-50))
    turtle.left(135)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80
  

def draw_F(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_I(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.penup()
    return x_pos + 80


def draw_D(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.goto((x_pos+50),(y_pos-25))
    turtle.goto(x_pos, y_pos)
    turtle.penup()
    return x_pos + 80
  
def draw_E(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_L(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_A(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    return x_pos + 80


def draw_R(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(90)
    turtle.goto((x_pos+50), (y_pos-12.5))
    turtle.goto(x_pos, (y_pos-25))
    turtle.goto((x_pos+50),(y_pos-50))
    turtle.penup()
    turtle.goto(x_pos, (y_pos-50))
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    return x_pos + 80


def draw_S(x_pos: int, y_pos: int):
    turtle.goto((x_pos+50), (y_pos-10))
    turtle.pendown()
    turtle.goto((x_pos+25), y_pos)
    turtle.goto(x_pos, (y_pos-10))
    turtle.goto((x_pos+50), (y_pos-40))
    turtle.goto((x_pos+25), (y_pos-50))
    turtle.goto(x_pos, (y_pos-40))
    turtle.penup()
    return x_pos + 80

def draw_H(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.penup()
    return x_pos + 80


def draw_P(x_pos: int, y_pos: int):
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.penup()
    return x_pos + 80
  


###############################################################
# Part 2) Original Words
# Rewrite your original words here, modifying the code below


#Writes "CONFIDENCE" at (-385, 240)
x_position = draw_C(-385, 240)
x_position = draw_O(x_position, 240)
x_position = draw_N(x_position, 240)
x_position = draw_F(x_position, 240)
x_position = draw_I(x_position, 240)
x_position = draw_D(x_position, 240)
x_position = draw_E(x_position, 240)
x_position = draw_N(x_position, 240)
x_position = draw_C(x_position, 240)
draw_E(x_position, 240)


#Writes "LEADERSHIP" at (-385, 180)
x_position = draw_L(-385, 180)
x_position = draw_E(x_position, 180)
x_position = draw_A(x_position, 180)
x_position = draw_D(x_position, 180)
x_position = draw_E(x_position, 180)
x_position = draw_R(x_position, 180)
x_position = draw_S(x_position, 180)
x_position = draw_H(x_position, 180)
x_position = draw_I(x_position, 180)
draw_P(x_position, 180)



###############################################################
# Part 3) New Words
# Write your new words here. Make sure all words are readable.

#elf, fan, dip, can, hop, hip, cap
#inch, face, half, crop, chin, help, cafe, flap, flop, flip, clap, chef, calf, cape, epic
#pinch, child, peach, chips, cheap, pecan, chief
#flinch, falcon, cipher, placed,
#spinach, dolphin
#fishpond
#franchise

#franchise, dolphin, cipher, peach, inch, elf

#Writes "FRANCHISE" at (-385, 120)
x_position = draw_F(-385, 120)
x_position = draw_R(x_position, 120)
x_position = draw_A(x_position, 120)
x_position = draw_N(x_position, 120)
x_position = draw_C(x_position, 120)
x_position = draw_H(x_position, 120)
x_position = draw_I(x_position, 120)
x_position = draw_S(x_position, 120)
draw_E(x_position, 120)

#Writes "DOLPHIN" at (-385, 60)
x_position = draw_D(-385, 60)
x_position = draw_O(x_position, 60)
x_position = draw_L(x_position, 60)
x_position = draw_P(x_position, 60)
x_position = draw_H(x_position, 60)
x_position = draw_I(x_position, 60)
draw_N(x_position, 60)

#Writes "CIPHER" at (-385, 0)
x_position = draw_C(-385, 0)
x_position = draw_I(x_position, 0)
x_position = draw_P(x_position, 0)
x_position = draw_H(x_position, 0)
x_position = draw_E(x_position, 0)
draw_R(x_position, 0)

#Writes "PEACH" at (-385, -60)
x_position = draw_P(-385, -60)
x_position = draw_E(x_position, -60)
x_position = draw_A(x_position, -60)
x_position = draw_C(x_position, -60)
draw_H(x_position, -60)

#Writes "INCH" at (-385, -120)
x_position = draw_I(-385, -120)
x_position = draw_N(x_position, -120)
x_position = draw_C(x_position, -120)
draw_H(x_position, -120)

#Writes "ELF" at (-385, -180)
x_position = draw_E(-385, -180)
x_position = draw_L(x_position, -180)
draw_F(x_position, -180)

#240, 180, 120, 60, 0, -60, -120, -180
#y values -> -120, -280, -240, -300, +180, +240, +300 

###############################################################
# Wrap-up turtles; don't need to change this
turtle.mainloop()


