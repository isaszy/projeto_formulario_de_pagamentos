from banco import bd


class Pay_insert:
    def __init__(self, titulo, valor: float, imposto: float, data_pagamento, comentarios):
        self.titulo= titulo
        self.valor= valor
        self.imposto= imposto
        self.data_pagamento= data_pagamento
        self.comentarios= comentarios

#inserir os dados no banco de dados
    def salvar (self):
        sql = '''insert into pay (titulo, valor, imposto, data_pagamento, comentarios) values (?, ?, ?, ?, ?)'''
        primeiro_interrogacao= self.titulo
        segundo_interrogacao= self.valor
        terceiro_interrogacao= self.imposto
        quarta_interrogacao= self.data_pagamento
        quinta_interrogacao= self.comentarios

        bd().execute(sql, [terceiro_interrogacao, primeiro_interrogacao, segundo_interrogacao, quarta_interrogacao, quinta_interrogacao])

        bd().commit()
    

