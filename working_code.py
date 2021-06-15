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

            # Generating the password using random
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

            # Checking against the user's details, password's policy and the most common password list.
            user_details_check = self.check_user_details(password, user_firstname, user_lastname, user_birthyear)
            policy_compliance_check = self.check_policy(password)
            checking_list = self.check_list(password)
            if user_details_check == False or policy_compliance_check == False or checking_list == False:
                # print("Regenerating a new password: ") # this is a test to check against user details
                continue

            print(password)

            while True:
                write_report = input("Would you like a report on this password? (y/n) ")
                if write_report.lower() == 'y':
                    self.check_password(password, user_firstname, user_lastname, user_birthyear)
                    break
                elif write_report.lower() == "n":
                    break
                else:
                    print("Please input a valid option.")

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

            # strongpassword.txt - give append or overwrite - ask user if they want to

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

    #########################TESTBED


password_tester = PasswordChecker()
password_tester.take_input()
# password_tester.generate_password("Afshana", "Begum", "1997")