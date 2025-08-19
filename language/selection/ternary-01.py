# Use of single line ternary operator...

nums=[0,1,2,3]

print("x - result")
print("_   ------")

for x in nums:
    result = "x=1" if (x==1) else "x NOT 1"
    print(x,"-", result)
