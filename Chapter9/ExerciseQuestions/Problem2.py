'''
The game() function in a program lets a user play a game and returns the score
as an integer.
You need to read a file 'Hiscore.txt' which is either blank or contains the previous 
Hi-score.
You need to write a program to update the Hi-score whenever
game() breaks the Hi-score.


'''
import random
def game():
    print("You are playing a game.")
    score = random.randint(1,1000)
    print(f"Your score is {score}")
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        print(f"Your hiscore was {hiscore}")
    if(score>hiscore):
        hiscore = score
        with open("hiscore.txt", "w") as f:
            f.write(str(hiscore))
        
    
    return score
    
game()


    
