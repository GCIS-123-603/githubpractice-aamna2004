import turtle 

angle = 90 #global variable 

def testdrive(): # to practice all in built functions of turtle
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

def square(a,b,c): # display of 3 squares which fill up with given color
    turtle.pensize(10)
    turtle.pencolor('pink')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.left(angle)
       
    for i in range(4):
        turtle.forward(b)
        turtle.left(angle)
        
    for i in range(4):
        turtle.forward(c)
        turtle.left(angle)
    turtle.end_fill()
        
#turtle.done() # comment this statement to execute the triangle function 

def triangle(side):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.done()    
        

def main():
    testdrive() 
    turtle_state()

    #square func below
    a=int(input("Enter the length of the 1st square :")) 
    b=int(input("Enter the length of the 2nd square :"))
    c=int(input("Enter the length of the 3rd square :"))
    square(a,b,c) 
    
    #tiangle func below 
    side=int(input("Enter the length of the triangle :"))
    triangle(side)
    
main()

 #         turtle.done() # to keep turtle window open after execution    #
