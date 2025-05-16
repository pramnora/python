#  CREATED: Fri 16th May 2025 17:11 PM GMT
#  UPDATED: Fri 16th May 2025 17:11 PM GMT
# ---------------------------------------
#  PROGRAM: Encoding hash
# LANGUAGE: Python version 3
# COMPUTER: Home based PC
#       OS: Linux Mint
# ---------------------------------------
# EXPLANATION

# The idea behind this program is...
# We get the user to type in their password as being a series of digits ranging from: 0-9;
# say 6 number digits in all.

# Next, we 'hash' each of the numbers which they typed in...;
# so, that we can store the data in a 'masked' -(or, hidden)- format;
# as opposed to 'plaintext' format...where anybody observing the code
# can get to see exactly what each digit means.

# NOTE: In this particular case, I've choosen just a very simple 
#       'substitution cypher'...where each number is exchanged for 1 code
#       eg. 1=L0T
#       In the real world, however...each separate digit...
#       might have 100+ 'unique' random numbers to select from;
#       thus, making it far less easy to be able to clearly identify
#       what are any repeats.
# ------------------------------------------------------------------------

# ----------
# initialise
# ----------

# initialise global variables

num="743219"              # password
output=""                 # working variable, stores each output code
underline_char="-"        # the underline character
screen_width_length=80    # the screen width length

# initialise code output dictionary

codes={
 "0":"JXK",
 "1":"L0T",
 "2":"XQR",
 "3":"UMN",
 "4":"TV9",
 "5":"PRQ",
 "6":"MNE",
 "7":"GI7",
 "8":"FUL",
 "9":"RAC"
}

# initialise function to, repeatedly, print underline

def printUnderline():
    print(underline_char*screen_width_length)

# ------------
# main program
# ------------

print("Printing the whole dictionary, 'key/value' pairs...\n")
print(codes)
printUnderline()


print("Printing each number/plus, it's corresponding output code...\n")
print("num", "codes")
print("----------")
for eachNum in num:
    if eachNum in codes:
       print(eachNum," - ",codes[eachNum])
       output+=codes[eachNum]

printUnderline()
print("Printing only the output codes having been all conjoined together...\n")
print(output)
print(f"={num}") # printing what was the original number we started with in order to compare
