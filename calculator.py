"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input(">")
    tokenized_input = user_input.split(" ")
    if tokenized_input[0] == "+":
        output = add(int(tokenized_input[1]),int(tokenized_input[2]))
    print output