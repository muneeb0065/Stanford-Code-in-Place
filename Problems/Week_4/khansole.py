import random

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():

    print("Khansole Academy")

    rand_num_1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    rand_num_2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    total = rand_num_1 + rand_num_2

    print("What is " + str(rand_num_1) + " + " + str(rand_num_2) + "?")
    result = int(input("Your answer: "))

    if result == total:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {total}")

if __name__ == '__main__':

    main()