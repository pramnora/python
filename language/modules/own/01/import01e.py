# Make call to an external file: [myModules.py];
# so, that one can use multiple 'specific' named modules...which have been written inside of that external file...
# inside of this same file.

# NOTE: Using this syntax means...
#       one can specify a comma separated list of which named functions to use inside of external file: [myModules.py];
#       so one can call multiple specifically named fuctions: one, two, -etc.;
#       thus, helping to save memory...by not calling all (*).

from myModules import two, three

def one():
	print("Function one")

one()   # calling an *internal* module function code
two()   # calling an *external* module function code
three() # calling an *external* module function code
