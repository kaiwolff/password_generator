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
  
## Final Working Code:

```python
import string
import random
import configparser

class PasswordChecker:

    def take_input(self):
        #Take full user name, year of birth. as user what option (generate, check, or exit).
        user_choice = None
        while True:

            while True:
                options_choices = input('Please enter one of the following options: Check Password (1), Generate Password (2) or Exit (3) ')
                if options_choices in ('1', '2', '3'):
                    user_choice = options_choices
                    break
                else:
                    print('Please choose a valid option')

            if user_choice == '3':
                break

            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')

            while True:
                birth_year = input('Enter your year of birth: ')
                if birth_year.isdigit() == True:
                    break
                else:
                    print("Please enter a number.")

            if user_choice == '1':
                password = input('Please input password to check: ')
                self.check_password(password, first_name, last_name, birth_year)
            elif user_choice == '2':
                self.generate_password(first_name, last_name, birth_year)

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

    def check_password(self, password, first_name, second_name, birth_year):
        print("opened check_password")
        # check password against password policy, their name, DOB, and common passwords. Written by KW
        report = []

        policy_compliant = self.check_policy(password)
        # print(f"checked policy compliance {policy_compliant}")

        if policy_compliant:
            report.append("Complies with password policy")
            # print("Complies with password policy")
        else:
            report.append("Does not comply with password policy")
            # print("Does not comply with password policy")

        not_common = self.check_list(password)
        # print("common passwords checked")

        if not_common:
            report.append("Not in list of common passwords")
            # print("Not in list of common passwords")
        else:
            report.append("Found in list of common passwords")
            # print("Found in list of common passwords")

        user_detail_free = self.check_user_details(password, first_name, second_name, birth_year)
        if user_detail_free:
            report.append("No user details in password")
        else:
            report.append("User Details Found in Password")

        if policy_compliant and not_common and user_detail_free:
            report.append("This means that the password is STRONG.")
        else:
            report.append("This means that the password is weak")

        self.generate_report(report, password)
        if not policy_compliant or not not_common or not user_detail_free:
            while True:
                generate_new_password = input("Would you like to have a strong password generated for you? (y/n): ")
                if generate_new_password.lower() == "y":
                    self.generate_password(first_name, second_name, birth_year)
                    break
                elif generate_new_password.lower() == "n":
                    break
                else:
                    print("Please enter a valid input")

    def check_list(self, password):
        # checks password against passwords in common_passwords.txt. Returns True if password is not in file, False if found.Written by KW
        with open('common_passwords.txt', 'r') as password_file:
            # iterates through whole file
            for line in password_file:
                if password in line:
                    password_file.close()
                    return False
                elif line == False:
                    # line will be empty if nothing left in file
                    print("end of file reached")
                    password_file.close()
                    break
        return True

    def check_policy(self, password):
        # reads password policy, checks if password complies with requirements. Returns True if yes, False if not. Written by KW
        policy_list = self.read_password_policy()
        # print(policy_list)
        # now hav ea list defining password policy
        num_specials = policy_list[0]
        num_lowercase = policy_list[1]
        num_uppercase = policy_list[2]
        num_numbers = policy_list[3]
        min_length = policy_list[4]
        max_length = policy_list[5]
        allowed_specials = policy_list[6]

        count_specials = 0
        count_lower = 0
        count_upper = 0
        count_numbers = 0

        if len(password) < min_length or len(password) > max_length:
            # not compliant if too short or too long
            return False

        for letter in password:
            # check each letter to see if special, lower, upper, or number. Count each of these
            if letter.isdigit():
                count_numbers += 1
            elif letter.isupper():
                count_upper += 1
            elif letter.islower():
                count_lower += 1
            elif letter in allowed_specials:
                count_specials += 1
            else:
                # return false if part of password is not in any allowed category
                print("illegal character")
                return False

        # now have a count of all the lower, upper, special characters and numbers
        if count_upper >= num_uppercase and count_lower >= num_lowercase and count_specials >= num_specials and count_numbers >= num_numbers:
            return True
        else:
            return False

    def check_user_details(self, password, user_firstname, user_lastname, user_birthyear):
        # checks if the password contains the user name or year of birth. Outputs True if no user details in the password. Written by KW
        if user_firstname in password:
            return False
        elif user_lastname in password:
            return False
        elif user_birthyear in password:
            return False
        else:
            return True

    def generate_report(self, report, password):
        # formats output in human-readable way. Checks if user wants this put into a file. Written by KW
        print(f"Password was: {password}")
        for line in report:
            print(line)
        # ask user if they want to write to file
        wants_file = input("Would you like this written to a file (y/n) ? ")
        if wants_file.lower() == "y":
            self.write_to_file(report, password)
        else:
            return "Report not written to file"

    def write_to_file(self, report, password):
        while True:
            # writes report to file. can append or overwrite. Written by KW
            write_type = input("Please select 1 to append, or 2 to overwrite: ")

            if write_type != "1" and write_type != "2":
                print("Please input a valid option.")
                continue

            elif write_type == "1":
                file = open('password_report.txt', 'a')

            elif write_type == "2":
                file = open('password_report.txt', 'w')

            file.write(f"Password was: {password} \n")
            for line in report:
                file.write(f"{line}\n")

            file.write(f"\n")
            return "Report written to password_report.txt"
            break

    def read_password_policy(self):
        # reads in password policy, returns variables as a list. Written by KW
        # password_policy = open('password_policy.txt', 'r')
        policy = configparser.ConfigParser()
        policy.read('password_policy.txt')
        num_specials = policy.getint('Policy', 'num_specials')
        num_lowercase = policy.getint('Policy', 'num_lowercase')
        num_uppercase = policy.getint('Policy', 'num_uppercase')
        num_numbers = policy.getint('Policy', 'num_numbers')
        min_length = policy.getint('Policy', 'min_length')
        max_length = policy.getint('Policy', 'max_length')
        allowed_specials = policy.get('Policy', 'allowed_specials')

        return [int(num_specials), int(num_lowercase), int(num_uppercase), int(num_numbers), int(min_length),
                int(max_length), allowed_specials]


password_tester = PasswordChecker()
password_tester.take_input()
# password_tester.generate_password("Afshana", "Begum", "1997")
```