import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("cyan")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the svreen updates

#snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High_score:0", align="center", font=("Courier", 24, "normal"))

#functions

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def go_left():
    if snake_head.direction!="right":
        snake_head.direction="left"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y+20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)

#keyboard button setup


wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main game loop
while True:
    wn.update()

    #check collision with border
    if snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()>290 or snake_head.ycor()<-290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

    #hide segments

        for segment in segments:
            segment.goto(1000,1000)

    #clear the segment list

        segments.clear()

    #reset the score
        score = 0

    #reset the delay

        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for collisiom
    if snake_head.distance(food) < 20:
        #movement of food in random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add segment
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

        #shorten delay

        delay -= 0.001

        #increase score

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()

        pen.write("Score:{} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #move end segment in reverse order

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        #move segments 0 at where head is 

    if len(segments)>0:
        x = snake_head.xcor()
        y = snake_head.ycor()

        segments[0].goto(x,y)

    move()
        
        #check for head collisiom with body segments

    for segment in segments:
        if segment.distance(snake_head)<20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            for segments in segments:
                segments.goto(1000,1000)
                
                #
            segments.clear()
                #reset the score
            score = 0
                # reste the delay
            delay = 0.1

            pen.clear()
            pen.write("Score:{} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
