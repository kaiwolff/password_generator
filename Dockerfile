FROM python:3
ADD password_generator/working_code.py /password_generator/
ADD password_generator/common_passwords.txt /password_generator/
ADD password_generator/password_policy.txt /password_generator/
WORKDIR /password_generator/
CMD [ "python", "working_code.py" ]

