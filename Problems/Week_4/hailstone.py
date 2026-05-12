"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: "))

    while n != 1:
        if n%2 == 1:
            odd_case = (n*3) +1
            print(f"{n} is odd, so I make 3n + 1: {odd_case}")
            n = odd_case

        else:
            even_case = n//2
            print(f"{n} is even, so I take half: {even_case}")
            n = even_case

if __name__ == "__main__":
    main()