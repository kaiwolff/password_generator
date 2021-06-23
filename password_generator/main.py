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

# query string version

@app.route('/passcheck')
def perform_password_check_query():

    password = request.args.get('passw')
    user_firstname = request.args.get('firstname')
    user_secondname = request.args.get('lastname')
    birthyear = request.args.get('birthyear', type=int)


    if password is None or user_firstname is None or user_secondname is None or birthyear is None:
        abort(401)

    password_tester = PasswordChecker()
    report = password_tester.check_password(password, user_firstname, user_secondname, str(birthyear))
    response = '. '.join([str(item) for item in report])
    return response
# if __name__ == "__main__":
#     main_func()
@app.route('/passgen')
def perform_password_gen_query():

    user_firstname = request.args.get('firstname')
    user_secondname = request.args.get('lastname')
    birthyear = request.args.get('birthyear', type=int)


    if user_firstname is None or user_secondname is None or birthyear is None:
        abort(401)

    password_tester = PasswordChecker()
    response = password_tester.generate_password(user_firstname, user_secondname, str(birthyear))

    return response
