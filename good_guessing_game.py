import random

while True:
    a = random.randint(1, 2)

    try:
        userInput = int(input("Guess the number between 1 and 2: "))
    except ValueError:
        print("Not an integer!")
        continue

    if userInput == a:
        print("you guessed it :3")
    else:
        print("The number is not right. Try again.")