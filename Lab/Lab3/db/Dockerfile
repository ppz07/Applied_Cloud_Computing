FROM postgres:12.12

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=pass
ENV POSTGRES_DB=web

EXPOSE 5432

# cd ..
# cwd full path
# must find the correct file path to run the code

# docker build -t my_db .
# docker run --name mydb -itd -p5432:5432 my_db
# itd means interact as demon

# create network between db and dba
# docker network create mynetwork
# docker network ls : can show all the networks


# run code: docker run --name mydba --network mynetwork -p 8081:80 -d my_dba
# to connect the network with database admin

# run code:docker run --name mydb --network mynetwork -itd -p5432:5432 my_db
# to connect the network with database
# need to specify the volume
