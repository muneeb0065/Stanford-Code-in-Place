from karel.stanfordkarel import *

def main():
    #Move and find the supplies
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()


   #Tell the karel how to build hospital     
def build_hospital():
    pick_beeper()
    build_1st_coloumn()
    build_2nd_coloumn()



def build_1st_coloumn():
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    return_to_base()
    turn_left()
    move()


def build_2nd_coloumn():
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    return_to_base()
    turn_left()



# Return to Starting Point
def return_to_base():
    turn_around()
    move_to_starting_point()



def move_to_starting_point():
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def safe_move():
    if front_is_clear():
        move()

if __name__ == '__main__':
    main()