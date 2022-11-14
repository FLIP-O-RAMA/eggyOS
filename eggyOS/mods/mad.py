def col():
 import main2

import os
import time
import colorama
from colorama import Fore
 



colorama.init()
cange = ["boy", "girl", "number", "place", "year", "date", "time", "name"]
i = []
while len(i) != 8:
    i.extend(input("pls enter {}: ".format(cange[len(i)])))
print(
    "at {} {} met {} and went on a adventure  they went to the {}'s big city they asked everyone if they found any power stars  someone called {} said they saw a the power star at the woodland mansion they had a map of the city  they found the woodland mansion and they found the power star and restored peace to the world"
    .format(i[3], i[0], i[1], i[3], i[7]))
print(Fore.LIGHTMAGENTA_EX + "the end")
print('\033[39m')
time.sleep(5)
os.system('clear')
col()

