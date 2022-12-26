DROP DATABASE IF EXISTS codetest;

create database codetest;

use codetest;

drop table if exists people_stg;
create table `people_stg` (
  `first_name` varchar(100) not null ,
  `last_name` varchar(100) ,
  `birth_date` varchar(100) not null ,
  `place_of_birth` varchar(100) not null 
);

drop table if exists places_stg;
create table `places_stg` (
    `city` varchar(100) not null ,
    `county` varchar(100) ,
    `country` varchar(100) not null 
);