minNo=int(input("Enter min no: ")) 
maxNo=int(input("Enter max no: ")) 
total=0
for x in range(minNo,maxNo+1):
    total+=x
print("Total: ",total)
