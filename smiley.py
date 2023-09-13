import turtle as t

screen = t.Screen()
screen.setup(width=1000, height=1000)     
screen.bgcolor("white")

# создаем черепашку
pen = t.Turtle()
pen.speed(20)

#face
pen.penup()
pen.goto(0, -200)                       
pen.pendown()
pen.begin_fill()                        
pen.color("yellow")                     
pen.circle(200)                         
pen.end_fill()                          

#eye
pen.penup()
pen.goto(-80, 50)                       
pen.pendown()
pen.begin_fill()                       
pen.color("white")                      
pen.circle(40)                           
pen.end_fill()                         

pen.penup()
pen.goto(80, 50)
pen.pendown()
pen.begin_fill()
pen.color("white")
pen.circle(40)
pen.end_fill()

#pupils
pen.penup()
pen.goto(-80, 80)
pen.pendown()
pen.begin_fill()
pen.color("black")
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(80, 80)
pen.pendown()
pen.begin_fill()
pen.color("black")
pen.circle(20)
pen.end_fill()

#smile
pen.setheading(270)

pen.penup()
pen.goto(-100, -30)
pen.pendown()
pen.begin_fill()
pen.color("black")
pen.circle(100, 180)
pen.end_fill()

pen.penup()
pen.goto(10, 0)
pen.pendown()
pen.begin_fill()
pen.color("orange")
pen.circle(10)
pen.end_fill()



pen.hideturtle()                        

t.done()

