from turtle import *
import threading
from playsound import playsound 

# _____________Function 
def play_song():
    playsound("D:\Ganpati Bappa - Song.mp3")

# ____________Start the song playback in a separate thread
song_thread = threading.Thread(target=play_song)
song_thread.start()

title("Ganpati")
bgcolor("#ffcccc")
color("#ff0000")
pensize(3)
speed(5.4)


#crown
#lower 
penup()
goto(0,200)
pendown()
left(0)
forward(100)
circle(10,180)
left(0)
forward(200)
circle(10,180)
forward(100)
penup()

#middle
setpos(0,220)
pendown()
forward(60)
circle(10,180)
left(0)
forward(120)
circle(10,180)
forward(60)
penup()

#higher
setpos(0,240)
pendown()
forward(30)
circle(10,180)
left(0)
forward(60)
circle(10,180)
forward(30)
penup()

setpos(0,260)
pendown()
circle(20,360)



#left face curve
color("red")
penup()
goto(-100,200)
pensize(2)
pendown()
right(-260)
forward(50)
circle(110,110)


penup()
goto(-56,-31)
pendown()
left(-80)
forward(50)
left(15)
circle(60,200)
forward(30)
penup()

#nose
#right face curve
goto(-54,-31)
pendown()
right(-60)
forward(20)
right(70)
forward(20)
left(130)
forward(30)


left(20)
circle(100,180)
left(-23)
forward(130)
left(20)
forward(78)
penup()

#eare
#left
goto(-101,190)
pendown()
left(40)
forward(100)
right(50)
forward(-180)


penup()
goto(-95,75)
pendown()
circle(40,-180)
penup()

#right
goto(110,190)
pendown()
left(120)
forward(100)
right(-50)
forward(-180)
circle(40,-105)
penup()

#tikka
goto(0,200)
left(-80)
pendown()
forward(30)
circle(7,185)
left(20)
forward(30)
penup()

#eyes
#right
goto(90,155)
pendown()
circle(20,-180)
penup()
left(180)
goto(100,155)
pendown()
circle(30,180)
penup()

#left

goto(-45,155)
left(180)
pendown()
circle(20,-180)
penup()
left(180)
goto(-35,155)
pendown()
circle(30,180)
penup()

# U
goto(15,197)
right(10)
pendown()
forward(30)
left(180)
circle(15,-180)
left(180)
forward(30)
penup()

#teet
goto(0,20)
left(130)
pendown()
forward(60)
right(150)
forward(50)
penup()

#neck
goto(-70,30)
left(120)
pendown()
circle(200,30)
penup()

#Left Hand
goto(-150,-120)
right(128)
right(30)
pendown()
forward(40)
left(60)
forward(40)
right(30)
forward(15)
circle(10,200)
right(20)
forward(50)

right(180)
forward(60)
circle(80,50)
left(50)
circle(100,100)
right(20)
forward(20)
left(50)
circle(100,83)
penup()

#modak

goto(235,0)
right(180)
pendown()
circle(150,34)
left(85)
circle(230,20)
left(85)
circle(110,55)
penup()

#left hand
goto(297,-70)
pendown()
circle(10,360)
left(90)
circle(4,180)
penup()
goto(280,-100)
pendown()

left(30)
circle(10,180)
right(180)
circle(10,180)
right(180)
circle(10,180)
right(180)
circle(10,180)
left(60)
circle(78,60)
left(110)

penup()

#neck2
goto(200,-10)
right(-10)
pendown()
circle(390,9)
penup()

#bottum left curve
goto(-30,-260)
pendown()
circle(500,30)
circle(50,180)
right(5)
circle(700,20)
#bottum right curve
right(30)
forward(280)
circle(50,180)
circle(500,32)
penup()

#leag
goto(-30,-280)
right(20)
pendown()
circle(150,30)
left(130)
forward(30)
circle(60,90)

#stomach
penup()
goto(-200,-150)
pendown()
right(150)
circle(100,50)

penup()
goto(250,-110)
pendown()
left(25)
right(90)
circle(-140,50)

penup()
goto(0,-200)
pendown()
circle(4)
ht()


#text
pencolor("orange")
write("\t\t\t\tHappy Ganesh Chaturthi.", font=("balloon", 15, "normal"), align="left")
penup()
right(35)
forward(380)
pendown()
pencolor("gray")
write("Created by Shubham Kapase & \nPrabuddha Sonalkar.", font=("balloon", 10, "normal"), align="right")

done()