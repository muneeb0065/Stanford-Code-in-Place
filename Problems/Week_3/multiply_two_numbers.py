"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    # your code here
    first_number=int(input("Enter first number: "))
    second_number=int(input("Enter second number: "))
    print(first_number*second_number)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()