# Created: Mon 13th Feb 2023 11:15 AM GMT
# Updated: Mon 13th Feb 2023 11:15 AM GMT

# ----------------------------------------------------------------------  
# This code was borrowed from...
# https://www.geeksforgeeks.org/writing-to-file-in-python/
# ...then, adapted by me. 

# I, carefully, looked at what the above example code had said; then, after memorising it...; 
# went and re-created that same code myself starting from total scratch.
# ----------------------------------------------------------------------  

# fh1 = fileHandle1

# open file/and, write a single line of data into it...

fh1=open ("test02.txt",'w')
fh1.write("abc\n")
fh1.close

# open file/and, read from it...;
# by displaying it's contents onto the output screen...

fh1=open ("test02.txt",'r')
print(fh1.read())
fh1.close

# create a list based array...;
# to hold multiple lines of data...

myData=[
 "def\n"
 "ghi\n"
 "jkl\n"
]

# open file/in order to append to it...;
# without overwriting any of the file's previous contents...

fh1=open ("test02.txt",'a')
fh1.writelines(myData)
fh1.close

# open file/and, read from it...;
# by displaying it's contents onto the output screen...

fh1=open ("test02.txt",'r')
print(fh1.read())
fh1.close

