x = int(input('Enter any integer: '))

# And
print('Number', x, 'is greater than 3 AND less than 10:', x > 3 and x < 10)

# Or
print('Number', x, 'is greater than 3 OR less than 10:', x > 3 or x < 10)

# Not
print('Number', x, 'is NOT greater than 3 and less than 10:', not(x > 3 and x < 10))

print()

# Happy or rich game
print('Answer "yes" or "no".')
happy_string = input('Are you happy? ')
if happy_string == 'yes' or happy_string == 'Yes':
    happy = True
elif happy_string == 'no' or happy_string == 'No':
    happy = False
else:
    print('I don’t understand!')

rich_string = input('Are you rich? ')
if rich_string == 'yes' or rich_string == 'Yes':
    rich = True
elif rich_string == 'no' or rich_string == 'No':
    rich = False
else:
    print('I don’t understand!')

if rich and happy:
    print('Congratulations!')
elif rich:
    print('Try smiling more.')
elif happy:
    print('Try spending less.')
else:
    print('I’m sorry to hear that.')
