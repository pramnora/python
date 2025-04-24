from dataclasses import dataclass

@dataclass
class Class_Name:
    var1:str
    var2:int
    var3:list[str]

# declare name of instance: instance_name...;
# and, initialise all 3 variables: var1, var2, var3

instance_name:Class_Name=Class_Name("Anystring",0,['a','b','c'])

# do printouts...

print(instance_name)                     # prints: Class_Name('Anystring', var2=0, var3=['a','b','c'])
print("var1: ",instance_name.var1)       # prints: Anystring
print("var2: ",instance_name.var2)       # prints: 0
print("var3: ",instance_name.var3)       # prints: ['a','b','c']
print("var3[0]: ",instance_name.var3[0]) # prints: a

