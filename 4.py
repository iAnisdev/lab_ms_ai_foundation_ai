import random

numbers = random.sample(range(1, 100), 25)

guess = int(input("Enter a number to check if it is in the list: "))


if guess in numbers:
    print(True)
else:
    print(False)
