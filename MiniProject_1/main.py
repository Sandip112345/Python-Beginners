'''
We all have played rock, paper, Scissors game in our childhood.
If you haven't, google the rules of this game and write a python 
program capable of playing this game with the user.

'''
import random

def game(comp_choice, user_choice):

    if (user_choice=="r" and comp_choice =="s") or (user_choice=="p" and comp_choice=="r") or (user_choice=="s" and comp_choice=="p"):
        print("You won!\n")
        return 1

    elif(user_choice==comp_choice):
        print("You Draw!\n")
        return 0
    else:
        print("You Lost, Computer has Won!\n")
        return -1

    # elif (user_choice=="r"):
    #     if(comp_choice == "p"):
    #         print("You Lost, Computer won!\n")
    #         return -1
    #     elif(comp_choice=="s"):
    #         print("You Won, Computer Lost!\n")
    #         return 1
    #     elif(comp_choice=="r"):
    #         print("You Draw!\n")
    #         return 0
    # elif (user_choice=="p"):
    #     if(comp_choice == "p"):
    #         print("You Draw!\n")
    #         return 0
    #     elif(comp_choice=="s"):
    #         print("You Lost, Computer has won!\n")
    #         return -1
    #     elif(comp_choice=="r"):
    #         print("You Won, computer has lost!\n")
    #         return 1
    # elif (user_choice=="s"):
    #     if(comp_choice == "s"):
    #         print("You Draw!\n")
    #         return 0
    #     elif(comp_choice=="p"):
    #         print("You won, Computer has lost!\n")
    #         return 1
    #     elif(comp_choice=="r"):
    #         print("You Lost, Computer has won!\n")
    #         return -1


def main():
    
    choose = ["r", "p", "s"]
    rounds = 3
    user_score = 0
    computer_score = 0
    for i in range(rounds):
        comp_choice = random.choice(choose).lower()

        user_choice = input("Enter your choice R for Rock, P for Paper and S for scissor: ").lower()
        while user_choice not in choose:
            print("You input the Invalid choices, Please try again!\n")
            user_choice = input("Enter your choice R for Rock, P for Paper and S for scissor: ").lower()

        print(f"You choose {user_choice} and computer choosed {comp_choice}")
        result = game(comp_choice,user_choice)
        
        if result>0:
            user_score = user_score + 1
        elif result<0:
            computer_score = computer_score + 1


    if user_score>computer_score:
        print(f"YOU Won The Game by {user_score}:{computer_score}")
    elif(user_score==computer_score):
        print(f"You Drew the game by {user_score}:{computer_score}")
    else:
        print(f"You lost the game by {user_score}:{computer_score}")


main()



