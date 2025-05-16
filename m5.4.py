# Name: Erbol Zamirov
# Date: May 16, 2025

# This program prints special messages for numbers divisible by 3, 5, or both from 1 to 50

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)