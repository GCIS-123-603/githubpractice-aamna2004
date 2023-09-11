import turtle 

def testdrive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)

def turtle_state():
    print("Is Turtle down ?" ,turtle.isdown()) #checking whether the turtle pen is down or up
    print()
    print("Where is turtle heading ?" ,turtle.heading())
    print()
    print("The X coordinate of turtle is " ,turtle.xcor()) # gives x coordinate
    print()
    print("The y coordinate of turtle is ",turtle.ycor()) # gives y coordinate

def main():
    testdrive() 
    turtle_state()

main()
turtle.done() # to keep turtle window open after execution 

