import os
# Prints all the files this code can see/read
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  print(f)
def re():
  num = int(input("text one[1] text two[2] text three[3] exit[e]: "))
  if num == 1:
    load = open('eggyOS/txts/f.txt','r')
    pr = load.read()
    append = open('eggyOS/txts/f.txt','a')
    print(pr)
    text = input()
    append.write(text)
    load.close()
    append.close()
    re()
  elif num == 2:
    load = open('eggyOS/txts/s.txt','r')
    pr = load.read()
    append = open('eggyOS/txts/s.txt','a')
    print(pr)
    text = input()
    append.write(text)
    load.close()
    append.close()
    re()
  elif num == 3:
    load = open('eggyOS/txts/t.txt','r')
    pr = load.read()
    append = open('eggyOS/txts/t.txt','a')
    print(pr)
    text = input()
    append.write(text)
    load.close()
    append.close()
    re()
  elif num == "e":
    import main2
re()