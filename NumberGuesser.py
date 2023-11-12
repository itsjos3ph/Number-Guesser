import random

print("Hello! In this game, you get to guess the number in my mind!")

number = random.randint(1,9)

guess = input("Guess the number: ")

if guess == number:
    print(f"Nice Job! You guessed it! {number} was correct!")
else:
    print(f"Nice try... The answer was {number}")