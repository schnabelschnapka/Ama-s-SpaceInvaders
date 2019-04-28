#Space Inaders


import turtle


#Screen Setup (generate Window) ###################################
wn  = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


#Draw border ######################################################
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("yellow")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    #drawing corner
    border_pen.lt(90)
border_pen.hideturtle()


#player ############################################################
player = turtle.Turtle()
#color
player.color("blue")
#form
player.shape("triangle")
player.penup()
#Player Speed  0 = fastest
player.speed(0)
#position
player.setposition(0, -250)
#Player Orientation
player.setheading(90)

#Player Movement
playerspeed = 15


#Enemy's ##########################################################
enemy = turtle.Turtle()
#color
enemy.color("red")
#form
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
#position
enemy.setposition(-200, 250)
#speed
enemyspeed = 2

#Player Movement #################################################

#Player Movement left
def move_left():
    x = player.xcor()
    #moves the  player left(-=) by "playerspeed" (15)
    x -= playerspeed
    #prevents the player to be out of gamingarea left hand
    if x < -280:
        x =  - 280
    player.setx(x)

#Player Movement right
def move_right():
    x = player.xcor()
    #moves the  player right(+=) by "playerspeed" (15)
    x += playerspeed
    #prevents the player to be out of gamingarea right hand
    if x > 280:
        x = 280
    player.setx(x)
    
#Keyboard bindings ##############################################
turtle.listen()
#Left Key Binding
turtle.onkey(move_left, "Left")
#Right Key Binding
turtle.onkey(move_right, "Right")

#Main loop ######################################################
while 1==1:
    
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    
    #reverse the Ememy between borders and go down
    #right border reverse
    if enemy.xcor() > 280:
        enemyspeed *= -1
        #enemy hops down by 40
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
    #left  border  reverse  
    if enemy.xcor() < -280:
        enemyspeed *= -1
        #enemy hops down by 40
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
    



delay = raw_input("Press to finish")
