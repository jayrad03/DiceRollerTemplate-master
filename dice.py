import sys
import random as rnd

def dice_roll(Faces):
    result = rnd.randint(1,Faces)
    return(int(result))

