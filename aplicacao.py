# aplicacao.py
import flask
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(__name__)

# configuração
app.config.update(
    DATABASE = 'projeto_vox.db',
    DEBUG = True, #atualiza automático
    
)
