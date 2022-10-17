FROM python

# ENV API_HOST=api_host
# ENV API_PORT=api_port
# ENV API_ENDPOINT=rec  

# how to tell consumer the API's name?

RUN pip install flask
RUN pip3 install requests

VOLUME /app
WORKDIR /app

EXPOSE 5000

CMD python api.py runserver 0.0.0.0:5000
