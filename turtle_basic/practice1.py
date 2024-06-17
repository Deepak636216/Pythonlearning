from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Make ur guess",prompt="which color turtle wins... ")

colors=["red", "green", "blue", "orange", "yellow", "purple"]
y_cord=[-80,-50,-20,10,40,70]
all_turtles=[]

for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()     
    tim.goto(x=-230,y=y_cord[i])
    all_turtles.append(tim)

if user_bet:
    race_on=True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print("You won!")
            else:
                print(f"You lost!{winning_color} won")

        rand_dist=random.randint(0,15)
        turtle.forward(rand_dist)    


screen.exitonclick()