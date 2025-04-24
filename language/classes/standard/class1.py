# CREATED: Thu 240425 19:15 PM GMT
# UPDATED: Thu 240425 19:15 PM GMT
# --------------------------------------------------------------- 

# This example tries to break down the properties of a class...
# into its various different parts and pieces...

class Class_name:
    def __init__(self,var1):
        self.var1=var1

Instance_name: Class_name=Class_name(var1='Testing...') # intialise var1

# printouts...
print("Printing...")
print(f"Instance_name:",Instance_name) # just prints out the memory address
print(f"Instance_name.var1:", Instance_name.var1) # prints variable value
