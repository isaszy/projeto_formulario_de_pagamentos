from banco import bd

#alteração do banco de dados
class Pay:
    def __init__(self, id, titulo, valor: float, imposto: float, data_pagamento, comentarios):
        self.id= id
        self.titulo= titulo
        self.valor= valor
        self.imposto= imposto
        self.data_pagamento= data_pagamento
        self.comentarios= comentarios

#recuperar dados para enviá-los ao banco e também para mostrar os valores
    @staticmethod
    def recupera_todos():
        sql = '''select id, titulo, valor, imposto, data_pagamento, comentarios from pay order by id desc'''
        cur = bd().execute(sql)
        # dicionários com os resultados da consulta para passar para a view
        informações = []
        for id, titulo, valor, imposto, data_pagamento, comentarios in cur.fetchall():
            # fetchall() gera uma lista com os resultados:
            imposto = "{0:.2f}".format(valor * 0.05) #calcula imposto automaticamente
            dados = Pay(id, titulo, valor, imposto, data_pagamento, comentarios)
            informações.append(dados)

        return informações 

    

