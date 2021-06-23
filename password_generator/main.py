import string
import random
import configparser
from flask import Flask, request, abort
from password_generator.passwordchecker import PasswordChecker

app = Flask(__name__)

@app.route('/passcheck/<password>/<user_firstname>/<user_secondname>/<int:birthyear>')
def perform_password_check(password, user_firstname, user_secondname, birthyear):
    password_tester = PasswordChecker()
    report = password_tester.check_password(password, user_firstname, user_secondname, birthyear)
    response = '. '.join([str(item) for item in report])
    return response
# if __name__ == "__main__":
#     main_func()
