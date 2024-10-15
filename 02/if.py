# Comparison operators
print(1 == 1)
print(1 == 2)
print('True' != 'False')
print(1 < 2)
print(1 <= 2)
print(1 > 2)
print(1 >= 2)

print()

# Equals signs
first = a = 1       # assigning
second = a == 1     # comparison

print("First:", first)
print("Second:", second)

print()

# If-else
side = float(input('Enter the side of the square in centimeters: '))

if side > 0:
    print('The perimeter of the square with side', side, 'is', 4 * side, 'cm')
    print('The area of the square with side', side, 'is', side * side, 'cm2')
else:
    print('The side must be positive, otherwise it won\'t be a square!')

print()

# If-elif-else
number = int(input('Enter any integer: '))

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

number = 5

print()

# Equivalent code using nested if statements
if number >= 0:
    if number == 0:
      print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')
