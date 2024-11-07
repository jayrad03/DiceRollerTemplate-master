import sys
import random as rnd

arg_count = len(sys.argv)
firstArg = sys.argv[0]
if arg_count > 1:
    diceA = sys.argv[1] 
    diceF = sys.argv[2] 
    print(f"You have selected {diceA} dice with {diceF} faces.")

def dice_roll(Faces):
    result = rnd.randint(1,Faces)
    return(result)

for roll in range(int(diceA)):
    whichOne = roll + 1
    result = dice_roll(int(diceF))
    print(f"Roll {whichOne} = {result}")