# Vypíše ke každému z prvních n čísel, zda je sudé, nebo liché
n = 20

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, "je sudé")
    else:
        print(i, "je liché")
