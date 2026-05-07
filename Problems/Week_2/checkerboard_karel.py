from karel.stanfordkarel import *

def main():

    fill_odd()
    return_to_base()
    
    # 2. Check if there is a ceiling above us
    while left_is_clear():
        # If we can go up, the next row is an EVEN row
        move_to_next()
        fill_even()
        return_to_base()
        
        # Inside the loop, check if there is STILL a ceiling above us
        if left_is_clear():
            # If so, the next row is an ODD row
            move_to_next()
            fill_odd()
            return_to_base()
    starting_position()


def return_to_base():
    turn_around()
    move_to_wall()
    turn_around()


def move_to_next():
    if left_is_clear():
        turn_left()
        move()
        turn_right()



def fill_odd():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def fill_even():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()

           

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def starting_position():
    face_west()
    move_to_wall()
    face_south()
    move_to_wall()
    face_east()


def face_east():
    while not_facing_east():
        turn_left()

def face_west():
    while not_facing_west():
        turn_left()

def face_south():
    while not_facing_south():
        turn_left()

if __name__ == '__main__':

    main()