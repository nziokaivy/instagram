# Ingramgram

## Description.

Ingramgram is a web application clone of a well-known photo-sharing app called instagram.

#### By **Ivy Nzioka**

## Working of the application

When the user opens the website, he/she will be prompted to sign up or sign in.
* The user will be able to see posts that other users have posted. 
* The user can also add their own posts. 
* The user can follow other users and view images posted by those users.
* The user also has a personalized profile where they can edit their profile and view the photos they have posted.

# Getting Started
## Prerequisites

To get started , one will need to install python3.6 or a higher version, django and postgres using the commands below:

```
* python3.6
$ sudo apt-get install python3.6.

* django 
$ pip install django==1.11

* postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

```

## Requirements

```
config==0.3.9
confusable-homoglyphs==3.2.0
dj-database-url==0.5.0
Django==1.11
django-bootstrap3==11.0.0
django-forms-bootstrap==3.1.0
django-heroku==0.3.1
django-registration==2.4.1
django-tinymce==2.8.0
gunicorn==19.9.0
Pillow==5.4.1
psycopg2==2.7.7
python-decouple==3.1
pytz==2018.9
whitenoise==3.3.1

```

## .env file
```
SECRET_KEY='1@j(rqi-n7kzj6#b@9@lx2cpa$$29*f48dclsefns4gn^#@3uy'
DEBUG=True 
DB_NAME='insta'
DB_USER='ivy'
DB_PASSWORD='data123'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1

```

## Setup/Installation Requirements

* Install galerie by cloning this repository: ``` <https://github.com/nziokaivy/instagram> ``` 
* Install the prerequisites in a virtual environment or globally
* Install all the extensions listed in the requirements.txt file       using the command ```pip install -r requirements.txt ```
* Run the command "python3.6 manage.py runserver" to launch the        application

## Running tests
* You can run tests: 
```
python3.6 manage.py test photos
```


## Live Demo

Here is a link to a live demo:[id]<https://ivygram.herokuapp.com/>




## Technologies Used
* Python3.6 
* postgress
* HTML
* CSS
* Django framework


## Bugs

Incase of any bugs:-

-   Fork a repo
-   Create a new branch (git checkout -b improve-feature)
-   Make the appropriate changes in the files
-   Add changes to reflect the changes made
-   Commit your changes (git commit -m "Improve feature"
-   Push to the branch (git push origin improve-feature)
-   Create a Pull Request



## Support and contact details

If you have any issues feel free to contact me at nziokaivy@gmail.com.

## License

MIT License. Copywright (c) 2018 _Ivy Nzioka._
