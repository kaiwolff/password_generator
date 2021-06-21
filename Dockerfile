FROM python:3
WORKDIR /usr/src/app

ADD working_code.py ./
ADD common_passwords.txt ./
ADD password_policy.txt ./

CMD [ "python", "./working_code.py" ]
