"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
import sys

#Calculator Art:
#by Jeremy J. Olson http://www.chris.com/ascii/index.php?art=objects/calculators
print " _____________________ "
print "|  _________________  |"
print "| |   HACKBRIGHT X  | |"
print "| |_________________| |"
print "|  ___ ___ ___   ___  |"
print "| | 7 | 8 | 9 | | + | |"
print "| |___|___|___| |___| |"
print "| | 4 | 5 | 6 | | - | |"
print "| |___|___|___| |___| |"
print "| | 1 | 2 | 3 | | x | |"
print "| |___|___|___| |___| |"
print "| | . | 0 | = | | / | |"
print "| |___|___|___| |___| |"
print "|_____________________|"



# Your code goes here
while True:
    user_input = raw_input(">")
    tokenized_input = user_input.split(" ")

    #check to see if the input is valid here:
    confirm_numbers = tokenized_input[1:]
    for num in confirm_numbers:
        if num.isdigit() == False:
            print "Please enter valid numbers."
            break
        else:
            if tokenized_input[0] == "+":
                output = add(int(tokenized_input[1]),int(tokenized_input[2]))
            elif tokenized_input[0] == "-":
                output = subtract(int(tokenized_input[1]),int(tokenized_input[2]))
            elif tokenized_input[0] == "*":
                output = multiply(int(tokenized_input[1]),int(tokenized_input[2]))
            elif tokenized_input[0] == "/":
                output = divide(float(tokenized_input[1]),float(tokenized_input[2]))
            elif tokenized_input[0] == "square":
                if len(tokenized_input) != 2:
                    print "Please only enter one argument after typing square."

                output = square(int(tokenized_input[1]))
            elif tokenized_input[0] == "cube":
                output = cube(int(tokenized_input[1]))
            elif tokenized_input[0] == "pow":
                output = power(int(tokenized_input[1]),int(tokenized_input[2]))
            elif tokenized_input[0] == "mod":
                output = mod(int(tokenized_input[1]),int(tokenized_input[2]))
            elif tokenized_input[0] == "q":
                sys.exit()
            return output
