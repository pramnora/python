# Make calls to an external file: [myModules.py];
# so, that one can use a single 'specific' named module which is written inside of that external file...inside of this same file.

# NOTE: Using this syntax means...
#       one can specify which of the named functions inside of external file: myModules, is to be called;
#       thus, helping to save memory...by not calling all (*).

from myModules import two

def one():
	print("Function one")

one()   # calling an *internal* module function code
two()   # calling an *external* module function code
three() # calling an *external* module function code/this call will bug out...as function three hasn't been declared...?! (NameError: name 'three' is not defined)
