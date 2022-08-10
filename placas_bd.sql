create database placas;

use placas;

create table tbi_produto(
id_produto int auto_increment not null primary key,
nome_produto varchar(100),
marca varchar(15),
preco varchar(10)
);


select*from tbi_produto;