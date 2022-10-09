# django container, framework, python based

FROM python

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# frame
# volume
VOLUME /app
WORKDIR /app


EXPOSE 8000

# docker build -t my_django .

# -it means interact with terminal

# create the volume
# docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash

# rm text.txt  remove
# touch text.txt
# cd ..
# django-admin startproject app
# cd app/

# python /app/app/manage.py migrate
# python /app/app/manage.py runserver 0.0.0.0:8000
# go to localhost:8000/admin
# python /app/app/manage.py createsuperuser
# create email address a@a.com and password: pass0909
# then go to localhost:8000/admin and user is root, password pass0909
# project is mapped to a volume, all the changes are being captured outside the container
# sqlite is a database format, superuser is stored in db.sqlite3

