while True:
    decision = ""
    while decision.lower() not in ["rock", "paper", "scissor"]:
        decision = input("Rock, paper, or scissors? ")
        if decision.lower() not in ["rock", "paper", "scissor"]:
            print("That is not a valid answer!")
    
    if decision=="rock":
        print("You lose")
        print("The computer chose paper.")
    elif decision=="paper":
        print("You lose")
        print("The computer chose scissor.")
    else:
        print("You lose")
        print("The computer chose rock.")