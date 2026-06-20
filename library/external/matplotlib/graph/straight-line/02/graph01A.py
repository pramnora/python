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

import matplotlib.pyplot as plt  

x=[5,10,15,20,11,12,14,6,18,25,2,8]  
y=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]  

plt.plot(x,y)  
plt.show()  

