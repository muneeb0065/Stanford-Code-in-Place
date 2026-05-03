# Karel MIdpoint


from karel.stanfordkarel import *


def main():

    # Put Beeper on all over the row
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    move_to_start()
    
     # Pick beepers from Last points
    pick_beeper()
    safe_move()
    pick_beeper()
    turn_around()
    move()

    # Pick rest of beepers from edges
    while beepers_present():
        edges()
    put_beeper()
    face_east()

def edges():
        pick_beeper()    
        move()    
        while beepers_present():
            move()
        turn_around()  # face east
        if no_beepers_present():
            move()



    #Move to Start
def move_to_start():
    turn_around()
    safe_move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def safe_move():
    while front_is_clear():
        move()



def face_east():
    if facing_west():
        turn_around()

if __name__ == '__main__':
    main()