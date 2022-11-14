def col():
    import main2



import os
import time


one = int(input("input number one to one hundred:"))
sec = int(input("input number another one to one hundred: "))
way = input("add[a] multiplication[t] division[d] subtraction[s]: ")
if way == "a":
    print(one + sec)
    time.sleep(2)
    os.system('clear')
    col()
elif way == "s":
    print(one - sec)
    time.sleep(2)
    os.system('clear')
    col()
elif way == "t":
    print(one * sec)
    time.sleep(2)
    os.system('clear')
    col()
elif way == "d":
    print(one / sec)
    time.sleep(2)
    os.system('clear')
    col()
