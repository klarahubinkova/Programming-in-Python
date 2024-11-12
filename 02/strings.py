# Syntax of "Hello world!"
print("Hello world!")

# Operations with strings
print("Hello" * 5)
print("Hello" + "world")

print("1")
print("2" * 2)
print("3" * 3)

# Use of f-string
print("The area of a square is:", 4*4)
print(f"The area of a square is: {4*4}")

# Integer variables
length = 4
print(f"The area of a square is: {length*length}")

# Operations with variables
area = length*length
print(f"The area of a square is: {area}")

# Excercise: Given a = 2, print value of b so "10" is printed, b has to be computed using a
a = 2
b = None # Solution: b = a * 5 OR b = a + 8
print(b)

# String variables
hello = "Hello"
world = "World"
print(hello, world)

# Substrings
print(hello[1:])    # Substring from index 1 to an end
print(hello[:-1])   # Substring from the beginning to an end without the last character
print(hello[2:4])   # Substring from character at index 2 to character at index 4 including the first character and excluding the last

# Excercise: https://www.w3schools.com/python/exercise.asp?x=xrcise_strings_slicing1
