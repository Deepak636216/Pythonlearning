from turtle import Turtle,Screen
import random

t_color=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
the_turtle=Turtle()
the_turtle.shape("turtle")
the_turtle.pensize(15)
the_turtle.forward(50)
the_turtle.setheading(90)
the_turtle.forward(10)
the_turtle.setheading(180)
the_turtle.forward(50)

# for i in range(10):
#         the_turtle.color(random.choice(t_color))
#         the_turtle.forward(10)
#         the_turtle.penup()
#         the_turtle.forward(15)
#         the_turtle.pendown()
    


screen=Screen()
screen.exitonclick()

# Turtle.colormode(255)
# def random_color():
    # r=random.randint(0,255)
    # g=random.randint(0,255)
    # b=random.randint(0,255)
    # random_colors=(r,g,b)
    # return random_colors


# the_turtle.speed("fastest")
# # def draw_shape(num_sides):
# #     angle=360/num_sides
# #     for _ in range(num_sides):    
# #         the_turtle.forward(100)
# #         the_turtle.right(angle)

# # for i in range(3,10):
# #     the_turtle.color(random.choice(t_color))
# #     draw_shape(i)

# dir=[0,90,180,270,360]
# for _ in range(100):
#     the_turtle.color(random.choice(t_color))
#     the_turtle.forward(30)
#     the_turtle.right(random.choice(dir))