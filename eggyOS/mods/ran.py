def col():
 import main2
import random
import os
import time


os.system("clear")
typee = input("dice[d] color[c] random word[r] coin[c] 4-digit number[4]")
if typee == "d":
  try:
   o = []
   imput = int(input("chose how much dice: "))
   for i in range(imput):
    p = random.randint(1,6)
    o.append(i)
   print(o)
   time.sleep(5)
   import main2
  except ValueError:
   print("NO WORDS!!!!!!!!!!!!!!!!!!")
   col()

elif typee == "c":
  colers = ["red","orange","yellow","green","blue","purple"]
  l = random.randint(0,6)
  print(colers[l])
  time.sleep(5)
  import main2
elif typee == "r":
   vart = ""
   hl = []
   hi = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
   ]
   lenth = random.randint(1, 100)
   hi1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   for i in range(lenth):
       ht = random.randint(1, 2)
       if ht == 1:
           hs = random.randint(0, 25)
           hl.append(hi[hs])
#        vart + hi[hs]
       if ht == 2:
           hy = random.randint(0, 9)
           hl.append(hi1[hy])
#        vart + hi1[hy]
   print(hl)
   time.sleep(5)
   import main2
elif typee == "c":
 h = random.randint(1,2)
 if h == 1:
  print("heads")
  time.sleep(5)
  import main2
 if h == 2:
  print("tails")
  time.sleep(5)
  import main2
elif typee == 4:
 op = []
 
 a = random.randint(0,9)
 op.append(a)
 b = random.randint(0,9)
 op.append(b)
 c = random.randint(0,9)
 op.append(c)
 d = random.randint(0,9)
 op.append(d)
 print(op)
 time.sleep(5)
 import main2