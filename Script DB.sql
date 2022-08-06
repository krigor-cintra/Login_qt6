create database IF not exists programa1;
use programa1;
create table if not exists login(
email varchar (150),
senha0 varchar (50),
senha1 varchar (50),
senha2 varchar (50),
primary key (email));

create table if not exists usuarios(
id_user int auto_increment,
nome varchar(100),
cfp int(11)
);

create table if not exists db_bancos(
nome_banco varchar(50),
saldo varchar(50),
id_banco int auto_increment);