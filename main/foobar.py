#!/usr/local/bin/python3
import getpass
import hashlib

salt = 'xyz'


# Login script - y'alls
# PEP 8 standards for format -Amilcar
# 3 validation functions - Andrew
# Try/except statement - Steven
# Ability to log info of any type. Must include login levels - Alex


##########################
#     	Login script
##########################

# Username - function
# Password - function
# dictionary
# 5 attempts
# Stretch goal: timeout 30s, 2 mins, 10 mins, etc.


##########################
#     	PEP 8
##########################
# Names/naming scheme
# Tabs indent -4
# limit all lines to 79 chars max


##########################
#     	Validation
##########################

# password validation - 1 capital letter, 1 special characer, 1 number,
# regular expression
# 8 char min, 24 char max
# No show password
# prevent certain characters
# /n, SELECT,

##########################
#     	Try/except
##########################

# Try/except instead of while loops
# Try to validate
# Try to login


##########################
#     	Logs
##########################

# Succesful login
# log for exempt characters
# log for attempts(5)
# log to sys
# log to file




def namePrompt():
    return input('Username: ')

def passPrompt():
    # Get pass hides password input on stdout
    # return getpass.getpass()
    return input('password: ')

def fileReader():
    filed = open('./loginInfo.txt', 'r').read().split(':')
    return filed
    # Close file later

def passwordHash():
    password = passPrompt() + salt
    return hashlib.sha256(password)


def loginChecker():
    try:
        print('hello world')

    except:
        print('Invalid username or password')