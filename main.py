from pyscript import document
from pyodide.ffi import create_once_callable
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list

def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code


def roll_all_dice(event):

    dice_type = int(document.getElementById("Coin"))
    diceA = int(document.getElementById("DiceAmount"))
    #dice.dice_roll(dice_type)

    for roll in range(diceA):
        document.getElementById("roll-history").innerText = dice.dice_roll(int(dice_type))
        roll += 1

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""
    
button = document.getElementById("rollButton")
button.addEventListener("click", create_once_callable(roll_all_dice))