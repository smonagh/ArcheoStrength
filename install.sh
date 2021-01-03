#!/bin/sh

# Install python
sudo apt install python3
sudo apt install python3-pip

# Setup python environment
sudo pip3 install virtualenv
python3 -m virtualenv env
. env/bin/activate
pip install -r requirements.txt

# Setup flask database 
flask db init
flask db migrate
flask db upgrade


