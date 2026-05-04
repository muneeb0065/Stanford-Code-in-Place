from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""
def main():

    move()
    spread()
    step_back()


def step_back():
    turn_around()
    move()
    turn_around()


def spread():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_suitable_place()
            put_beeper()
            return_back()
    put_beeper()

def move_to_suitable_place():
    while beepers_present():
        move()
        
def return_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()


def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()