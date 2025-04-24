from dataclasses import dataclass

@dataclass
class Class_Name:
    var1:str
    var2:int
    var3:list[str]

test_case:Class_Name=Class_Name("Anystring",0,['a','b','c'])
print(test_case)
