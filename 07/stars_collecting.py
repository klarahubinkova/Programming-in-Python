stars = 0
continue_collecting = True

print("Collect stars! Type 'star' to collect one. Type 'done' to finish.")
while continue_collecting:
    action = input("What do you do? ")
    if action == "star":
        stars += 1
        print(f"You collected a star! Total stars: {stars}")
    elif action == "done":
        print(f"You finished with {stars} stars. Well done!")
        continue_collecting = False
    else:
        print("Invalid action. Try 'star' or 'done'.")

"""
# Another possible solution using 'break' keyword:
stars = 0

print("Collect stars! Type 'star' to collect one. Type 'done' to finish.")
while True:
    action = input("What do you do? ")
    if action == "star":
        stars += 1
        print(f"You collected a star! Total stars: {stars}")
    elif action == "done":
        print(f"You finished with {stars} stars. Well done!")
        break
    else:
        print("Invalid action. Try 'star' or 'done'.")

"""
