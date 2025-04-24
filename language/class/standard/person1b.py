# --------------------------------------------------------------- 
# CREATED: Thu 240425 19:15 PM GMT
# UPDATED: Thu 240425 19:15 PM GMT
# --------------------------------------------------------------- 
# Borrowed this code from...
# 5 Cool Dataclass Features In Python - YouTube channel: Indently
# https://www.youtube.com/watch?v=E9tl3hP03lk
# --------------------------------------------------------------- 
# This is my own adaptation of the code...; using a short form...
# Here I did not include explicit variable types: str,int,list[str],None:

class Person:
    def __init__(self, name, age, friends):
        self.name=name
        self.age=age
        self.friends=friends
bob: Person=Person(name='testing',age=29,friends=['Luigi','James'])
print(bob)
print(bob.name,bob.age,bob.friends)
