from dataclasses import dataclass

@dataclass
class Class_Name:
    var1:str
    var2:int
    var3:list[str]

test_case:Class_Name=Class_Name("Anystring",0,['a','b','c'])
print(test_case)
print("var1: ",test_case.var1)       # prints: Anystring
print("var2: ",test_case.var2)       # prints: 0
print("var3: ",test_case.var3)       # prints: ['a','b','c']
print("var3[0]: ",test_case.var3[0]) # prints: a

