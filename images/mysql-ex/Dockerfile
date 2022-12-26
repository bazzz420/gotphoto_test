FROM mysql

WORKDIR /app

ENV MYSQL_DATABASE=codetest \
    MYSQL_ROOT_PASSWORD=swordfish

ADD gotphoto_schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306