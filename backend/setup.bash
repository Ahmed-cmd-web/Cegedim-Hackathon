#!/bin/bash

BBlue='\033[1;34m'
BGreen='\033[1;32m'

python3 -m venv v1

source "$PWD/v1/bin/activate"
pip install --upgrade pip

pip3 install -r requirements.txt

printf "${BBlue}Project has been setup successfully! \nTry running the following command: \n ${BGreen}python3 manage.py runserver \n"