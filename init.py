from classs import Super_Hero

enemy = Super_Hero('Kiril', 'best')
friend = Super_Hero('Misha', 'fly')
Super_Hero.__str__(friend)
Super_Hero.__str__(enemy)

from turtle import *
color("red")
bgcolor("black")
speed(20)
hideturtle()
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
