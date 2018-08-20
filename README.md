# Service Providers

This Django app includes a rest api that allows the creation of service providers and their associated service areas.

# Requirements

  - Mysql = 14.14
  - Django = 1.10.6
  - Python = 3.5

# Setup

  Mysql
```sh
$ sudo apt-get update
$ sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
```

Python & Packages
```sh
$ sudo apt-get update
$ apt install python3
$ apt install python3-pip
$ pip3 install -I Django==1.10.6
$ pip3 install django-tastypie
$ pip3 install mysqlclient
 ```


# Running the App
```sh
python3 manage.py runserver 0.0.0.0:8000
```

# Api Docs 
https://documenter.getpostman.com/view/5143436/RWTprbwT


# Notes

 - Post development change ALLOWED_HOSTS in mozio/settings.py to your server's address for added security
 - If you get a  "curl: (3) [globbing]" error while executing the 'Available Location Service Providers' example curl request given in the api docs, turn curl globbing off by using the -g parameter in your request
   EX - curl --request GET -g  --url 'http://18.206.147.92/api/service_area/?polygon__contains={%22type%22:%20%22Point%22,%20%22coordinates%22:%20[-23.16,%20113.11]}'
