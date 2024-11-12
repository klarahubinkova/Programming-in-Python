import random

class NumberGuessingGame:
    def __init__(self, attempts=5):
        # Set up the game with a random number to guess and a limit on attempts
        self.target_number = random.randint(1, 100)
        self.attempts_left = attempts
        self.is_won = False

    def guess(self, number):
        # Check the player's guess
        if self.is_won:
            print("You've already won! Start a new game to play again.")
            return

        if self.attempts_left <= 0:
            print("No attempts left! The game is over.")
            return

        self.attempts_left -= 1

        if number == self.target_number:
            print(f"Congratulations! You guessed the number {self.target_number} correctly!")
            self.is_won = True
        elif number < self.target_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        if not self.is_won and self.attempts_left > 0:
            print(f"Attempts left: {self.attempts_left}")
        elif not self.is_won:
            print(f"Game over! The correct number was {self.target_number}. Better luck next time!")

    def reset_game(self, attempts=5):
        # Reset the game to play again
        self.target_number = random.randint(1, 100)
        self.attempts_left = attempts
        self.is_won = False
        print(f"Game reset! You have {attempts} attempts to guess the new number.")

game = NumberGuessingGame()

game_end = False
while(not game_end):
    while(game.attempts_left > 0 and not game.is_won):
        guessed_number = int(input("Guess a number: "))
        game.guess(guessed_number)
    
    new_game = input("Do you want to play again? Answer 'yes' or 'no': ")
    if (new_game == 'yes'):
        game.reset_game()
    elif (new_game == 'no'):
        print("The game ended.")
        game_end = True
    else:
        print("Unexpected input. Ending the game...")
        game_end = True
