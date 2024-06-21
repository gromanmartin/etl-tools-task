FROM postgres:16.3

ENV POSTGRES_USER test_user
ENV POSTGRES_PASSWORD test_user
ENV POSTGRES_DB lottery

ADD ./db/create_table.sql /docker-entrypoint-initdb.d/