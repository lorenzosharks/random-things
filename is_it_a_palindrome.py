print("Is it a palindrome?")

raw=list(input("Enter here: "))

rawLength=len(raw)

rawEven=""
rawOdd=""

if rawLength%2 == 0:
    rawEven=raw
else:
    rawOdd=raw

index=0
correct=1

if rawEven==raw:
    while index<(len(rawEven)/2):
        if rawEven[index]==rawEven[rawLength-index-1]:
            correct=1
            index=index+1
        else:
            correct=0
            break
else:
    while index<((len(rawOdd)/2)-1):
        if rawOdd[index]==rawOdd[rawLength-index-1]:
            correct=1
            index=index+1
        else:
            correct=0
            break


if correct==1:
    print("It is indeed a palindrome!")
else:
    print("No, it isn't a palindrome.")