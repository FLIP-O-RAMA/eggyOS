import os
import time





def col():
   os.system("clear")
   coise = input("rps[r] hangman[h] madlibs[m] calculator[c] tictactoe[t] drawing[d] random func[f] exit[e]: ")
   if coise == "r" or coise == "R":
    import ROCKPAP
   elif coise == "h" or coise == "H":
    import hangma
   elif coise == "m" or coise == "M":
    import mad
   elif coise == "c" or coise == "C":
    import calcu
   elif coise == "t":
    import tic
   elif coise == "d" or coise == "D":
    import tur
   elif coise == "e" or coise == "E":
    import exi
   elif coise == "f" or coise =="F":
    import ran
   elif coise != "b" or coise != "B":
     import bank
   elif coise != "r" or coise != "h" or coise != "m" or coise != "c" or coise != "t" or coise != "e" or coise != "R" or coise != "H" or coise != "M" or coise != "C" or coise != "E" or coise != "d" or coise != "D" or coise != "f" or coise != "F" or coise != "b" or coise != "B":
        print("invalid command")
        time.sleep(0.50)
        os.system('clear')
        col()

col()