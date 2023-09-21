import turtle


screen = turtle.Screen()
screen.bgcolor("white")

semi_major_axis = 150 ## ig we can customize this to user defined but note major axis needs to be way bigger than minor axis 
semi_minor_axis = 5

screen.setup(semi_major_axis*1,semi_minor_axis*1)


ellipse = turtle.Turtle()
ellipse.speed(1)

# Function to draw an ellipse
def draw_ellipse(semi_major_axis, semi_minor_axis):
    ellipse.penup()
    ellipse.goto(-semi_major_axis, 0)  # Start from the left end of the major axis
    ellipse.pendown()
    ellipse.setheading(45) #dont change this , its a specific angle to make the ellipse
    
    # Draw the left half of the ellipse
    for _ in range(2):
        ellipse.circle(semi_minor_axis, 90)
        ellipse.circle(semi_major_axis, 90)  # Note that we swap semi-major and semi-minor axes here


draw_ellipse(semi_major_axis, semi_minor_axis)

ellipse.done()
