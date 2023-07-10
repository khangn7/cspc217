# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 217 Spring 2023
# INSTRUCTOR: Jonathan Hudson
# XywaW4RTguuM0XLxXdlD
# DO NOT EDIT THE ABOVE LINES

#INFORMATION FOR YOUR TA

from SimpleGraphics import *

# STYLE CONSTANTS

# AXIS CONSTANTS

# Get user input own size of window

inp_size = 0
while inp_size < 600:   
    inp_size = input("enter integer >= 600 for window size: ")
    if inp_size.isnumeric() and len(inp_size) != 0:
        inp_size = int(inp_size)
    else:
        inp_size = 0

print(inp_size)
# Get user input to show axis

show_axis = 0
cond = True
while cond:
    show_axis = input("show axes? enter 'Y' or 'N': ")
    cond = show_axis != 'Y' and show_axis != 'N'

print(show_axis)

# Set up the window to draw in
resize(inp_size + 50, inp_size + 50)
background("black")

half_size = inp_size/2

setColor("white")
font_size = 10
setFont("Times", font_size)

if show_axis:
    
    setOutline("white")
    setFill("black")
    ellipse(25, 25, inp_size, inp_size)

    # Draw x and y axis
    line(25, 25 + half_size, 25 + inp_size, 25 + half_size)
    line(25 + half_size, 25, 25 + half_size, 25 + inp_size)

    # Draw and label x-axis ticks
    tick_length = 5

    tick_interval = inp_size/20
    tick_start = 25

    # for center
    tick_x = tick_start
    tick_y = 25 + half_size

    for i in range(-9, 10):
        tick_x += tick_interval
        if i == 0:
            continue
        line(tick_x, tick_y - tick_length, tick_x, tick_y + tick_length)
        text(tick_x, tick_y + font_size + tick_length, str(i/10))

    # Draw and label y axis ticks

    tick_x = 25 + half_size
    tick_y = tick_start

    for i in range(-9, 10):
        tick_y += tick_interval
        if i == 0:
            continue
        line(tick_x - tick_length, tick_y, tick_x + tick_length, tick_y)
        text(tick_x + font_size + tick_length, tick_y, str(-i/10))

# Draw the NESW lettering always

nesw = {
    'N': [25 + half_size, font_size], 
    'S': [25 + half_size, 50 + inp_size - font_size], 
    'E': [50 + inp_size - font_size, 25 + half_size], 
    'W': [font_size, 25 + half_size]
}

for key in nesw:
    text(nesw[key][0], nesw[key][1], key)


star_count = 1
while True:

    # Get constellation star count

    star_count = int(input("enter how many stars to plot for constellation (<=0 to exit):\n"))
    if star_count <= 0:
        break


    # get first star

    star_mag = float(input("give star magnitude: \n"))
    star_size = 13 / (star_mag + 2.5)
    star_color = (1 - ((star_mag + 1.5) / 12)) * 255

    starxy = [
        # final coords, all math here
        25 + (1 + float(input("give star x coord: \n")))*half_size - star_size/2, 
        25 + (1 + float(input("give star y coord: \n")))*half_size - star_size/2
    ]

    setColor(star_color, star_color, star_color)
    ellipse(starxy[0], starxy[1], star_size, star_size)


    # get number of edges


    

print("done drawing constellations")

# Continue to make constellations until given 0 or a negative number of star count

    # Loop to get input for each star (magnitude, followed by x and then y coordinates)
        # Do conversions for drawing
        # Draw star

    # Get number of edges to draw

    # Loop to get input for each edge two (x, y) coordinates
        # Do conversions for drawing
        # Set color for edges of constellation (cycles 6 colours)
        # Draw edge

    # Get next constellation star count

# Done
