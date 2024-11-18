countdown = int(input("Enter a number where countdown should start: "))

print("Countdown starting!")
while countdown > 0:
    print(countdown)
    countdown = countdown - 1   # Another possibility: countdown -= 1
print("Countdown ended!")
