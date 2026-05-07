import random

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    correct_no_of_times= 0

    print("Khansole Academy")



    while correct_no_of_times<3:
        rand_num_1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        rand_num_2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        total = rand_num_1 + rand_num_2

        print("What is " + str(rand_num_1) + " + " + str(rand_num_2) + "?")
        result = int(input("Your answer: "))

        if result == total:
            print("Correct!")
            correct_no_of_times +=1
            print("You've gotten " + str(correct_no_of_times) + " correct in a row."                       )
        else:
            correct_no_of_times =0
            print("Incorrect.")
            print(f"The expected answer is {total}")   

    print("Congratulations! You mastered addition.")  



if __name__ == '__main__':
    main()