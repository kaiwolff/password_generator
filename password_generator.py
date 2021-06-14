from passwort_policy import PasswordPolicy

class PasswordGenerator(PasswordPolicy):

    def __init__(self):

    import string
    import random

    password = ""
    for _ in range(min_length, max_length):
        password = random.choice(characters)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(symbols)

password_generator = PasswordGenerator()

print(password)

