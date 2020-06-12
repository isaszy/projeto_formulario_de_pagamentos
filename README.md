# Formulário de pagamento

# Inicialização

1)Download da pasta zipada do projeto;

2)Descompacte-a 

3)Navegue até a pasta pelo terminal

4)Digite o comando para instalar todos os requisitos da aplicação:

```
pip3 install -r requirements.txt 
```

ou 

navegue até ven/bin/ 

´´´
pip freeze > requirements.txt
´´´

5)Digite o comando:
```
python cria_bd.py
```
#para criar o banco de dados

6)Digite o comando:
```
python controllers.py
```
```
Entre no link indicado
```
7) Para atualizar o valor do imposto e fazer com que ele apareça no arquivo projeto_vox.db, altere o valor do pagamento uma unica vez no primeiro pagamento e atualize o banco de dados.

8)Para recomeçar o banco de dados exclua o arquivo projeto_vox.db e prossiga do passo 5) ao 7)

## Estrutura

Esse projeto contém a seguinte estrutura:

### aplicacao.py

Inicializa e configura a aplicação Flask.

### controllers.py

Contém os controllers e rotas da aplicação.

### static/

Contém arquivos estáticos, como css.

### templates/

Contém as views da aplicação. O arquivo base.html é usado como arquivo principal, herdado por todos os templates.

### banco.py

Contém as funções necessárias para conectar no banco.

### cria_bd.py

cria a conexão com o banco


### banco.sql
sqlite3
Contém a estrutura do banco de dados; script para a criação da tabela 

###Models
interações com o banco de dados


-------------------------------------------------------------------------------------
###Processo
Foi escolhida a utilização do flask.
Instalação do flask por pip install
Criação das rotas de paginas
Definição do run da aplicação no arquivo controllers.py
Instalação do ambiente virtual para acomodar os requisitos da aplicação e outros utilitários;
Pastas:

- Templates em html na pasta 'templates':
    1. base.html
        base de toda a parte visual da aplicação e dos outros templates;
    2. index.html
        parte visual da página principal/lançamento de pagamentos da aplicação;
    3. index_1.html
        versão antiga do index; cópia de segurança
    4. inserir_arquivo.html
        base de toda parte visual da inserção de arquivos xlsx
    5. inserir_pagamentos.html
        parte visual do formulário de pagamentos;

- Static: 
    parte estáica; arquivos css; img e js

- Venv:
    ambiente virtual da aplicação;

- Pasta principal:
    1. aplicacao.py
        configuração da aplicação
    2. banco.py
        conexão com sqlite3
    3. banco.sql
        config do banco
    4. Check List
        objetivos que precisam ser feitos
    5. controllers.py
        lógica de cálculo
    6. models.py            --models ficam presentes
    7. models_alterar.py    -- as interações
    8. models_deletar.py    -- com o banco 
    9. models_insert.py     -- de dados.
    10. projeto_vox.db
        banco de dados
    11. requirements.txt
        onde ficam os requisitos da aplicação;

README.md

Maiores dificuldades em tentar subir um arquivo xlsx;


