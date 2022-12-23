import string
import random

# getting password length
length = int(input("Enter password length: "))

print("""
Choose character set for password from these: 
        1: Letters
        2: Digits
        3: Special characters
        4: Exit
        """)

character_list = ""

# Getting character set for password
while True:
    choice = int(input("Pick a number "))
    if choice == 1:
        # adding letters to possible characters
        character_list += string.ascii_letters
    elif choice == 2:
        # adding digits to possible characters
        character_list += string.digits
    elif choice == 3:
        # adding special characters to possible characters
        character_list += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option! ")

password = []
for i in range(length):
    # Picking a random character from our character list
    random_char = random.choice(character_list)

    # appending a random character to password
    password.append(random_char)

# printing password as astring
print("The random password is " + "".join(password))