# Created: 060424 14:03 PM GMT
# Updated: 200626 05:03 AM GMT - (added alternative coding method/plus, NOTE)  

# Example code borrowed from Simplilearn Python3 tutorial.
# https://www.simplilearn.com

# The following 3 lines of Python3 code 
# can be used to create a very simple diagional straight line graph:(/); 
# which is, then, being displayed on screen.

# I tested the code is working, properly, on:
# Linux Mint OS using: python3

# ------------------------------------------------

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,2,3,4])
plt.show()

# ------------------------------------------------

# Alternative coding method...separating out both : x, y...

''' commented out code...
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,2,3,4]
plt.plot(x,y)
plt.show()
'''
# -------------------------------------------------

# NOTE: It can clearly be shown from the above example that in a straight line graph...
#       both the x,y co-ordinates are written in ascending order which parallel's one another.
#       And, that each of these points intersects forming an x,y 'square' manner, eg: 1,1 - 2,2 - 3,3 - 4,4  
