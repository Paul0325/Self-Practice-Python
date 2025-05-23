import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)

print("Make a guess of the number between 1 and 100")

while True:
    try:
        a = int(input("Your guess: "))
        
        if a < 1 or a > 100:
            print("Please guess a number between 1 and 100.")
            continue
        
        if a < num:
            print("Your guess is too small")
        elif a > num:
            print("Your guess is too big")
        else:
            print("Bingo! You've guessed the correct number!")
            break
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")  