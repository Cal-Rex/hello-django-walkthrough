##### Create a directory with all necessary files and a managment utility at the top level of the project directory: 
django-admin startproject  django_todo .

**creates following files:**
 ____init__.py: file that tells project that this is a driectory that we can import from
 settings.py: contains settings for entire django project (Debug menu show etc.)
 urls.py: contains routing information, analogous to app.root in flask
 wsgi.py: allows web server to communicate with python application
 asgi.py:
 db.sqlite3: acts as the database for the project, do not delete or change!

#### Allows web server to communicate with python application:
python3 manage.py runserver

##### creates a django "app" called "todo"
python3 manage.py startapp todo

##### migrations
migrations django's way of turning python code into database operations, basically mimics running raw SQL commands in the terminal by writing python code.
###### 3 key python terminal commands to manage migrations
- python3 manage.py makemigrations --dry-run
    - when new models have been made/changed, this command needs to be run without the "--dry-run" tag
    - basically creates the necessary files for a created model/s to become a database item/table
- python3 manage.py showmigrations
    - lists current apps to be migrated into project, including some stock django apps
- python3 manage.py migrate --plan
    - will carry out necessay migrations. "--plan" flag will show you what would happen if you would run the command
- python3 manage.py createsuperuser
    - create an admin to log into the database to view it and make changes
    - admin for this repo: calrex
    - password: crunchyroll password

##### Installing Coverage
Coverage is a tool that shows how much of the code in the project has actually been tested.
it can be installed in the terminal:
    - pip3 install coverage

this can then be utilised in the terminal with the following command:
    - coverage run --source=FOLDER manage.py test
    - in this instance, it should be:
        - coverage run --source=todo manage.py test
It will then run the tests and store a report. the report can then be accessed with the following command:
    - coverage report
to get more specific data from your report, you can look at a fully interactive HTML version of the report
with the following command:
    - coverage html
This generates a folder in the project called htmlcov
it can then be viewed by using the standard viwing html console command:
    - python3 -m http.server