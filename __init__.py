from flask import Flask
from flask import render_template
from flask import request
import creador


app = Flask(__name__)

temp = [2,4,8,3],[6,1,7,1],[12,1,2,6.3]
#   [1.5,1,1,1]
#    [6,1,2,1]
#    [12,1,2,1]

def cargarImagen():
    creador.crear_html_imagen()

@app.route('/camara', methods = ['POST', 'GET'])
def camara():
    print "caca"
    if request.form.get('iniciar') == "1":
        print "caca2"
       # prueba.comenzar();
    return render_template('camara.html')

@app.route('/como-se-hace')
def comoSeHace():
    #cargarImagen()
    return render_template('como-se-hace.html')

def cargarImagen():
    creador.crear_html_imagen()

@app.route('/quien-soy')
def quienSoy():
    return render_template('quien-soy.html')

@app.route('/resultado')
def resultado():
    return render_template('datos.html')

@app.route('/') # define la ruta con la que se ingresa en el explorador
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run (host = '127.0.0.1', port = 5000)
    
