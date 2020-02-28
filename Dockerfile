FROM python:alpine3.7
COPY . /app
WORKDIR /app
run pip3 install -r requirements.txt
CMD python3 ./modified_palindrome.py -w "rotor"