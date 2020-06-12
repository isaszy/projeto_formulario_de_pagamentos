--Exclui a tabela pay caso ela pré-exista quando for iniciada a aplicação

drop table if exists pay;

--comando que cria tabela pay no sqlite
--ela possui 6 colunas (id,titulo,valor,imposto,data_pagamento, comentarios), 
--a coluna id, é auto incrementada com os valores sendo inseridos automaticamente
--as colunas titulo, imposto, data_pagamento e comentários são do tipo string

create table pay (
  id integer primary key autoincrement,
  titulo string not null,
  valor FLOAT not null,
  imposto FLOAT not null,
  data_pagamento string not null,
  comentarios string not null

);

