import random

# Rock, paper, scissors game
computer_choice = random.choice(['rock', 'paper', 'scissors'])
human_choice = input('rock, scissors, or paper? ')

if human_choice == 'rock':
    if computer_choice == 'rock':
        print('It’s a tie.')
    elif computer_choice == 'scissors':
        print('You win!')
    elif computer_choice == 'paper':
        print('The computer wins.')
elif human_choice == 'scissors':
    if computer_choice == 'rock':
        print('The computer wins.')
    elif computer_choice == 'scissors':
        print('It’s a tie.')
    elif computer_choice == 'paper':
        print('You win!')
elif human_choice == 'paper':
    if computer_choice == 'rock':
        print('You win!')
    elif computer_choice == 'scissors':
        print('The computer wins.')
    elif computer_choice == 'paper':
        print('It’s a tie.')
else:
    print('I don’t understand.')
