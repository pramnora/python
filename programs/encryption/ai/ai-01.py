# Created: 250324 14:32 PM GMT
# Updated: 250324 14:32 PM GMT

'''
 Program: Translate user entered text into being numbers.
 I went to bing.com/and, used CoPilot to ask it to write me 
 a program that would translate user entered letters into becoming numbers.

 NOTE: Each letter inside of the user entered text is not translated precisely;
       as there are multiple options to choose from; for example,
       Letter: A, is translated as being the number: 2;
       Letter: B, is translated as being the number: 2;
       Letter: C, is translated as being the number: 2.
       ...therefore, this means that if the user were to type in...as text to be translated:
       ABC
       ...the answer that would get returned back would simply say:
       222
       ?!

       When I put in the following text to be translated:
       This is a secret message.
       The translated text that got returned was: 
       8447 47 2 732738 6377243. 
       ?!
'''

def get_number(uppercase_letter):
    # Define the mapping of letters to digits
    char_numbers = [
        ('ABC', 2), ('DEF', 3), ('GHI', 4), ('JKL', 5),
        ('MNO', 6), ('PQRS', 7), ('TUV', 8), ('WXYZ', 9)
    ]
    
    # Convert uppercase letter to its corresponding digit
    for chars, digit in char_numbers:
        if uppercase_letter in chars:
            return digit
    
    # If the letter is not in the mapping, return the original letter
    return uppercase_letter

def translate_number():
    phone_number = input("Enter a string: ")
    translated_number = ""

    for char in phone_number.upper():
        if char.isalpha():
            translated_number += str(get_number(char))
        else:
            translated_number += char

    print("Translated number:", translated_number)

# Call the function to translate the user input
translate_number()
