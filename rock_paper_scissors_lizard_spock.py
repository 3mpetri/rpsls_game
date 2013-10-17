#! /usr/bin/env python

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
import sys

def number_to_name(number):
    # fill in your code below
    
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else: 
        sys.exit("Wrong input!")
        
    return number
        
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    number = name_to_number(name)

    # convert name to player_number using name_to_number
    
    comp_number = random.randrange(0,5)

    # compute random guess for comp_number using random.randrange()
    
    diff = (number - comp_number) % 5

    # compute difference of player_number and comp_number modulo five
    
    if diff == 1 or diff == 2:
        result = 'Player wins!'
    elif diff == 3 or diff == 4:
        result = 'Computer wins!'
    elif diff == 0:
        result = 'Its a draw!'

    # use if/elif/else to determine winner
    
    comp_name = number_to_name(comp_number)

    # convert comp_number to name using number_to_name
    
    print "\n--------------------"
    print "Player choses", name
    print "Computer choses", comp_name
    print result
    print "--------------------"
    
    # print results

    

print "rock, paper, scissors, lizard, Spock?\n"
input = raw_input("One.. Two.. Three!\n\n")

rpsls(input)

