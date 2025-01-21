import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Set up the Turtle graphics
speed(0)  # Fastest drawing speed
bgcolor("black")  # Set background color to black
color("#f73487")  # Set the turtle color (pink)

penup()  # Lift the pen to move without drawing

# Loop through angle range to plot the heart shape
for k in range(0, 360):  # Looping through angles from 0 to 360 degrees
    radians = math.radians(k)  # Convert angle k from degrees to radians
    x = hearta(radians) * 20  # Calculate x-coordinate of the heart
    y = heartb(radians) * 20  # Calculate y-coordinate of the heart
    goto(x, y)  # Move the turtle to the calculated position
    pendown()  # Start drawing

# Optional: Return the turtle to the origin (center)
goto(0, 0)

# Finish the drawing and show the window
done()