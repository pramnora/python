import time
print("Counting down for 10 seconds...")
maxNoOfSecs=10
for countdown in range(maxNoOfSecs+1,1,-1):
    print(countdown-1)
    time.sleep(1)
print("...finished countdown.")

# printout...
# Counting down for 10 seconds...
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# ...finished countdown!
