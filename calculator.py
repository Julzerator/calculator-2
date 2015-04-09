"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
import sys


# Your code goes here
while True:
    user_input = raw_input(">")
    tokenized_input = user_input.split(" ")
    if tokenized_input[0] == "+":
        output = add(int(tokenized_input[1]),int(tokenized_input[2]))
    elif tokenized_input[0] == "-":
        output = subtract(int(tokenized_input[1]),int(tokenized_input[2]))
    elif tokenized_input[0] == "*":
        output = multiply(int(tokenized_input[1]),int(tokenized_input[2]))
    elif tokenized_input[0] == "/":
        output = divide(float(tokenized_input[1]),float(tokenized_input[2]))
    elif tokenized_input[0] == "square":
        output = square(int(tokenized_input[1]))
    elif tokenized_input[0] == "cube":
        output = cube(int(tokenized_input[1]))
    elif tokenized_input[0] == "pow":
        output = power(int(tokenized_input[1]),int(tokenized_input[2]))
    elif tokenized_input[0] == "mod":
        output = mod(int(tokenized_input[1]),int(tokenized_input[2]))
    elif tokenized_input[0] == "q":
        sys.exit()
    print output