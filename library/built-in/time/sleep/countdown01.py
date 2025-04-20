import time
print("Counting down for 10 seconds...")
maxNo=10
for countdown in range(maxNo+1,1,-1):
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
