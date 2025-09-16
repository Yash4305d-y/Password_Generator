import random 
import string

def generate_password(min_length , numbers=True, Special_characters=True):
    letters = string.ascii_letters
    special = string.punctuation
    digits = string.digits

    characters = letters
    if numbers :
        characters += digits
    if Special_characters:
        characters += special
    
    pwd = "" 
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True

        elif new_char in special:
            has_special = True


        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers

        if Special_characters:
            meet_criteria = meet_criteria and has_special
    return pwd


min_length = int(input("Enter the length of password you want:"))
has_number = input("Do you want numbers in your password (y/n)? " ).lower() == "y"
has_special = input("Do you want special characters in your password? (y/n) ").lower() == "y"
 
passowrd = generate_password(min_length , has_number, has_special)

print("Generated password:- " , passowrd)