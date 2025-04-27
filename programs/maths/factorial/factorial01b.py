# CREATED: Fri 250425 04:33 PM GMT
# UPDATED: Fri 250425 04:33 PM GMT
# --------------------------------
# Example code borrowed from...
# https://www.youtube.com/shorts/lo9ErkgqLMU

from functools import reduce
nums=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,nums)
print(product)

#  x y x*y
#  1 2 2
#  2 3 6
#  6 4 24
# 24 5 120
