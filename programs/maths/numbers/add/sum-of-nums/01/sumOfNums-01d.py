# Created: Mon 13th Feb 2023 19:18 PM GMT
# Updated: Mon 13th Feb 2023 19:18 PM GMT

# I went and did an internet search for:  
# 'How to add up successive numbers from 1 up to 1 million?'  
# ...just to see how others had, possibly, chosen to solve the same problem.  

# I found one 'top ranking' solution on Quora...  
# https://www.quora.com/What-is-the-sum-of-all-numbers-from-1-to-1-000-000?fbclid=IwAR1Or1cBkLGz3Z9qcBGkX487HMK5Mv0o9iIyvJQ3wL6dIfEna-pKyHcVUrQ#:~:text=So%2C%20n%20%3D%201%2C000%2C000%20%3D,10%5E6%20%28in%20short%29.%20Substituting%20in%20%281%29%2C&text=So%2C%20n%20%3D%201%2C000%2C000,short%29.%20Substituting%20in%20%281%29%2C&text=%3D%201%2C000%2C000%20%3D,10%5E6%20%28in%20short%29.%20Substituting  
# ...the solution is put forwards by a certain Mr. Choutapally Prabhakar  

# The solution he suggested goes as follows...if you wish to add up all the successive numbers:  
# 1 up to 10; then, half 10 = 5/and, just write that same number down, twice = 55  
# 1 up to 100; then, half 100 = 50/and, just write that same number down, twice = 5050  
# 1 up to 1000000; then half of 1 million is 500,000; now, just write that same number down, twice: 500000500000  
# ...how, truly, amazing is maths...(that is, when you already 'know' it/me, I must confess that I didn't, yet)?!  

# NOTE: Instead, of the previous algorithm which took 1 million steps to calculate 1 million successive additions;  
#       we, now, have a solution which finds the answer in just 3 steps.  
# 1> Get number  
# 2> half it  
# 3> Write the halfed number down, twice.  

# And, so now the 'new' program algorithm becomes...;   
# -(and, I do note that these numbers are related to series of 10's: 10/100/1000/10000/-etc.; as opposed to any other numbers)-;    
# ...get the user to input their number as a string;   
# convert the user input string into being a number;  
# next, half that number;   
# convert the number halfed into being a string;  
# finally, print out that same number, twice...on the same row; and, with no spaces showing in between.  

 
