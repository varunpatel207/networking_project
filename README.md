#Project Setup
 - clone git repo
 - `cd networking_project`
 - create python virtual environment `python3 -m venv venv`
 - activate virtual env `source venv/bin/activate`
 - install all the dependencies from requirements file `pip install -r requirements.txt`
 - `cd src`
 - run migration command `python manage.py migrate`
 - run server `python manage.py runserver localhost:8000`