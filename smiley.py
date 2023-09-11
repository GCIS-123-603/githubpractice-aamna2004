import turtle

turtle=turtle.Turtle()

def draw_circle():
    turtle.color('red','blue')
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    

def main():
    draw_circle()
    input("enter to continue..")

main()
