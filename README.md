# TO-DO Application for Demo

## 1. Create Django project directory


2. Create virtual env
   
    python3 -m venv [ virtual env name ]

    cd [ virtual env name ]

  a) Activate virtual env
  
    source bin/activate

  b) Deactivate virtual env

    deactivate


3. Install Django (current directory => Django project directory: create at 1.)

  pip3 install django

  python3 -m django --version


4. Create Django Project

  django-admin startproject [ project name ]
  
  cd [ project name ]


5. Run server

    python3 manage.py runserver

    python3 manage.py runserver 8000

    python3 manage.py runserver 0.0.0.0:8000


6. Checkout local server

    http://127.0.0.1:8000

    http://127.0.0.1:8000/admin


7. Create Admin User

    python3 manage.py makemigrations

    python3 manage.py migrate
   
    python3 manage.py createsuperuser

    
8. Create target app

    python3 manage.py startapp [ app name ]



Reference - https://docs.djangoproject.com/ko/5.0/intro/
