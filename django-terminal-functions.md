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
