#!/usr/local/bin/python3
import sys
import logging
import getpass
import hashlib
import re

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

##########################
#     	Code
##########################

logging.basicConfig(filename='login.log',level=logging.WARNING)

def namePrompt():
    return validator(input('Username: '))

def passPrompt():
    # Get pass hides password input on stdout
    return getpass.getpass()
    # return input('password: ')

def fileReader():
    filed = open('./loginInfo.txt', 'r').read().split(':')
    return filed
    # Close file later

def validator(entry):
    if(len(entry) < 4 or len(entry) > 25):
        print('Entry must be between 5 and 25 characters')
    elif(re.search(r"\n", entry)):
        print('New lines not allowed')
        logging.critical(entry, 'Input was a line break')
        sys.exit(exit)
    else:
        return entry

def passwordHash():
    password = hashlib.sha256((passPrompt() + salt).encode('utf-8')).hexdigest()
    return password.upper()

def credentialChecker():
    name = namePrompt()
    fd = fileReader()
    passcode = passwordHash()
    validator(name)
    if(name == fd[0]):
        if(passcode == fd[1]):
            print('Login Succesful!')
    else:
        print('Invalid Username or Password')

def loginChecker():
  try:
      credentialChecker()

# Raised when a function gets argument of correct type but improper value.
  except ValueError:
    logging.warning('Invalid input by user')
    print('Invaild username or password') 
    sys.exit(exit) 

# Raised when the user hits interrupt key (Ctrl+c or delete).
  except KeyboardInterrupt:
    logging.warning('Interrupt command input')
    print('Invaild keystrokes, try again') 
    sys.exit(exit) 

# Raised when the imported module is not found.
  except ImportError:
    logging.error('Module import error')
    print('Module Error') 
    sys.exit(exit) 

# Raised when an error does not fall under any other category.
  except RuntimeError:
    logging.error('An unknown error has occured')
    print('An unknown error has occured') 
    sys.exit(exit) 

loginChecker()