text = []

while True:

   user_input = input("Enter some text('q' to quit): ")

   if (user_input in ['q','Q']):
      break

   text += user_input

for eachItem in text:
    print(eachItem)
