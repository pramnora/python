# --------------------------------------
# PROGRAM: Draw a square
# SITE: trinket.io
# LANGUAGE: Python
# --------------------------------------
# CREATED: Wed 3rd Nov 2021 10:52 AM GMT
# UPDATED: Wed 3rd Nov 2021 10:52 AM GMT
# --------------------------------------

# NOTE: It's been a long time since I went and visited Trinket.io web site where I have an online a/c.;
#       today, I decided to sign into the a/c. to complete doing a tutorial there called: 1 hour of Python
#       Written below is my own personal adaptation of the code I found...
#       https://pramnora-5736.trinket.io/an-hour-of-python#/welcome-to-python/meet-tina

import turtle # Fetch turtle library

# set variable values...

size=360/4 # This line draws a 4 sided shape
degrees=90 # This line sets the amount of degrees the turtle is to turn each time

# Draw square...using 4 seperate lines...

turtle.forward(size) # draw line 1

turtle.left(degrees) # turn turtle a number of degrees
turtle.forward(size) # draw line 2

turtle.left(degrees) # turn turtle a number of degrees
turtle.forward(size) # draw line 3

turtle.left(degrees) # turn turtle a number of degrees
turtle.forward(size) # draw line 4
