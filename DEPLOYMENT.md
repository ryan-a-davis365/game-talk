# Deployment

## Table of Contents

### Setting up a basic Django project and deploying to Heroku

* [**Deployment**](#deployment)
    * [***Initial Deployment***](#initial-deployment)
    * [***Create Repository***](#create-repository)
    * [***Setting up the Workspace***](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [***Deploying an app to Heroku***](#deploying-an-app-to-heroku)
        * [***Create a New External Database***](#create-a-new-external-database)



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

