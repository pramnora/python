# Created: Sun 12th Feb 2023 16:00 PM GMT
# Updated: Sun 12th Feb 2023 16:00 PM GMT

# set filemode: w-write,r-read,r+...read/write,a-append

# set filename...

# if a path was not specified along with the name;
# then, the file will be written inside of the 'current' path...

filename="text01.txt"

# set data...

# \n = new line
# \ = line continuation character
data = "abc\n"\
     + "def\n"\
     + "ghi\n"

# NOTE: If there is no new line (\n) being included at the end of the file;
#       then, what data is appended, later on...will be placed on the same line
#       as was the end line; as opposed to being placed on a new line down.

# file write...

print("1: File mode:(w)/File write: abc\\ndef\\nghi\\n:\n")

file1 = open(filename,"w")    
file1.write(data)
file1.close()

# NOTE: If the file already exists...;
#       then, all of it's previous data will be overwritten

# file read...

print("2: File mode: (r)/File read...\n")

file1 = open(filename,"r")    
print(file1.read())
file1.close()

# file append...

print("3: File mode: (a)/File append: jkl...\n")

newData="jkl\n"
file1 = open(filename,"a")    
file1.write(newData)
file1.close()

print("4: File mode: (r+)/File read/write: mno...\n")

# file read/write...
moreData="mno\n"
file1 = open(filename,"r+")    
print(file1.read())
file1.write(moreData)
print(file1.read()) # no read update gets displayed here/but, it did write
file1.close()

# The "r+" mode...appends data onto the end of the previous file;
# without overwriting it's contents.

# if you wish to see the newly appended data;
# then, it's necessary to open/read/close all over again;
# otherwise, just using file1.read() doesn't show any immediate update

print("5: File Mode: (r+)/File read...\n")

file1 = open(filename,"r+")    
print(file1.read())
file1.close()

# The advantage of using the 'with' statement...;
# is you don't have to keep on using file.close();
# this is because 'with' will, automatically, close the file for you, instead.  

print("6: File Mode: (a)/Using 'with' to write file contents: pqr...\n")

with open(filename,'a') as fh:  # fh = fileHandle
    fh.write("pqr")

print("7: File Mode: (r)/Using 'with' to read file contents...\n")
    
with open(filename,'r') as fh:
    print(fh.read())
