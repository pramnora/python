# This code borrowed from:
# https://www.youtube.com/shorts/Mf9GCn_LsUI
# ------------------------------------------
# It illustrates both 'long form/short form' use of 'if/else'...

number=4

# long way...

if number % 2 == 0:
   print("Even")
else:
   print("Odd")

# VS short...

print("Even" if number % 2 == 0 else "Odd")
