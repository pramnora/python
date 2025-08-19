# Use of the 'match/case' selection...

nums=[0,1,2,3]

print("x - result")
print("-   ------")

for x in nums:
    match x:
        case 1:
            print(x,"- x=1")
        case 2:
            print(x,"- x=2")
        case _:
            print(x,"- x NOT 1 & x NOT 2")
