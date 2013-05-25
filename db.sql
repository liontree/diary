create database if not exists New charset 'utf8';
use New;
create table account (
    id int not null auto_increment,
    email varchar(64) not null,
    password varchar(256) not null,
    username varchar(16) not null,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    status char(1) NOT NULL DEFAULT '',
    displayid varchar(16);
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='account info';

create table note (
    id int not null auto_increment,
    user_id int not null,
    contents text not null,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='account info'
