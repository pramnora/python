# created: 220520 04:43 AM GMT
# updated: 220520 04:43 AM GMT

fileName=""
fileExtension=""
getUserInputFlag = True
aString=""
fileContent=""

print("PROGRAM: Filing")

while(getUserInputFlag):
    fileName = input("\nEnter filename(name, only/no extension): ")
    fileExtension = input("Enter file extension(.txt/.dat/.csv/-etc.): ")
    fileName += fileExtension
    print("\nFilename: ",fileName)
    yesNo = input("Ok, Y/N: ")
    if yesNo[0].lower() == "y": getUserInputFlag = False

print("\nFile contents...\n")

with open(fileName,'w') as f:
    getUserInputFlag = True
    while(getUserInputFlag):
        aString = input("Enter file content(type nothing to end): ")
        if aString == "":
            getUserInputFlag = False
        else:
            f.write(aString + "\n")
    f.close()

with open(fileName,'r') as f:
    fileContent=f.read()
    print(fileContent)

