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

#### Installing a database external of Heroku
    - once deployed, Heroku will use an Ephemeral file system, meaning that any time it is closed or redeployed, all files are deleted and recreated on the next iteration
    - this means databases get wiped
    - to mitigate this, psycopg2 is installed to connect to a postGres database to keep the database extarnal from the Heroku deployment
    - a package called Gunicorn (green unicorn) will also need to be installed to replace the development server once the app is deployed (acts as the webserver for the app)

#### installing psycopg2
    needed to use postGREs database functionality
    command to install psygopg2:
        - pip3 install psycopg2-binary

#### installing Green unicorn
    - pip3 install gunicorn

#### creating a requirements.txt
    - this file tells heroku what packages to install every time the app starts up
    - once all necessary packages above have been installed, use the following command to create the requirements.txt file:
    - pip3 freeze --local > requirements.txt

#### deploying on Heroku
    Unless using the code institute template, Heroku needs to be installed into the project via the command line. this can be done by google searching "install heroku CLI" 
        - you can use the code snippet to install the CLI in the browser-based gitpod environment, even though it says it's specifically for linux
        - once installed, you can log into heroku in the terminal by using:
            - heroku login -i
        - enter username and password
            - because of 2FA/MFA, the password is set your API key on heroku
    
    ##### Creating an app on heroku
        use command:
         - heroku apps:create APPNAME --region eu
            - remove --region if you want data server to default to united states

#### using Git
    - when an app is created in heroku, it automatically creates a code repository that we can push our code changes to
    - to get the remote urls for the Git repo on heroku:
        - git remote -v
            - v for verbose
    - this will display the 2 git repos for the project, the one on heroku, and the one native on gitpod
        - the one on gitpod/hub is origin
        - heroku is heroku
    - each one has 2 key remote urls
        - one to fetch code from the repo
        - one to push code to the repo
    to utilise these commands you would use commands as such:
        - git push origin main
        - git push heroku main
    
    