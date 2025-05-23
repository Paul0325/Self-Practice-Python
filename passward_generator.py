import string
import random

def get_password_length():
    length = int(input("Tell me the password length you want to have: "))
    if length<1:
        print("It must be bigger than 1")
    else:
        return length

def get_inclusion_options():
    include_letters = input("Do you want letters in your password? (y/n): ").lower() == 'y'
    include_digits = input("Do you want digits? (y/n): ").lower() == 'y'
    include_special = input("Do you want special characters? (y/n): ").lower() == 'y'
    return include_letters, include_digits, include_special

def generate_password(length, include_letters, include_digits, include_special):
    character_set = ""
    if include_letters==True:
        character_set += string.ascii_letters  # Includes both upper and lower case
    if include_digits==True:
        character_set += string.digits
    if include_special==True:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for item in range(length))
    return password

def main():
    length = get_password_length()
    include_uppercase, include_lowercase, include_digits, include_special = get_inclusion_options()
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()