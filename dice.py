import sys
import random as rnd

def dice_roll(Faces):
    value = int(Faces)
    result = rnd.randint(1,value)
    return(result)

