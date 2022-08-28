# Make calls to an external file: [myModules.py];
# so, that one can use modules written inside of that external file inside of this same file.

# NOTE: Using this syntax means...
#       import all (*) functions from the external file called: 'myModules.py';
#       this calling method does away with the need for prefixes: myModules.two()/myModules.three()/-etc.;  
#       instead, just call using the explict function name: two()/three();
#       as if you were calling an internally written function.

from myModules import *

def one():
	print("Function one")

one()   # calling an *internal* module function code/
#         NOTE: In the case of name conflict,
#               The external function name: one() is NOT called; because the internal function call name: one()  seems to take top priority
two()   # calling an *external* module function code
three() # calling an *external* module function code
