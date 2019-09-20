SecureSet Academy
=================================================

## Login Script

#### Group: Andrew Galvin, Amilcar Spezia, Alex White, Steven Wilkins

### Why switch to our code
Our login code offers a secure way to manage your users logins. With this secure code, you can have peace of mind. Our code is compliant with PEP8 standards, uses efficient logging methods, validates user entries, and implements an efficient Try/Except statement to keep everything running smoothly.

### Modules
```
main/
├── login.py
├── loginInfo.text
└── 10K-common-passwords.txt
```
#### `login.py`
This is the main file that contains the login script

#### `loginInfo.txt`
This file contains all the usernames and salted/hashed passwords

#### `10k-common-passwords.txt`
This file contains the 10K most common paswwords to compare against

### Running the app

* Run `./login.py`

### Psuedo Code

#### Login script
1. PEP 8 standards for format `-Amilcar`
2. 3 validation functions - `Andrew`
3. Try/except statement - `Steven`
4. Ability to log info of any type. Must include login levels - `Alex`

#### Login script
* Username - function
* Password - function
* dictionary
* 5 attempts
* Stretch goal: timeout 30s, 2 mins, 10 mins, etc.

#### PEP 8
* Names/naming scheme
* Tabs indent -4
* limit all lines to 79 chars max

#### Validation
* password validation - 1 capital letter, 1 special characer, 1 number,
* regular expression
* 8 char min, 24 char max
* No show password
* prevent certain characters
* /n, SELECT,

#### Try/except
* Try/except instead of while loops
* Try to validate
* Try to login

#### Logs
* Succesful login
* log for exempt characters
* log for attempts(5)
* log to sys
* log to file

### Login Script
This secure login script uses:
* Hashing
* PEP8 Standards
* Logging
* Entry validation


### PEP8 Standards
* Python Enhancement Proposal.Makes your code more organized and readable. 
* Use 4 spaces per indentation level.
* Spaces are the preferred indentation method.
* Pick a rule and stick to it when a string contains single or double quote characters.
* limit all lines to 79 chars max.
* Comments should have 72 characters of line length. 

### Validation
Our validation ensures the user input doesn't contain illegal symbols
* no "\n"
* Between 5 and 25 characters

### Try/Except
* Exception handling allows a programmer to enbale flow control. Try and except is the most common way of handling unexpected errors along with many exception handling constructs. Try allows you to implement an exception and handle the error inside an expect block, when the code breaks inside a try block the regular code flow will step and control will get switched to the except block for handling the error. The try and expect can slove race conditions really well.

* In this script I used 4 common expception error that occured in programming scripts

* VauleError occurs when a function gets a argument correct type but improper value, I used this to slove if a user puts in the correct name but wrong passwoord.

* KeyboardInterrput is raised when the user hits a interrput key (Ctrl+c or delete). I used this to slove if a user hits these keys on accident or in a attepmt to hack the login page.

* ImportError is raised when the imported module is not found. Since our code is using five modules I want to use this in case of any issues with the modules

* RuntimeError raised when an error does not fall under any other category. In the event if an unknown error occures, this exception will address it. This is a catch all error.
### Logs
Logging 
* Level set to warning
* Critical log if user tries to input "\n" - new line

### References
* https://www.programiz.com/python-programming/exceptions
* https://www.w3schools.com/python/python_try_except.asp

