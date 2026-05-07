from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while left_is_clear():
        put_beepers_in_row()
        return_to_base()
        move_to_next_row()

    put_beepers_in_row()

def put_beepers_in_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def return_to_base():
    turn_around()
    safe_move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

def safe_move():
    while front_is_clear():
        move()

def move_to_next_row():
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()