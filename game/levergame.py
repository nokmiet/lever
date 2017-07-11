import tkinter as tk
import random as ra

techo = tk()
pullcount = 0
capsuleinventory = 0

def staticpull():
  ran = randomizer()
  pullcount += 1
  print "You pull the lever."
  if ran == True:
    print "A capsule falls out."
    capsuleinventory += 1
  else:
    print "Nothing happens."
    
def randomizer():
  value = ra.randint(0,100)
  if value == 42:
    return True
  else:
    return False

def prize():
  prizeno = ra.randint(0,20)
  if any(prizeno%5 == 0):
    print "The capsule is empty."
  

pull = Button(techo, text="Pull Lever", command=staticpull)
pull.pack()

mainloop()
