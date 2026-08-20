# variable declarations

nums = []            # nums, is a list variable which is used to hold each number the user types in 
total = 0            # total, is a variable used to store the total value of all numbers the user typed in
user_input = ""      # user_input, this is the string variable 'text' value the user types in

# main program

while True: # use while loop to both print menu insructions/and, collect each user data entry...

   user_input = input("Enter number/(-1 to Quit): ")

   if user_input == '-1': # when user types in the string value: '-1' the loop stops
      break
   else:                  # the users number is first converted to being an integer value/then, added to the nums array 
      nums.append(int(user_input))

for each_num in nums: # for loop is used to calculate total of nums the user has entered
    total += each_num

average_of_nums = total/len(nums) # calculate the average of the total nums
print(average_of_nums)            # print the average of the total nums 
