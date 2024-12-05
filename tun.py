#mẫu vẽ hình
import turtle
from playsound import *
win = turtle.Screen()
win.title("Code Tặng bé cụt")
win.register_shape("pen2.gif")
pen = turtle.Pen()
pen.speed(1)
pen.shape("pen2.gif")
pen.penup()
file =open('vietnam.txt', 'r')
vietnams = file.readlines()
pen.color("red", "red")
count = 0
for vietnam in vietnams:
    viet = vietnam.strip().split()
    pen.goto(float(viet[0]), float(viet[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
        playsound("haokhivietnam.wav", False)
        count +=1
        pen.end_fill()
        pen.penup()

        file = open ('saovang.txt', 'r')
saovangs = file.readlines()
pen.color("yellow", "yellow")
count = 0
for sao in saovangs:
    s = sao.strip().split()
    pen.goto(float(s[0]), float(s[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
        playsound("haokhivietnam.wav", False)
        count +=1
        pen.end_fill()
        pen.penup()

        pen.color("red", "red")
        pen.pensize(2)
        file = open('cacdao.txt', 'r')
        cacdao = file.readlines()
        file.close()
        count = 0
        for dao in cacdao:
            count += 1
            d = dao.strip().split()
    pen.goto(float(d[0]), float(d[1]))
    if count  % 7 == 0:
        pen.end_fill()
        pen.penup
pen.hideturtle()
