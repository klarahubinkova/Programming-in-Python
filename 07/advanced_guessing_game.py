"""
(CZ) Pravidla:
- Hra náhodně vybere číslo mezi 1 a 10.
- Máte 3 pokusy, abyste uhodli správné číslo.
- Po každém tipu vám hra řekne, jestli je číslo příliš vysoké, nebo nízké.
- Pokud uhodnete správné číslo, vyhráváte.
- Můžete kdykoliv napsat 'quit' pro ukončení hry.

(EN) Rules:
- The game will randomly choose a number between 1 and 10.
- You have 3 attempts to guess the correct number.
- After each guess, the game will tell you if the number is too high or too low.
- If you guess the correct number, you win.
- You can type 'quit' at any time to stop playing.
"""

import random

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 10. You have 3 attempts.")
print("Type 'quit' to exit the game.\n")

# Rules
number_to_guess = random.randint(1, 10)  # Random number between 1 and 10
attempts_left = 3  # Player starts with 3 attempts

while attempts_left > 0:
    guess = input(f"You have {attempts_left} attempts left. Enter your guess: ")
    
    if guess == "quit":
        print("You chose to quit the game. Goodbye!")
        break
    
    if not guess.isdigit():  # Check if input is a number
        print("Please enter a valid number.")
        continue

    guess = int(guess)  # Convert input to an integer

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
        break
    elif guess < number_to_guess:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    attempts_left -= 1

if attempts_left == 0 and guess != number_to_guess:
    print(f"Game over! The correct number was {number_to_guess}. Better luck next time!")
