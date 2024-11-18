command = ""

print("Type 'quit' to exit the game.")
while command != "quit":
    command = input("What do you want to do? ")
    if command != "quit":
        print(f"You said: {command}")
    else:
        print("Goodbye!")
