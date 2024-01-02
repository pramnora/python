minNo=0
maxNo=0
total=0
minNo=int(input("Enter min no: ")) 
maxNo=int(input("Enter max no: ")) 
for x in range(minNo,maxNo+1):
    total+=x
print("Total: ",total)
