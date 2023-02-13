# Created: Mon 13th Feb 2023 12:24 PM GMT
# Updated: Mon 13th Feb 2023 12:24 PM GMT

# -----------------------------------------------------------------------------------  
# EXPLANATION...
# This program demonstrates that it's possible to use 'one' single procedure to do...
# file read/write; as well as, set file mode: r-read/w-write/a-append.

# It also allows the user to either write...
# a single line of data to a file
# or, multiple lines of data to a file
# -----------------------------------------------------------------------------------  

# initialise global variables...

fileHandle="fh1"
fileName="test02.txt"

mySingleLineOfData="abc\n"

myMultipleLinesOfData=[
 "def\n"
 "ghi\n"
 "jkl\n"
]

# procedures

def fileReadWrite(fileHandle,fileName,fileMode,fileData="",noOfLines=""):
    fileHandle=open(fileName,fileMode)
    if (fileMode=="r"):                    # read file
        print(fileHandle.read())           # output and display the file contents on screen  
    elif (fileMode=="w" or fileMode=="a"): # write/append file   
        if noOfLines == 's':               # single line to be written
            fileHandle.write(fileData)
        elif noOfLines == 'm':             # multiple lines to be written
            fileHandle.writelines(fileData)
    fileHandle.close

fileReadWrite(fileHandle,fileName,'w',mySingleLineOfData,'s')    # write a single line of data to the file  

fileReadWrite(fileHandle,fileName,'r')                           # read the file/and, display it's output contents on screen  

fileReadWrite(fileHandle,fileName,'a',myMultipleLinesOfData,'m') # write multiple lines of data to the file  

fileReadWrite(fileHandle,fileName,'r')                           # read the file/and, display it's output contents on screen  
