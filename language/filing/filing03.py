# Created: Mon 13th Feb 2023 12:24 PM GMT
# Updated: Mon 13th Feb 2023 12:24 PM GMT

# -----------------------------------------------------------------------------------  
# EXPLANATION...
# This program demonstrates that it's possible to use 'one' single procedure to do...
# file read/write; as well as, set file mode: r/w/a.

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
    if (fileMode=="r"):        # read file
        print(fileHandle.read())
    elif (fileMode=="w"):      # write file   
        if noOfLines == 's':   # single line to be written
            fileHandle.write(fileData)
        elif noOfLines == 'm': # multiple lines to be written
            fileHandle.writelines(fileData)
    elif (fileMode=="a"):      # append file   
        if noOfLines == 's':   # single line to be written
            fileHandle.write(fileData)
        elif noOfLines == 'm': # multiple lines to be written
            fileHandle.writelines(fileData)
    fileHandle.close

# open file/and, write a single line of data into it...

fileReadWrite(fileHandle,fileName,'w',mySingleLineOfData,'s')

# open file/and, read from it...;
# by displaying it's contents onto the output screen...

fileReadWrite(fileHandle,fileName,'r')

# open file/in order to append to it...;
# without overwriting any of the file's previous contents...

fileReadWrite(fileHandle,fileName,'a',myMultipleLinesOfData,'m')

# open file/and, read from it...;
# by displaying it's contents onto the output screen...

fileReadWrite(fileHandle,fileName,'r')
