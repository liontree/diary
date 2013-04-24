create database if not exists New charset 'utf8';
use New;
create table if not exists account (
    id int not null auto_increment,
    email varchar(64) not null,
    password varchar(16) not null,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='account info';

