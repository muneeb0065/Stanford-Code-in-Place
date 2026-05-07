from karel.stanfordkarel import *

def picks_beeper():
    while no_beepers_present():
        move()
    pick_beeper()

def put_at_given_position():
    move()
    turn_left()
    move()
    move()
    put_beeper()

def come_back_home():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    face_east()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_east():
    turn_around()

def main():
    picks_beeper()
    put_at_given_position()
    come_back_home()
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()