# -------------------------------------------------  
# This code borrowed from  
# YouTube Channel: Bro Code  
# https://www.youtube.com/watch?v=c9vhHUGdav0  
# -------------------------------------------------  
# NOTE: His own code was simpler.../  
#       and, therefore, was uniquely adapted by me.  
# -------------------------------------------------  
# CREATED: 200626 02:18 AM GMT  
# UPDATED: 200626 02:18 AM GMT  
# -------------------------------------------------  

# Explanation:  

# This code outputs a straight line graph...;  
# which shows up in the form of numerous V shapes;  
# that extend going across the page, horizontally.  

# This is because the data both grows and shrinks in size,  
# ranging from the lowest point: 2;  
# and, going up to the highest point: 25.  

# -(In my next version B...;  
# I have deliberately switched the axes around:    
# y to become x/x to become y;     
# so, in that particular case,   
# the data is being plotted going vertically upwards, instead.)-    

# ==================================================  

import matplotlib.pyplot as plt                                              # import matplotlib library together with pyplot method as short form alias: plt

x=[5,10,15,20,11,12,14,6,18,25,2,8]                                          # horizontal graph axis, extends going across from left to right
y=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]  # vertical graph axis, extends going upwards from bottom to top

plt.plot(x,y)                                                                 # plot the graph co-ordinates
plt.show()                                                                    # show it/display it as an output file which can actually be 'saved'   

