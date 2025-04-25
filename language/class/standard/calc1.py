# ------------------------------------
# CREATED: 250425 03:26 PM GMT
# UPDATED: 250425 03:26 PM GMT
# ------------------------------------
# Created my 1st Math Class program...
# ------------------------------------

class MyMath:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    # create class  methods...

    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2

myNums: MyMath=MyMath(3,3)  # instantiation

# call and method results...

print(myNums.add())      # 6 
print(myNums.subtract()) # 0 
print(myNums.multiply()) # 9
print(myNums.divide())   # 1.0 
