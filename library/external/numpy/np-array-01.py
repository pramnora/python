import numpy as np
xArrayName=np.arange(start=1,stop=10)
xArrayName
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
xArrayName.reshape(3,3)
xArrayName
#...output...
#array[[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]])

#*** NOTE: When I tried saving the file as: [np-array-01.py];
#          then, tried doing the printout by running the program;
#          both printouts showed exactly the same 1 line output structure.

#          However, when I moved over to the Python shell;
#          and, there tried typing in the commands,
#          it displayed a 3 x 3 grid as I was hoping to see.

#          That is why the output commands here do have no: print()
