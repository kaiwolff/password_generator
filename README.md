# Password Group Project

A strong password is one of the main elements in cybersecurity.

As a cybersecurity expert, you've been asked to develop a python application to check the strength of a password and to recommend a strong password in case the entered password doesn't meet the password's policy.

App Specifications:
- The app can be a Command Line Interface (CLI) or a Graphical User Interface (GUI)
- The app should provide a list of actions so the user can choose the wanted action by entering the a number or a letter (for example, 1) Password Strength Checker, 2) Strong Password Generator, 3) Exit, etc).
- The app should show the action list after executing and finishing each action (loop).


Project Tasks:
1- Password Strength Checker:
  - Password's Policy: Write a password's policy (For example, number of characters, special characters, etc), this policy should be used to validate the entered passwords.
  - Most Common Password List: compile an updated list of the most common passwords and check the entered password against this list to protect against dictionary attacks.
  - Reading the Password: Read a password from the user.
  - General Password Strength Check: Check it against the password policy and the most common password list.
  - User-Based Password Strength Check: Read the user first name, last name and birthdate and check the existence of these information in the password.
  - Generate a report for each password (on the screen and can be exported to a text file), the report should provide the following information in a human-friendly language:
    - The final result whether the password is strong or weak.
    - The detailed reason(s) of this final result.
  - The user can export the report to a text file.

2-   Strong Password Generator:
  - Generate a password
  - Check it against the password's policy and the most common password list.
  - Check the existence of user's information (first name, last name, birthdate, etc) in the password.
  - Show the generated password and ask the user whether to generate another password using same user's information  

