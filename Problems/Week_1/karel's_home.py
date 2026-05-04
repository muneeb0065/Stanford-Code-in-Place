from karel.stanfordkarel import *


def go_and_pick_beeper():
    safe_move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def return_home():
    turn_around()
    safe_move()
    turn_right()
    move()
    face_east()


def safe_move():
    while front_is_clear():
        move()

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    for _ in range(2):
        turn_left()

def face_east():
    turn_right()

def main():

    go_and_pick_beeper()
    return_home()
    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()