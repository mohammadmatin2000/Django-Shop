<div align="center">
<h1 align="center">Django Online Shop</h1>
</div>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://jquery.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jquery/jquery-vertical.svg" alt="jquery" width="60" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>
<a href="https://www.gunicorn.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
<a href="https://min.io/" target="_blank" rel="noreferrer"> <img src="https://dl.min.io/logo/Minio_logo_light/Minio_logo_light.svg" alt="Minio" width="50" height="50"/> </a>

</p>


<hr>
<img width="1894" height="895" alt="Screenshot 2025-07-27 233714" src="https://github.com/user-attachments/assets/b8fe5ccb-9e87-421c-88b7-c3775e65fc27" />
<hr>
<img width="1893" height="912" alt="Screenshot 2025-07-27 233735" src="https://github.com/user-attachments/assets/051d8528-282e-4776-8e2b-4b3373508882" />
<hr>
<img width="1897" height="908" alt="Screenshot 2025-07-27 233900" src="https://github.com/user-attachments/assets/38e00140-812d-4f4e-a264-e6e81e3df367" />


# Guideline
- [Goal](#goal)
- [Extera features](#extera-features)
- [Setup](#setup)
    - [First step](#first-step)
    - [Clone it](#clone-it)
    - [Docker](#docker)
        - [Development](#development)
            - [Django Debug Toolbar](#pytest)
            - [Pytest](#django-debug-toolbar)
            - [MinIO Address](#minio-address)
            - [Flake8 and Black](#flake8-and-black)
        - [Deployment](#deployment)
            - [Gunicorn and Nginx](#gunicorn-and-nginx)
- [DB schema](#db-schema)
            


## Goal
I create this website for testing all skills that i've learned

<hr>

# Extera features
I added a lot of useful tools to make this site better, These features include :

### Development & Deployment
I separate all codes and files for use it on [Development](#development) or [Deployment](#deployment)


### Reformatted code
I reformat all codes depends on PEP8 rule with [Flake8 and Black](#flake8-and-black)

### Testing system
I used [Pytest](#pytest) for testing system and test various parts of site


<img width="1894" height="912" alt="Screenshot 2025-07-27 233927" src="https://github.com/user-attachments/assets/f6332793-1093-46b1-ae75-8c4d9e067932" />


### Various User
This shop has 3 types of user :
- <h1>customer</h1>

<img width="1904" height="917" alt="Screenshot 2025-07-27 234109" src="https://github.com/user-attachments/assets/50968cf0-1aec-4fba-bb67-36d27f21d8ce" />


<hr>

- <h1>admin</h1>

<img width="1892" height="911" alt="Screenshot 2025-07-27 234031" src="https://github.com/user-attachments/assets/e4be9126-6a6f-46c5-a8e8-577a5a782d20" />


<hr>

- <h1>superuser</h1>

Superuser can remove or add some stuff that admin couldn't

Each of them has a specific profile that has own properties
### Sitemap
A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them

### Payment Method
I used <a href='https://www.zarinpal.com/'>ZarinPal</a> for my Payment Method

<img width="1916" height="909" alt="Screenshot 2025-07-27 234149" src="https://github.com/user-attachments/assets/13aa8abb-89c7-4b10-817b-f5292e19822c" />


<hr>

### MinIO
To me : It's an usful tools for store medias in a safe and accessible place . 

<hr>

# Setup

## First step
For setup this site and walk through it you need to have <a href='https://www.docker.com/'>docker</a> on you computer

## Clone it
Next step is cloning this project
```bash
git clone https://github.com/Benfoxyy/Django-Online-Shop.git
```

## Docker
Docker is a powerful tool for run, deploying and transferring project, so i decided to use it .

As i said i separet my site, so for running it on development or deployment mode, you should follow one of these section :

## Development
```bash
docker-compose up --build -d
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1:8000'>127.0.0.1:8000</a> on your browser to see the resault

This version of website is for <b>developers</b> to testing and editting

This version has some tools that it is not exist in [Deployment](#deployment) like :

### Django Debug Toolbar
<a href='https://pypi.org/project/django-debug-toolbar/'>django_debug_toolbar</a> is an useful library for django to get reports of every single page and manage it better



### MinIO Address
For seeing all medias that is stored you can visit this url :
```bash
http://127.0.0.1:9001
```
- Username : minioadmin
- Password : minioadmin

<hr>

### Flake8 and Black
As i said <a href='https://pypi.org/project/flake8-django/'>Flake8</a> and <a href='https://pypi.org/project/black/'>Black</a> are helping for reformat all codes by <a href='https://peps.python.org/pep-0008/'>PEP8</a> rule, for using enter this command :
```bash
docker-comopose exec backend sh -c "black . -l 78 && flake8"
```


## Deployment
```bash
docker-compose -f docker-compose-deployment.yml up --build -d
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1:8000'>127.0.0.1</a> on your browser to see the resault

This version of website is for <b>normal user</b> to take a look to site

This version has some tools that it is not exist in [Development](#development) like :
### Gunicorn and Nginx
To set your project to deployment mode, you have to change DEBUG mode to False . This thing is a good way to make your site more secure but there is a disadvantages, statics and medias doesn't serve moreover django can't transfer requests on website so it's the time that <a href='https://gunicorn.org/'>Gunicorn</a> and <a href='https://nginx.org/en/'>Nginx</a> come .
<hr>


<hr>


# DB schema
<img width="2649" height="3338" alt="db-diagram" src="https://github.com/user-attachments/assets/48af87f6-f26c-4cff-bb72-da31319494ee" />


<div align="center">
<h1 align="center">Thanks for visiting</h1>
<h3 align="center">I hope that you enjoy it, Let me know if you have any suggestion</h3>
</div>
