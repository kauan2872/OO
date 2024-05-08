from flask import Blueprint, render_template, request, redirect, url_for
from models import Usuario
from database import db
import os
views = Blueprint("views", __name__)

@views.route('/')
def index():
    return render_template('index.html')


@views.route('/registrar/', methods = ['POST'])
def registrar():
    usuario =  Usuario.query.filter_by(nome=request.form['nome']).first()
    if (usuario is None):
        novo = Usuario(nome = request.form['nome'], senha = request.form['senha'])
        db.session.add(novo)
        db.session.commit()
        print("Deu certo")
    else:
        print("Esse usuário já existe")
    
    return redirect(url_for('views.index'))

@views.route('/loginc/', methods= ['POST'])
def valida_usuario():
    usuario = Usuario.query.filter_by(nome=request.form["nome"]).first()
    if usuario is not None:
         if(usuario.senha == (request.form["senha"])):
              return redirect(url_for('views.upload'))

    return redirect(url_for('views.login'))

@views.route('/login/', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@views.route('/upload/')
def upload():
    return render_template('upload.html')

@views.route('/uploadc/', methods = ['POST'])
def uploadc():
    if request.method == 'POST':
        file = request.files["arquivo"]
        savePath = os.path.join('UPLOAD_FOLDER', file.filename)
        file.save(savePath)
        return "upload feito com sucesso"
    
    return render_template("upload.html")
    
def configure(app):
    app.register_blueprint(views)
    