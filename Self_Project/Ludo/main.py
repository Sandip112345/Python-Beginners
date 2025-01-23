''' Create a Ludo game for two player, the first to reach 50 wins, 
It takes turns to roll for each user in sequences.'''
import random
import time

def roll_dice():
    return random.randint(1,6)

def play_game():
    user1_score = 0
    user2_score = 0

    while True:
        
        
        dice_roll = roll_dice()
        # print(f"Player 1 rolled a {dice_roll}")
        user1_score = user1_score + dice_roll
        print(f"Player 1's rolled a {dice_roll} his score goes to:\n {user1_score}\n")

        if user1_score >= 25:
            print("Player 1 wins!")
            break
        time.sleep(3)

        # Player 2's turn
        dice_roll = roll_dice()
        # print(f"Player 2 rolled a {dice_roll}")
        user2_score = user2_score + dice_roll
        print(f"Player 2's rolled a {dice_roll} his score goes to:\n {user2_score}\n")

        if user2_score >= 25:
            print("Player 2 wins!")
            break
        time.sleep(4)
play_game()




