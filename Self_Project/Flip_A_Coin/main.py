
import random

def game():
    choices = ["H","T"]
    userscore = 0
    lost = 0
    rounds = 3
    for i in range(rounds):

        luck = random.choice(choices)   
        user = input("Heads or Tails (H for heads, T for Tails)").upper()
        while user not in choices:
            print("Invalid Choices! Please Try again!")
            user = input("Heads or Tails (H for heads, T for Tails)").upper()
        
        if user==luck:
            if user == "H":
                print(f"It's a Heads. You Won! \n")
            else:
                print(f"It's a Tails. You Won! \n")
            userscore = userscore + 1

        else:
            if user == "H":
                print(f"It's a Tails. You Lost! \n")
            else:
                print(f"It's a Heads. You Lost! \n")
            lost =lost + 1
    

    print(f"Your Win=Lose score is {userscore}:{lost}")
                


game()

    

