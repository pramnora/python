# python arrays can store mixed data types, including: number/string/numeric expression/
# and, even, include other sub-arrays, as well 

num = [1,"111+111",111+111,"one",[1,2,3]]
for eachArrayItemNo in num:
	print eachArrayItemNo

# python arrays can be searched using a specific array 'index number';
# the number count starts at: 0/and, ends at array last item number-1; 
# in this case, the first array index data item number [0] stores a: 1
	
print num[0] 

# this is how one indexes an array stored inside of an array by using 2 separate index numbers
# the first number refers to where inside the 'outer array' the 'inner array' item is stored;
# the second number refers to which particular array item we wish to select from the 'inner array': in this case, 2

print num[4][1]

#1
#111+111
#222
#one
#[1,2,3]
#1
#2
