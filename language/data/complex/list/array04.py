# How to use Python numeric arrays with functions...

#assigning values into an array...
numbers=[5,63,22,90,5]

#printout out the array values...
print(numbers)
#5,63,22,90,5

#finding what is the minimum number included inside of the array...
print(min(numbers))
5

#finding what is the maximum number included inside of the array...
print(max(numbers))
90

#finding out the number of times a list item repeats itself...
print(numbers.count(5))
#2

#sort the array items going in ascending order...
numbers.sort()
print(numbers)
#5,5,22,63,90

#sort the array items going in reverse order...
numbers.sort(reverse=True)
print(numbers)
#90,63,22,5,5


