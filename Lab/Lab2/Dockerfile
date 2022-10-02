# docker build 
# docker run -it
FROM python:3.8.13

# need specify user
USER root

RUN pip install jupyter

ENV JUPYTER_USER our_user

RUN useradd -ms /bin/bash our_user

# port
EXPOSE 8888
RUN wget 'https://github.com/ppz07/Applied_Cloud_Computing/blob/main/Lab/Linear%20Regression%20Complete-Copy1.ipynb'


USER ${JUPYTER_USER}
CMD jupyter notebook --ip=0.0.0.0 --port 8888 

COPY requirements.txt .

RUN pip install -r requirements.txt
