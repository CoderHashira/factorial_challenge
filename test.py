from math import factorial

number = input("Enter a number: ")
sum_digit = 0

def my_number(number, sum_digit):
    
    for digit in number: # The for loop is to loop through the string literal and convert the strings into numbers so that we can perform mathematical operations
    
        #digit = int(digit)

        factorial_digit = factorial(int(digit)) + sum_digit # created sum_digit as a global variable to avoid any namespace and variable initialization errors

        sum_digit = factorial_digit # Used sum digit to store the results from factorial_digit

        print(sum_digit)
        

    if sum_digit == int(number):
        print(f'The sum of the factorial of the single digits of {number} are equal to the number')
    else:
        print(f'The sum of the factorial of the single digits of {number} are not equal to the number')

my_number(number, sum_digit)

