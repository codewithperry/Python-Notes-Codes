import random
#fetch hiscore
with open("hiscore.txt") as f:
    hiscore = int(f.read())

def game():
    score = random.randint(1,100)
    if score>hiscore or hiscore=="":
        #print the hiscore in hiscore.txt
        with open("hiscore.txt", "w") as writefile:

        #write the hiscore
            writefile.write(str(score))
            print(score)
    else:
        print(f"Your current highscore is {hiscore}")


game()
