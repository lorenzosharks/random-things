def number_or_not(input):
    try:
        float(input)
        return "Is number"
    except ValueError:
        return "Not a number"
    

check = input("Input: ")
print(number_or_not(check))