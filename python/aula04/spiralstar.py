#Python program to draw spiral star in turtle programming
import turtle
 
t = turtle.Turtle()
side = 200
for i in range(100):
   t.forward(side)
   t.right(144) #Exterior angle of a star is 144 degree
   side = side - 2