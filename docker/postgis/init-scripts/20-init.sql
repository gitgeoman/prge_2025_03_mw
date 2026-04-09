create table users
(
    name     text,
    posts    integer,
    id       smallserial
        constraint users_pk
            primary key,
    location text,
    geom     geometry
);

alter table users
    owner to mapservice;

