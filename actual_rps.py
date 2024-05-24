import random

while True:
    c_decision = random.randint(1,3)
    comp=""
    if c_decision == 1:
        comp = "rock"
    elif c_decision == 2:
        comp = "paper"
    elif c_decision == 3:
        comp = "scissor"

    decision = ""
    while decision.lower() not in ["rock", "paper", "scissor", "skibidi toilet"]:
        decision = input("Rock, paper, or scissors? ")
        if decision.lower() not in ["rock", "paper", "scissor", "skibidi toilet"]:
            print("That is not a valid answer!")

    if comp=="rock" and decision=="paper":
        print("u win")
    elif comp=="rock" and decision=="scissor":
        print("u lose")
    elif comp=="paper" and decision=="scissor":
        print("u win")
    elif comp=="paper" and decision=="rock":
        print("u lose")
    elif comp=="scissor" and decision=="rock":
        print("u win")
    elif comp=="scissor" and decision=="paper":
        print("u lose")
    elif comp==decision:
        print("tie")
    elif decision=="skibidi toilet":
        print("bruh")
        print("*loads shotgun with malicious intent*")
        break
    
