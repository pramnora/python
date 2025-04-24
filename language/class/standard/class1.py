# CREATED: Thu 240425 19:15 PM GMT
# UPDATED: Thu 240425 19:15 PM GMT
# --------------------------------------------------------------- 

# This example tries to break down the properties of a class...
# into its various different parts and pieces...

# --------------------------------------------------------------- 

# NOTES:-
# NOTE(1): The first letter of the class name is Capitalised
# NOTE(2): inside the class, 'self', will be replaced by the: instance_name

# --------------------------------------------------------------- 

class Class_Name:                                       # declare class name
    def __init__(self,var1):                            # initialise the class parameter argument names
        self.var1=var1                                  # set the class instance name variable value of: var1

instance_name: Class_Name=Class_Name(var1='Testing...') # declare instance_name/plus, intialise var1

# printouts...
print("Printing...")                                    # print heading text: Printing... 
print("-"*11)                                           # print underline for heading text
print(f"instance_name:",instance_name)                  # prints out the Class_Name memory address
print(f"instance_name.var1:", instance_name.var1)       # prints variable value: Testing...
