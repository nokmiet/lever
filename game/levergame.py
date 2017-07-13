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

#sticks, sharp metal, nail file, mouse, string, cheese, paper, ashes
#start in a room with nothing but a lever and a mousehole on a large locked door and a narrow open mail slot at the top of the wall
    #opt 1: paper airplane * string
    #opt 2: mouse * cheese * string
    #opt 3: cut up a bunch of empty capsules and shove them through the door
        #extras: 
            # nail file/sharp metal + mouse = dead mouse
            # sticks + sharp metal = shiv
            # string + sticks + capsule = fishing rod
                #OR string + sharp metal + sticks
            # sticks + cheese = cheesesticks
            # metal + file = sharper metal
                # sharper metal + stick = exacto knife
            
def prize():
  prizeno = ra.randint(0,20)
  if any(prizeno%5 == 0):
    print "The capsule is empty."
  elif prizeno == 1
  elif prizeno == 2
  elif prizeno == 3
  elif prizeno == 4
  elif prizeno == 6

def checkinventory():
  if capsuleinventory == 0:
    print "You have no capsules."
  else:
    print "You open a capsule."
    prize()
    

pull = Button(techo, text="Pull Lever", command=staticpull)
pull.pack()

capsule_inventory = Button(techo, text="Open Capsule ("+str(capsuleinventory)+")", command=checkinventory)

mainloop()
