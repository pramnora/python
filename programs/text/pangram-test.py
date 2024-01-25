  GNU nano 6.2                       for-test.py                                
# -----------------------------------------
#     PROGRAM: Pangram/alphabet checker
# -----------------------------------------
#    LANGUAGE: Python 3, Version: 3.10.12
# COMPUTER/OS: Home based PC/Linux Mint
# -----------------------------------------
#     CREATED: Thu 25 Jan 2024 01:18 AM GMT
#     UPDATED: Thu 25 Jan 2024 01:18 AM GMT
# -----------------------------------------

# The program checks to see if each letter of the alphabet: 'a-z' is contained 
# inside of the pangram: 'the quick brown fox jumps over the lazy dog'     

# Initialise variables...
pangram="The quick brown fox jumps over the lazy dog."
alphabet="abcdefghijklmnopqrstuvwxyz"

# Remove all spaces from pangram text...
# Remove the full stop: (.)
# Change all upper case letters into being lower case, instead...
pangram=pangram.replace(" ","").replace(".","").lower()

# print pangram...
print("pangram =",pangram)

# print pangram length...
print("pangram length =",len(pangram))

# print alphabet...
print("alphabet =",alphabet)

# print alphabet length...
print("alphabet length = ",len(alphabet))

# check if each letter of the alphabet is contained inside of the pangram...
# by using a for loop...
for x in alphabet:
        if x in pangram:
                print("found letter:", x," in ", pangram)
        else:
                print("letter:",x,"NOT found in ", pangram)

