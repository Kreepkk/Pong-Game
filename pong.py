import turtle
import time

wn = turtle.Screen( )
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0



#Timer
start = time.time()
count = turtle.Turtle()
count.speed(0)
count.penup()
count.hideturtle()
count.color("white")
count.goto(260, 260)
count3=0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)




# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 8
ball.dy = 8


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#End
end = turtle.Turtle()
end.color("black")
end.speed(0)
end.goto(-20,0)
end.hideturtle()




#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)




#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop
while time.time() - start < 60:
        wn.update()

        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a +=1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b +=1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        #Paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1.031 
            ball.dy *= 1.031
            
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1.031
            ball.dy *= 1.031

        #Timer
        count.clear()
        count.write(int(time.time() - start), font=("Arial", 24, "normal"))
        wn.update()
        
        if time.time() - start == 60:
            break

#End Scene
wn.clear()
nwn = turtle.Screen()
nwn.title("Game Over")
nwn.bgcolor("white")
nwn.setup(width = 800, height = 600)
nwn.tracer(0)

#End Display
if score_a > score_b:
    end.showturtle()
    end.write("Player A wins!", align = "center", font=("Arial", 60, "normal"))

elif score_a < score_b:
    end.showturtle()
    end.write("Player B wins!", align = "center", font=("Arial", 60, "normal"))
else:
    end.showturtle()
    end.write("Draw!", align = "center", font=("Arial", 60, "normal"))

        
    
