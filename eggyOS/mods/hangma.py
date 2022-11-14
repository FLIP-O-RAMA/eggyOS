def col():
 import main2
import random
import os
import time


worbank = ["bank", "python", "marker", "html", "team", "you"]
answer_num = random.randint(0, 5)
answer = worbank[answer_num]
print("the possible combinations  is {}".format(worbank))
unscore = "_ " * len(answer)
print("the len of the word is {}".format(len(answer)))
emergency = 0
gess = 6
stages = [
    """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
           """, """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
           """, """
          --------
          |      |
          |      O
          |     \\|/
          |      |
          |
          -
          """, """
          --------
          |      |
          |      O
          |     \\|
          |      |
          |
          -
           """, """
           --------
          |      |
          |      O
          |      |
          |      |
          |
          -
           """, """
          --------
          |      |
          |      O
          |
          |
          |
          -
          """, """
           --------
          |      |
          |      
          |
          |
          |
          -
          """
]
coreectt = 0
agan = []
while gess > 0:
    print(worbank)
    if coreectt == len(answer):
        print("you win the answer  was {}".format(answer))
        time.sleep(1)
        os.system('clear')
        col()
    user = input("enter A-Z: ")
    if user in agan:
        print("you all ready said that")
        time.sleep(1)
        os.system("clear")
    elif user in answer and user not in agan:
        print("correct")
        coreectt += 1
        agan.append(user)
        time.sleep(1)
        os.system('clear')
    else:
        print("incorrect")
        gess -= 1
        if gess == 6:
            print(stages[6])
            time.sleep(1)
            os.system('clear')
        elif gess == 5:
            print(stages[5])
            time.sleep(1)
            os.system('clear')
        elif gess == 4:
            print(stages[4])
            time.sleep(1)
            os.system('clear')
        elif gess == 3:
            print(stages[3])
            time.sleep(1)
            os.system('clear')
        elif gess == 1:
            print(stages[2])
            time.sleep(1)
            os.system('clear')
        elif gess == 1:
            print(stages[1])
            time.sleep(1)
            os.system('clear')
        elif gess == 0:
            print("you lose the answer was {}".format(answer))
            time.sleep(0.50)
            os.system('clear')
            col()
print("you lose the answer was {}".format(answer))
time.sleep(0.50)
os.system('clear')
col()