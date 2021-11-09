# Summary

Application to allow quiz to be integrated into workspace using existing employee number. 

Quiz and question database full and easy CRUD operations through admin panel.

Results saved to database and can be viewed from admin panel.

Basic protection used to prevent url manipulation by crypting url including coding preventing answering same question twice.

# Installation

* clone repo 
* run ```pip install -r requirements.txt```
* run ```python manage.py makemigrate```
* run ```python manage.py migrate```
* run ```python manage.py createsuperuser```
* run ```python manage.py runserver```

