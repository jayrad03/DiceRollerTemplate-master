from pyscript import document
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"
diceA = "DiceAmount"
button = document.getElementById("rollButton")

def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code


def roll_all_dice(event):
    global dice_type
    global diceA
    #dice.dice_roll(dice_type)

    for roll in range(int(diceA)):
        document.getElementById("roll-history").innerText = dice.dice_roll(int(dice_type))
        roll += 1
    


def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""

document.getElementById("rollButton").addEventListener("click", roll_all_dice)