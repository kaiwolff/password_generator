# Strong Password Generator Project

*Group Project by Kai Wolff, Munira Mohamed and Afshana Begum*

## Introduction

A strong password is one of the main elements in cybersecurity.

As a cybersecurity expert, you've been asked to develop a python application to check the strength of a password and to recommend a strong password in case the entered password doesn't meet the password's policy.

## Aims and Objectives:

App Specifications:
- The app can be a Command Line Interface (CLI) or a Graphical User Interface (GUI)
- The app should provide a list of actions so the user can choose the wanted action by entering the a number or a letter (for example, 1) Password Strength Checker, 2) Strong Password Generator, 3) Exit, etc).
- The app should show the action list after executing and finishing each action (loop).


Project Tasks:

[1] Password Strength Checker:

  - Password's Policy: Write a password's policy (For example, number of characters, special characters, etc), this policy should be used to validate the entered passwords.
  - Most Common Password List: compile an updated list of the most common passwords and check the entered password against this list to protect against dictionary attacks.
  - Reading the Password: Read a password from the user.
  - General Password Strength Check: Check it against the password policy and the most common password list.
  - User-Based Password Strength Check: Read the user first name, last name and birthdate and check the existence of this information in the password.
  - Generate a report for each password (on the screen and can be exported to a text file), the report should provide the following information in a human-friendly language:
    - The final result whether the password is strong or weak.
    - The detailed reason(s) of this final result.
  - The user can export the report to a text file.

common_passwords.txt - This list was taken from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

### Manual

### Required Files
#### Password Policy

This file is a config file for the password policy, and allows a user to change the various requirements for a password (such as minimum and maximum length, or the list of allowed characters). These can be edited by a user. It is advised to avoid localised characters (2.g £, or Umlauts) as allowed special characters as this interfered our unit testing.

#### Common Passwords File

A file listing (at the moment) 10 thousand common passwords. This serves to protect a user from a basic dictionary attack

The file can be replaced with any list of passwords, as long as it is named "common_passwords.txt". Passwords should be one per line.
### Required Modules

This code imports `configparser`, `random` and `string`.
### Key Functions

#### check_password

This function will take in a user's first and last names, the year of birth and a password to be checked against the user details. The  functions runs checks against the password policy, checks the password against a list of common passwords (see also "Password Policy" and "Common Passwords File", above), and makes sure that no user details are contained in the password. The function then lists which tests are passed (by their test functions returning `True`), and declares the password strong if all tests were passed (weak otherwise).

The information is presented in a list called report, containing a line on a particular test per entry. This is passed to `generate_report`, where the user is given the option to save this information.

#### generate_report

Unpacks the `report` list and prints it for the user to see. Will then offer the user the option of saving the report in a file, calling write_to_file if this option is selected.

#### write_to file

Asks the user if they want to append or overwrite the file `password_report.txt`. prints tested password and report on tests passed or failed into the file.

## Test Functions

Tests were packed into separate functions as this would allow reuse to check any generated passwords. Three test functions were created: `check_policy`, `check_user_details`, and `check_list`.

`check_policy` calls a function to read in the password policy from the filed `password_policy.txt`, and uses the returned values to make sure that the password is the correct length (between `min_length` and `max_length`) and that the password has at least the required number of numbers, lowercase characters, uppercase characters and special characters. If special characters that are not part of the `allowed_specials` string are used, the password policy is considered failed. The policy can be edited via the password_policy.txt file. Will return `True` if password policy is obeyed, `False` otherwise.

`check_user_details` looks for the user details (First name, second name, year of birth) as part of the password. If any user details are found, it returns `False`.

`check_list` looks at the file `common_passwords`, and returns `True` if the password is not part of the list. Otherwise, will return `False`.


[2]   Strong Password Generator - the requirements are as follows:

  - Generate a password
    
    - A new function was defined and named as `generate_password` which passes the argument's `user_firstname`, `user_lastname` and `user_birthyear` as these will be required to be passed in the function. 
      
    - In order to generate a password, it was necessary to extract some values from the `password_policy` function such as the `max_length` (number of characters that will be added in the password) and `allowed_characters`. 
      
    - A new variable was defined as password with an empty string so that when the password is generated by the system, it will add to this empty string. 
      
    - random and string modules were imported in order to use them as part of the password generator.
      
    - The password was generated using a:
      - for loop ( which will iterates over the if else statements) 
      - if, else statement
      - the range() function (returns a sequence of characters starting from 0 to maximum_length ) 
      - we defined a variable called random_character with the random module called the randint() method (randomly returns a character of its choice according to the if else statement)
    - string.ascii_lowercase and string.ascii_uppercase gives you a string with the alphabet letters in lower case and upper case which, if the randint() method chooses can store it in the password, and the random.choice() method picks a random character from this pre-initialised string.
    
      
  - Check it against the password's policy, and the most common password list.
    
    - The password generated was checked against the password's policy and common password list. We defined a variable called `policy_compliance_check` and called the `check_policy` function which runs the check and checks if certain policies are met such as the password being between the minimum and maximum length and counting the particular type of character in the password etc.
      
    - This is the same with the check_list which runs a check against the list of common passwords.
    

  - Check the existence of user's information (first name, last name, birthdate, etc) in the password.
    
    - The password generated was checked against the password user's information. We defined a variable called user_details_check and called the check_user_details function which runs the check to check that the password is does not include the user's first name, last name and birth year.
    
    
  - Show the generated password and ask the user whether to generate another password using same user's information  
    
    - user was prompted an option for if they wanted to generate another password which was done using an if, else statement. 
    
Extra Added feature:
- User has the option also for if they would to generate a report on the password that they were given to reveal with how the password complies with password policy. 

Code for password generator:

```python
    def generate_password(self, user_firstname, user_lastname, user_birthyear):

        while True:

            # reading through the password policy and looping through to extract necessary values to check and generates the password
            policy_checklist = self.read_password_policy()
            max_length = policy_checklist[5]
            allowed_characters = list(policy_checklist[6])

            # Generating the password using random and string modules 
            password = ""
            for character in range(max_length):

                random_character = random.randint(1,4)

                if random_character == 1:
                    password += random.choice(allowed_characters)
                elif random_character == 2:
                    password += random.choice(string.ascii_lowercase)
                elif random_character == 3:
                    password += random.choice(string.ascii_uppercase)
                else:
                    password += random.choice(string.digits)

            # checking against the user's details, password's policy and the most common password list.
            user_details_check = self.check_user_details(password, user_firstname, user_lastname, user_birthyear)
            policy_compliance_check = self.check_policy(password)
            checking_list = self.check_list(password)
            if user_details_check == False or policy_compliance_check == False or checking_list == False:
                # print("Regenerating a new password: ") # this is a test to check against user details
                continue

            # shows the generated password
            print(password)
            
            # asks the user whether they would like a compliance report on their password 
            while True:
                write_report = input("Would you like a report on this password? (y/n) ")
                if write_report.lower() == 'y':
                    self.check_password(password, user_firstname, user_lastname, user_birthyear)
                    break
                elif write_report.lower() == "n":
                    break
                else:
                    print("Please input a valid option.")

            # asks the user whether to generate another password using same user's information
            while True:
                ask_again = input("Would you like to generate a new password? (y/n) ")
                if ask_again.lower() == "y":
                    break
                elif ask_again.lower() == "n":
                    break
                else:
                    print("Please input a valid option.")

            if ask_again == "n":
                break
```