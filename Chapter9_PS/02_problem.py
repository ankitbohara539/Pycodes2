import random

def game ():
    print("--You are playing game---")
    score = random.randint(1,65)

    # fetch the high score

    with open ('highscore.txt') as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)

        else:
            highscore = 0

    print(f"your score: {score}")
    if (score>highscore):
        # write this highscore to the file
        with open('highscore.txt','w') as f:
            f.write(str(score))

    return score
game()