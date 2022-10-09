## How to run the code

in app/app/app/settings.py  change DATABASES: NAME, USER, PASSWORD, HOST, PORT

RERUN THE migrate using code: python app/app/manage.py migrate

ERROR MESSEGE:'Error loading psycopg2 module: No module named 'psycopg2''

COPY 'psycopg2' INTO requirements.txt and save then exit 

Then rebuild the my_django container

RUN CODE   docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash

RUN CODE   python /app/app/manage.py migrate

RUN CODE   exit

network RUN CODE    docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash

RUN CODE            python /app/app/manage.py runserver 0.0.0.0:8000
