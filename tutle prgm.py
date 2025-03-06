# 1.How to draw a star shape using turtle in Python. 

import turtle
t = turtle.Turtle()
t.speed(3)

for _ in range(5):
    t.forward(100)  
    t.right(144)   
turtle.done()

#2.Write a python function to draw a square using turtle graphics

import turtle

def draw_square(side_length):
    t = turtle.Turtle()  
    t.speed(3)  

    for _ in range(4): 
        t.forward(side_length) 
        t.right(90turtle.done() 
draw_square(100)
                
# 3.Write a python function to draw an hexagon using turle graphics

import turtle

def draw_hexagon(side_length):
    t = turtle.Turtle()  
    t.speed(3)  

    for _ in range(6):  
        t.forward(side_length) 
        t.right(60)  
    turtle.done()  
draw_hexagon(100)