import random
possible_options = ["R", "P", "S"]
computer = random.choice(possible_options)
user = False
while user == False:
    user = input("Pick R for Rock, P for Paper and S for Scissors: ")
    if user == computer:
        print("Its a tie, play again.")
    elif user == "R":
        if computer == "P":
            print("Player (Rock) : CPU (Paper)")
            print("You lose!, Paper covers Rock")
            break
        else:
            print("Player (Rock) : CPU (Scissors)")
            print("You win!, Rock smashes Scissors" )
            break
    elif user == "P":
        if computer == "S":
            print("Player (Paper) : CPU (Scissors)")
            print("You lose!, Scissors cuts Paper")
            break
        else:
            print("Player (Rock) : CPU (Paper)")
            print("You win!, Paper covers Rock")
            break
    elif user == "S":
        if computer == "R":
            print("Player (Scissors) : CPU (Rock)")
            print("You lose!, Rock smashes Scissors")
            break
        else:
            print("Player (Scissors) : CPU (Paper)")
            print("You win!, Scissors cuts Paper")
            break
    else:
        print("That's not a valid play. Check your spelling!")
    
    user = False
    computer = random.choice(possible_options)    