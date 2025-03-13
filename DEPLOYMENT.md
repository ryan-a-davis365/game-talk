# Deployment

## Table of Contents

### Setting up a basic Django project and deploying to Heroku

* [**Deployment**](#deployment)
    * [***Initial Deployment***](#initial-deployment)
    * [***Create Repository***](#create-repository)
    * [***Setting up the Workspace***](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [***Deploying an app to Heroku***](#deploying-an-app-to-heroku)
        * [***Create a New External Database***](#create-a-new-external-database)
        * [***Create Heroku App***](#create-heroku-app)
        * [***Attach the Database***](#attach-the-database)
        * [***Preparing Environment and settings.py File***](#preparing-environment-and-settings.py-file)



## Initial Deployment

I took the following steps to deploy the site to Heroku and have listed any console commands required to initiate it.

### Create repository:

* Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * **Note** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
        * pip install -r requirements.txt
    * **IMPORTANT** - If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will put other projects at risk

### Setting up the Workspace (To be done locally via the console of your chosen editor):
1. Create a virtual environment on your machine:
    * python -m venv .venv
1. To ensure the virtual environment is not tracked, add .venv to the .gitignore file.
1. Install Django:
    * `py -m pip install Django==5.1.7`
1. Install supporting libraries:
    * `pip install dj_database_url==0.5.0 psycopg2`
    * `pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15`
1. Create requirements.txt:
    * `pip freeze --local > requirements.txt`
1. Create an empty folder for your project in chosen location.
1. Create a project in the above folder:
    * `django-admin startproject PROJECT_NAME .` (in the case of this project, the project name was "game-talk")
1. Create an app within the project:
    * `python3 manage.py startapp APP_NAME` (in the case of this project, the app name was "home")
1. Add new app to bottom of the list of installed apps in settings.py and save file
1. Migrate changes: 
    * `python3 manage.py migrate`
1. Test server works locally: 
    * `python3 manage.py runserver`  (This should display the default Django success page)

## Deploying an App to heroku
### Create a New External Database:

For the purposes of this project I used ([PostgreSQL](https://dbs.ci-dbs.net/)) which is Code Institutes database system they provide you.
1. If you are participating in a Code Institute course you will enter the email you use to log into the LMS.
1. Then you will enter the email you wish to receive the PostgreSQL Database URL
1. The email should now be in your inbox with the URL to the newly created database

### Create Heroku App:

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    *Click "New" in the top right-hand corner of the dashboard page, then click "Create New App."
1. Give the app a unique name:
    * It will form part of the URL (in the case of this project, I called the Heroku app gametalk)
1. Select the nearest location:
    * For me, this was Europe.
1. Add Database to the Heroku app:
    * Open *settings* tab and click **Reveal Config Vars**
    * Add a Config Var called **DATABASE_URL**
    * **NOTE:** The **value** should be the PostgreSQL database url copied in the previous step.
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.
1. Add Cloudinary database to the Heroku app:
    * Open *settings* tab and click **Reveal Config Vars**
    * Add a Config Var called **CLOUDINARY_URL**
    * **NOTE:** The **value** should be the Cloudinary database url copied from the cloudinary website.

### Attach the Database
I used **Visual studio code** for this project:
1. In **VSCode**:
    * Create a new ***env.py*** file on top level directory
    * in **env.py**:
        * Import os library: `import os`
        * Set environment variables: `os.environ.setdefault("DATABASE_URL", "*Paste in PostgreSQL database URL*")`
        * Add in secret key: `os.environ.setdefault("SECRET_KEY", "*Paste in Secret Key*")`
        * Set cloudinary database: `os.environ.setdefault("CLOUDINARY_UR:", "*Paste in Cloudinary database URL*")`

### Preparing **Environment** and **settings.py** File:
1. Reference env.py in settings.py:
    * `from pathlib import Path`
    * `if os.path.isfile('env.py'):`
    * `import env`
1. * Remove insecure secret key and replace with:
    * `SECRET_KEY = os.environ.get("SECRET_KEY")`
1. Comment out old databases section and add new links to database_url
    * `DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}`
1. Save all Files and Make Migrations:

    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
1. Add allowed hosts to settings.py:

    * `ALLOWED_HOSTS = ['127.0.0.1','.herokuapp.com']`

### Final Steps

1. In VSCode:
    * Create Procfile at the top level of the file structure and insert the following:
    `web: gunicorn PROJECT_NAME.wsgi` (In this instance, the project name was **gametalk**)

    * Create *media, static and templates* folders in root directory

**[Back to Readme](README.md)**
