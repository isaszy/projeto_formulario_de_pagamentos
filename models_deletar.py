from banco import bd

#deleta os dados pelo numero do id
class Pay_delete:
    def __init__(self, id):
        self.id= id

    def excluir(self):
        sql = '''delete from pay where id=?'''
        primeiro_interrogacao= self.id
        
        bd().execute(sql, [primeiro_interrogacao])
        bd().commit()
