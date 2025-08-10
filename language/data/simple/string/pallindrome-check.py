# This code is borrowed from: 
# https://www.youtube.com/shorts/ks34zTmi2ac

# CREATED: Sun 10 Aug 2025 18:48 PM GMT
# UDDATED: Sun 10 Aug 2025 18:48 PM GMT 

# -------------------------------------

def is_palindrome(s):
    # convert the string named, s/
    # into being all lower case letters, first;
    # next, remove all spaces inside of the string
    s=s.lower().replace(" ","")

    # compare the current string value with the string being reversed; 
    # then, return that result as a boolean value either: True/or, False
    return s==s[::-1]

print(is_palindrome("Racecar"))
print(is_palindrome("python"))

# output...
# True  - (the first string: Racecar...is a pallindrome)
# False - (the second string: python...is NOT a pallindrome)

# -----------------------------------------------------------------------------------------------------------------

# NOTE: A 'pallindrome' is a text/or, number value that reads exactly the same
#       going either backwards forwards.
#       eg. BAB is a pallindrome: reading it forwards: BAB/reading it going backwards: BAB...BAB = BAB
#       on the other hand
#       eg. CAB is NOT a pallindome: reading it forwards: CAB/reading it going backwards: BAC...CAB does NOT = BAC
