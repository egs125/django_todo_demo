# TO-DO Application for Demo

1. Create Django project directory


2. Create virtual env
    python3 -m venv [ virtual env name ]

    cd [ virtual env name ]

  1) Activate virtual env
  
    source bin/activate

  2) Deactivate virtual env

    deactivate


3. Install Django (current directory => Django project directory: create at 1.)

  pip3 install django

  python3 -m django --version


4. Create Django Project

  django-admin startproject [ project name ]
  
  cd [ project name ]


5. Run server
  python3 manage.py runserver
  !! In case of changing server port || IP
   => python3 manage.py runserver 8000
      python3 manage.py runserver 0.0.0.0:8000

7. Checkout local server
  http://127.0.0.1:8000
  http://127.0.0.1:8000/admin

8. Create Admin User
  python3 manage.py createsuperuser
  !! In case of error occurred (our project may not work properly until you apply the migrations for app)
    => python3 manage.py makemigrations
       python3 manage.py migrate

9. Create target app
  python3 manage.py startapp [ app name ]


Reference
=> https://docs.djangoproject.com/ko/5.0/intro/
