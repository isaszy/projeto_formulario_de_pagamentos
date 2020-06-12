
from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Pay
from models_insert import Pay_insert
from models_deletar import Pay_delete
from models_alterar import Pay_alterar
from flask import Flask, render_template, request

#Por meio da rota voxus/gravar o usuario consegue ter acesso ao metodo gravar pagamento
@app.route('/voxus/gravar', methods=[ 'POST'])
#Método responsável por receber a requisição do usuario via POST
def gravar_pagamentos():
    #É definido as variaveis com os dados enviados pelo formulario
    valor = request.form['valor']
    imposto = request.form['imposto']
    titulo = request.form['titulo']
    data_pagamento = request.form['data_pagamento']
    comentarios = request.form['comentarios']
    #É instanciado o objeto registro_pagamento da classe Pay_insert que recebe como parametros os valores das variaveis acima
    registro_pagamento = Pay_insert(valor, imposto, titulo, data_pagamento, comentarios)
    registro_pagamento.salvar()
    #Usuario é redirecionado para tela inicial após finalizar o método
    return redirect('/')

#nessa rota o método que possibilita que o usuário mude os valores do seu pagamento
@app.route('/voxus/mudar', methods=['POST'])
def alterar_pagamentos():
    #altera as variáveis que haviam sido enviadas ao banco pelo formulário
    idd = request.form['id']
    valor = request.form['valor']
    imposto = request.form['imposto']
    titulo = request.form['titulo']
    data_pagamento = request.form['data_pagamento']
    comentarios = request.form['comentarios']
    registro_pagamento = Pay_alterar(idd, valor, imposto, titulo, data_pagamento, comentarios)
    registro_pagamento.mudar()
    return redirect('/')

#possibilidade de deletar dados enviados anteriormente pelo valor da id
@app.route('/voxus/deletar', methods=['POST'])
def deletar_pagamentos():
    idd = request.form['id']
    registro_pagamento = Pay_delete(idd)
    registro_pagamento.excluir()
    return redirect('/')

#rota preliminar não completada; objetivo de possibilitar a inserção de um arquivo xlsx
@app.route('/inserir_arquivo')
def inserir_arquivo():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/inserir_pagamentos',
                'texto': 'Inserir Pagamentos'})
    menu.append({'active': True,
                'href': '/inserir_arquivo',
                'texto': 'Inserir Arquivo xlsx'})
    
    context = {'titulo': 'Voxus', #muda frase na tela e titulo página
            'menu': menu}
    return render_template('inserir_arquivo.html', **context)


#rota principal com os lançamentos 
@app.route('/')
def index():
    dados = Pay.recupera_todos()
    ##  o objeto retornado por bd() realiza comandos sql
    
    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/inserir_pagamentos',
                'texto': 'Inserir Pagamentos - VOXUS'})
    menu.append({'active': False,
                'href': '/inserir_arquivo',
                'texto': 'Inserir Arquivo xlsx - VOXUS'})
    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'posts': dados
            }
    return render_template('index.html', **context)

@app.route('/inserir_pagamentos')
def inserir_dados():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': True,
                'href': '/inserir_pagamentos',
                'texto': 'Inserir Pagamentos - VOXUS'})
    menu.append({'active': False,
                'href': '/inserir_arquivo',
                'texto': 'Inserir Arquivo xlsx - VOXUS'})
    
    context = {'titulo': 'Voxus', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('inserir_pagamentos.html', **context)

app.run()
