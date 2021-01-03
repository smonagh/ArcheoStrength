# ArcheoStrength

## About
A small flask application I put together to help keep track of my progress on the starting strength routine.
I've started this over now a few different times, so I'm hoping that by keeping track of my data I will
remain motivated to continue... we'll see!


## Installation

This is still in its infancy, so the intall is fairly manual. An application installer will be created in the near future.

1. Clone the repository
2. Setup a virtual environment
3. pip install -r requirements.txt
4. flask db init
5. flask db migrate
6. flask db upgrade
7. export FLASK_APP=starting_strength
8. flask run

Then you can access the application in your browser by accessing http://127.0.0.1:5000. Of course, if you are already familiar
with flask then you can edit most of these step according to your preferences.
