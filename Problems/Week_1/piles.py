from karel.stanfordkarel import *

def pick_all_the_beepers():
    while beepers_present():
        pick_beeper()
        if no_beepers_present():
            move()



def main():

    while front_is_clear():
        move()
        pick_all_the_beepers()


   

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()