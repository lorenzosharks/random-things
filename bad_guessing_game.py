import random

# Set the target number to guess
a = random.randint(1, 20)

while True:
    try:
        userInput = int(input("Guess the number between 1 and 20: "))
    except ValueError:
        print("Not an integer!")
        continue

    if userInput == a:
        a = random.randint(1,20)
        break
    else:
        print("The number is not right. Try again.")