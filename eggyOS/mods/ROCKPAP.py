def col():
 import main2
import time
import random
import os



y = int(input("rock[1] paper[2] scissors[3]: "))
r = random.randint(1, 3)
if r == 1 and y == 1:
    print("tie")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 2 and y == 2:
    print("tie")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 3 and y == 3:
    print("tie")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 1 and y == 3:
    print("you win")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 2 and y == 1:
    print("you win")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 3 and y == 2:
    print("you win")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 3 and y == 1:
    print("you lose")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 2 and y == 1:
    print("you lose")
    time.sleep(1)
    os.system('clear')
    col()
elif r == 2 and y == 3:
    print("you lose")
    time.sleep(1)
    os.system('clear')
    col()