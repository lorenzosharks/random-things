import random

person = ["first", "second", "third"]

number = ["singular", "plural"]

verb = ["2", "3", "3i", "4"]

print(random.choice(person) + " person, " + random.choice(number) + ", " + random.choice(verb) + " declension")