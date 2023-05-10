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
- python3 manage.py showmigrations
    - lists current apps to be migrated into project, including some stock django apps
- python3 manage.py migrate --plan
    - will carry out necessay migrations. "--plan" flag will show you what would happen if you would run the command
- python3 manage.py createsuperuser
    - create an admin to log into the database to view it and make changes
    - admin for this repo: calrex
    - password: crunchyroll password

