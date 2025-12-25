import turtle
import time

x = 0

#Intro window
wn = turtle.Screen( )
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Cursor
CURSOR_SIZE = 20
FONT_SIZE = 12

#Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.goto(0,0)
title.hideturtle()
title.write("PONG", align = "center", font=("Arial", 100, "bold"))
title.dy = 4

#Next Button
next_button = turtle.Turtle()
next_button.shape("square")
next_button.shapesize(stretch_wid=2, stretch_len=10)
next_button.speed(0)
next_button.fillcolor("white")
next_button.penup()
next_button.goto(0,-150)


#Next Text
next_text = turtle.Turtle()
next_text.speed(0)
next_text.color("black")
next_text.penup()
next_text.goto(0,-150)
next_text.hideturtle()
next_text.write("Next..", align='center', font=('Arial', 40, "bold"))


wn.update()


