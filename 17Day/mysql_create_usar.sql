/*Comentarios*/
create user 'teste'@'localhost' identified  by 'teste'; /*Criando usuário para localhost*/
create user 'teste'@'%' identified  by 'teste'; /*Usuário para acesso externo, isso é, permissão para acesso externo*/
/*
all privileges -> Todas as permissões possiveis -> Create, update, select e delete -> Se quiser tem que expecificar para deixar mais restrito
banco de dados -> Tem que ja ter o branco criado
tabelas -> tabelas selecionadas ou todas as tabelas, todas as tabelas é *, se não especifica a tabela que quer trabalhar
teste@localhost -> teste = usuário e localhost = permissao local ou externa
*/
/*permissao total*/
grant all privileges on 'banco_de_dados' . 'tabelas_permitidas' to 'teste'@'localhost';
/*permissao externa e todos os bancos*/
grant all privileges on 'banco_de_dados' . * to 'teste'@'%';
/*Subir as permissão*/
flush privileges;