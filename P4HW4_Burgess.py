# A brief description of the project
# 03/19/2019
# CTI-110 P4HW4 - Nested Loop
# Your Name
#


import turtle

def side():
    for i in range(3):
        for i in range(3):
            turtle.forward(10*5/3)
            turtle.backward(10*5/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10*5/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10*5/3)
        


for i in range(8):
    side()
    turtle.left(45)
