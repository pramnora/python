'''
This code borrowed from YouTube...
https://www.youtube.com/shorts/Ht_LdGroNZE

 Created: 22:43 18/07/2023
 Updated: 22:44 18/07/2023
'''

import time
from itertools import cycle
lights = [
   ('Green',2),
   ('Yellow',0.5),
   ('Red',2)
]
colors = cycle(lights)
while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)

# The output...shows...

# Green
# Yellow
# Red
# Green
# Yellow
# Red
# ...-etc.

# Press: [CTRL] + [C] to cancel/stop the infinite loop... 
