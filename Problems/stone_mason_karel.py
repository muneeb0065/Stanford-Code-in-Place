from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    while front_is_clear():
        build_coloumn()
        move_to_next_coloumn()
    build_coloumn()

def build_coloumn():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    return_to_base()

def return_to_base():
    turn_around()
    safe_move()
    turn_left()

def move_to_next_coloumn():
    for i in range(4):
        move()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def safe_move():
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()