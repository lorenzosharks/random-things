while True:  # Infinite loop to keep the script running
    decision = ""
    while decision.lower() not in ["angel", "devil"]:
        decision = input("Do you want to hear the angel or the devil? ")
        if decision.lower() not in ["angel", "devil"]:
            print("Make up your mind, you backward fool!.")
            print("Glass of juice, not gas the Jews! Answer the question properly!")

    if decision == "devil":
        d2 = ""
        while d2.lower() != "yes" or "no":
            print("ngl, Hitler was right in gassing the Jews.")
            d2 = input("Do you agree? ")
            if d2 == "yes":
                print("HEIL HITLER!!")
            elif d2 == "no":
                print("You're right, Stalin's better anyways.")
            else:
                print("Troll move! I'm going to nuke India now!")
                      
    elif decision == "angel":
        print("We shoulda nuked japan more than twice.")
        d3 = input("Do you agree? ")
        if d3 == "yes":
            print("time to deploy rice cooker 2.0")
        elif d3 == "no":
            print("get the flip out, you Japanese sympathizer")
        else:
            print("*says racial slur*")