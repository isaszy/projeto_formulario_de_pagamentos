from banco import bd

#Classe Pay_alterar responsavel por alterar os valores no banco de dados
class Pay_alterar:
    def __init__(self, id, titulo, valor: float, imposto: float, data_pagamento, comentarios):
        self.id= id
        self.titulo= titulo
        self.valor= valor
        self.imposto= imposto
        self.data_pagamento= data_pagamento
        self.comentarios= comentarios
        
#Método responsavel por atualizar os registros do banco de dados
    def mudar(self):
        sql = '''UPDATE pay SET titulo=?, valor=?, imposto=?,
         data_pagamento=?, comentarios=? where id=?'''
        primeiro_interrogacao= self.titulo
        segundo_interrogacao= self.valor
        terceiro_interrogacao= self.imposto
        quarta_interrogacao= self.data_pagamento
        quinta_interrogacao= self.comentarios        
        sexta_interrogacao= self.id

        
        bd().execute(sql, [  terceiro_interrogacao, primeiro_interrogacao, segundo_interrogacao,
                             quarta_interrogacao, 
                            quinta_interrogacao, sexta_interrogacao])
        bd().commit()



    

