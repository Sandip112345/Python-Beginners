'''
We are going to write a program that generates 
a random number and asks the user to guess it.

If the player's guess is higher than the actual number. 
the displays "Lower number please".  Similarly, if the user's guess is too low, the 
program prints "higher number please" When the user guesses the corect number. the program
displays the number of guesses the player used to arrive at the number.

Use Random Module


'''
import random

def Guess(n, guesses):
    computer = random.randint(1,100)
    # print(f"The computer's num is {computer}")
    
    while True:
        if n > computer:
            print("Your number is higher, Give a low value.")
        elif n<computer:
            print("Your number is lower, Give a high value.")
        elif n==computer:
            print("Your guess is correct!\n")
            break
        n = int(input("Enter you number: "))
        guesses = guesses + 1
    
    print(f"You have guessed the value in {guesses} attempts, and Won")
    

no_of_guesses = 0

user = int(input("Enter you number: "))
no_of_guesses = no_of_guesses + 1
Guess(user, no_of_guesses)