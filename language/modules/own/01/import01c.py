# Make calls to an external file: [myModules.py];
# so, that one can use modules written inside of that external file inside of this same file.

# NOTE: Using this syntax means...
#       one doesn't need to include the 'myModules' name, anymore...; 
#       and, therefore, you don't need to prefix an external function name before calling it;
#       but, instead, you can simply call using the function name: two()/three();
#       as if you were calling an internally written function.

from myModules import *

def one():
	print("Function one")

one()   # calling an *internal* module function code
two()   # calling an *external* module function code
three() # calling an *external* module function code
