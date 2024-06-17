from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
screen.listen()

def move_forward():
    tim.forward(20)
def move_backward():
    tim.backward(20)
def move_up():
    tim.right(90)
    
def move_down():
    tim.left(90)
def screen_clear():    
    tim.clear()

screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=move_up)
screen.onkey(key="a",fun=move_down)
screen.onkey(key="c",fun=screen_clear)

screen.exitonclick()