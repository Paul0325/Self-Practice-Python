import string
import random

def get_password_length():
    length = int(input("Tell me the password length you want to have: "))
    if length < 1:
        print("It must be bigger than 1")
        return get_password_length()  # Ask again
    return length

def get_inclusion_options():
    include_letters = input("Do you want letters in your password? (y/n): ").lower() == 'y'
    include_digits = input("Do you want digits? (y/n): ").lower() == 'y'
    include_special = input("Do you want special characters? (y/n): ").lower() == 'y'

    if not (include_letters or include_digits or include_special):
        print("You must include at least one type of character. Please try again.")
        return get_inclusion_options()  # Ask again

    return include_letters, include_digits, include_special

def generate_password(length, include_letters, include_digits, include_special):
    character_set = ""
    if include_letters:
        character_set += string.ascii_letters
    if include_digits:
        character_set += string.digits
    if include_special:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    length = get_password_length()
    include_letters, include_digits, include_special = get_inclusion_options()
    password = generate_password(length, include_letters, include_digits, include_special)
    print("Generated Password:", password)


main()
