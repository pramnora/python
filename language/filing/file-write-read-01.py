# created: 220520 04:33 AM GMT
# updated: 220520 04:33 AM GMT

fileName = "test.txt"

fileContent = "Line 1\n"
fileContent += "Line 2\n"

with open(fileName, 'w') as fileHandle:
    fileHandle.write(fileContent)
    fileHandle.close()

with open(fileName, 'r') as fileHandle:
    contents = fileHandle.read()
    print(contents)
    fileHandle.close()
    
