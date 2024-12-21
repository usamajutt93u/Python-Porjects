## Simple calculator

calculator_shape = """
 _____________________
|  _________________  |
| | AC           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(calculator_shape)

## 2nd step for data input and calculation has to be in same step
## so there would be two steps one is calculation inside the box and also
## inside the box. e.g., first would be like four functions for sum, addition, multiplications, and division

## Functions part of the code

## Defining Functions for sum, multiplication, addition and subtraction that can take infinite arguments.
## only needed if it's blind addition this functionality will be added in the future version of this calculator
'''
def sum(*arg):
    sum_of_number = 0
    for n in arg:
        sum_of_number += n
    return sum_of_number

def multiplication(*arg):
    mon = 0
    for n in arg:
        mon *= n
    return mon

def division(*arg):
    dom = 0
    for n in arg:
        dom /= n
    return dom

def subtraction(*arg):
    son = 0
    for n in arg:
        son -= n        
    return son

'''
## End Functions part of the code
conti = True
while conti:
    
    ## asking for fist number
    while True:
        try:
            num_input_i = float(input("Please enter your first number: "))
            print(f"Thank you! You entered the number: {num_input_i}")
            break  # Only Exit with correct float
        except ValueError:
            print("Invalid input. Please enter a number (int or float).\n")

    ## asking for math operation
    while True:
        math_operator = input("Please Enter your desired math operation you want: ")
        operators = ['+', '-', '*', '/']
        if math_operator in operators:
            break
        else:
            print("Please Enter correct math operator.")
    
    ## asking for next number
    while True:
        try:
            num_input_n = float(input("Please enter your second number: "))
            print(f"Thank you! You entered the number: {num_input_n}")
            break  # Only Exit with correct float
        except ValueError:
            print("Invalid input. Please enter a number (int or float).\n")
    
    ## applying math operations
    if math_operator == operators[0]:
        final_num = num_input_i + num_input_n
    if math_operator == operators[1]:
        final_num = num_input_i - num_input_n
    if math_operator == operators[2]:
        final_num = num_input_i * num_input_n
    if math_operator == operators[3]:
        final_num = num_input_i / num_input_n
    print("So, your total results is as follow.\n")
    print(f"{num_input_i} {math_operator} {num_input_n} = {final_num}")
    
    while True:
        cal_more = input("You want to continue more calculations, y/n: ")
        if cal_more == 'y':
            print("let's calculate more")
            break
        elif cal_more == 'n':
            conti = False
            break
        else:
            cal_more = input("Please Enter correct choice, y/n: ")
