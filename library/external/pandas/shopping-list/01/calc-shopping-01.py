# pandas...

import pandas as pd 
data=[
 ['','Apples','Bananas','Pears'],
 ['Cost per item:', 0.2,0.25,0.5],
 [' 7 days worth:', 7*0.2,7*0.25,7*0.5],
]
print(pd.DataFrame(data))

# printout...
#           0     1      2       3
# 0               Apples Bananas Pears
# 1  Cost per item: 0.2    0.25    0.5
# 2   7 days worth: 1.4    1.75    3.5

# ------------------------------------------------------------------------------------------------

# NOTE: I think, the above is extremely 'inefficient' code;
#       of the kind only a 'total beginner' might write.
#       For example, I should not need to 'hard code' the values every single time;
#       rather the values should be placed inside of an array; 
#       where they can be more quickly and easily mainpulated from there;
#       also, I think, there's probably a function which sums up what is the final overal total...?
