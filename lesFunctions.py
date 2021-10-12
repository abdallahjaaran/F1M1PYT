print ("Hello world")
def add(getal1, getal2):
    som = getal1 + getal2
    print(som)
    
add(1, 2)
add(56, 57)

def multiply(getal1, getal2):
    som = getal1 * getal2
    print(som)

multiply(1,2)

import random

def roll_dice():
    rand_getal = random.randrange(1, 7)
    print("ik rol een getal")
    return rand_getal 

r1 = roll_dice()
r2 = roll_dice()
r3 = roll_dice()
r4 = roll_dice()
print(r1, r2, r3, r4)

def larger_num(getal1, getal2):
    if geral 1 > getal2:
        return getal1
    elif getal2 > getal1:
        return getal2
    else:
        return 0

