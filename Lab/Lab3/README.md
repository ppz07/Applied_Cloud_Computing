# How to run the code

## In dba Dockerfile

docker build -t my_dba .

docker run --name mydba  -p 8081:80 -d my_dba

browser localhost:8081

login admin@admin.com

password pass

docker network create mynetwork

docker run --name mydba --network mynetwork -p 8081:80 -d my_dba


## In the db Dockerfile

docker build -t my_db .

docker run --name mydb -itd -p5432:5432 my_db

docker run --name mydb --network mynetwork -itd -p5432:5432 my_db



## In the Dockerfile

docker build -t my_django .

docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash

django-admin startproject app

python /app/app/manage.py migrate

python /app/app/manage.py runserver 0.0.0.0:8000

python /app/app/manage.py createsuperuser



in app/app/app/settings.py  change DATABASES: NAME, USER, PASSWORD, HOST, PORT

RERUN THE migrate using code: 

python app/app/manage.py migrate

ERROR MESSEGE:'Error loading psycopg2 module: No module named 'psycopg2''

COPY 'psycopg2' INTO requirements.txt and save then exit 

Then rebuild the my_django container

RUN CODE:

docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash

RUN CODE:

python /app/app/manage.py migrate

RUN CODE   exit

network RUN CODE:

docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash

RUN CODE:

python /app/app/manage.py runserver 0.0.0.0:8000
